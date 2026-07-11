# Secure Water Treatment (SWaT) Dataset

**Summary:** The SWaT dataset represents a scaled-down but high-fidelity replica of a modern six-stage water treatment facility that processes approximately 19 litres of water per minute and contains both normal operational data and records of various cyber-physical attacks.

| Parameter | Value |
| --- | --- |
| **Dataset** | Secure Water Treatment (SWaT) Dataset |
| **Domain** | Cyber-Physical Security; Water & Utilities |
| **Asset / Process** | Water Treatment / Distribution; SCADA / ICS |
| **Modality** | Time Series |
| **Task** | Cyberattack Detection; Anomaly Detection; Process Monitoring |
| **Annotation** | Time / Event Label; Fault Type Label |
| **Source Type** | Real Lab / Testbed |
| **Access** | Official Portal; Form Request; Gated Approval |
| **Size** | Information not available |
| **Year** | 2020 |
| **License** | Custom Research |

## Description

The Secure Water Treatment (SWaT) dataset was collected from an operational water treatment testbed over 11 days, consisting of 7 days under normal operation and 4 days with multiple cyber-physical attack scenarios. It contains network traffic and sensor/actuator values, with data labelled according to normal and abnormal behaviors. Attack scenarios are derived from the intent space of a cyber-physical system with 41 attacks launched during the four days.

The dataset provides a time series of 51 sensors and actuators data collected continuously, serving as a benchmark for anomaly detection in industrial control systems and cybersecurity research. Updates to the dataset include different versions with attack data and normal operating conditions, with data collected at different times from 2015 to 2020, including network traffic (pcap files) and historian data.

Researchers use this dataset for developing machine learning approaches to detect anomalies, including convolutional and recurrent neural networks, leveraging advanced deep learning techniques to secure critical infrastructure like water treatment facilities.

## References

- [A Dataset to Support Research in the Design of Secure Water Treatment Systems](https://www.researchgate.net/publication/305809559_A_Dataset_to_Support_Research_in_the_Design_of_Secure_Water_Treatment_Systems)
- [SWaT: a water treatment testbed for research and training on ICS security](https://ieeexplore.ieee.org/document/7469060)
- [iTrust Datasets Page](https://itrust.sutd.edu.sg/itrust-labs_datasets/)

[⬅️ Back to Index](../README.md)
