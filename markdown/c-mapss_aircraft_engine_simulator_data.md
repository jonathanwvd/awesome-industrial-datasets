# C-MAPSS Aircraft Engine Simulator Data

Simulated turbofan flights from NASA's C-MAPSS model with an injected engine fault, at 1 Hz over 30 engine and flight parameters.

- **Domain:** Aerospace and defense
- **Asset / Process:** Turbines and engines
- **Modality:** Time series
- **Task:** Anomaly detection; Anomaly localization
- **Source Type:** Simulation
- **Size:** 30 parameters at 1 Hz per flight
- **Publisher:** NASA

## Description

C-MAPSS Aircraft Engine Simulator Data was generated with C-MAPSS (Commercial Modular Aero-Propulsion System Simulation), a MATLAB Simulink tool for simulating a large commercial turbofan engine. It is filed under the subject area Engine Health.

The data comes from a high-fidelity, system-level engine simulation of nominal and faulty degradation over a series of flights. Each flight of about 90 minutes contains 7 distinct flight conditions, and the data is sampled at 1 Hz over 30 engine and flight-condition parameters. A fault is injected at a given time in one of the flights; faults arise in the inlet fan, the low and high pressure compressors and the high and low pressure turbines.

The task is to find which flight and when in that flight the fault occurred. NASA lists the C-MAPSS and C-MAPSS40K data as currently unavailable for download.

## References

- [Official page](https://data.nasa.gov/dataset/c-mapss-aircraft-engine-simulator-data)
- [Industrial Atlas page](https://www.indatlas.com/datasets/c-mapss-aircraft-engine-simulator-data/)

[⬅️ Back to Index](../README.md)
