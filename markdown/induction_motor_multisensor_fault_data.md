# Motor Fault Detection Data (Three-Phase Induction Motor)

Synchronised vibration, voltage and current at 50 kHz from a healthy and a faulty 0.2 kW squirrel cage induction motor under load steps and phase removal.

- **Domain:** Manufacturing
- **Asset / Process:** Motors and drives; Bearings
- **Modality:** Vibration; Time series
- **Task:** Fault diagnosis; Classification
- **Annotation:** Class label
- **Source Type:** Lab or testbed
- **Access:** Zenodo, Dataverse or Figshare
- **Size:** Ten recordings in CSV and MAT formats, plus a label file
- **Year:** 2025
- **License:** CC BY

## Description

This dataset records a 0.2 kW three-phase squirrel cage induction motor in healthy and faulty states, with vibration, voltage and current captured together. It is published on figshare with a descriptor in Scientific Data by Kevin Thomas and co-authors, and was built to give fault diagnosis research synchronised electrical and mechanical signals from the same motor.

A dSPACE platform sampled every channel at 50 kHz: a three-axis accelerometer, the supply voltage and the motor current. The faulty motor has a deep groove ball bearing (SKF 6202-Z) with small holes drilled into its outer ring, and the electrical scenarios remove a supply phase.

The data comes as ten recordings, each in CSV and MAT format with a separate label file, five for the healthy motor and five for the faulty one. Each set covers normal operation without load, a phase removed while running, mechanical loads of 0.4 and 0.8 Nm, and running with one phase disconnected from startup. The authors trained a random forest classifier on the files and report 99.82% accuracy.

## References

- [DOI](https://doi.org/10.6084/m9.figshare.27216219)
- [api.figshare.com](https://api.figshare.com/v2/articles/27216219)
- [pmc.ncbi.nlm.nih.gov](https://pmc.ncbi.nlm.nih.gov/articles/PMC12373825/)
- [Industrial Atlas page](https://www.indatlas.com/datasets/induction-motor-multisensor-fault-data/)

[⬅️ Back to Index](../README.md)
