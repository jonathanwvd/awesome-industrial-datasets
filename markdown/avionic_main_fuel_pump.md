# Avionic Main Fuel Pump Simulation and Fault-Diagnosis Benchmark

Simulink Simscape model of an aircraft main fuel pump system with scripts that inject faults and write healthy and faulty multivariate time series with component labels.

- **Domain:** Aerospace and defense
- **Asset / Process:** Pumps, compressors and fans
- **Modality:** Simulator; Time series
- **Task:** Fault diagnosis
- **Annotation:** Class label
- **Source Type:** Simulation
- **Access:** Code repository
- **Size:** Around 12 GB of generated CSV files
- **Year:** 2026
- **License:** MIT

## Description

This benchmark is a MATLAB/Simulink Simscape Fluids model of an aircraft main fuel pump system, together with the scripts that generate multivariate time series from it. The model covers the tank, main pump, bypass, fuel metering unit, pressure relief valve and injectors. It accompanies a 2026 IFAC World Congress paper by F. L. Janzen, L. Moddemann, A. Diedrich and O. Niggemann.

A throttle command profile stands for a typical flight power profile. A generation script runs the model in healthy or faulty mode, injects predefined fault scenarios and writes the time series with identifiers to CSV files, with health and fault modes labelled at component level. The generated files take around 12 GB of disk space.

Running the model needs MATLAB with Simulink, Simscape and Simscape Fluids; it was built in MATLAB R2025a. The paper applies a recurrent variational autoencoder for anomaly detection and a SOM-VAE for operating mode discretization. The repository is under the MIT License.

## References

- [GitHub repository](https://github.com/Elix96J/Avionic_Main_Fuel_Pump_Simulation_and_Fault-Diagnosis_Benchmark)
- [Preprint (arXiv)](https://arxiv.org/abs/2604.22869)
- [Industrial Atlas page](https://www.indatlas.com/datasets/avionic-main-fuel-pump/)

[⬅️ Back to Index](../README.md)
