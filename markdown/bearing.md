# Bearing

**Summary:** NASA/University of Cincinnati IMS bearing run-to-failure dataset with 3 complete degradation tests on 4 double-row bearings at 2000 RPM under 6,000 lb radial load; 100 kHz vibration data recorded every 10 minutes until failure.

| Parameter | Value |
| --- | --- |
| **Associated Tasks** | Remaining Useful Life Prediction, Prognostics, Fault Detection |
| **Data Source** | Real |
| **Dataset Characteristics** | Multivariate, Time-Series |
| **Date Donated** | 2007 |
| **Feature Type** | Real (vibration acceleration) |
| **Labeled** | Yes |
| **Missing Values** | No |
| **Name** | Bearing |
| **Number of Features** | 8 accelerometer channels (4 bearings × 2 directions); 100 kHz sampling rate; 1-second snapshots every 10 minutes |
| **Number of Instances** | 3 run-to-failure tests; Test 1: ~2,156 snapshots (34 days), Test 2: ~984 snapshots (7 days), Test 3: ~6,324 snapshots (37 days); each snapshot contains 20,480 data points per channel |
| **Source** | NASA Prognostics Center of Excellence (PCoE) / University of Cincinnati IMS Center |
| **Time Series** | Yes |

## Description

The IMS (Intelligent Maintenance Systems) Bearing Dataset was collected at the University of Cincinnati's Center for Intelligent Maintenance Systems and contributed to NASA's Prognostics Center of Excellence (PCoE) Data Repository by Hai Qiu, Jay Lee, Jing Lin, and Gang Yu in 2003.

The test rig consists of a shaft loaded with 6,000 lb radial force, rotating at a constant speed of 2,000 RPM, with 4 Rexnord ZA-2115 double-row rolling element bearings mounted on the shaft. PCB 353B33 accelerometers are mounted on the bearing housings, recording vibration in two directions at 100 kHz. Data snapshots of 1 second (20,480 points) are collected every 10 minutes until bearing failure.

Three run-to-failure tests were conducted:
- Test 1 (Oct–Nov 2003, ~34 days): Bearing 3 outer race fault, Bearing 4 rolling element defect
- Test 2 (Feb 2004, ~7 days): Bearing 1 outer race fault
- Test 3 (Mar–Apr 2004, ~37 days): Bearing 3 outer race fault

This dataset is a primary benchmark for bearing RUL estimation, prognostics, and condition monitoring research. It has been used with LSTM, CNN, autoencoder, and transformer architectures for health indicator construction and failure prediction.

## Tags

Accelerometer, Bearing, IMS, NASA, Predictive Maintenance, Prognostics, Remaining Useful Life, Rotating Machinery, Run-to-Failure, Vibration

## References

- [NASA PCoE Data Repository - Bearing Dataset](https://ti.arc.nasa.gov/tech/dash/groups/pcoe/prognostic-data-repository/#bearing)
- [Original Paper: Self-organizing map based on bearing health evaluation (Qiu et al., 2006, JSV)](https://doi.org/10.1016/j.jsv.2005.06.072)

[⬅️ Back to Index](../README.md)
