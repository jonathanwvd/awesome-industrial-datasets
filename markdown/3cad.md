# 3CAD

**Summary:** 27,039 high-resolution images of eight aluminum, copper and iron parts, split into training and test sets, with pixel-level anomaly labels across 47 defect types.

| Parameter | Value |
| --- | --- |
| **Domain** | Electronics and semiconductors |
| **Asset / Process** | Castings and metal parts |
| **Modality** | Image |
| **Task** | Anomaly detection; Anomaly localization |
| **Annotation** | Pixel mask; Sample label |
| **Source Type** | Real production |
| **Access** | — |
| **Size** | 27,039 images in 8 part categories |
| **Year** | 2025 |
| **License** | — |

## Description

3CAD is an image dataset for unsupervised anomaly detection in 3C product quality control, presented at AAAI 2025 by Enquan Yang, Peng Xing, Hanyang Sun, Wenbo Guo, Yuanwei Ma, Zechao Li and Dan Zeng. Its images come from real 3C production lines, drawn from segmentation data that a company accumulated over several years of production line projects.

The 27,039 images cover eight manufactured parts, including an aluminum camera cover, aluminum middle frames, and copper and iron stators. They split into 10,493 training and 16,546 test images, of which 5,084 test images are good and 11,462 defective. Anomalies are labeled at pixel level across 47 defect types, and one defective image can hold several anomalous regions and several anomaly types.

The repository also provides CFRG, a coarse-to-fine detection framework with recovery guidance, and reports P-AUROC, AP, I-AUROC and P-PRO results of common anomaly detection methods on each category.

## References

- [GitHub repository](https://github.com/EnquanYang2022/3CAD)
- [Industrial Atlas page](https://www.indatlas.com/datasets/3cad/)

[⬅️ Back to Index](../README.md)
