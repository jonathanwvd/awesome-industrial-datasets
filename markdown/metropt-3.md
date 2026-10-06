# MetroPT-3

**Summary:** Operational sensor data from the air production unit of a metro train compressor, recorded from February to August 2020 with company failure reports for predictive maintenance.

| Parameter | Value |
| --- | --- |
| **Dataset** | MetroPT-3 |
| **Domain** | Transportation & Mobility |
| **Asset / Process** | Vehicles / Fleets |
| **Modality** | Time Series; Tabular |
| **Task** | Predictive Maintenance; Anomaly Detection; Failure Prediction; RUL / Prognostics |
| **Annotation** | Unlabeled; Time / Event Label |
| **Source Type** | Real Production / Field |
| **Access** | UCI |
| **Size** | 1,516,948 records, 15 features (208 MB CSV) |
| **Year** | 2021 |
| **License** | CC BY |

## Description

MetroPT-3 contains readings from the compressor Air Production Unit (APU) of a metro train in operation, logged by an onboard embedded device between February and August 2020. The 15 features combine seven analogue signals, such as compressor and reservoir pressures, motor current, and oil temperature, with eight digital signals from the compressor control and pneumatic system.

The data are not labeled, but the operator's failure reports are provided, listing air-leak failures with their time windows and maintenance dates. The maintainers suggest using the first month for training and the remaining months for testing, and note that the dataset suits incremental learning. Typical uses are anomaly detection, failure prediction, anomaly explanation, and remaining-useful-life estimation for compressors.

The dataset was created by researchers at INESC TEC and the University of Porto and is distributed through the UCI Machine Learning Repository under CC BY 4.0.

## References

- [UCI Machine Learning Repository dataset page](https://archive.ics.uci.edu/dataset/791/metropt+3+dataset)
- [Dataset DOI: 10.24432/C5VW3R](https://doi.org/10.24432/C5VW3R)
- [Davari et al. (2021). Predictive maintenance based on anomaly detection using deep learning for air production unit in the railway industry. IEEE DSAA 2021](https://ieeexplore.ieee.org/abstract/document/9564181)

[⬅️ Back to Index](../README.md)
