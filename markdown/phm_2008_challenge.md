# PHM 2008 Challenge

**Summary:** Turbofan engine degradation dataset used for the PHM 2008 Data Challenge, generated with the C-MAPSS simulator; designed for remaining useful life (RUL) prediction from multivariate sensor streams across a fleet of engines.

| Parameter | Value |
| --- | --- |
| **Associated Tasks** | Remaining Useful Life Prediction, Prognostics, Regression |
| **Data Source** | Synthetic |
| **Dataset Characteristics** | Multivariate, Time-Series |
| **Date Donated** | 2008 |
| **Feature Type** | Real |
| **Labeled** | Yes |
| **Missing Values** | No |
| **Name** | PHM 2008 Challenge |
| **Number of Features** | 26 per record: engine unit, cycle, 3 operational settings, 21 sensor measurements |
| **Number of Instances** | 218 turbofan engine trajectories (training and two test subsets) |
| **Source** | NASA Prognostics Center of Excellence / PHM Society |
| **Time Series** | Yes |

## Description

The PHM 2008 Challenge dataset was developed by the Prognostics Center of Excellence (PCoE) at NASA Ames Research Center and used in the International Conference on Prognostics and Health Management (PHM08) data challenge competition. It was generated using the Commercial Modular Aero-Propulsion System Simulation (C-MAPSS) tool, simulating realistic turbofan engine degradation.

Each engine in the fleet starts from a different initial health state with unknown initial wear. The multivariate time series consist of 26 columns: a unit identifier, the operational cycle counter, three operational setting columns that influence engine performance, and 21 sensor measurements of temperatures, pressures, and rotational speeds contaminated with realistic noise. The training set provides complete run-to-failure trajectories; the test set provides truncated trajectories ending before failure. Two separate test subsets are provided with a single training subset.

The challenge task is to estimate the remaining useful life (RUL) for each engine in the test set. The dataset is closely related to the CMAPSS series and is hosted on the NASA Open Data Portal and the PHM Society data repository.

## Tags

NASA, PHM Challenge, Predictive Maintenance, Prognostics, Remaining Useful Life, Run-to-Failure, Turbofan Engine

## References

- [NASA Open Data Portal](https://data.nasa.gov/Raw-Data/PHM-2008-Challenge/nk8v-ckry/data)
- [PHM Society Data Repository](https://data.phmsociety.org/nasa/)

[⬅️ Back to Index](../README.md)
