# Real-IAD

**Summary:** Large-scale real-world multi-view industrial anomaly detection dataset from a production line, with 150,000+ images across 30 objects at 1024×1024 resolution, distributed via Hugging Face.

| Parameter | Value |
| --- | --- |
| **Associated Tasks** | Industrial Anomaly Detection, Multi-View Evaluation |
| **Data Source** | Real |
| **Dataset Characteristics** | Image, Multi-View, Large-Scale, Anomaly Detection |
| **Date Donated** | 2024 |
| **Feature Type** | Multi-View RGB Images + JSON Split Metadata |
| **Labeled** | Yes |
| **Missing Values** | No |
| **Name** | Real-IAD |
| **Number of Features** | Information not available |
| **Number of Instances** | 150000+ high-resolution images across 30 object categories |
| **Source** | https://realiad4ad.github.io/Real-IAD/ |
| **Time Series** | No |

## Description

Real-IAD is a large-scale industrial anomaly detection dataset captured from a real production line using a multi-view acquisition pipeline. The dataset contains over 150,000 high-resolution images (1024×1024 in the standard release) across 30 industrial object categories, with multiple defect types per category. Annotations include image-level labels and pixel-level masks for anomalous samples.

The acquisition pipeline proceeds through material preparation, prototype selection, multi-view capture, annotation, and data cleaning stages. Multiple camera viewpoints per object enable evaluation of multi-view fusion methods. JSON split files are provided for standardised evaluation. The 1024×1024 version is approximately 53 GB; raw high-resolution data is approximately 507 GB.

Real-IAD was presented at CVPR 2024 and is distributed via Hugging Face (gated access requiring agreement to data sharing terms). It is licensed under CC BY-NC-SA 4.0 for non-commercial research use.

## Tags

Defect Detection, Industrial Vision, Large-Scale Anomaly Detection, Manufacturing Quality Control, Multi-View Inspection, Non-Commercial, Real Production Line

## References

- [Project page](https://realiad4ad.github.io/Real-IAD/)
- [Hugging Face dataset](https://huggingface.co/datasets/Real-IAD/Real-IAD)
- [Paper (arXiv / CVPR 2024)](https://arxiv.org/abs/2403.12580)

[⬅️ Back to Index](../README.md)
