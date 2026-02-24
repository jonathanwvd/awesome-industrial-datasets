# VisA

**Summary:** Multi-object industrial anomaly detection dataset with 10,821 images, image-level labels and pixel-level anomaly masks across 12 object subsets, including PCB inspection and multiple-instance scenes.

| Parameter | Value |
| --- | --- |
| **Associated Tasks** | Anomaly Detection, Anomaly Segmentation, Localisation |
| **Data Source** | Real |
| **Dataset Characteristics** | Image, Anomaly Detection, Multi-Class |
| **Date Donated** | 2022 |
| **Feature Type** | RGB Images + Annotation Masks |
| **Labeled** | Yes |
| **Missing Values** | No |
| **Name** | VisA |
| **Number of Features** | Information not available |
| **Number of Instances** | 10821 images (9621 normal; 1200 anomalous) across 12 subsets |
| **Source** | https://github.com/amazon-science/spot-diff |
| **Time Series** | No |

## Description

VisA (Visual Anomaly) is a large-scale industrial anomaly detection and segmentation dataset released by Amazon Science. The dataset contains 10,821 images distributed across 12 object subsets, of which 9,621 are normal and 1,200 are anomalous. For all anomalous images, pixel-level segmentation masks are provided. Both image-level labels and pixel-level annotations are available, enabling evaluation of both classification and localisation performance.

The 12 object subsets span a diverse range of industrial objects, including printed circuit boards (PCBs), mechanical parts, and objects that appear as multiple instances in a single image. This diversity—especially the multiple-instance subsets—makes VisA more challenging than single-object benchmarks and closer to real inspection scenarios.

VisA was introduced at ECCV 2022 (Zou et al., SPot-the-Difference Self-Supervised Pre-training) and is hosted on AWS S3 with an open data registry entry. The dataset is licensed under CC BY 4.0.

## Tags

Anomaly Detection, Image Segmentation, Industrial Inspection, Multi-Object Benchmark, Open Dataset, PCB Inspection, Visual Quality Control

## References

- [GitHub repository](https://github.com/amazon-science/spot-diff)
- [AWS Open Data Registry](https://registry.opendata.aws/amazon-visual-anomaly/)
- [Paper (arXiv / ECCV 2022)](https://arxiv.org/abs/2207.14315)

[⬅️ Back to Index](../README.md)
