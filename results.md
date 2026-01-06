Tokyo - XS
| Method   | Backbone | Metric      |  R@1 |  R@5 | R@10 | R@20 | TIME(mm:ss) |
| -------- | -------- | ----------- | ---: | ---: | ---: | ---: | ----------: |
| NetVlad  | vgg16    | L2          | 54.0 | 64.4 | 69.5 | 74.6 |       06:16 |
| NetVlad  | vgg16    | dot-product | 54.0 | 64.4 | 69.5 | 74.6 |       06:24 |
| CosPlace | ResNet50 | L2          | 73.3 | 83.8 | 87.9 | 91.4 |       03:55 |
| CosPlace | ResNet50 | dot-product | 73.3 | 83.8 | 87.9 | 91.4 |       03:29 |
| MixVPR   | ResNet50 | L2          | 76.5 | 88.6 | 92.1 | 94.3 |       02:31 |
| MixVPR   | ResNet50 | dot-product | 76.5 | 88.6 | 92.1 | 94.3 |       02:28 |
| MegaLoc  | DINOv2   | L2          | 95.6 | 97.8 | 98.7 | 99.0 |       22:27 |
| MegaLoc  | DINOv2   | dot-product | 95.6 | 97.8 | 98.7 | 99.0 |       22:15 |
SF-XS
| Method   | Backbone | Metric      |  R@1 |  R@5 | R@10 | R@20 | TIME(mm:ss) |
| -------- | -------- | ----------- | ---: | ---: | ---: | ---: | ----------: |
| NetVlad  | vgg16    | L2          | 42.2 | 53.7 | 60.8 | 65.3 |       13.30 |
| NetVlad  | vgg16    | dot-product | 42.2 | 53.7 | 60.8 | 65.3 |       13.16 |
| CosPlace | ResNet50 | L2          | 70.9 | 80.0 | 84.0 | 86.9 |       07.45 |
| CosPlace | ResNet50 | dot-product | 70.9 | 80.0 | 84.0 | 86.9 |       08.12 |
| MixVPR   | ResNet50 | L2          | 69.6 | 78.7 | 81.1 | 83.6 |       05.29 |
| MixVPR   | ResNet50 | dot-product | 69.6 | 78.7 | 81.1 | 83.6 |       05.28 |
| MegaLoc  | DINOv2   | L2          | 86.9 | 90.4 | 91.2 | 91.5 |       39.18 |
| MegaLoc  | DINOv2   | dot-product | 86.9 | 90.4 | 91.2 | 91.5 |       49.21 |
SVOX - Sun
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
SVOX - Night
| Method   | Backbone | Metric      |  R@1 |  R@5 | R@10 | R@20 | TIME(mm:ss) |
| -------- | -------- | ----------- | ---: | ---: | ---: | ---: | ----------: |
| NetVlad  | vgg16    | L2          | 8.5  | 18.2 | 22.7 | 28.5 |       08:39 |
| NetVlad  | vgg16    | dot-product | 8.5  | 18.2 | 22.7 | 28.5 |       08:41 |
| CosPlace | ResNet50 | L2          | 49.2 | 66.1 | 72.8 | 78.6 |       04:52 |
| CosPlace | ResNet50 | dot-product | 49.2 | 66.1 | 72.8 | 78.6 |       04:58 |
| MixVPR   | ResNet50 | L2          | 62.6 | 80.6 | 83.8 | 87.4 |       03:20 |
| MixVPR   | ResNet50 | dot-product | 62.6 | 80.6 | 83.8 | 87.4 |       03:21 |
| MegaLoc  | DINOv2   | L2          | 96.5 | 98.7 | 99.0 | 99.3 |       30:19 |
| MegaLoc  | DINOv2   | dot-product | 96.5 | 98.7 | 99.0 | 99.3 |       30:18 |
SVOX - Full
| Method   | Backbone | Metric      |  R@1 |  R@5 | R@10 | R@20 | TIME(mm:ss) |
| -------- | -------- | ----------- | ---: | ---: | ---: | ---: | ----------: |
| NetVlad  | vgg16    | L2          | 86.6 | 93.7 | 95.5 | 96.9 |       17:52 |
| NetVlad  | vgg16    | dot-product | 86.6 | 93.7 | 95.5 | 96.9 |       17:53 |
| CosPlace | ResNet50 | L2          | xx.x | xx.x | xx.x | xx.x |       xx:xx |
| CosPlace | ResNet50 | dot-product | xx.x | xx.x | xx.x | xx.x |       xx:xx |
| MixVPR   | ResNet50 | L2          | 97.8 | 98.9 | 99.2 | 99.3 |       06:55 |
| MixVPR   | ResNet50 | dot-product | 97.8 | 98.9 | 99.2 | 99.3 |       06:58 |
| MegaLoc  | DINOv2   | L2          | 98.7 | 99.5 | 99.6 | 99.7 |       55:49 |
| MegaLoc  | DINOv2   | dot-product | xx.x | xx.x | xx.x | xx.x |       xx:xx |