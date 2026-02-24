# MVTec MV-ball

**Summary:** Synthetic multi-view benchmark for evaluating 6D pose estimation under pose ambiguity that cannot be resolved from single views, featuring a multi-hemisphere ball object with easy and hard evaluation splits.

| Parameter | Value |
| --- | --- |
| **Associated Tasks** | Multi-View 6D Pose Estimation |
| **Data Source** | Synthetic |
| **Dataset Characteristics** | Image, Multi-View, Pose Estimation, Synthetic |
| **Date Donated** | 2025 |
| **Feature Type** | Rendered Multi-View Images |
| **Labeled** | Yes |
| **Missing Values** | No |
| **Name** | MVTec MV-ball |
| **Number of Features** | Information not available |
| **Number of Instances** | 112042 training images; 3853 easy + 3458 hard evaluation images |
| **Source** | https://www.mvtec.com/company/research/datasets/mvtec-mv-ball |
| **Time Series** | No |

## Description

MVTec MV-ball is a synthetic benchmark specifically designed to stress-test multi-view 6D pose estimation methods under pose ambiguity. The dataset uses a multi-hemisphere ball object that, when viewed from a single camera, does not provide sufficient information to resolve its orientation uniquely. Only by combining information from multiple viewpoints can the pose be determined.

The dataset contains 112,042 training images and two evaluation splits: an easy split with 3,853 images and a hard split with 3,458 images. All data is synthetically rendered, enabling controlled experiments on multi-view fusion strategies. This benchmark is particularly relevant for robotic assembly and handling applications where precise pose knowledge is required but objects have rotational symmetry or visual ambiguity.

MVTec MV-ball was introduced in arXiv:2508.03243 (2025) and is licensed under CC BY-NC-SA 4.0 for non-commercial research use.

## Tags

6D Pose Estimation, Industrial Robotics, MVTec, Multi-View, Pose Ambiguity, Robotics Vision, Synthetic Dataset

## References

- [Dataset page](https://www.mvtec.com/company/research/datasets/mvtec-mv-ball)
- [Paper (arXiv 2025)](https://arxiv.org/abs/2508.03243)

[⬅️ Back to Index](../README.md)
