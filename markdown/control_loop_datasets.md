# Control loop datasets

**Summary:** GIMSCOP/UFRGS industrial oil and gas SISO control loop dataset with 2.5 days of real PV/MV data in three variants (raw, selected fragments, constant sampling); companion to the oscillation detection artificial dataset (ODADS).

| Parameter | Value |
| --- | --- |
| **Dataset** | Control loop datasets |
| **Domain** | Oil & Gas; Chemical & Process |
| **Asset / Process** | Chemical Process |
| **Modality** | Time Series |
| **Task** | Anomaly Detection; Process Monitoring; Simulation / Control |
| **Annotation** | Sample Label |
| **Source Type** | Real Production / Field |
| **Access** | Official Portal |
| **Size** | Multiple SISO control loops from an oil and gas company over 2.5 days; 3 variants: SISO-RAW (non-constant sampling), SISO-SEL (selected fragments), SISO-SAMP (constant sampling rate) |
| **Year** | 2018 |
| **License** | Information not available |

## Description

The GIMSCOP Control Loop Datasets are provided by the Group of Intensification, Modeling, Simulation, Control and Optimization of Processes at UFRGS (Federal University of Rio Grande do Sul, Brazil). They consist of real industrial data from an oil and gas company.

Three variants are provided:
- SISO-RAW: Raw time series collected over approximately 2.5 days from multiple SISO control loops; non-constant sampling time due to data historian storage.
- SISO-SEL: Selected fragments from SISO-RAW with particular operating conditions or behaviors of interest.
- SISO-SAMP: Resampled version of SISO-SEL with constant sampling time, suitable for standard time-series analysis algorithms.

Each record contains the process variable (PV) and manipulated variable (MV) of a control loop. The dataset is used for control loop performance monitoring research, particularly oscillation detection. A companion synthetic dataset (ODADS — Oscillation Detection Artificial Dataset) is also available for machine learning algorithm development and validation.

## References

- [GIMSCOP Datasets Repository](https://www.ufrgs.br/gimscop/repository/sisoviewer/datasets/)
- [Download SISO Data (Google Drive)](https://drive.google.com/open?id=1hnsj85dSJz344UyxbYcUlFi08xfhMALJ)
- [Download ODADS (Google Drive)](https://drive.google.com/open?id=1XUkEKSSTrF7pJ_6K82OpJkwnls1TSdgo)

[⬅️ Back to Index](../README.md)
