# Real3D-AD

**Summary:** High-precision 3D point-cloud anomaly detection benchmark with 1,254 scanned samples of 12 object categories and point-level ground truth.

| Parameter | Value |
| --- | --- |
| **Domain** | Manufacturing |
| **Asset / Process** | — |
| **Modality** | 3D point cloud |
| **Task** | Anomaly detection; Anomaly localization |
| **Annotation** | Normal-only training; 3D point mask |
| **Source Type** | Lab or testbed |
| **Access** | Code repository |
| **Size** | 1,254 samples in 12 categories |
| **Year** | 2023 |
| **License** | — |
| **Publisher** | Jiaqi Liu et al. |
| **Benchmark** | Yes |

## Description

Real3D-AD is a point-cloud anomaly detection dataset by Jiaqi Liu, Guoyang Xie and co-authors, presented in the NeurIPS 2023 Datasets and Benchmarks Track. The objects were scanned with a PMAX-S130 optical system while a turntable completed a full 360° revolution, and further samples were made by copying and cutting edges.

The 1,254 samples cover 12 categories, including Airplane, Car, Candybar, Diamond, Gemstone, Seahorse, Shell, Starfish and Toffees. Training uses 4 defect-free prototypes per category; the test sets hold anomalies of two kinds, incompleteness and redundancy (for example bulges and sinks), with ground truth annotated in CloudCompare. Data is distributed in PCD format and as source PLY files from the camera.

Object-level and point-level detection are scored with AUROC, and point-level results are also reported as AUPR. Downloads of both formats are linked from the GitHub repository.

## References

- [GitHub repository](https://github.com/M-3LAB/Real3D-AD)
- [Preprint (arXiv)](https://arxiv.org/abs/2309.13226)
- [Industrial Atlas page](https://www.indatlas.com/datasets/real3d-ad/)

[⬅️ Back to Index](../README.md)
