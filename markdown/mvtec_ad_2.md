# MVTec AD 2

**Summary:** Expanded industrial anomaly detection benchmark with over 8,000 high-resolution images across eight new inspection scenarios, featuring varied lighting conditions and a partially private test set evaluated via an official server.

| Parameter | Value |
| --- | --- |
| **Dataset** | MVTec AD 2 |
| **Domain** | Manufacturing & Production |
| **Asset / Process** | Surface Defects |
| **Modality** | Image |
| **Task** | Anomaly Detection; Anomaly Localization; Defect Segmentation; Quality Prediction |
| **Annotation** | Normal-Only Training; Sample Label; Pixel Mask; Partial |
| **Source Type** | Real Lab / Testbed |
| **Access** | Official Portal; Form Request; Gated Approval |
| **Size** | 8000+ images across 8 scenarios |
| **Year** | 2025 |
| **License** | CC BY-NC-SA |

## Description

MVTec AD 2 is the successor benchmark to the widely used MVTec AD dataset, extending it with eight entirely new inspection scenarios designed to challenge modern anomaly detection methods under more realistic conditions. Key novelties include varied lighting conditions between training and test sets (introducing a controlled domain shift) and a split test set where only the public portion has downloadable pixel-precise ground truth masks.

The dataset contains over 8,000 images totalling approximately 30.4 GB. For the public test set, pixel-precise anomaly masks are provided, enabling local evaluation. For the private test set, results must be submitted to the official MVTec evaluation server to obtain scores, ensuring a fair comparison of methods under held-out conditions.

MVTec AD 2 was introduced at arXiv in 2025 (Heckler-Kram et al., arXiv:2503.21622) and is licensed under CC BY-NC-SA 4.0 for non-commercial research use.

## References

- [Dataset page](https://www.mvtec.com/company/research/datasets/mvtec-ad-2)
- [Downloads](https://www.mvtec.com/company/research/datasets/mvtec-ad-2/downloads)
- [Paper (arXiv 2025)](https://arxiv.org/abs/2503.21622)

[⬅️ Back to Index](../README.md)
