# PIAD

**Summary:** Multi-view images of 30 industrial products, 16 rendered in Blender and 14 photographed, for anomaly detection under changing pose and lighting.

| Parameter | Value |
| --- | --- |
| **Domain** | Manufacturing |
| **Asset / Process** | — |
| **Modality** | Image |
| **Task** | Anomaly detection |
| **Annotation** | — |
| **Source Type** | Mixed |
| **Access** | — |
| **Size** | 11,268 multi-view images |
| **Year** | 2025 |
| **License** | — |

## Description

PIAD (Pose and Illumination agnostic Anomaly Detection) is both a problem setting and a dataset from Kaichen Yang, Junjie Cao, Zeyu Bai, Zhixun Su and Andrea Tagliasacchi, presented at CVPR 2025. The setting generalizes pose-agnostic anomaly detection (PAD) by dropping the assumption that training images of an object share the light configuration of the query images.

The dataset holds 11,268 multi-view images of 30 distinct industry products: 16 synthetic products generated with Blender and 14 real-world products photographed with a Redmi K40 smartphone on a gimbal. It varies poses, illuminations, materials and anomaly types. Products shown include a motor, spring, gear, sprockets, valve, filter, wheel and bearing.

The authors pair the dataset with a baseline that estimates camera pose with RGB and RGB-and-reflectance Gaussians and is evaluated on both PAD and PIAD.

## References

- [Official page](https://kaichen-yang.github.io/piad/)
- [Industrial Atlas page](https://www.indatlas.com/datasets/piad/)

[⬅️ Back to Index](../README.md)
