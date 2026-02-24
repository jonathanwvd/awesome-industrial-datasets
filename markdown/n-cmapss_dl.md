# N-CMAPSS_DL

**Summary:** New generation turbofan engine degradation dataset (N-CMAPSS) with 100 engines, 21 sensors, 7 failure modes, and 3 flight classes; designed for deep learning RUL estimation under realistic variable operating conditions and unknown initial health states.

| Parameter | Value |
| --- | --- |
| **Associated Tasks** | Remaining Useful Life Prediction, Prognostics, Deep Learning Benchmarking |
| **Data Source** | Synthetic |
| **Dataset Characteristics** | Multivariate, Time-Series |
| **Date Donated** | 2021 |
| **Feature Type** | Real |
| **Labeled** | Yes |
| **Missing Values** | No |
| **Name** | N-CMAPSS_DL |
| **Number of Features** | 26 per record: unit number, flight cycle, 3 operational settings (altitude, Mach number, throttle-resolver angle), 21 sensor measurements |
| **Number of Instances** | 100 engines; 4089 training cycles and 2736 test cycles; 7 failure modes; 3 flight classes |
| **Source** | NASA Prognostics Center of Excellence (PCoE) / PHM Society 2021 Data Challenge |
| **Time Series** | Yes |

## Description

N-CMAPSS (New Commercial Modular Aero-Propulsion System Simulation) extends the original CMAPSS dataset with more realistic degradation scenarios. It simulates a fleet of 100 high-bypass twin-spool turbofan engines (with 6 main components: fan, low-pressure compressor, high-pressure compressor, combustor, high-pressure turbine, low-pressure turbine) experiencing 7 different failure modes distributed across the fleet.

Key improvements over original CMAPSS: engines start from unknown initial health states (rather than nominally healthy), degradation trajectories follow non-linear paths, operating conditions have high variability (altitude, Mach number, temperature, throttle angle), and data is organized into 3 flight classes (short, medium, long) representing different mission profiles. Each record has 26 columns: unit number, flight cycle, 3 operational settings, and 21 sensor measurements with realistic noise. The Health Index (HI) decreases from 1 to 0 at failure.

The dataset was used for the PHM 2021 Data Challenge and is the basis for the N-CMAPSS_DL GitHub repository, which provides Python preprocessing scripts for deep learning workflows. Commonly used with Bidirectional LSTMs, CNNs, and transformer architectures.

## Tags

Deep Learning, PHM 2021, Predictive Maintenance, Prognostics, Remaining Useful Life, Sensor Data, Turbofan Engine

## References

- [GitHub - N-CMAPSS_DL preprocessing code](https://github.com/mohyunho/N-CMAPSS_DL)
- [NASA N-CMAPSS dataset on NASA Open Data Portal](https://data.nasa.gov/Aerospace/N-CMAPSS-dataset-for-the-PHME-2021-data-challenge/h9y2-p6dz/about_data)
- [PHM 2021 Data Challenge](https://data.phmsociety.org/2021-phm-conference-data-challenge/)

[⬅️ Back to Index](../README.md)
