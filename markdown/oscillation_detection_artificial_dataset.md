# Oscillation detection artificial dataset

**Summary:** GIMSCOP/UFRGS synthetic SISO control loop dataset (ODADS) for machine learning-based oscillation detection; artificially generated process variable time series labeled as oscillating or non-oscillating.

| Parameter | Value |
| --- | --- |
| **Associated Tasks** | Oscillation Detection, Binary Classification, Control Loop Monitoring |
| **Data Source** | Synthetic |
| **Dataset Characteristics** | Univariate, Time-Series |
| **Date Donated** | 2018 |
| **Feature Type** | Real |
| **Labeled** | Yes |
| **Missing Values** | No |
| **Name** | Oscillation detection artificial dataset |
| **Number of Features** | Process variable (PV) time series per control loop; constant sampling rate |
| **Number of Instances** | Synthetic SISO control loop time series; labeled as oscillating or non-oscillating |
| **Source** | GIMSCOP / UFRGS (Group of Intensification, Modeling, Simulation, Control and Optimization of Processes) |
| **Time Series** | Yes |

## Description

The Oscillation Detection Artificial Dataset (ODADS) was created by the GIMSCOP group at UFRGS (Federal University of Rio Grande do Sul, Brazil) to support the development and benchmarking of machine learning techniques for oscillation detection in industrial control loops.

Oscillation is a common problem in industrial PID control loops, caused by aggressive tuning, valve stiction, or external disturbances. The dataset provides synthetically generated SISO (single-input single-output) process variable (PV) time series at a constant sampling rate, with binary labels indicating whether each time series exhibits oscillatory behavior.

The synthetic generation allows controlled creation of diverse oscillation patterns and non-oscillating behaviors, including various frequencies, amplitudes, and noise levels. This makes it suitable for training and evaluating classification algorithms for automated control loop performance monitoring without requiring access to proprietary industrial data.

The dataset is available as a companion to the real industrial SISO control loop datasets (SISO-RAW, SISO-SEL, SISO-SAMP) on the GIMSCOP datasets repository.

## Tags

Binary Classification, Control Loop, GIMSCOP, Machine Learning, Oscillation Detection, Process Monitoring, SISO, Synthetic Dataset, UFRGS

## References

- [GIMSCOP Datasets Repository](https://www.ufrgs.br/gimscop/repository/sisoviewer/datasets/)
- [Dataset download (Google Drive)](https://drive.google.com/open?id=1XUkEKSSTrF7pJ_6K82OpJkwnls1TSdgo)

[⬅️ Back to Index](../README.md)
