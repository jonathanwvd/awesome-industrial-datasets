# AeBAD

**Summary:** Single-blade images with ground-truth masks plus blade videos, in which normal test samples differ from training ones mainly in illumination and view.

| Parameter | Value |
| --- | --- |
| **Domain** | Aerospace and defense |
| **Asset / Process** | Turbines and engines |
| **Modality** | Image; Video |
| **Task** | Anomaly detection; Anomaly localization |
| **Annotation** | Normal-only training; Pixel mask |
| **Source Type** | — |
| **Access** | Code repository |
| **Size** | — |
| **Year** | 2023 |
| **License** | CC BY |

## Description

AeBAD (Aero-engine Blade Anomaly Detection) is a dataset of aero-engine blade images and videos released with the 2023 paper "Industrial Anomaly Detection with Domain Shift: A Real-world Dataset and Masked Multi-scale Reconstruction" by Zilong Zhang, Zhibin Zhao, Xingwu Zhang, Chuang Sun and Xuefeng Chen. The same repository holds the PyTorch implementation of the paper's MMR method.

AeBAD has two parts: AeBAD-S, a single-blade image set with ground-truth masks, and AeBAD-V, a video set of blades. Training data holds only good samples. The target samples are not aligned and appear at different scales, and the normal test samples are shifted in illumination, view and background relative to training.

AeBAD-S is evaluated with sample-level AUROC, pixel-level AUROC and PRO, while AeBAD-V uses only the sample-level metric. The data is downloadable from Google Drive or Tian Yi Yun Pan and is released under CC BY 4.0; the code is under Apache 2.0.

## References

- [GitHub repository](https://github.com/zhangzilongc/MMR)
- [Industrial Atlas page](https://www.indatlas.com/datasets/aebad/)

[⬅️ Back to Index](../README.md)
