# CXR-AD

X-ray images of five industrial component categories with 653 normal and 561 defect samples, the defects marked by pixel-level masks.

- **Domain:** Manufacturing
- **Modality:** X-ray and CT
- **Task:** Anomaly detection; Anomaly localization
- **Annotation:** Sample label; Pixel mask
- **Size:** 653 normal and 561 defect samples
- **Year:** 2025

## Description

CXR-AD (Component X-ray Image Dataset for Industrial Anomaly Detection) is a collection of real-world X-ray images for detecting internal defects in industrial components. It was described in an arXiv preprint submitted in May 2025 by Haoyu Bai, Jie Wang, Gaomin Li, Xuan Li, Xiaohu Zhang and Xia Yang.

The images cover five component categories, with 653 normal samples and 561 defect samples. Each defect sample carries a pixel-level mask. The authors name three difficulties in the data: complex internal structures that are strongly coupled with defect regions, low contrast and heavy noise in X-ray imaging, and wide variation in defect scale and shape.

Three anomaly detection approaches were tested on it: feature-based, reconstruction-based and zero-shot. Their performance was on average 29.78% lower than on MVTec AD.

## References

- [Preprint (arXiv)](https://arxiv.org/abs/2505.03412)
- [Industrial Atlas page](https://www.indatlas.com/datasets/cxr-ad/)

[⬅️ Back to Index](../README.md)
