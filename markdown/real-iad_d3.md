# Real-IAD D3

**Summary:** Aligned RGB images, photometric-stereo pseudo-3D data and point clouds of 8,450 samples across 20 product categories and 69 defect types for industrial anomaly detection research.

| Parameter | Value |
| --- | --- |
| **Domain** | Manufacturing |
| **Asset / Process** | — |
| **Modality** | Image; 3D point cloud; Multimodal |
| **Task** | Defect detection; Anomaly localization |
| **Annotation** | — |
| **Source Type** | — |
| **Access** | Hugging Face |
| **Size** | 8,450 samples |
| **Year** | 2025 |
| **License** | Academic or non-commercial terms |

## Description

Real-IAD D3 is a multimodal dataset for industrial anomaly detection that combines 2D RGB images, pseudo-3D surface information and 3D point clouds of the same samples. It was presented at CVPR 2025 by Wenbing Zhu, Lidong Wang, Ziqing Zhou and co-authors, together with D³M, a method that combines all three modalities for detection and localization.

The 8,450 samples cover 20 compact industrial product categories and 69 defect types. One acquisition system takes 3,648 × 5,472 RGB images, lights each sample from four directions for photometric stereo and reconstructs point clouds. Each point cloud resolves 0.01 mm with a precision of 0.002 mm per point, and ASC, PLY, STL, OBJ, IGES and TIFF files are available. Pseudo-3D data captures small height and normal variations.

The dataset is released for research purposes. Access is requested on Hugging Face, where users accept its conditions.

## References

- [Official page](https://realiad4ad.github.io/Real-IAD_D3/)
- [Hugging Face dataset](https://huggingface.co/datasets/Real-IAD/Real-IAD_D3)
- [Industrial Atlas page](https://www.indatlas.com/datasets/real-iad-d3/)

[⬅️ Back to Index](../README.md)
