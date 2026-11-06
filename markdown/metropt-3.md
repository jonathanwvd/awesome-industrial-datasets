# MetroPT-3

Unlabelled multivariate sensor readings from the air production unit of an operating metro train compressor, February to August 2020, with failure reports.

- **Domain:** Transportation and mobility
- **Asset / Process:** Pumps, compressors and fans; Vehicles and fleets
- **Modality:** Time series
- **Task:** Anomaly detection; RUL and prognostics
- **Annotation:** Unlabeled
- **Source Type:** Real production
- **Access:** UCI repository
- **Size:** 1,516,948 instances, 15 features
- **Year:** 2023
- **License:** CC BY
- **Publisher:** INESC TEC

## Description

MetroPT-3 holds readings from the compressor's air production unit (APU) of a metro train in operation. Narjes Davari, Bruno Veloso, Rita Ribeiro and Joao Gama of INESC TEC created it, and it was donated to the UCI Machine Learning Repository in 2023. Its introductory paper on anomaly detection for the APU appeared at IEEE DSAA 2021.

The 1,516,948 instances span February to August 2020 and carry 15 signals from 7 analogue and 8 digital sensors: pressures, motor current, oil temperature and electrical signals such as the air intake valves. An onboard embedded device logged the data, and no values are missing.

The data has no labels, but the company's failure reports list four air leak failures with start and end times, which allows anomaly detection, failure prediction and RUL estimation to be evaluated. The first month can serve for training and the rest for testing. The data is licensed under CC BY 4.0.

## References

- [UCI Machine Learning Repository](https://archive.ics.uci.edu/dataset/791/metropt%2B3%2B)
- [Industrial Atlas page](https://www.indatlas.com/datasets/metropt-3/)

[⬅️ Back to Index](../README.md)
