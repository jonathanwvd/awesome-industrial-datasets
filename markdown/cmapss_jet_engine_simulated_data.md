# CMAPSS Jet Engine Simulated Data

**Summary:** The dataset comprises simulated jet engine data from NASA's CMAPSS. It includes operational settings and sensor measurements for engines under various fault conditions, aimed at prognostics and health management research.

| Parameter | Value |
| --- | --- |
| **Name** | CMAPSS Jet Engine Simulated Data |
| **Labeled** | Yes |
| **Time Series** | Yes |
| **Simulation** | Yes |
| **Missing Values** | No |
| **Dataset Characteristics** | Time-Series, Multivariate |
| **Feature Type** | Real |
| **Associated Tasks** | Regression, Anomaly Detection |
| **Number of Instances** | INA |
| **Number of Features** | INA |
| **Date Donated** | INA |
| **Source** | NASA |

## Dataset Information

Data sets consists of multiple multivariate time series. Each data set is further divided into training and test subsets. Each time series is from a different engine i.e., the data can be considered to be from a fleet of engines of the same type. Each engine starts with different degrees of initial wear and manufacturing variation which is unknown to the user. This wear and variation is considered normal, i.e., it is not considered a fault condition. There are three operational settings that have a substantial effect on engine performance. These settings are also included in the data. The data is contaminated with sensor noise.
The engine is operating normally at the start of each time series, and develops a fault at some point during the series. In the training set, the fault grows in magnitude until system failure. In the test set, the time series ends some time prior to system failure. The objective of the competition is to predict the number of remaining operational cycles before failure in the test set, i.e., the number of operational cycles after the last cycle that the engine will continue to operate. Also provided a vector of true Remaining Useful Life (RUL) values for the test data.

## Tags

Jet engines, Simulation data, Prognostics, Health management, Aerospace engineering

## References

- [NASA Open Data Portal](https://data.nasa.gov/Aerospace/CMAPSS-Jet-Engine-Simulated-Data/ff5v-kuh6/about_data)

[⬅️ Back to Index](../README.md)
