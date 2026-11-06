# CMAPSS Jet Engine Simulated Data

**Summary:** Simulated run-to-failure trajectories of a turbofan engine fleet in four subsets, with truncated test series and true remaining useful life values.

| Parameter | Value |
| --- | --- |
| **Domain** | Aerospace and defense |
| **Asset / Process** | Turbines and engines |
| **Modality** | Time series |
| **Task** | RUL and prognostics; Regression |
| **Annotation** | RUL label |
| **Source Type** | Simulation |
| **Access** | Direct download |
| **Size** | 4 subsets (FD001 to FD004) of multivariate time series |
| **Year** | 2008 |
| **License** | — |
| **Publisher** | NASA Ames Prognostics Center of Excellence (PCoE) |

## Description

CMAPSS Jet Engine Simulated Data is the Turbofan Engine Degradation Simulation data set from the NASA Ames Prognostics Center of Excellence (PCoE). It was produced with the Commercial Modular Aero-Propulsion System Simulation (C-MAPSS) and is cited as A. Saxena and K. Goebel (2008).

Each time series comes from a different engine of the same type, each starting with its own undisclosed initial wear and manufacturing variation, with sensor noise added. Rows are single operational cycles with 26 space-separated columns: unit number, time in cycles, three operational settings and sensor measurements.

FD001 and FD003 have 100 training and 100 test trajectories at sea level; FD002 (260 and 259) and FD004 (248 and 249) cover six conditions. FD001 and FD002 have HPC degradation only; FD003 and FD004 add fan degradation. Training series run until failure, while test series stop earlier. The task is to predict the remaining operational cycles, and a vector of true RUL values is supplied for the test data.

## References

- [Official page](https://data.nasa.gov/dataset/cmapss-jet-engine-simulated-data)
- [nasa.gov](https://www.nasa.gov/intelligent-systems-division/discovery-and-systems-health/pcoe/pcoe-data-set-repository/)
- [Industrial Atlas page](https://www.indatlas.com/datasets/cmapss-jet-engine-simulated-data/)

[⬅️ Back to Index](../README.md)
