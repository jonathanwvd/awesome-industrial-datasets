# LUMEN Fault Diagnosis Benchmark

Hot-fire test and simulation data from a DLR liquid oxygen and methane rocket engine, with its simulator, for diagnosing fuel turbopump sensor and system faults.

- **Domain:** Aerospace and defense
- **Asset / Process:** Turbines and engines; Pumps, compressors and fans
- **Modality:** Time series; Simulator
- **Task:** Fault diagnosis
- **Source Type:** Mixed
- **Access:** Request or approval
- **Size:** 10 pre-simulated fault runs
- **Year:** 2025
- **Publisher:** German Aerospace Center (DLR)
- **Benchmark:** Yes

## Description

The LUMEN Fault Diagnosis Benchmark is built on LUMEN (Liquid Upper stage demonstrator Engine), a modular pump-fed rocket engine burning liquid oxygen and liquid methane, developed at the German Aerospace Center (DLR) Institute of Space Propulsion in Lampoldshausen. It was part of the competition at DX36, the 36th International Conference on Principles of Diagnosis and Resilient Systems in Nashville. The target is diagnosis of the engine's fuel turbopump subsystem.

Experimental data from the first hot-fire test campaign in early 2024 covers a transition between two stationary operating points, stored as CSV at 10 Hz. A simulation set adds five test runs with open-loop valve sequences and 10 pre-simulated fault runs. Faults include failed pump bearings, a blocked turbine inlet nozzle, pump leakage, a stuck fuel control valve and multiplicative faults in all sensors. The simulator generates noise-free data from four control valve positions.

The simulator and data are available on e-mail request. Python solutions are scored on secret test data at three levels (sensor faults, system faults, both) by false alarm rate, missed detection rate and fault isolation accuracy.

## References

- [Official page](https://vehsys.gitlab-pages.liu.se/dx25benchmarks/lumen/lumen_index)
- [Industrial Atlas page](https://www.indatlas.com/datasets/liu-lumen/)

[⬅️ Back to Index](../README.md)
