# Performance of the VPR methods

### **Tokyo - XS**
| Method   | Backbone | Metric      |  R@1 |  R@5 | R@10 | R@20 | Total Time(mm:ss) |
| -------- | -------- | ----------- | ---: | ---: | ---: | ---: | ----------------: |
| NetVlad  | vgg16    | L2          | 54.0 | 64.4 | 69.5 | 74.6 |             06:06 |
| NetVlad  | vgg16    | dot-product | 54.0 | 64.4 | 69.5 | 74.6 |             06:02 |
| CosPlace | ResNet50 | L2          | 73.3 | 83.8 | 87.9 | 91.4 |             03:32 |
| CosPlace | ResNet50 | dot-product | 73.3 | 83.8 | 87.9 | 91.4 |             03:29 |
| MixVPR   | ResNet50 | L2          | 76.5 | 88.6 | 92.1 | 94.3 |             02:27 |
| MixVPR   | ResNet50 | dot-product | 76.5 | 88.6 | 92.1 | 94.3 |             02:24 |
| MegaLoc  | DINOv2   | L2          | 95.6 | 97.8 | 98.7 | 99.0 |             21:29 |
| MegaLoc  | DINOv2   | dot-product | 95.6 | 97.8 | 98.7 | 99.0 |             21:35 |

### **SF-XS**
| Method   | Backbone | Metric      |  R@1 |  R@5 | R@10 | R@20 | Total Time(mm:ss) |
| -------- | -------- | ----------- | ---: | ---: | ---: | ---: | ----------------: |
| NetVlad  | vgg16    | L2          | 42.2 | 53.7 | 60.8 | 65.3 |             13:26 |
| NetVlad  | vgg16    | dot-product | 42.2 | 53.7 | 60.8 | 65.3 |             13:11 |
| CosPlace | ResNet50 | L2          | 70.9 | 80.0 | 84.0 | 86.9 |             07:43 |
| CosPlace | ResNet50 | dot-product | 70.9 | 80.0 | 84.0 | 86.9 |             08:10 |
| MixVPR   | ResNet50 | L2          | 69.6 | 78.7 | 81.1 | 83.6 |             05:24 |
| MixVPR   | ResNet50 | dot-product | 69.6 | 78.7 | 81.1 | 83.6 |             05:04 |
| MegaLoc  | DINOv2   | L2          | 86.9 | 90.4 | 91.2 | 91.5 |             49:12 |
| MegaLoc  | DINOv2   | dot-product | 86.9 | 90.4 | 91.2 | 91.5 |             49:13 |

### **SVOX - Sun**
| Method   | Backbone | Metric      |  R@1 |  R@5 | R@10 | R@20 | Total Time(mm:ss) |
| -------- | -------- | ----------- | ---: | ---: | ---: | ---: | ----------------: |
| NetVlad  | vgg16    | L2          | 37.1 | 54.4 | 62.2 | 69.0 |             08:29 |
| NetVlad  | vgg16    | dot-product | 37.1 | 54.4 | 62.2 | 69.0 |             08:33 |
| CosPlace | ResNet50 | L2          | 77.0 | 89.0 | 92.4 | 95.0 |             04:52 |
| CosPlace | ResNet50 | dot-product | 77.0 | 89.0 | 92.4 | 95.0 |             04:50 |
| MixVPR   | ResNet50 | L2          | 84.4 | 92.7 | 94.6 | 95.4 |             03:12 |
| MixVPR   | ResNet50 | dot-product | 84.4 | 92.7 | 94.6 | 95.4 |             03:13 |
| MegaLoc  | DINOv2   | L2          | 97.2 | 99.3 | 99.5 | 99.6 |             30:12 |
| MegaLoc  | DINOv2   | dot-product | 97.2 | 99.3 | 99.5 | 99.6 |             30:02 |

### **SVOX - Night**
| Method   | Backbone | Metric      |  R@1 |  R@5 | R@10 | R@20 | Total Time(mm:ss) |
| -------- | -------- | ----------- | ---: | ---: | ---: | ---: | ----------------: |
| NetVlad  | vgg16    | L2          |  8.5 | 18.2 | 22.7 | 28.5 |             08:36 |
| NetVlad  | vgg16    | dot-product |  8.5 | 18.2 | 22.7 | 28.5 |             08:38 |
| CosPlace | ResNet50 | L2          | 49.2 | 66.1 | 72.8 | 78.6 |             04:57 |
| CosPlace | ResNet50 | dot-product | 49.2 | 66.1 | 72.8 | 78.6 |             04:57 |
| MixVPR   | ResNet50 | L2          | 62.6 | 80.6 | 83.8 | 87.4 |             03:17 |
| MixVPR   | ResNet50 | dot-product | 62.6 | 80.6 | 83.8 | 87.4 |             03:18 |
| MegaLoc  | DINOv2   | L2          | 96.5 | 98.7 | 99.0 | 99.3 |             30:14 |
| MegaLoc  | DINOv2   | dot-product | 96.5 | 98.7 | 99.0 | 99.3 |             30:13 |

### **SVOX - Full**
| Method   | Backbone | Metric      |  R@1 |  R@5 | R@10 | R@20 | Total Time(mm:ss) |
| -------- | -------- | ----------- | ---: | ---: | ---: | ---: | ----------------: |
| NetVlad  | vgg16    | L2          | 86.6 | 93.7 | 95.5 | 96.9 |             17:52 |
| NetVlad  | vgg16    | dot-product | 86.6 | 93.7 | 95.5 | 96.9 |             17:53 |
| CosPlace | ResNet50 | L2          | 97.1 | 98.4 | 98.7 | 99.0 |             08:22 |
| CosPlace | ResNet50 | dot-product | 97.1 | 98.4 | 98.7 | 99.0 |             08:23 |
| MixVPR   | ResNet50 | L2          | 97.8 | 98.9 | 99.2 | 99.3 |             06:55 |
| MixVPR   | ResNet50 | dot-product | 97.8 | 98.9 | 99.2 | 99.3 |             06:58 |
| MegaLoc  | DINOv2   | L2          | 98.7 | 99.5 | 99.6 | 99.7 |             55:49 |
| MegaLoc  | DINOv2   | dot-product | 98.7 | 99.5 | 99.6 | 99.7 |             52:55 |

# Performance of Image Matching Methods

### **Tokyo-XS (L2)**
| Method   | Backbone | Matcher              |  R@1 |  R@5 | R@10 | R@20 | Total Time (mm:ss) | Time per Query (s) |
| -------- | -------- | -------------------- | ---: | ---: | ---: | ---: | -----------------: | -----------------: |
| NetVlad  | vgg16    | SuperPoint+LightGlue | 68.9 | 71.7 | 73.0 | 74.6 |              18:42 |               3.56 |
| NetVlad  | vgg16    | Superglue            | 67.0 | 71.1 | 72.7 | 74.6 |              07:34 |               1.44 |
| NetVlad  | vgg16    | LoFTR                | 68.9 | 70.8 | 73.0 | 74.6 |              19:41 |               3.75 |
| CosPlace | ResNet50 | SuperPoint+LightGlue | 86.0 | 89.2 | 89.8 | 91.4 |              18:43 |               3.57 |
| CosPlace | ResNet50 | Superglue            | 84.8 | 88.6 | 90.2 | 91.4 |              07:25 |               1.41 |
| CosPlace | ResNet50 | LoFTR                | 86.7 | 89.2 | 90.5 | 91.4 |              19:42 |               3.75 |
| MixVPR   | ResNet50 | SuperPoint+LightGlue | 89.2 | 92.4 | 94.0 | 94.3 |              18:41 |               3.56 |
| MixVPR   | ResNet50 | Superglue            | 87.0 | 92.4 | 93.3 | 94.3 |              07:33 |               1.44 |
| MixVPR   | ResNet50 | LoFTR                | 90.5 | 92.7 | 94.0 | 94.3 |              19:44 |               3.76 |
| MegaLoc  | DINOv2   | SuperPoint+LightGlue | 94.3 | 98.4 | 98.7 | 99.0 |              18:16 |               3.48 |
| MegaLoc  | DINOv2   | Superglue            | 93.0 | 98.1 | 98.4 | 99.0 |              07:25 |               1.41 |
| MegaLoc  | DINOv2   | LoFTR                | 94.3 | 97.8 | 98.7 | 99.0 |              19:05 |               3.63 |

### **SF-XS (L2)**
| Method   | Backbone | Matcher              |  R@1 |  R@5 | R@10 | R@20 | Total Time (mm:ss) | Time per Query (s) |
| -------- | -------- | -------------------- | ---: | ---: | ---: | ---: | -----------------: | -----------------: |
| NetVlad  | vgg16    | SuperPoint+LightGlue | 62.3 | 64.5 | 64.9 | 65.3 |              58:42 |               3.52 |
| NetVlad  | vgg16    | Superglue            | 61.1 | 64.4 | 64.9 | 65.3 |              23:50 |               1.43 |
| NetVlad  | vgg16    | LoFTR                | 61.5 | 63.9 | 64.6 | 65.3 |              61:37 |               3.70 |
| CosPlace | ResNet50 | SuperPoint+LightGlue | 82.5 | 85.6 | 86.3 | 86.9 |              59:50 |               3.59 |
| CosPlace | ResNet50 | Superglue            | 81.5 | 84.9 | 86.3 | 86.9 |              23:39 |               1.42 |
| CosPlace | ResNet50 | LoFTR                | 81.7 | 84.7 | 86.1 | 86.9 |              64:05 |               3.85 |
| MixVPR   | ResNet50 | SuperPoint+LightGlue | 80.6 | 82.5 | 83.3 | 83.6 |              60:57 |               3.66 |
| MixVPR   | ResNet50 | Superglue            | 79.2 | 82.0 | 83.2 | 83.6 |              23:37 |               1.42 |
| MixVPR   | ResNet50 | LoFTR                | 79.6 | 82.7 | 83.4 | 83.6 |              64:19 |               3.86 |
| MegaLoc  | DINOv2   | SuperPoint+LightGlue | 87.0 | 90.6 | 91.3 | 91.5 |              59:08 |               3.55 |
| MegaLoc  | DINOv2   | Superglue            | 85.8 | 89.9 | 90.7 | 91.5 |              23:35 |               1.42 |
| MegaLoc  | DINOv2   | LoFTR                | 86.5 | 89.7 | 90.8 | 91.5 |              63:01 |               3.79 |

### **SVOX - Sun (L2)**
| Method   | Backbone | Matcher              |  R@1 |  R@5 | R@10 | R@20 | Total Time(mm:ss) | Time per Query (s) |
| -------- | -------- | -------------------- | ---: | ---: | ---: | ---: | ----------------: | -----------------: |
| NetVlad  | vgg16    | SuperPoint+LightGlue | 65.1 | 66.5 | 67.9 | 69.0 |             50:12 |               3.53 |
| NetVlad  | vgg16    | Superglue            | 64.3 | 66.3 | 67.4 | 69.0 |             21:10 |               1.49 |
| NetVlad  | vgg16    | LoFTR                | 64.6 | 66.9 | 67.8 | 69.0 |             52:19 |               3.68 |
| CosPlace | ResNet50 | SuperPoint+LightGlue | 90.4 | 93.4 | 94.6 | 95.0 |             50:19 |               3.54 |
| CosPlace | ResNet50 | Superglue            | 87.6 | 92.6 | 94.3 | 95.0 |             20:52 |               1.47 |
| CosPlace | ResNet50 | LoFTR                | 92.0 | 93.8 | 94.5 | 95.0 |             52:57 |               3.72 |
| MixVPR   | ResNet50 | SuperPoint+LightGlue | 91.7 | 94.4 | 95.1 | 95.4 |             49:58 |               3.51 |
| MixVPR   | ResNet50 | Superglue            | 89.6 | 93.6 | 95.0 | 95.4 |             20:54 |               1.47 |
| MixVPR   | ResNet50 | LoFTR                | 93.1 | 94.6 | 95.2 | 95.4 |             52:16 |               3.67 |
| MegaLoc  | DINOv2   | SuperPoint+LightGlue | 96.0 | 99.1 | 99.4 | 99.6 |             50:27 |               3.54 |
| MegaLoc  | DINOv2   | Superglue            | 93.8 | 98.7 | 99.4 | 99.6 |             21:25 |               1.50 |
| MegaLoc  | DINOv2   | LoFTR                | 97.3 | 99.3 | 99.5 | 99.6 |             52:56 |               3.72 |

### **SVOX - Night (L2)**
| Method   | Backbone | Matcher              |  R@1 |  R@5 | R@10 | R@20 | Total Time (mm:ss) | Time per Query (s) |
| -------- | -------- | -------------------- | ---: | ---: | ---: | ---: | -----------------: | -----------------: |
| NetVlad  | vgg16    | SuperPoint+LightGlue | 24.3 | 27.3 | 28.6 | 29.5 |              48:33 |               3.54 |
| NetVlad  | vgg16    | Superglue            | 24.8 | 27.1 | 28.4 | 29.5 |              19:58 |               1.46 |
| NetVlad  | vgg16    | LoFTR                | 25.3 | 27.8 | 28.7 | 29.5 |              50:20 |               3.67 |
| CosPlace | ResNet50 | SuperPoint+LightGlue | 72.2 | 75.8 | 77.4 | 78.6 |              50:10 |               3.66 |
| CosPlace | ResNet50 | Superglue            | 71.3 | 75.7 | 76.9 | 78.6 |              20:57 |               1.53 |
| CosPlace | ResNet50 | LoFTR                | 72.2 | 77.0 | 78.1 | 78.6 |              53:08 |               3.87 |
| MixVPR   | ResNet50 | SuperPoint+LightGlue | 81.2 | 85.7 | 86.4 | 87.4 |              50:06 |               3.65 |
| MixVPR   | ResNet50 | Superglue            | 81.0 | 85.7 | 86.9 | 87.4 |              20:54 |               1.52 |
| MixVPR   | ResNet50 | LoFTR                | 82.0 | 86.0 | 86.9 | 87.4 |              52:47 |               3.85 |
| MegaLoc  | DINOv2   | SuperPoint+LightGlue | 91.1 | 97.4 | 98.9 | 99.3 |              50:05 |               3.65 |
| MegaLoc  | DINOv2   | Superglue            | 90.5 | 97.6 | 98.7 | 99.3 |              21:03 |               1.53 |
| MegaLoc  | DINOv2   | LoFTR                | 92.6 | 98.5 | 99.0 | 99.3 |              52:49 |               3.85 |