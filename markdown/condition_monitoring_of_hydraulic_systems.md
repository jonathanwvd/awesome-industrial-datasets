# Condition monitoring of hydraulic systems

**Summary:** Multi-sensor recordings of 2,205 load cycles on a hydraulic test rig, with cycle-wise condition grades for cooler, valve, pump and accumulator.

| Parameter | Value |
| --- | --- |
| **Domain** | Manufacturing |
| **Asset / Process** | Pumps, compressors and fans; Valves and actuators |
| **Modality** | Time series |
| **Task** | Fault diagnosis; Condition monitoring; Regression |
| **Annotation** | Class label; Scalar target |
| **Source Type** | Lab or testbed |
| **Access** | UCI repository |
| **Size** | 2,205 load cycles |
| **Year** | 2018 |
| **License** | CC BY |

## Description

The Condition Monitoring of Hydraulic Systems dataset was recorded on a hydraulic test rig with a primary working circuit and a secondary cooling-filtration circuit joined through the oil tank. Nikolai Helwig, Eliseo Pignanelli and Andreas Schütze created it, and it was donated to the UCI Machine Learning Repository in 2018.

The rig repeats constant 60-second load cycles while the condition of the cooler, valve, pump and accumulator is varied. Raw sensor signals come as tab-delimited matrices, one row per cycle: six pressures and motor power at 100 Hz, two volume flows at 10 Hz, and four temperatures, vibration, virtual cooling efficiency and cooling power, and an efficiency factor at 1 Hz.

The four fault types are superimposed at several severity grades. A profile file labels each of the 2,205 cycles with cooler condition (3, 20 or 100 %), valve condition (100 to 73 %), internal pump leakage (none, weak, severe), accumulator pressure (130 to 90 bar) and a stability flag. There are no missing values; the license is CC BY 4.0.

## References

- [DOI](https://doi.org/10.24432/C5CW21)
- [Industrial Atlas page](https://www.indatlas.com/datasets/condition-monitoring-of-hydraulic-systems/)

[⬅️ Back to Index](../README.md)
