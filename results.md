Tokyo - XS
| Method   | Backbone | Metric      |  R@1 |  R@5 | R@10 | R@20 |
| -------- | -------- | ----------- | ---: | ---: | ---: | ---: |
| NetVlad  | vgg16    | L2          | 54.0 | 64.4 | 69.5 | 74.6 |
| NetVlad  | vgg16    | dot-product | 54.0 | 64.4 | 69.5 | 74.6 |
| CosPlace | ResNet50 | L2          | 73.3 | 83.8 | 87.9 | 91.4 |
| CosPlace | ResNet50 | dot-product | 73.3 | 83.8 | 87.9 | 91.4 |
| MixVPR   | ResNet50 | L2          | 76.5 | 88.6 | 92.1 | 94.3 |
| MixVPR   | ResNet50 | dot-product | 76.5 | 88.6 | 92.1 | 94.3 |
| MegaLoc  | DINOv2   | L2          | 95.6 | 97.8 | 98.7 | 99.0 |
| MegaLoc  | DINOv2   | dot-product | 95.6 | 97.8 | 98.7 | 99.0 |
SF-XS
| Method   | Backbone | Metric      |  R@1 |  R@5 | R@10 | R@20 | TIME(min) |
| -------- | -------- | ----------- | ---: | ---: | ---: | ---: | ---: |
| NetVlad  | vgg16    | L2          | 42.5 | 53.7 | 60.8 | 65.3 |      |
| NetVlad  | vgg16    | dot-product | 42.5 | 53.7 | 60.8 | 65.3 |      |
| CosPlace | ResNet50 | L2          | 70.9 | 80.0 | 84.0 | 86.9 |      |
| CosPlace | ResNet50 | dot-product | 70.9 | 80.0 | 84.0 | 86.9 |      |
| MixVPR   | ResNet50 | L2          | 69.6 | 78.7 | 81.1 | 83.6 |      |
| MixVPR   | ResNet50 | dot-product | 69.6 | 78.7 | 81.1 | 83.6 |      |
| MegaLoc  | DINOv2   | L2          | 86.9 | 90.4 | 91.2 | 91.5 |      |
| MegaLoc  | DINOv2   | dot-product | 86.9 | 90.4 | 91.2 | 91.5 |      |