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