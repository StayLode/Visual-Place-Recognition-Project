#!/usr/bin/env python3
import math
import os, argparse, sys
import numpy as np
from glob import glob
from pathlib import Path
import torch
import numpy as np
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import precision_recall_curve, auc
from scipy.stats import spearmanr
from sklearn.model_selection import train_test_split

sys.path.append(str(Path(__file__).parent.parent))

from util import get_list_distances_from_preds
from vpr_uncertainty.baselines import compute_l2, compute_pa, compute_sue, compute_random

np.random.seed(42)
EPS = 1e-9

def list_query_txts(preds_dir: str):
    """
    Lists all .txt files in preds_dir, sorted by query index.
    Returns:
        list of .txt file paths
    """
    txt_files = glob(os.path.join(preds_dir, "*.txt"))
    txt_files.sort(key=lambda x: int(Path(x).stem)) # sort by query index
    return txt_files


def load_z_data(z_data_path: str):
    """
    Loads z_data torch file.
    Returns:
        ref_poses: (M, 2) reference poses
        preds: list of (K,) predicted indices per query
        dists: list of (K,) predicted distances per query
    """
    d = torch.load(z_data_path, weights_only=False)
    ref_poses = d["database_utms"]
    preds = d["predictions"]
    dists = d["distances"]
    return ref_poses, preds, dists


def build_arrays(preds_dir, inliers_dir, z_data_path, positive_dist_threshold):
    """
    Builds arrays needed for uncertainty metrics computation.
    Returns:
        matched: (N,) 1.0 if correct, 0.0 if wrong
        inliers_scores: (N,) number of inliers per query
        ref_poses: (M, 2) reference poses
        preds: list of (K,) predicted indices per query
        dists: list of (K,) predicted distances per query
    """
    preds_folder = preds_dir
    inliers_folder = Path(inliers_dir)
    threshold = positive_dist_threshold

    txt_files = list_query_txts(preds_folder)

    ref_poses, preds, dists = load_z_data(z_data_path)

    total_queries = len(txt_files)
    if len(preds) != total_queries:
        raise RuntimeError(
            f"Mismatch: {total_queries} .txt files but z_data has {len(preds)} queries. "
            f"Check that the predictions directory and z_data correspond to the same split."
        )

    matched = np.zeros(total_queries, dtype="float32")
    inliers_scores = np.zeros(total_queries, dtype="float32")

    for itr, txt_file_query in enumerate(txt_files):
        geo_dists = get_list_distances_from_preds(txt_file_query)
        matched[itr] = 1.0 if geo_dists[0] <= threshold else 0.0

        torch_file_query = inliers_folder.joinpath(Path(txt_file_query).name.replace("txt", "torch"))
        q = torch.load(torch_file_query, weights_only=False)
        inliers_scores[itr] = q[0]["num_inliers"]

    return matched, inliers_scores, ref_poses, preds, dists


def sue_variance_per_query(ref_poses, preds, dists, num_NN=10, slope=350.0):
    """
    Computes SUE variance per query.
    Args:
        ref_poses: (M, 2) reference poses
        preds: list of (K,) predicted indices per query
        dists: list of (K,) predicted distances per query
        num_NN: number of nearest neighbors to consider
        slope: slope parameter for weight computation
    Returns:
        sue_var: (N,) SUE variance per query
    """
    total_queries = len(preds)
    sue_var = np.zeros(total_queries, dtype=np.float32)

    for i in range(total_queries):
        top_preds = preds[i][:num_NN]
        nn_poses = ref_poses[top_preds]  # (num_NN, 2)

        # safe weights
        w = np.empty(num_NN, dtype=np.float64)
        for k in range(num_NN):
            v = float(dists[i][k])
            if not np.isfinite(v):
                v = 1e9
            w[k] = math.exp(-abs(v) * slope)

        den = np.sum(w)
        if (not np.isfinite(den)) or den < 1e-12:
            w[:] = 1.0 / num_NN
        else:
            w /= den

        mean_pose = np.asarray([
            np.average(nn_poses[:, 0], weights=w),
            np.average(nn_poses[:, 1], weights=w),
        ])

        if not np.all(np.isfinite(mean_pose)):
            mean_pose = np.asarray([np.mean(nn_poses[:, 0]), np.mean(nn_poses[:, 1])], dtype=np.float64)

        var_lat = 0.0
        var_lon = 0.0

        for k in range(num_NN):
            diff_lat = min(500.0, float(nn_poses[k, 0] - mean_pose[0]))
            diff_lon = min(500.0, float(nn_poses[k, 1] - mean_pose[1]))
            var_lat += w[k] * (diff_lat ** 2)
            var_lon += w[k] * (diff_lon ** 2)

        val = float((var_lat + var_lon) / 2.0)
        if not np.isfinite(val):
            val = 0.0
        sue_var[i] = val

    return sue_var


def auprc_from_scores(y_true, scores):
    """
    Computes the Area Under the Precision-Recall Curve (AUPRC).
    Args:
        y_true: Ground truth binary labels (0 or 1).
        scores: Predicted scores or probabilities.
    Returns:
        AUPRC value.
    """
    precision, recall, _ = precision_recall_curve(y_true, scores)
    return auc(recall, precision)


def aurc_from_conf(y_correct, conf_scores):
    """
    Computes AURC and AUSE (Area Under Risk-Coverage curve and its excess over oracle).
    We assume conf_scores: higher = more confident (more likely correct).
    We reject samples with lowest confidence first.

    Returns: (aurc, aurc_oracle, ause)
    """
    y_correct = np.asarray(y_correct).astype(np.int32)
    conf_scores = np.asarray(conf_scores).astype(np.float64)

    N = len(y_correct)
    if N == 0:
        return np.nan, np.nan, np.nan

    # True error labels: 1 = error, 0 = correct
    y_err = 1 - y_correct

    # Order by confidence ascending: remove least confident first
    order = np.argsort(conf_scores)

    coverages = np.empty(N + 1, dtype=np.float64)
    risks = np.empty(N + 1, dtype=np.float64)

    for k in range(N + 1):
        remain = order[k:]
        coverages[k] = len(remain) / N
        risks[k] = y_err[remain].mean() if len(remain) > 0 else 0.0

    # Integrate risk over coverage
    cov_sort = np.argsort(coverages)
    aurc = np.trapezoid(risks[cov_sort], coverages[cov_sort])

    # Oracle: remove true errors first
    order_oracle = np.argsort(-y_err)  # errors (1) first
    coverages_o = np.empty(N + 1, dtype=np.float64)
    risks_o = np.empty(N + 1, dtype=np.float64)

    for k in range(N + 1):
        remain = order_oracle[k:]
        coverages_o[k] = len(remain) / N
        risks_o[k] = y_err[remain].mean() if len(remain) > 0 else 0.0

    cov_sort_o = np.argsort(coverages_o)
    aurc_oracle = np.trapezoid(risks_o[cov_sort_o], coverages_o[cov_sort_o])

    return float(aurc), float(aurc_oracle)


def make_features(inliers_scores, preds, ref_poses, dists, features,
                  sue_numNN=10, sue_slope=50.0,gate_T=None):
    """
    Returns:
      X: (N, D) feature matrix
      names: list of feature names

    """
    feats = []
    names = []
    features = [f.strip() for f in features.split(",") if f.strip()]
    N = len(inliers_scores)

    # compute SUE variance if needed
    sue_var = None
    if "sue" in features:
        sue_var = sue_variance_per_query(ref_poses, preds, dists,
                                        num_NN=sue_numNN, slope=sue_slope).astype(np.float32)

    for f in features:
        if f == "inliers":
            feats.append(inliers_scores.astype(np.float32))
            names.append("inliers")
        elif f == "l2":
            l2 = np.array([float(dists[i][0]) for i in range(N)], dtype=np.float32)

            if gate_T is None:
                # l2 without gating
                feats.append(-l2)
                names.append("l2")
            else:
                g = (inliers_scores.astype(np.float32) < float(gate_T)).astype(np.float32)
                feats.append(g * -l2)
                names.append("gated l2")
        elif f == "pa":
            pa = np.array([float(dists[i][0]) / (float(dists[i][1]) + 1e-9) for i in range(N)], dtype=np.float32)
            feats.append(pa)
            names.append("pa")
        elif f == "sue":
            feats.append(sue_var)
            names.append("sue_var")
        else:
            raise ValueError(f"Feature non supportata: {f}")

    X = np.stack(feats, axis=1)
    return X, names


def compute_ausc(uncertainty_scores, labels):
    """
    Computes the Area Under the Sparsification Curve (AUSC).
    This metric measures the remaining error rate as we progressively discard
    the most uncertain predictions.
    
    Args:
        uncertainty_scores (np.array): Higher value means MORE uncertain (discarded first).
        labels (np.array): 1 for Correct, 0 for Wrong.
        
    Returns:
        float: The Area Under the Curve (Lower is Better).
    """
    # 1. Sort samples by uncertainty in descending order (most uncertain first)
    idxs = np.argsort(uncertainty_scores)[::-1]
    sorted_labels = labels[idxs]
    
    # Calculate errors (0 if Correct, 1 if Wrong)
    errors = 1 - sorted_labels
    n_samples = len(errors)
    
    # 2. Compute the Error Rate Curve
    # "If we remove the top K uncertain samples, what is the error rate of the remaining ones?"
    
    # Inverse cumulative sum of errors (from the least uncertain to the most uncertain)
    remaining_errors_sum = np.cumsum(errors[::-1])[::-1]
    
    # Count of remaining samples at each step
    remaining_count = np.arange(1, n_samples + 1)[::-1]
    
    # Error rate for the remaining subset
    error_curve = remaining_errors_sum / remaining_count
    
    # 3. Compute AUC
    # X-axis: Fraction of rejected samples (from 0 to 1)
    rejection_rates = np.linspace(0, 1, n_samples)
    
    # We exclude the last point where remaining_count is 0/undefined
    ausc_val = auc(rejection_rates[:-1], error_curve[:-1])
    
    return ausc_val


def oracle_ausc(y_true, return_curve=False):
    """
    Oracle AUSC: best possible ordering by uncertainty (1-y). Removes wrong predictions first. 
    Lower is better.    
    Args:
        y_true (np.array): 1 for Correct, 0 for Wrong.
        return_curve (bool): If True, also returns the sparsification curve.
    Returns:
        float: The Oracle AUSC value.
    """
    y = np.asarray(y_true).astype(float)
    N = len(y)
    if N == 0:
        out = float("nan")
        return (out, None, None) if return_curve else out

    # Oracle ordering: "uncertainty" perfetta = 1-y (errori più incerti)
    u_oracle = 1.0 - y
    return compute_ausc(
        uncertainty_scores=u_oracle,
        labels=y,
    )
    

def ausc_gap_to_oracle(y_true, unc_scores):
    """
    Computes the AUSC gap to oracle.
    Lower is better, 0 is optimal.
    Args:
        y_true (np.array): 1 for Correct, 0 for Wrong.
        unc_scores (np.array): Higher value means MORE uncertain.
    Returns:
        float: AUSC gap to oracle.
    """
    ausc = compute_ausc(uncertainty_scores=unc_scores, labels=y_true)
    ausc_or = oracle_ausc(y_true)
    return float(ausc_or - ausc)


def parse_arguments():
    parser = argparse.ArgumentParser()

    # TRAIN split (for training/validation)
    parser.add_argument("--train-preds-dir", type=str, required=True)
    parser.add_argument("--train-inliers-dir", type=str, required=True)
    parser.add_argument("--train-z-data-path", type=str, required=True)

    # TEST split (for final evaluation)
    parser.add_argument("--test-preds-dir", type=str, required=True)
    parser.add_argument("--test-inliers-dir", type=str, required=True)
    parser.add_argument("--test-z-data-path", type=str, required=True)

    parser.add_argument("--positive-dist-threshold", type=int, default=25)

    # split train->train/val
    parser.add_argument("--val-ratio", type=float, default=0.15)
    parser.add_argument("--split-mode", choices=["contiguous", "random"], default="contiguous")
    parser.add_argument("--seed", type=int, default=42)

    # logistic regressor
    parser.add_argument("--Cs", type=str, default="0.01,0.1,1,10,100",
                        help="comma-separated list for C grid-search on val")

    # features
    parser.add_argument("--features", type=str, default="inliers",
                        help="comma-separated: inliers,l2,pa,sue")
    #Threshold for inliers
    parser.add_argument(
        "--gate-percentiles",
        type=str,
        default="10,20,30",
        help="percentili (su inliers del train_sub) per la soglia T del gating B1"
    )

    return parser.parse_args()

def main(args):
    thr = args.positive_dist_threshold

    # === Load TRAIN split ===
    y_train_all, inliers_train_all, ref_poses_tr, preds_tr, dists_tr = build_arrays(
        args.train_preds_dir, args.train_inliers_dir, args.train_z_data_path, thr
    )

    # === Split train -> train/val ===
    Ntr = len(y_train_all)

    idx_tr, idx_val = train_test_split(np.arange(Ntr),test_size=args.val_ratio,random_state=args.seed,shuffle=True)

    gate_percentiles = [float(x.strip()) for x in args.gate_percentiles.split(",") if x.strip()]
    inl_tr = inliers_train_all[idx_tr]
    T_candidates = [np.percentile(inl_tr, p) for p in gate_percentiles]

    # === Choose C and T on VAL (AUPRC, positive = correct) ===

    Cs = [float(x.strip()) for x in args.Cs.split(",") if x.strip()]
    bestC, bestT, bestVal = None, None, 1.0
    best_feat_names = None

    for T in T_candidates:
        X_train_all, feat_names = make_features(
            inliers_train_all, preds_tr, ref_poses_tr, dists_tr, args.features,
            sue_numNN=10, sue_slope=50, gate_T=T
        )

        X_tr, y_tr = X_train_all[idx_tr], y_train_all[idx_tr]
        X_val, y_val = X_train_all[idx_val], y_train_all[idx_val]

        for C in Cs:
            clf = Pipeline([
                ("scaler", StandardScaler()),
                ("lr", LogisticRegression(C=C, solver="liblinear", max_iter=2000, class_weight="balanced"))
            ])
            clf.fit(X_tr, y_tr)
            val_scores = clf.decision_function(X_val)
            val_ausc = compute_ausc(uncertainty_scores=1-val_scores, labels=y_val)

            if val_ausc < bestVal:
                bestVal = val_ausc
                bestC = C
                bestT = T
                best_feat_names = feat_names

    # === Recompute features on FULL TRAIN with best T ===
    X_train_all, feat_names = make_features(
        inliers_train_all, preds_tr, ref_poses_tr, dists_tr, args.features,
        sue_numNN=10, sue_slope=50, gate_T=bestT
    )

    print("\n=== Train/Val split ===")
    print(f"N_train_all={Ntr} | train_sub={len(idx_tr)} | val_sub={len(idx_val)}")
    print(f"split_mode={args.split_mode} val_ratio={args.val_ratio} seed={args.seed}")
    print(f"features={best_feat_names}")
    print(f"best T={bestT:.3f} | best C={bestC} (VAL AUPRC={bestVal*100:.1f})")


    # === Refit on FULL TRAIN (train_sub + val_sub) ===
    final_clf = Pipeline([
        ("scaler", StandardScaler()),
        ("lr", LogisticRegression(C=bestC, solver="liblinear", max_iter=2000, class_weight="balanced"))
    ])
    final_clf.fit(X_train_all, y_train_all)

    # === Load TEST split ===
    y_test, inliers_test, ref_poses_te, preds_te, dists_te = build_arrays(
        args.test_preds_dir, args.test_inliers_dir, args.test_z_data_path, thr
    )

    X_test, _ = make_features(
        inliers_test, preds_te, ref_poses_te, dists_te, args.features,
        sue_numNN=10, sue_slope=50, gate_T=bestT
    )


    test_scores = final_clf.decision_function(X_test)
    auc_logreg = auprc_from_scores(y_test, test_scores)

    # === Baselines on TEST (come eval.py) ===
    inliers_norm = np.interp(inliers_test, (inliers_test.min(), inliers_test.max()), (0.0, 1.0))
    prec_inl, rec_inl, _ = precision_recall_curve(y_test, inliers_norm)
    auc_inliers = auc(rec_inl, prec_inl)

    auc_l2 = compute_l2(y_test, dists_te)
    auc_pa = compute_pa(y_test, dists_te)
    auc_sue = compute_sue(y_test, preds_te, ref_poses_te, dists_te, slope=50)
    auc_rand = compute_random(y_test)

    # === Score arrays (for calibration metrics) ===
    Nte = len(y_test)

    # L2 confidence: -d1 normalizzato in [0.1, 1.0]
    l2_raw = -np.array([float(dists_te[i][0]) for i in range(Nte)], dtype=np.float64)
    l2_scores = np.interp(l2_raw, (l2_raw.min(), l2_raw.max()), (0.1, 1.0))

    # PA confidence: -(d1/d2) normalizzato in [0.1, 1.0]
    pa_raw = -np.array([float(dists_te[i][0]) / (float(dists_te[i][1]) + EPS) for i in range(Nte)], dtype=np.float64)
    pa_scores = np.interp(pa_raw, (pa_raw.min(), pa_raw.max()), (0.1, 1.0))

    # SUE confidence: -variance normalizzato in [0.1, 1.0]
    sue_var_te = sue_variance_per_query(ref_poses_te, preds_te, dists_te, slope=350.0).astype(np.float64)
    sue_raw = -sue_var_te
    # evita degenerate min==max
    if sue_raw.max() - sue_raw.min() < 1e-12:
        sue_scores = np.ones_like(sue_raw, dtype=np.float64)
    else:
        sue_scores = np.interp(sue_raw, (sue_raw.min(), sue_raw.max()), (0.1, 1.0))

    print("\n=== TEST AUPRC (positive = correct) ===")
    print(f"LogReg({'+'.join(best_feat_names)}): {auc_logreg * 100:.1f}")
    print(f"L2-distance:            {auc_l2 * 100:.1f}")
    print(f"PA-score:               {auc_pa * 100:.1f}")
    print(f"SUE:                    {auc_sue * 100:.1f}")
    print(f"Random:                 {auc_rand * 100:.1f}")
    print(f"Inliers:                {auc_inliers * 100:.1f}")

    rows = [
        (f"LogReg({'+'.join(best_feat_names)})", test_scores),
        ("Inliers", inliers_norm),
        ("L2-distance", l2_scores),
        ("PA-score", pa_scores),
        ("SUE", sue_scores),
    ]
    
    print("\n=== TEST Sparsification (Risk-Coverage) ===")
    # AURC: area under risk vs coverage curve (lower is better).
    # AUSE: AURC - oracle_AURC (lower is better, 0 is optimal).
    for name, scores in rows:
        aurc_val, aurc_oracle = aurc_from_conf(y_test, scores)
        print(f"{name:22s} | AURC={aurc_val: .4f} | oracle={aurc_oracle: .4f}")
     
    print("\n=== TEST Spearman R ===") 
    for name, scores in rows:
        s, _ = spearmanr(1-scores, y_test)
        print(f"{name:22s} | Spearman R={s: .4f}")
    
    print("\n=== TEST AUSC:===")
    for name, scores in rows:
        ausc_val= compute_ausc(uncertainty_scores=1-scores, labels=y_test)
        ausc_oracle= oracle_ausc(y_test)
        print(f"{name:22s} | AUSC={ausc_val: .4f} | oracle={ausc_oracle: .4f} ")

    
    # Save scores for plotting curves (optional)
    #probs=final_clf.predict_proba(X_test)[:, 1]
    #np.save("curves_inliers/netvlad/svox_sun_svox_night/Probs_L2.npy", np.array(probs))
    #np.save("curves_inliers/netvlad/svox_sun_svox_night/Probs_Inliers_L2.npy", np.array(probs))
    #np.save("curves_inliers/netvlad/svox_sun_svox_night/Probs_pa.npy", np.array(probs))
    #np.save("curves_inliers/netvlad/svox_sun_svox_night/Probs_Inliers_L2_pa.npy", np.array(probs))
    #np.save("curves_inliers/netvlad/svox_sun_svox_night/Probs_Inliers_L2_gated.npy", np.array(probs))
    #np.save("curves_inliers/netvlad/svox_sun_svox_night/Inliers.npy", np.array(inliers_test))
    #np.save("curves_inliers/netvlad/svox_sun_svox_night/Probs_Inliers.npy", np.array(probs))
    #np.save("curves_inliers/netvlad/svox_sun_svox_night/Y_test_l2.npy", np.array(y_test))

if __name__ == "__main__":
    args = parse_arguments()
    main(args)