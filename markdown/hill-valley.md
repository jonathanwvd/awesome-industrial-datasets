# Hill-Valley

**Summary:** Each record represents 100 points on a two-dimensional graph that create either a Hill (a bump) or a Valley (a dip) when plotted in order as the Y coordinate.

| Parameter | Value |
| --- | --- |
| **Dataset** | Hill-Valley |
| **Domain** | General / Cross-Industrial |
| **Asset / Process** | Other / Cross-Domain |
| **Modality** | Time Series |
| **Task** | Classification; Benchmark Suite |
| **Annotation** | Sample Label; Class Label |
| **Source Type** | Real Lab / Testbed |
| **Access** | UCI |
| **Size** | 606 |
| **Year** | 2008 |
| **License** | CC BY |

## Description

The Hill-Valley dataset contains several files representing hill or valley terrain shapes. There are six files, including two training/testing sets without noise where the hills or valleys have a smooth transition, and two training/testing sets with noise where the terrain is uneven making the hill or valley less obvious. Additionally, a sample ARFF file is provided for setting up experiments, and a graphic showing example instances from the data.

Each record consists of 100 floating point values labeled as "X##" representing coordinates, followed by a binary class label {0, 1} representing valley or hill respectively. The dataset contains 606 instances with 101 features. It is intended for classification tasks, and does not contain missing values.

This dataset is provided under the Creative Commons Attribution 4.0 International (CC BY 4.0) license, allowing sharing and adaptation with appropriate credit.

## References

- [Graham, L. & Oppacher, F. (2008). Hill-Valley [Dataset]. UCI Machine Learning Repository. https://doi.org/10.24432/C5JC8P.](https://doi.org/10.24432/C5JC8P)
- [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/Hill-Valley)

[⬅️ Back to Index](../README.md)
