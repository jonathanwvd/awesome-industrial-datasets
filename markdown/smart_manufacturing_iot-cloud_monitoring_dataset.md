# Smart Manufacturing IoT-Cloud Monitoring Dataset

Simulated IoT sensor dataset of 100,000 one-minute records from 50 machines, with anomaly flags, failure types and a maintenance target.

- **Domain:** Manufacturing
- **Modality:** Time series; Tabular
- **Task:** Classification; Fault diagnosis
- **Annotation:** Class label
- **Source Type:** Synthetic
- **Access:** Kaggle
- **Size:** 100,000 sensor records from 50 machines
- **License:** CC0 and public domain

## Description

The Smart Manufacturing IoT-Cloud Monitoring Dataset is a simulated set of IoT sensor readings from manufacturing machines. Its stated aim is to help with process monitoring, predictive maintenance and anomaly detection in industrial settings. The data is released under CC0 1.0.

The file smart_manufacturing_data.csv holds 100,000 sensor records from 50 machines, timestamped at 1-minute intervals. Each record gives temperature, vibration, humidity, pressure and energy consumption together with the machine's operational status, which is idle, running or failure.

Three kinds of label accompany the readings. Anomaly flags mark records with extreme sensor values, a failure type names the fault, and the target column maintenance_required states whether a machine needs maintenance. The readings come from simulation, not from an operating shop floor, although they are presented as real-time sensor data.

## References

- [Kaggle dataset](https://www.kaggle.com/datasets/ziya07/smart-manufacturing-iot-cloud-monitoring-dataset)
- [Industrial Atlas page](https://www.indatlas.com/datasets/smart-manufacturing-iot-cloud-monitoring-dataset/)

[⬅️ Back to Index](../README.md)
