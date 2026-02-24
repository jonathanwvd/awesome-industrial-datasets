# Eyecandies

**Summary:** Synthetic multimodal anomaly detection dataset with RGB images, depth maps, and surface normals captured under multiple lighting conditions in a conveyor-like industrial scenario across 10 candy-shaped object classes.

| Parameter | Value |
| --- | --- |
| **Associated Tasks** | Multimodal Anomaly Detection, Localisation, Segmentation |
| **Data Source** | Synthetic |
| **Dataset Characteristics** | Image, Depth, Multimodal, Anomaly Detection, Synthetic |
| **Date Donated** | 2022 |
| **Feature Type** | RGB Images + Depth Maps + Surface Normal Maps |
| **Labeled** | Yes |
| **Missing Values** | No |
| **Name** | Eyecandies |
| **Number of Features** | Information not available |
| **Number of Instances** | 10 object classes; per-class: 1000 normal train, 100 normal val, 25/25 public test, 200/200 private test |
| **Source** | https://eyecan-ai.github.io/eyecandies/ |
| **Time Series** | No |

## Description

Eyecandies is a synthetic multimodal benchmark dataset for industrial anomaly detection, generated using a procedural rendering pipeline that simulates a conveyor belt inspection scenario. Each sample consists of RGB images captured under multiple lighting conditions, a 16-bit depth PNG, and surface normal maps, enabling evaluation of methods that fuse complementary modalities.

The dataset covers 10 object classes (candy-shaped objects) with standardised splits: 1,000 normal training images, 100 normal validation images, and a test set divided into a public portion (25 normal + 25 anomalous) and a private portion (200 normal + 200 anomalous). Anomalies are injected directly in the rendering pipeline with pixel-wise ground truth masks.

Eyecandies was introduced at ACCV 2022 and is particularly useful for pre-training and benchmarking multimodal anomaly detection methods. The code is available on GitHub; dataset licensing should be confirmed with the authors before commercial use.

## Tags

Anomaly Segmentation, Benchmark Dataset, Conveyor Belt, Industrial Inspection, Multimodal, RGB-Depth-Normals, Synthetic Dataset

## References

- [Project page](https://eyecan-ai.github.io/eyecandies/)
- [Download instructions](https://eyecan-ai.github.io/eyecandies/download)
- [GitHub repository (code)](https://github.com/eyecan-ai/eyecandies)

[⬅️ Back to Index](../README.md)
