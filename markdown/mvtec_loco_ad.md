# MVTec LOCO AD

**Summary:** Unsupervised anomaly localization dataset of 3,644 images in five categories, with both structural and logical anomalies and pixel-precise ground truth.

| Parameter | Value |
| --- | --- |
| **Domain** | Manufacturing |
| **Asset / Process** | — |
| **Modality** | Image |
| **Task** | Anomaly detection; Anomaly localization |
| **Annotation** | Pixel mask |
| **Source Type** | — |
| **Access** | — |
| **Size** | 3,644 images |
| **Year** | 2022 |
| **License** | CC BY-NC-SA |
| **Publisher** | MVTec |

## Description

MVTec LOCO AD (MVTec logical constraints anomaly detection) is a dataset from MVTec for evaluating unsupervised anomaly localization algorithms. It is described by Paul Bergmann, Kilian Batzner, Michael Fauser, David Sattlegger and Carsten Steger in "Beyond Dents and Scratches: Logical Constraints in Unsupervised Anomaly Detection and Localization", published in the International Journal of Computer Vision in 2022.

Its 3,644 images come from five categories inspired by industrial inspection scenarios. Structural anomalies appear as scratches, dents or contaminations on the products, while logical anomalies break underlying constraints, such as an allowed object in an invalid location or a required object that is missing. Pixel-precise ground truth is given for each anomalous region.

Python scripts with a readme support a fair and consistent evaluation of methods, and the metrics are defined in the paper. The data is released under CC BY-NC-SA 4.0, which does not allow commercial use.

## References

- [Official page](https://www.mvtec.com/company/research/datasets/mvtec-loco)
- [Industrial Atlas page](https://www.indatlas.com/datasets/mvtec-loco-ad/)

[⬅️ Back to Index](../README.md)
