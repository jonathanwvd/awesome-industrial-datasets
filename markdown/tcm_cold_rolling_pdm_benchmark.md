# TCM: Benchmark Datasets for Predictive Maintenance in Steel Manufacturing

Six simulated data streams from a mathematical model of a five-stand tandem cold mill, with labelled motor, bearing, work-roll and reduction anomalies.

- **Domain:** Manufacturing
- **Modality:** Time series; Tabular
- **Task:** Fault diagnosis
- **Annotation:** Class label
- **Source Type:** Simulation
- **Access:** Zenodo, Dataverse or Figshare
- **Size:** 6 datasets, 51 features each
- **Year:** 2024
- **License:** CC BY
- **Publisher:** AGH University of Krakow and Jagiellonian University

## Description

TCM is a set of synthetic datasets for predictive maintenance in the cold rolling of steel. Jakub Jakubowski of AGH University of Krakow and Szymon Bobek and Grzegorz J. Nalepa of Jagiellonian University published it on Zenodo in 2024 under CC BY 4.0.

A mathematical model of a five-stand tandem cold mill computes rolling force, torque, speed, tension, gap, thickness reduction and motor power, and physics-based anomalies were introduced into it. Each of the six datasets is a data stream in chronological order, tracked by work roll mileage that resets after a threshold, with 51 features and anomaly shares between 4.6 and 5.2 %.

Two datasets contain one anomaly type and four contain four types: reduction scheme, electric motor, stand bearing and work roll friction, giving 16 anomaly labels in total. The six datasets vary in complexity, with different numbers of products, and datasets 5 and 6 include data drift; they are meant for benchmarking machine learning methods for predictive maintenance.

## References

- [DOI](https://doi.org/10.5281/zenodo.11469702)
- [Zenodo record](https://zenodo.org/records/11469702)
- [Industrial Atlas page](https://www.indatlas.com/datasets/tcm-cold-rolling-pdm-benchmark/)

[⬅️ Back to Index](../README.md)
