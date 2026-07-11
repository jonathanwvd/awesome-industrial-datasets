# Kolektor Surface-Defect Dataset (KolektorSDD)

**Summary:** The dataset is constructed from images of defective production items that were provided and annotated by Kolektor Group d.o.o. in a controlled industrial environment in a real-world case.

| Parameter | Value |
| --- | --- |
| **Dataset** | Kolektor Surface-Defect Dataset (KolektorSDD) |
| **Domain** | Materials & Metrology; Manufacturing & Production |
| **Asset / Process** | Surface Defects |
| **Modality** | Image |
| **Task** | Defect Detection; Defect Segmentation; Classification |
| **Annotation** | Sample Label; Pixel Mask |
| **Source Type** | Real Lab / Testbed |
| **Access** | Official Portal |
| **Size** | 399 |
| **Year** | Information not available |
| **License** | CC BY |

## Description

The Kolektor Surface-Defect Dataset consists of 399 images of production items, including 52 images with visible defects and 347 images without any defects. Original images have a width of 500 pixels and height varying from 1240 to 1270 pixels. For training and evaluation, images should be resized to 512 x 1408 pixels. Each item has at least one image where the defect is visible, with two items having defects on two images. The dataset provides negative examples with non-defective surfaces for robust model training.

The dataset has been annotated with fine and box annotations available for download to support several research papers. It is split into three folds for 3-fold cross-validation, with prepared TensorFlow datasets available. The dataset is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License, and commercial use requires contacting Danijel Skočaj. The dataset is used for defect detection in industrial surface images and supports segmentation-based deep-learning approaches.

## References

- [ViCoS Lab KolektorSDD Dataset](https://go.vicos.si/kolektorsdd)
- [Journal of Intelligent Manufacturing Paper](https://prints.vicos.si/publications/370)
- [Creative Commons License](http://creativecommons.org/licenses/by-nc-sa/4.0/)

[⬅️ Back to Index](../README.md)
