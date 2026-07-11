# MPDD

**Summary:** Industrial metal-part defect dataset with over 1,000 images and pixel-precise defect masks for 6 part categories, following the MVTec-style train/validation split protocol.

| Parameter | Value |
| --- | --- |
| **Dataset** | MPDD |
| **Domain** | Manufacturing & Production |
| **Asset / Process** | Casting / Metal Parts |
| **Modality** | Image |
| **Task** | Anomaly Detection; Defect Detection; Defect Segmentation; Quality Prediction |
| **Annotation** | Normal-Only Training; Sample Label; Pixel Mask |
| **Source Type** | Mixed |
| **Access** | Repository |
| **Size** | 1064 images across 6 metal part categories |
| **Year** | 2021 |
| **License** | CC BY-NC-SA |

## Description

MPDD (Metal Parts Defect Detection Dataset) is a benchmark dataset for industrial anomaly detection focused on metal manufacturing components. The dataset provides real images of six different metal part categories, each with a defect-free training set and a mixed validation set containing both normal and anomalous samples. Pixel-precise defect masks are provided for anomalous validation samples.

The dataset was designed as a practical complement to MVTec AD, focusing on metallic components that exhibit defects commonly encountered in manufacturing quality control. The benchmark follows the standard unsupervised anomaly detection protocol where only defect-free samples are available at training time.

MPDD was introduced at ICUMT 2021 (DOI: 10.1109/ICUMT54235.2021.9631567) and is licensed under CC BY-NC-SA 4.0 for non-commercial research use.

## References

- [GitHub repository + download](https://github.com/stepanje/MPDD)
- [Paper DOI (ICUMT 2021)](https://doi.org/10.1109/ICUMT54235.2021.9631567)

[⬅️ Back to Index](../README.md)
