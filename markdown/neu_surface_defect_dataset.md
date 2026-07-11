# NEU Surface Defect Dataset

**Summary:** Northeastern University surface defect dataset with 1,800 grayscale images (200×200 px) of 6 hot-rolled steel strip defect types (crazing, inclusion, patches, pitted surface, rolled-in scale, scratches); 300 images per class.

| Parameter | Value |
| --- | --- |
| **Dataset** | NEU Surface Defect Dataset |
| **Domain** | Materials & Metrology; Manufacturing & Production |
| **Asset / Process** | Steel / Metal Surfaces; Materials / Chemistry |
| **Modality** | Image |
| **Task** | Defect Detection; Defect Segmentation; Classification |
| **Annotation** | Bounding Box; Fault Type Label; Sample Label; Class Label |
| **Source Type** | Real Lab / Testbed |
| **Access** | Official Portal |
| **Size** | 1,800 grayscale images; 300 images per class across 6 defect types |
| **Year** | 2013 |
| **License** | Information not available |

## Description

The NEU Surface Defect Database was created at Northeastern University (NEU), China, and contains images of six common surface defect types found on hot-rolled steel strips:

1. Crazing — network of fine surface cracks
2. Inclusion — foreign material embedded in the steel surface
3. Patches — irregular blotchy surface areas
4. Pitted Surface — small pits or holes
5. Rolled-in Scale — scale pressed into the steel surface
6. Scratches — linear surface scratches

The dataset contains 1,800 grayscale images total, with exactly 300 images per defect class. All images are 200×200 pixels. Inter-class and intra-class variability is significant due to variations in illumination and surface condition, making this a challenging classification benchmark.

An object detection version also exists with bounding box annotations (NEU-DET). The dataset has been widely used in deep learning research for steel surface defect detection and classification, and has been extended to include segmentation annotations in later works.

## References

- [NEU Surface Defect Database (Official Page)](http://faculty.neu.edu.cn/songkechen/zh_CN/zdylm/263270/list/index.htm)
- [Original Paper: A noise robust method based on completed LBP for hot-rolled steel strip surface defects (2013)](https://doi.org/10.1016/j.patcog.2013.05.001)

[⬅️ Back to Index](../README.md)
