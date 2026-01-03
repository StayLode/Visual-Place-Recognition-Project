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
| NetVlad  | vgg16    | L2          | 42.5 | 53.7 | 60.8 | 65.3 |             |
| NetVlad  | vgg16    | dot-product | 42.5 | 53.7 | 60.8 | 65.3 |             |
| CosPlace | ResNet50 | L2          | 70.9 | 80.0 | 84.0 | 86.9 |             |
| CosPlace | ResNet50 | dot-product | 70.9 | 80.0 | 84.0 | 86.9 |             |
| MixVPR   | ResNet50 | L2          | 69.6 | 78.7 | 81.1 | 83.6 |             |
| MixVPR   | ResNet50 | dot-product | 69.6 | 78.7 | 81.1 | 83.6 |             |
| MegaLoc  | DINOv2   | L2          | 86.9 | 90.4 | 91.2 | 91.5 |             |
| MegaLoc  | DINOv2   | dot-product | 86.9 | 90.4 | 91.2 | 91.5 |             |
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