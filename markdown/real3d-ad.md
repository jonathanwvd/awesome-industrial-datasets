# Real3D-AD

**Summary:** High-precision 3D point-cloud industrial anomaly detection benchmark with 1,254 samples across 12 object categories, per-sample ground truth annotations, and CC BY 4.0 licensing.

| Parameter | Value |
| --- | --- |
| **Dataset** | Real3D-AD |
| **Domain** | Materials & Metrology; Manufacturing & Production |
| **Asset / Process** | Surface Defects |
| **Modality** | Image; 3D Point Cloud |
| **Task** | Anomaly Detection; Anomaly Localization; 3D Understanding |
| **Annotation** | Normal-Only Training; Sample Label; 3D / Point Mask |
| **Source Type** | Real Lab / Testbed |
| **Access** | Repository; Direct Download |
| **Size** | 1254 samples across 12 categories |
| **Year** | 2023 |
| **License** | CC BY |

## Description

Real3D-AD is the first large-scale benchmark dedicated to 3D point-cloud anomaly detection in precision manufacturing and metrology applications. The dataset contains 1,254 samples across 12 industrial object categories. 3D data was acquired using high-precision optical scanning with turntable rotation to achieve complete 360° coverage of each object. Normal training prototypes and anomalous test samples (with per-sample ground truth files) are provided in PCD and PLY formats.

Anomaly types include bulge and sink deformations representing common manufacturing defects at the sub-millimetre scale. The dataset thus targets applications where visual inspection alone is insufficient and high-resolution 3D geometry is required. Unlike synthetic point-cloud datasets, Real3D-AD uses genuine industrial objects scanned in controlled conditions.

Real3D-AD was presented at NeurIPS 2023 Datasets & Benchmarks (arXiv:2309.13226) and is licensed under CC BY 4.0, permitting broad research use.

## References

- [GitHub repository + downloads](https://github.com/M-3LAB/Real3D-AD)
- [Paper (arXiv / NeurIPS 2023)](https://arxiv.org/abs/2309.13226)

[⬅️ Back to Index](../README.md)
