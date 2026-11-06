# IoT-Integrated Predictive Maintenance Dataset

**Summary:** Simulated time-series readings from several production-line machines with vibration, acoustic, temperature and current channels and a healthy or faulty label.

| Parameter | Value |
| --- | --- |
| **Domain** | Manufacturing |
| **Asset / Process** | — |
| **Modality** | Time series |
| **Task** | Classification; Condition monitoring |
| **Annotation** | Sample label |
| **Source Type** | Synthetic |
| **Access** | Kaggle |
| **Size** | — |
| **Year** | — |
| **License** | CC0 and public domain |

## Description

The IoT-Integrated Predictive Maintenance Dataset contains time-series sensor readings from multiple industrial machines on a production line. The data is simulated to resemble real-time collection through an IoT-enabled sensor network, and the simulation includes both normal and fault conditions. It comes as one CSV file, predictive_maintenance_dataset.csv.

Each entry has a timestamp, a machine identifier and raw measurements of vibration, acoustic signal, temperature in °C and current in amps. Three intrinsic mode functions (IMF_1, IMF_2 and IMF_3) give decomposed signal components intended to reflect patterns linked to early-stage faults. A label marks the machine state as healthy (0) or faulty (1).

The stated aim of the data is to support predictive maintenance and equipment health monitoring. It is released under CC0 1.0.

## References

- [Kaggle dataset](https://www.kaggle.com/datasets/ziya07/iot-integrated-predictive-maintenance-dataset)
- [Industrial Atlas page](https://www.indatlas.com/datasets/iot-integrated-predictive-maintenance-dataset/)

[⬅️ Back to Index](../README.md)
