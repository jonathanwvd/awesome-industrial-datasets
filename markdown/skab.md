# SKAB

**Summary:** Industrial anomaly detection benchmark for multivariate time series from sensor streams, with two types of anomaly annotations: single-point outliers and collective segment-level change-point anomalies.

| Parameter | Value |
| --- | --- |
| **Associated Tasks** | Time Series Anomaly Detection, Outlier Detection, Change-Point Detection |
| **Data Source** | Real |
| **Dataset Characteristics** | Multivariate, Time-Series, Anomaly Detection |
| **Date Donated** | 2020 |
| **Feature Type** | Sensor Time Series |
| **Labeled** | Yes |
| **Missing Values** | No |
| **Name** | SKAB |
| **Number of Features** | Information not available |
| **Number of Instances** | Information not available |
| **Source** | https://github.com/waico/SKAB |
| **Time Series** | Yes |

## Description

SKAB (Skoltech Anomaly Benchmark) is an industrial multivariate time series benchmark for evaluating anomaly detection algorithms. The dataset is collected from a water circulation testbed equipped with multiple sensors, producing synchronised time series of physical process measurements.

A key feature of SKAB is the provision of two distinct anomaly markup types for the same data: (1) single-point outlier annotations for methods that detect isolated anomalous measurements, and (2) collective anomaly / change-point annotations for methods that detect sustained regime changes. This dual-label design allows direct comparison of different algorithmic paradigms on the same data.

The benchmark repository includes tooling for standardised evaluation and comparison. SKAB is licensed under GPL-3.0, which may affect redistribution and derivative packaging; users should verify compatibility with their intended use case.

## Tags

Change Point Detection, Industrial Benchmark, Multivariate Time Series, Outlier Detection, Process Monitoring, Sensor Data, Time Series Anomaly Detection

## References

- [GitHub repository](https://github.com/waico/SKAB)

[⬅️ Back to Index](../README.md)
