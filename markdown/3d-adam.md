# 3D-ADAM

**Summary:** Image and 3D dataset for anomaly detection in additive manufacturing, released as raw data separated by part instance under CC BY-NC-SA 4.0.

| Parameter | Value |
| --- | --- |
| **Domain** | Manufacturing |
| **Asset / Process** | Additive manufacturing |
| **Modality** | Image; 3D point cloud |
| **Task** | Anomaly detection; Anomaly localization; Defect segmentation |
| **Annotation** | — |
| **Source Type** | — |
| **Access** | Hugging Face |
| **Size** | — |
| **Year** | — |
| **License** | CC BY-NC-SA |

## Description

3D-ADAM (3D Anomaly Detection in Additive Manufacturing) is hosted on Hugging Face in the pmchard account and described in an arXiv paper. The project behind it received support from the 1851 Royal Commission and HAL Robotics.

The main repository holds the raw data of the complete dataset, with image and 3D modalities, organised by part instance so that it can be split and combined as needed. A separate repository offers a subset recorded with a single MechMind-Nano camera.

That single-camera subset is prepared for unsupervised training on anomaly detection, localisation and segmentation tasks through the anomalib library. The main repository is open to download without gating, and its data is released under the CC BY-NC-SA 4.0 license.

## References

- [Hugging Face dataset](https://huggingface.co/datasets/pmchard/3D-ADAM)
- [Industrial Atlas page](https://www.indatlas.com/datasets/3d-adam/)

[⬅️ Back to Index](../README.md)
