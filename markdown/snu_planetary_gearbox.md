# SNU Planetary Gearbox Dataset

**Summary:** Vibration and encoder signals from a 2 kW-class planetary gearbox testbed with seven health and fault-severity conditions at constant and varying speed.

| Parameter | Value |
| --- | --- |
| **Dataset** | SNU Planetary Gearbox Dataset |
| **Domain** | Manufacturing & Production |
| **Asset / Process** | Gears / Gearboxes |
| **Modality** | Vibration; Time Series |
| **Task** | Fault Diagnosis |
| **Annotation** | Class Label |
| **Source Type** | Real Lab / Testbed |
| **Access** | Zenodo / Dataverse |
| **Size** | 14 configurations of about 100 minutes each |
| **Year** | 2026 |
| **License** | CC BY |

## Description

The SNU Planetary Gearbox Dataset provides vibration and encoder signals recorded on a 2 kW-class testbed with a single-stage, fixed-ring planetary gearbox, collected for fault diagnosis research. The gearbox has a 31-tooth sun gear, three 31-tooth planet gears and a 95-tooth ring gear. The data is published on Figshare by Jinoh Yoo, Taehyung Kim, Jong Moon Ha and Byeng Dong Youn.

Its 14 experimental configurations combine seven health and severity conditions with two operating modes: stationary operation at about 1579 rpm, and a sinusoidal speed profile from about 521 to 1588 rpm with a 20-second period. Besides the healthy state, machined line-shaped grooves of 0.50 to 1.25 mm seed planet-ring, planet-sun and sun gear faults. A PCB Piezotronics 601A02 accelerometer and an ONO SOKKI MP-981 encoder are sampled at 25,600 Hz for about 100 minutes per configuration.

Signals are stored as headerless tab-delimited text files arranged by fault type, severity and operating mode, each with about 1.54 x 10^8 samples. A file-level metadata table and MATLAB validation scripts come with the data, released under CC BY 4.0.

## References

- [DOI](https://doi.org/10.6084/m9.figshare.32025606)

[⬅️ Back to Index](../README.md)
