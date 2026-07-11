# Bearing

**Summary:** NASA/University of Cincinnati IMS bearing run-to-failure dataset with 3 complete degradation tests on 4 double-row bearings at 2000 RPM under 6,000 lb radial load; 100 kHz vibration data recorded every 10 minutes until failure.

| Parameter | Value |
| --- | --- |
| **Dataset** | Bearing |
| **Domain** | Manufacturing & Production |
| **Asset / Process** | Bearings |
| **Modality** | Time Series; Vibration |
| **Task** | Fault Diagnosis; RUL / Prognostics; Predictive Maintenance |
| **Annotation** | Sample Label; RUL Label |
| **Source Type** | Real Lab / Testbed |
| **Access** | Official Portal |
| **Size** | 3 run-to-failure tests; Test 1: ~2,156 snapshots (34 days), Test 2: ~984 snapshots (7 days), Test 3: ~6,324 snapshots (37 days); each snapshot contains 20,480 data points per channel |
| **Year** | 2007 |
| **License** | Information not available |

## Description

The IMS (Intelligent Maintenance Systems) Bearing Dataset was collected at the University of Cincinnati's Center for Intelligent Maintenance Systems and contributed to NASA's Prognostics Center of Excellence (PCoE) Data Repository by Hai Qiu, Jay Lee, Jing Lin, and Gang Yu in 2003.

The test rig consists of a shaft loaded with 6,000 lb radial force, rotating at a constant speed of 2,000 RPM, with 4 Rexnord ZA-2115 double-row rolling element bearings mounted on the shaft. PCB 353B33 accelerometers are mounted on the bearing housings, recording vibration in two directions at 100 kHz. Data snapshots of 1 second (20,480 points) are collected every 10 minutes until bearing failure.

Three run-to-failure tests were conducted:
- Test 1 (Oct–Nov 2003, ~34 days): Bearing 3 outer race fault, Bearing 4 rolling element defect
- Test 2 (Feb 2004, ~7 days): Bearing 1 outer race fault
- Test 3 (Mar–Apr 2004, ~37 days): Bearing 3 outer race fault

This dataset is a primary benchmark for bearing RUL estimation, prognostics, and condition monitoring research. It has been used with LSTM, CNN, autoencoder, and transformer architectures for health indicator construction and failure prediction.

## References

- [NASA PCoE Data Set Repository](https://www.nasa.gov/intelligent-systems-division/discovery-and-systems-health/pcoe/pcoe-data-set-repository/)
- [IMS Bearings entry on NASA Open Data](https://data.nasa.gov/dataset/ims-bearings)

[⬅️ Back to Index](../README.md)
