# Energy Efficiency

**Summary:** This study looked into assessing the heating load and cooling load requirements of buildings (that is, energy efficiency) as a function of building parameters.

| Parameter | Value |
| --- | --- |
| **Dataset** | Energy Efficiency |
| **Domain** | Buildings & Appliances; Energy & Power |
| **Asset / Process** | Buildings / Appliances |
| **Modality** | Tabular |
| **Task** | Regression; Energy Optimization; Classification |
| **Annotation** | Sample Label; Class Label; Scalar Target |
| **Source Type** | Simulation |
| **Access** | UCI |
| **Size** | 768 |
| **Year** | 2012 |
| **License** | Information not available |

## Description

We perform energy analysis using 12 different building shapes simulated in Ecotect. The buildings differ with respect to the glazing area, the glazing area distribution, and the orientation, amongst other parameters. We simulate various settings as functions of the afore-mentioned characteristics to obtain 768 building shapes. The dataset comprises 768 samples and 8 features, aiming to predict two real valued responses. It can also be used as a multi-class classification problem if the response is rounded to the nearest integer.

The dataset contains eight attributes (or features, denoted by X1...X8) and two responses (or outcomes, denoted by y1 and y2). The aim is to use the eight features to predict each of the two responses.

Specifically:
X1 Relative Compactness
X2 Surface Area
X3 Wall Area
X4 Roof Area
X5 Overall Height
X6 Orientation
X7 Glazing Area
X8 Glazing Area Distribution
y1 Heating Load
y2 Cooling Load

## References

- [Accurate quantitative estimation of energy performance of residential buildings using statistical machine learning tools - Tsanas, A. & Xifara, A. (2012)](https://www.semanticscholar.org/paper/Accurate-quantitative-estimation-of-energy-of-using-Tsanas-Xifara/719e65379c5959141180a45f540f707d583b8ce2)
- [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/Energy+efficiency)

[⬅️ Back to Index](../README.md)
