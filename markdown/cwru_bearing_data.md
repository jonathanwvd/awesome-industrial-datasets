# CWRU Bearing Data

**Summary:** Widely used bearing fault diagnosis benchmark from Case Western Reserve University, containing vibration time-series from a 2 HP motor with EDM-seeded bearing defects (inner race, outer race, rolling elements) under multiple operating loads and speeds.

| Parameter | Value |
| --- | --- |
| **Dataset** | CWRU Bearing Data |
| **Domain** | Manufacturing & Production |
| **Asset / Process** | Bearings |
| **Modality** | Time Series; Vibration |
| **Task** | Fault Diagnosis; Condition Monitoring; Classification |
| **Annotation** | Sample Label; Class Label; Fault Type Label |
| **Source Type** | Real Lab / Testbed |
| **Access** | Official Portal |
| **Size** | Multiple time-series records under motor loads of 0-3 HP (1720-1797 RPM); defects at 4 fault diameters (0.007-0.040 in) |
| **Year** | 2000 |
| **License** | Information not available |

## Description

The CWRU Bearing Dataset is one of the most widely referenced benchmarks in the bearing fault diagnosis and predictive maintenance communities. Data was collected on a dedicated test rig at Case Western Reserve University consisting of a 2 HP Reliance Electric motor, a torque transducer/encoder, a dynamometer, and control electronics.

Bearing faults were artificially introduced using electro-discharge machining (EDM) with controlled fault diameters of 0.007, 0.014, 0.021, and 0.040 inches. Defects were seeded at three locations: inner raceway, outer raceway, and rolling elements (balls). Vibration acceleration signals were recorded using accelerometers positioned at the drive end (DE) and fan end (FE) of the motor. The motor was operated under four loads (0–3 HP) corresponding to speeds of approximately 1797, 1772, 1750, and 1720 RPM. Baseline recordings of normal (defect-free) bearings are also provided.

The dataset has been widely adopted as the standard benchmark for bearing fault classification studies. It enables research on fault type identification, severity estimation, and generalisation across operating conditions.

## References

- [CWRU Bearing Data Center](https://engineering.case.edu/bearingdatacenter)
- [Download data files](https://engineering.case.edu/bearingdatacenter/download-data-file)

[⬅️ Back to Index](../README.md)
