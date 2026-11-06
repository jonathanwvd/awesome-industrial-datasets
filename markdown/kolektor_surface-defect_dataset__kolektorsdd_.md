# Kolektor Surface-Defect Dataset (KolektorSDD)

Surface-defect segmentation images of production items from Kolektor Group, with fine or box annotations and files that divide it into three cross-validation folds.

- **Domain:** Manufacturing
- **Asset / Process:** Surfaces and textures
- **Modality:** Image
- **Task:** Defect detection; Defect segmentation
- **Annotation:** Pixel mask; Bounding box; Sample label
- **Source Type:** Real production
- **Access:** Direct download
- **Size:** 399 images (52 defective, 347 defect-free)
- **Year:** 2019
- **License:** CC BY-NC-SA
- **Publisher:** ViCoS Lab

## Description

The Kolektor Surface-Defect Dataset (KolektorSDD) is an image set of defective production items that Kolektor Group d.o.o. provided and annotated. The images were taken in a controlled industrial environment, and the dataset is published by the ViCoS Lab together with the Journal of Intelligent Manufacturing paper "Segmentation-Based Deep-Learning Approach for Surface-Defect Detection" by Tabernik, Šela, Skvarč and Skočaj (2019).

It holds 399 images: 52 show a visible defect and 347 show defect-free surfaces used as negative examples. The originals are 500 px wide and 1240 to 1270 px high, and the publisher advises resizing them to 512 x 1408 px for training and evaluation. Two versions are offered, one with fine annotations and one with box annotations.

The authors divided the images into three folds for 3-fold cross-validation; the fold files and a TensorFlow version already split into those folds can be downloaded. The license is CC BY-NC-SA 4.0, and commercial use requires a separate agreement with Danijel Skočaj.

## References

- [Official page](https://www.vicos.si/resources/kolektorsdd/)
- [Industrial Atlas page](https://www.indatlas.com/datasets/kolektor-surface-defect-dataset-kolektorsdd/)

[⬅️ Back to Index](../README.md)
