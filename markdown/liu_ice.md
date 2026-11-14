# LiU-ICE Industrial Fault Diagnosis Benchmark - DeluXe 2025

Engine test bench recordings from the air path of a combustion engine with an intake manifold leak and sensor faults, set up as a scored diagnosis benchmark.

- **Domain:** Transportation and mobility
- **Asset / Process:** Turbines and engines; Vehicles and fleets
- **Modality:** Time series
- **Task:** Fault diagnosis
- **Annotation:** Class label; Event and time label
- **Source Type:** Lab or testbed
- **Access:** Direct download
- **Size:** 26 training datasets
- **Year:** 2025
- **Publisher:** Linköping University
- **Benchmark:** Yes

## Description

The LiU-ICE Industrial Fault Diagnosis Benchmark - DeluXe 2025 calls for diagnosing faults in the air path of an internal combustion engine. It was part of the competition at DX36, the 36th International Conference on Principles of Diagnosis and Resilient Systems in Nashville, organized by Daniel Jung, Erik Frisk and Mattias Krysander of the Department of Electrical Engineering at Linköping University, Sweden. It was used before in the IFAC Safeprocess 2024 competition.

The data comes from an engine test bench following the WLTP driving cycle in every training file. Each CSV file holds two actuator and eight sensor signals at 20 Hz. The 26 training datasets cover nominal operation, an intake manifold leakage and multiplicative faults in the air mass flow, intercooler pressure and intake manifold pressure sensors, each fault starting about 120 s into the run.

Participants also get an analytical engine model with unidentified parameters, implemented in the Python Fault Diagnosis Toolbox, and an evaluation environment. Solutions are scored on secret test data by false alarm rate, true detection rate and fault isolation accuracy, combined as ((1-FAR) + TDR + FIA)/3.

## References

- [Official page](https://vehsys.gitlab-pages.liu.se/dx25benchmarks/liuice/liuice_index)
- [Industrial Atlas page](https://www.indatlas.com/datasets/liu-ice/)

[⬅️ Back to Index](../README.md)
