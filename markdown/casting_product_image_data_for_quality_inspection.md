# Casting Product Image Data for Quality Inspection

**Summary:** Grayscale top-view images of submersible pump impeller castings labelled defective or ok, with 7,348 augmented images split for training and testing.

| Parameter | Value |
| --- | --- |
| **Domain** | Manufacturing |
| **Asset / Process** | Castings and metal parts |
| **Modality** | Image |
| **Task** | Defect detection; Classification |
| **Annotation** | Sample label |
| **Source Type** | — |
| **Access** | Kaggle |
| **Size** | 7,348 images |
| **Year** | — |
| **License** | CC BY-ND and NC-ND |

## Description

This image set was collected to automate the quality inspection of cast products, which is otherwise done by hand. Every photo shows the top view of a submersible pump impeller and is sorted into one of two categories, defective or ok. The images were taken under a special arrangement for stable lighting, with support from PILOT TECHNOCAST of Shapar, Rajkot.

The main set holds 7,348 grayscale images of 300 x 300 pixels to which augmentation has already been applied. It is split into a training folder with 3,758 defective and 2,875 ok images and a test folder with 453 defective and 262 ok images. A second set of 512 x 512 grayscale images without augmentation has 781 defective and 519 ok impellers.

The stated goal is a deep learning classification model for the inspection task. The images are released under CC BY-NC-ND 4.0.

## References

- [Kaggle dataset](https://www.kaggle.com/datasets/ravirajsinh45/real-life-industrial-dataset-of-casting-product)
- [Industrial Atlas page](https://www.indatlas.com/datasets/casting-product-image-data-for-quality-inspection/)

[⬅️ Back to Index](../README.md)
