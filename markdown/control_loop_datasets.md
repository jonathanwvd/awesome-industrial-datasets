# Control loop datasets

**Summary:** GIMSCOP/UFRGS industrial oil and gas SISO control loop dataset with 2.5 days of real PV/MV data in three variants (raw, selected fragments, constant sampling); companion to the oscillation detection artificial dataset (ODADS).

| Parameter | Value |
| --- | --- |
| **Associated Tasks** | Control Loop Performance Monitoring, Oscillation Detection, Anomaly Detection |
| **Data Source** | Real |
| **Dataset Characteristics** | Multivariate, Time-Series, Industrial Process Data |
| **Date Donated** | 2018 |
| **Feature Type** | Real |
| **Labeled** | Yes |
| **Missing Values** | No |
| **Name** | Control loop datasets |
| **Number of Features** | Process variable (PV) and manipulated variable (MV) per loop; sampling time varies by variant |
| **Number of Instances** | Multiple SISO control loops from an oil and gas company over 2.5 days; 3 variants: SISO-RAW (non-constant sampling), SISO-SEL (selected fragments), SISO-SAMP (constant sampling rate) |
| **Source** | GIMSCOP / UFRGS (Group of Intensification, Modeling, Simulation, Control and Optimization of Processes) |
| **Time Series** | Yes |

## Description

The GIMSCOP Control Loop Datasets are provided by the Group of Intensification, Modeling, Simulation, Control and Optimization of Processes at UFRGS (Federal University of Rio Grande do Sul, Brazil). They consist of real industrial data from an oil and gas company.

Three variants are provided:
- SISO-RAW: Raw time series collected over approximately 2.5 days from multiple SISO control loops; non-constant sampling time due to data historian storage.
- SISO-SEL: Selected fragments from SISO-RAW with particular operating conditions or behaviors of interest.
- SISO-SAMP: Resampled version of SISO-SEL with constant sampling time, suitable for standard time-series analysis algorithms.

Each record contains the process variable (PV) and manipulated variable (MV) of a control loop. The dataset is used for control loop performance monitoring research, particularly oscillation detection. A companion synthetic dataset (ODADS — Oscillation Detection Artificial Dataset) is also available for machine learning algorithm development and validation.

## Tags

Brazil, Control Loop, GIMSCOP, Oil and Gas, Oscillation Detection, Process Control, SISO, Time-Series, UFRGS

## References

- [GIMSCOP Datasets Repository](https://www.ufrgs.br/gimscop/repository/sisoviewer/datasets/)
- [Download SISO Data (Google Drive)](https://drive.google.com/open?id=1hnsj85dSJz344UyxbYcUlFi08xfhMALJ)
- [Download ODADS (Google Drive)](https://drive.google.com/open?id=1XUkEKSSTrF7pJ_6K82OpJkwnls1TSdgo)

[⬅️ Back to Index](../README.md)
