# SKAB

Multivariate sensor time series from a testbed with a water pump and circulation loop, one experiment and one anomaly per file, with outlier and changepoint labels.

- **Domain:** Water and utilities
- **Asset / Process:** Pumps, compressors and fans; Motors and drives
- **Modality:** Time series
- **Task:** Anomaly detection
- **Annotation:** Sample label; Event and time label
- **Source Type:** Lab or testbed
- **Access:** Code repository
- **Year:** 2020
- **Benchmark:** Yes

## Description

SKAB (Skoltech Anomaly Benchmark) is a set of multivariate time series for evaluating anomaly detection algorithms, recorded from sensors installed on a testbed. Iurii D. Katser and Vyacheslav O. Kozitsin released it in 2020; its data record is on Kaggle under DOI 10.34740/KAGGLE/DSV/1693952.

In SKAB v0.9, each CSV data file holds a single experiment with a single anomaly. Columns hold the timestamp, two accelerometer RMS values, motor current and voltage, pressure after the water pump, engine body temperature, fluid temperature and flow rate in the circulation loop. Two 0 or 1 markups label each point as anomalous and as a changepoint of a collective anomaly.

A leaderboard on the test set ranks methods for outlier detection, scored with F1, false alarm and missing alarm rates, and for changepoint detection, scored with NAB metrics.

## References

- [GitHub repository](https://github.com/waico/SKAB)
- [Industrial Atlas page](https://www.indatlas.com/datasets/skab/)

[⬅️ Back to Index](../README.md)
