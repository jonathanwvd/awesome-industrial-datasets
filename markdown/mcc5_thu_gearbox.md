# Multi-mode Fault Diagnosis Datasets of Gearbox Under Variable Working Conditions

Vibration, torque and speed signals from a two-stage parallel gearbox with seeded gear and bearing faults, recorded under time-varying speed and load.

- **Domain:** Manufacturing
- **Asset / Process:** Gears and gearboxes; Bearings
- **Modality:** Vibration; Time series
- **Task:** Fault diagnosis
- **Annotation:** Class label
- **Source Type:** Lab or testbed
- **Access:** Mendeley Data
- **Size:** 240 sets of time series data
- **Year:** 2024
- **Publisher:** Tsinghua University

## Description

These gearbox fault diagnosis datasets were collected by the Department of Automation at Tsinghua University and MCC5 Group Shanghai Co. LTD on a laboratory test rig. They are described in a 2024 Data in Brief article and published on Mendeley Data, where version 2 corrects the reversed sign of the torque measurements in version 1.

The rig has a 2.2 kW three-phase asynchronous motor, a two-stage parallel gearbox and a magnetic powder brake that applies the load. Faults machined into the 36-tooth intermediate-shaft gear or its support bearings include missing teeth, wear, pitting, root cracks, broken teeth and inner and outer race faults, at several severity degrees and as compound faults. The 240 CSV files each hold 60 seconds at 12.8 kHz under time-varying speed or load, across 12 working conditions.

Each file has eight columns: a key phase speed signal, input shaft torque, and triaxial vibration acceleration at the motor drive end and at the gearbox intermediate shaft bearing seat. Listed tasks include compound fault diagnosis and diagnosis under variable or transitional working conditions.

## References

- [Mendeley Data](https://data.mendeley.com/datasets/p92gj2732w/2)
- [GitHub repository](https://github.com/liuzy0708/MCC5-THU-Gearbox-Benchmark-Datasets)
- [DOI](https://doi.org/10.1016/j.dib.2024.110453)
- [Industrial Atlas page](https://www.indatlas.com/datasets/mcc5-thu-gearbox/)

[⬅️ Back to Index](../README.md)
