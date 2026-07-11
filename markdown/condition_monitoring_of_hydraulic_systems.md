# Condition monitoring of hydraulic systems

**Summary:** The data set addresses the condition assessment of a hydraulic test rig based on multi sensor data. Four fault types are superimposed with several severity grades impeding selective quantification.

| Parameter | Value |
| --- | --- |
| **Dataset** | Condition monitoring of hydraulic systems |
| **Domain** | Oil & Gas; Energy & Power; Manufacturing & Production |
| **Asset / Process** | Motors / Drives; Pumps; Valves / Actuators |
| **Modality** | Time Series; Vibration |
| **Task** | Fault Diagnosis; Condition Monitoring; Energy Optimization; Classification |
| **Annotation** | Fault Type Label; Scalar Target; Sample Label; Class Label |
| **Source Type** | Real Lab / Testbed |
| **Access** | UCI |
| **Size** | 2205 |
| **Year** | 2018 |
| **License** | Information not available |

## Description

The data set was experimentally obtained with a hydraulic test rig. This test rig consists of a primary working and a secondary cooling-filtration circuit which are connected via the oil tank [1], [2]. The system cyclically repeats constant load cycles (duration 60 seconds) and measures process values such as pressures, volume flows and temperatures while the condition of four hydraulic components (cooler, valve, pump and accumulator) is quantitatively varied.

Attribute Information:
The data set contains raw process sensor data (i.e. without feature extraction) which are structured as matrices (tab-delimited) with the rows representing the cycles and the columns the data points within a cycle. The sensors involved are:
PS1-PS6 (Pressure, bar, 100 Hz), EPS1 (Motor power, W, 100 Hz), FS1-FS2 (Volume flow, l/min, 10 Hz), TS1-TS4 (Temperature, °C, 1 Hz), VS1 (Vibration, mm/s, 1 Hz), CE (Cooling efficiency, %, 1 Hz), CP (Cooling power, kW, 1 Hz), SE (Efficiency factor, %, 1 Hz).

The target condition values are cycle-wise annotated in "profile.txt" (tab-delimited), with the columns representing cooler condition percentage, valve condition percentage, internal pump leakage, hydraulic accumulator pressure in bar, and a stable flag indicating if conditions were stable or not.

## References

- [Helwig, N., Pignanelli, E., & Schtze, A. (2015). Condition monitoring of hydraulic systems [Dataset]. UCI Machine Learning Repository. https://doi.org/10.24432/C5CW21.](https://doi.org/10.24432/C5CW21)
- [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/Condition+monitoring+of+hydraulic+systems)

[⬅️ Back to Index](../README.md)
