# MVTec AD 2

**Summary:** Expanded industrial anomaly detection benchmark with over 8,000 high-resolution images across eight new inspection scenarios, featuring varied lighting conditions and a partially private test set evaluated via an official server.

| Parameter | Value |
| --- | --- |
| **Associated Tasks** | Unsupervised Anomaly Detection, Anomaly Localisation, Segmentation |
| **Data Source** | Real |
| **Dataset Characteristics** | Image, Anomaly Detection, Domain Shift |
| **Date Donated** | 2025 |
| **Feature Type** | Images + Pixel Masks (public test) |
| **Labeled** | Partially |
| **Missing Values** | No |
| **Name** | MVTec AD 2 |
| **Number of Features** | Information not available |
| **Number of Instances** | 8000+ images across 8 scenarios |
| **Source** | https://www.mvtec.com/company/research/datasets/mvtec-ad-2 |
| **Time Series** | No |

## Description

MVTec AD 2 is the successor benchmark to the widely used MVTec AD dataset, extending it with eight entirely new inspection scenarios designed to challenge modern anomaly detection methods under more realistic conditions. Key novelties include varied lighting conditions between training and test sets (introducing a controlled domain shift) and a split test set where only the public portion has downloadable pixel-precise ground truth masks.

The dataset contains over 8,000 images totalling approximately 30.4 GB. For the public test set, pixel-precise anomaly masks are provided, enabling local evaluation. For the private test set, results must be submitted to the official MVTec evaluation server to obtain scores, ensuring a fair comparison of methods under held-out conditions.

MVTec AD 2 was introduced at arXiv in 2025 (Heckler-Kram et al., arXiv:2503.21622) and is licensed under CC BY-NC-SA 4.0 for non-commercial research use.

## Tags

Anomaly Detection, Benchmark Dataset, Domain Shift, Industrial Inspection, Lighting Variation, MVTec, Visual Quality Control

## References

- [Dataset page](https://www.mvtec.com/company/research/datasets/mvtec-ad-2)
- [Downloads](https://www.mvtec.com/company/research/datasets/mvtec-ad-2/downloads)
- [Paper (arXiv 2025)](https://arxiv.org/abs/2503.21622)

[⬅️ Back to Index](../README.md)
