# PHM North America 2025 Conference Data Challenge

Snapshot sensor data from eight commercial jet engines over 2001 flights, for predicting cycles left to turbine and compressor shop visits and compressor water-wash.

- **Domain:** Aerospace and defense
- **Asset / Process:** Turbines and engines
- **Modality:** Time series
- **Task:** RUL and prognostics; Regression
- **Annotation:** Scalar target
- **Access:** Competition
- **Size:** Eight engines
- **Year:** 2025
- **Benchmark:** Yes

## Description

The PHM North America 2025 Conference Data Challenge, hosted on the PHM Society data repository and also called the 2025 EHM Data Challenge, is about engine health management for commercial jet engines. Teams estimate the remaining cycles to three maintenance events: a High Pressure Turbine (HPT) shop visit, a High Pressure Compressor (HPC) shop visit and an HPC water-wash.

Eight engines, ESN101 to ESN108, are covered; each contributes up to 15,000 data points over 2001 flights, with up to eight snapshots per flight taken in phases such as takeoff, climb and cruise. Metadata hold the engine serial number, cycles, snapshot number and cumulative maintenance counts, next to 16 sensed engine variables, 14 of them primary, and the three remaining-cycle targets.

Teams set their own training, validation and test splits. Scoring is a time-weighted squared error that penalises late predictions more than early ones and errors close to the event more than those far from it; winners are judged on the validation data.

## References

- [Official page](https://data.phmsociety.org/phm-north-america-2025-conference-data-challenge/)
- [Industrial Atlas page](https://www.indatlas.com/datasets/phm-2025-jet-engine-maintenance/)

[⬅️ Back to Index](../README.md)
