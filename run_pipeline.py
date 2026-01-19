#!/usr/bin/env python3
"""
Run full VPR + Image Matching + Reranking pipeline for ONE dataset
and ALL VPR methods.

Usage:
    python run_dataset_pipeline.py --dataset svox_sun
"""

import argparse
from datetime import datetime
import subprocess
import sys
from pathlib import Path


def sh(cmd):
    subprocess.run(cmd, shell=True, check=True)


def main(dataset: str):
    py = sys.executable

    # -----------------------------
    # DATASETS
    # -----------------------------
    datasets = {
        "tokyo_xs": {
            "db": "data/tokyo_xs/test/database",
            "queries": "data/tokyo_xs/test/queries",
        },
        "sf_xs": {
            "db": "data/sf_xs/test/database",
            "queries": "data/sf_xs/test/queries",
        },
        "svox_sun": {
            "db": "data/svox/images/test/gallery",
            "queries": "data/svox/images/test/queries_sun",
        },
        "svox_night": {
            "db": "data/svox/images/test/gallery",
            "queries": "data/svox/images/test/queries_night",
        },
        "svox": {
            "db": "data/svox/images/test/gallery",
            "queries": "data/svox/images/test/queries",
        },
    }

    if dataset not in datasets:
        raise ValueError(f"Unknown dataset: {dataset}")

    paths = datasets[dataset]

    # -----------------------------
    # VPR METHODS
    # -----------------------------
    methods = [
        dict(name="netvlad_vgg16", method="netvlad", backbone="VGG16", dim=4096),
        dict(name="cosplace_resnet50", method="cosplace", backbone="ResNet50", dim=2048),
        dict(name="mixvpr_resnet50", method="mixvpr", backbone="ResNet50", dim=4096),
        dict(name="megaloc_dinov2", method="megaloc", backbone="Dinov2", dim=8448),
    ]

    # -----------------------------
    # MATCHERS
    # -----------------------------
    matchers = ["superpoint-lg", "superglue", "loftr"]

    # -----------------------------
    # COMMON PARAMS
    # -----------------------------
    image_size = "512 512"
    distance = "L2"
    num_preds = 20
    recall_vals = "1 5 10 20"
    num_workers = 8
    batch_size = 32


    for m in methods:
        # Retrieval phase
        log_base = Path("logs") / f"{m['name']}_{dataset}"
        if log_base.exists():
            print(f"Skipping VPR method {m['name']} on dataset {dataset} (already done).")
        else:
            sh(
                f"{py} VPR-methods-evaluation/main.py "
                f"--num_workers {num_workers} "
                f"--batch_size {batch_size} "
                f"--log_dir {m['name']}_{dataset} "
                f"--method {m['method']} "
                f"--backbone {m['backbone']} "
                f"--descriptors_dimension {m['dim']} "
                f"--image_size {image_size} "
                f"--database_folder {paths['db']} "
                f"--queries_folder {paths['queries']} "
                f"--distance {distance} "
                f"--num_preds_to_save {num_preds} "
                f"--recall_values {recall_vals} "
                f"--save_for_uncertainty"
            )

        #Get date of last run, which is the folder name
        date = sorted([d.name for d in log_base.iterdir() if d.is_dir()])[-1]
        
        preds_dir = log_base / date / "preds"

        # Image matching phase
        for matcher in matchers:

            inliers_dir = log_base / date / f"preds_{matcher}"
            
            if inliers_dir.exists():
                print(f"Skipping matcher {matcher} for method {m['name']} on dataset {dataset} (already done).")
            else:
                sh(
                    f"{py} match_queries_preds.py "
                    f"--preds-dir '{preds_dir}' "
                    f"--matcher '{matcher}' "
                    f"--device cuda "
                    f"--num-preds {num_preds}"
                )
            if not inliers_dir.exists():
                raise RuntimeError(f"Inliers not found: {inliers_dir}")

            # reranking phase
            sh(
                f"{py} reranking.py "
                f"--preds-dir '{preds_dir}' "
                f"--inliers-dir '{inliers_dir}' "
                f"--num-preds {num_preds} "
                f"--recall-values {recall_vals}"
            )


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--dataset",
        required=True,
        help="Dataset name (tokyo_xs, sf_xs, svox_sun, svox_night)",
    )
    args = parser.parse_args()
    main(args.dataset)