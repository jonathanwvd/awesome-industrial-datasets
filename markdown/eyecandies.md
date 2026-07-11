# Eyecandies

**Summary:** Synthetic multimodal anomaly detection dataset with RGB images, depth maps, and surface normals captured under multiple lighting conditions in a conveyor-like industrial scenario across 10 candy-shaped object classes.

| Parameter | Value |
| --- | --- |
| **Dataset** | Eyecandies |
| **Domain** | Materials & Metrology; Manufacturing & Production |
| **Asset / Process** | Surface Defects |
| **Modality** | Image; RGB-D; Multimodal |
| **Task** | Anomaly Detection; Anomaly Localization; Defect Segmentation |
| **Annotation** | Normal-Only Training; Sample Label |
| **Source Type** | Real Lab / Testbed |
| **Access** | Repository |
| **Size** | 10 object classes; per-class: 1000 normal train, 100 normal val, 25/25 public test, 200/200 private test |
| **Year** | 2022 |
| **License** | Information not available |

## Description

Eyecandies is a synthetic multimodal benchmark dataset for industrial anomaly detection, generated using a procedural rendering pipeline that simulates a conveyor belt inspection scenario. Each sample consists of RGB images captured under multiple lighting conditions, a 16-bit depth PNG, and surface normal maps, enabling evaluation of methods that fuse complementary modalities.

The dataset covers 10 object classes (candy-shaped objects) with standardised splits: 1,000 normal training images, 100 normal validation images, and a test set divided into a public portion (25 normal + 25 anomalous) and a private portion (200 normal + 200 anomalous). Anomalies are injected directly in the rendering pipeline with pixel-wise ground truth masks.

Eyecandies was introduced at ACCV 2022 and is particularly useful for pre-training and benchmarking multimodal anomaly detection methods. The code is available on GitHub; dataset licensing should be confirmed with the authors before commercial use.

## References

- [Project page](https://eyecan-ai.github.io/eyecandies/)
- [Download instructions](https://eyecan-ai.github.io/eyecandies/download)
- [GitHub repository (code)](https://github.com/eyecan-ai/eyecandies)

[⬅️ Back to Index](../README.md)
