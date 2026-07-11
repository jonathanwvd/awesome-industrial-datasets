# Genesis Pick-and-Place Demonstrator Dataset

**Summary:** The dataset consists of sensor and state data from a portable Genesis pick-and-place demonstrator, including normal behavior and labeled anomalies related to a linear drive.

| Parameter | Value |
| --- | --- |
| **Dataset** | Genesis Pick-and-Place Demonstrator Dataset |
| **Domain** | Robotics & Automation; Manufacturing & Production |
| **Asset / Process** | Robotic Manipulation |
| **Modality** | Time Series |
| **Task** | Anomaly Detection; Condition Monitoring |
| **Annotation** | Sample Label; Time / Event Label |
| **Source Type** | Real Lab / Testbed |
| **Access** | Kaggle; Login Required |
| **Size** | 16220 |
| **Year** | 2018 |
| **License** | Information not available |

## Description

The Genesis Demonstrator was created during the OPAK Project and further revised during the IMPROVE project. It is a portable pick-and-place machine that uses an air tank to supply gripping and storage units. The dataset records 5 continuous signals, 13 discrete signals, and 1 Unix Timestamp, with some datasets containing labels. The demonstrator sorts two different materials (wood and metal) into their corresponding target locations using four modules: Storage Magazine, Sensor, Metal storage, and Wood storage. A pneumatic linear drive transports the materials through a defined sequence of operations controlled by a PLC.

The first labeled dataset contains 16220 observations taken every 50ms via an OPC DA server, with labels indicating the internal PLC state machine or anomalies. The anomaly labels are manually annotated and include three types: no anomaly, jammed/tilted linear drive, and a linear drive breaking free to correct lag error. Missing values and zero-variance columns have been removed. A second unlabeled dataset contains normal runs and runs with errors for predictive maintenance or anomaly detection, with impairments such as linear drive degradation or reduced air pressure. The datasets may not be fully compatible with each other.

## References

- [Kaggle Dataset](https://www.kaggle.com/datasets/inIT-OWL/genesis-demonstrator-data-for-machine-learning)
- [von Birgelen, Alexander; Niggemann, Oliver: Anomaly Detection and Localization for Cyber-Physical Production Systems with Self-Organizing Maps. Springer Vieweg, Aug 2018.](https://www.init-owl.de/en/research/publications/detail/anomaly-detection-and-localization-for-cyber-physical-production-systems-with-self-organizing-maps/)

[⬅️ Back to Index](../README.md)
