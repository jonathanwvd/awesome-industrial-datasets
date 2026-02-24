# BTAD

**Summary:** Real-world industrial surface and body defect dataset with three product types and pixel-precise ground truth annotations, captured from industrial image acquisition systems with privacy-preserving transformations.

| Parameter | Value |
| --- | --- |
| **Associated Tasks** | Anomaly Detection, Anomaly Localisation, Segmentation |
| **Data Source** | Real |
| **Dataset Characteristics** | Image, Anomaly Detection, Defect Segmentation |
| **Date Donated** | 2021 |
| **Feature Type** | RGB Images + Pixel Masks |
| **Labeled** | Yes |
| **Missing Values** | No |
| **Name** | BTAD |
| **Number of Features** | Information not available |
| **Number of Instances** | 1799 images across 3 product types (Product1: 400 @ 1600x1600; Product2: 1000 @ 600x600; Product3: 399 @ 800x600) |
| **Source** | https://github.com/pankajmishra000/VT-ADL |
| **Time Series** | No |

## Description

BTAD (BeanTech Anomaly Detection Dataset) is a real-world industrial benchmark released to support anomaly detection and localisation research. The dataset contains images of three different product types captured using industrial image acquisition systems. To preserve industrial privacy, the images were cropped and log-transformed before release. Pixel-precise anomaly masks are provided for all anomalous test images.

The three product types have different image resolutions and quantities: Product 1 (400 images at 1600×1600 pixels), Product 2 (1,000 images at 600×600 pixels), and Product 3 (399 images at 800×600 pixels). Each product type has dedicated training (normal only) and test (normal and anomalous) splits following the standard MVTec-style protocol.

BTAD was introduced at ISIE 2021 (Mishra et al., VT-ADL: A Vision Transformer Network for Image Anomaly Detection and Localisation) and is licensed under CC BY-SA.

## Tags

Defect Detection, Industrial Anomaly Detection, Manufacturing Inspection, Real-World Dataset, Segmentation Masks, Surface Defects, Visual Quality Control

## References

- [GitHub (VT-ADL dataset + code)](https://github.com/pankajmishra000/VT-ADL)
- [Dataset download page](https://avires.dimi.uniud.it/)

[⬅️ Back to Index](../README.md)
