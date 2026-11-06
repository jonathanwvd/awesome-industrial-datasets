# N-CMAPSS_DL

**Summary:** Python code that slices NASA's N-CMAPSS turbofan engine data, downloaded separately, into time-windowed samples labelled with remaining useful life.

| Parameter | Value |
| --- | --- |
| **Domain** | Aerospace and defense |
| **Asset / Process** | Turbines and engines |
| **Modality** | Time series |
| **Task** | RUL and prognostics |
| **Annotation** | — |
| **Source Type** | — |
| **Access** | — |
| **Size** | — |
| **Year** | 2022 |
| **License** | — |

## Description

N-CMAPSS_DL is a Python code repository that prepares NASA's N-CMAPSS data, the Turbofan Engine Degradation Simulation Data Set-2, for machine learning and deep learning models. It holds code only: the N-CMAPSS file is downloaded from NASA's prognostic data repository. The code cites the paper "Multi-objective optimization of extreme learning machine for remaining useful life prediction" by Hyunho Mo and Giovanni Iacca, from EvoApplications 2022.

Its sample creator reads only the DS02 file, N-CMAPSS_DS02-006.h5, and slices each engine trajectory into time windows with a chosen window length, stride and subsampling. It writes one npz file per engine with a sample array and a label array; for test units the label is the ground-truth remaining useful life. Nine engines are prepared: six units (2, 5, 10, 16, 18 and 20) for training and three (11, 14 and 15) for testing.

## References

- [GitHub repository](https://github.com/mohyunho/N-CMAPSS_DL)
- [Industrial Atlas page](https://www.indatlas.com/datasets/n-cmapss-dl/)

[⬅️ Back to Index](../README.md)
