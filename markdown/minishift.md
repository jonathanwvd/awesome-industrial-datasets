# MiniShift

High-resolution 3D anomaly detection dataset of 2,577 point clouds with 500,000 points each and subtle generated defects covering less than 1% of the surface.

- **Domain:** Manufacturing
- **Modality:** 3D point cloud
- **Task:** Anomaly detection; Anomaly localization
- **Access:** Hugging Face
- **Size:** 2,577 point clouds, 12 categories
- **Year:** 2025
- **License:** Apache 2.0

## Description

MiniShift is a dataset for high-resolution 3D anomaly detection on industrial parts, published with a paper accepted as an oral at AAAI 2026. Its authors argue that subtle defects need dense spatial data, while common point cloud benchmarks use low-resolution inputs.

The dataset holds 2,577 point clouds, each with 500,000 points, in 12 categories with 4 defect types. The anomalies were made with an anchor-guided geometric synthesis pipeline that produces realistic, subtle defects occupying less than 1% of the points. The Hugging Face copy totals 38.9 GB, and a Baidu Drive mirror is also offered.

The same repository provides Simple3D, a detection framework built on multi-scale neighborhood descriptors and local feature aggregation that runs at more than 20 fps. The paper first appeared on arXiv in 2025.

## References

- [GitHub repository](https://github.com/hustcyq/MiniShift-Simple3D)
- [Hugging Face dataset](https://huggingface.co/datasets/ChengYuQi99/MiniShift)
- [Industrial Atlas page](https://www.indatlas.com/datasets/minishift/)

[⬅️ Back to Index](../README.md)
