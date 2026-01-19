**Tokyo - XS**
| Method   | Backbone | Metric      |  R@1 |  R@5 | R@10 | R@20 | TIME(mm:ss) |
| -------- | -------- | ----------- | ---: | ---: | ---: | ---: | ----------: |
| NetVlad  | vgg16    | L2          | 54.0 | 64.4 | 69.5 | 74.6 |       06:06 |
| NetVlad  | vgg16    | dot-product | 54.0 | 64.4 | 69.5 | 74.6 |       06:02 |
| CosPlace | ResNet50 | L2          | 73.3 | 83.8 | 87.9 | 91.4 |       03:32 |
| CosPlace | ResNet50 | dot-product | 73.3 | 83.8 | 87.9 | 91.4 |       03:29 |
| MixVPR   | ResNet50 | L2          | 76.5 | 88.6 | 92.1 | 94.3 |       02:27 |
| MixVPR   | ResNet50 | dot-product | 76.5 | 88.6 | 92.1 | 94.3 |       02:24 |
| MegaLoc  | DINOv2   | L2          | 95.6 | 97.8 | 98.7 | 99.0 |       21:29 |
| MegaLoc  | DINOv2   | dot-product | 95.6 | 97.8 | 98.7 | 99.0 |       21:35 |

**Tokyo-XS (L2) - Image Matching**
| Method   | Backbone | Matcher              |  R@1 |  R@5 | R@10 | R@20 | TIME(mm:ss) |
| -------- | -------- | -------------------- | ---: | ---: | ---: | ---: | ----------: |
| NetVlad  | vgg16    | SuperPoint+LightGlue | 68.9 | 71.7 | 73.0 | 74.6 |       18:42 |
| NetVlad  | vgg16    | Superglue            | 67.0 | 71.1 | 72.7 | 74.6 |       07:34 |
| NetVlad  | vgg16    | LoFTR                | 68.9 | 70.8 | 73.0 | 74.6 |       19:41 |
| CosPlace | ResNet50 | SuperPoint+LightGlue | 86.0 | 89.2 | 89.8 | 91.4 |       18:43 |
| CosPlace | ResNet50 | Superglue            | 84.8 | 88.6 | 90.2 | 91.4 |       07:25 |
| CosPlace | ResNet50 | LoFTR                | 86.7 | 89.2 | 90.5 | 91.4 |       19:42 |
| MixVPR   | ResNet50 | SuperPoint+LightGlue | 89.2 | 92.4 | 94.0 | 94.3 |       18:41 |
| MixVPR   | ResNet50 | Superglue            | 87.0 | 92.4 | 93.3 | 94.3 |       07:33 |
| MixVPR   | ResNet50 | LoFTR                | 90.5 | 92.7 | 94.0 | 94.3 |       19:44 |
| MegaLoc  | DINOv2   | SuperPoint+LightGlue | 94.3 | 98.4 | 98.7 | 99.0 |       18:16 |
| MegaLoc  | DINOv2   | Superglue            | 93.0 | 98.1 | 98.4 | 99.0 |       07:25 |
| MegaLoc  | DINOv2   | LoFTR                | 94.3 | 97.8 | 98.7 | 99.0 |       19:05 |


**SF-XS**
| Method   | Backbone | Metric      |  R@1 |  R@5 | R@10 | R@20 | TIME(mm:ss) |
| -------- | -------- | ----------- | ---: | ---: | ---: | ---: | ----------: |
| NetVlad  | vgg16    | L2          | 42.2 | 53.7 | 60.8 | 65.3 |       13:26 |
| NetVlad  | vgg16    | dot-product | 42.2 | 53.7 | 60.8 | 65.3 |       13:11 |
| CosPlace | ResNet50 | L2          | 70.9 | 80.0 | 84.0 | 86.9 |       07:43 |
| CosPlace | ResNet50 | dot-product | 70.9 | 80.0 | 84.0 | 86.9 |       08:10 |
| MixVPR   | ResNet50 | L2          | 69.6 | 78.7 | 81.1 | 83.6 |       05:24 |
| MixVPR   | ResNet50 | dot-product | 69.6 | 78.7 | 81.1 | 83.6 |       05:04 |
| MegaLoc  | DINOv2   | L2          | 86.9 | 90.4 | 91.2 | 91.5 |       49:12 |
| MegaLoc  | DINOv2   | dot-product | 86.9 | 90.4 | 91.2 | 91.5 |       49:13 |

**SVOX - Sun**
| Method   | Backbone | Metric      |  R@1 |  R@5 | R@10 | R@20 | TIME(mm:ss) |
| -------- | -------- | ----------- | ---: | ---: | ---: | ---: | ----------: |
| NetVlad  | vgg16    | L2          | 37.1 | 54.4 | 62.2 | 69.0 |       08:29 |
| NetVlad  | vgg16    | dot-product | 37.1 | 54.4 | 62.2 | 69.0 |       08:33 |
| CosPlace | ResNet50 | L2          | 77.0 | 89.0 | 92.4 | 95.0 |       04:52 |
| CosPlace | ResNet50 | dot-product | 77.0 | 89.0 | 92.4 | 95.0 |       04:50 |
| MixVPR   | ResNet50 | L2          | 84.4 | 92.7 | 94.6 | 95.4 |       03:12 |
| MixVPR   | ResNet50 | dot-product | 84.4 | 92.7 | 94.6 | 95.4 |       03:13 |
| MegaLoc  | DINOv2   | L2          | 97.2 | 99.3 | 99.5 | 99.6 |       30:12 |
| MegaLoc  | DINOv2   | dot-product | 97.2 | 99.3 | 99.5 | 99.6 |       30:02 |

**SVOX - Night**
| Method   | Backbone | Metric      |  R@1 |  R@5 | R@10 | R@20 | TIME(mm:ss) |
| -------- | -------- | ----------- | ---: | ---: | ---: | ---: | ----------: |
| NetVlad  | vgg16    | L2          |  8.5 | 18.2 | 22.7 | 28.5 |       08:36 |
| NetVlad  | vgg16    | dot-product |  8.5 | 18.2 | 22.7 | 28.5 |       08:38 |
| CosPlace | ResNet50 | L2          | 49.2 | 66.1 | 72.8 | 78.6 |       04:57 |
| CosPlace | ResNet50 | dot-product | 49.2 | 66.1 | 72.8 | 78.6 |       04:57 |
| MixVPR   | ResNet50 | L2          | 62.6 | 80.6 | 83.8 | 87.4 |       03:17 |
| MixVPR   | ResNet50 | dot-product | 62.6 | 80.6 | 83.8 | 87.4 |       03:18 |
| MegaLoc  | DINOv2   | L2          | 96.5 | 98.7 | 99.0 | 99.3 |       30:14 |
| MegaLoc  | DINOv2   | dot-product | 96.5 | 98.7 | 99.0 | 99.3 |       30:13 |

**SVOX - Full**
| Method   | Backbone | Metric      |  R@1 |  R@5 | R@10 | R@20 | TIME(mm:ss) |
| -------- | -------- | ----------- | ---: | ---: | ---: | ---: | ----------: |
| NetVlad  | vgg16    | L2          | 86.6 | 93.7 | 95.5 | 96.9 |       17:52 |
| NetVlad  | vgg16    | dot-product | 86.6 | 93.7 | 95.5 | 96.9 |       17:53 |
| CosPlace | ResNet50 | L2          | 97.1 | 98.4 | 98.7 | 99.0 |       08:22 |
| CosPlace | ResNet50 | dot-product | 97.1 | 98.4 | 98.7 | 99.0 |       08:23 |
| MixVPR   | ResNet50 | L2          | 97.8 | 98.9 | 99.2 | 99.3 |       06:55 |
| MixVPR   | ResNet50 | dot-product | 97.8 | 98.9 | 99.2 | 99.3 |       06:58 |
| MegaLoc  | DINOv2   | L2          | 98.7 | 99.5 | 99.6 | 99.7 |       55:49 |
| MegaLoc  | DINOv2   | dot-product | 98.7 | 99.5 | 99.6 | 99.7 |       52:55 |