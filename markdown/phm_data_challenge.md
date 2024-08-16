# PHM Data Challenge

**Summary:** The PHM Data Challenge focuses on fault detection and prognostics in industrial plant monitoring, requiring participants to predict and precisely localize plant faults.

| Parameter | Value |
| --- | --- |
| **Name** | PHM Data Challenge |
| **Labeled** | Yes |
| **Time Series** | Yes |
| **Simulation** | No |
| **Missing Values** | Yes |
| **Dataset Characteristics** | Time-Series |
| **Feature Type** | Real |
| **Associated Tasks** | Classification, Regression |
| **Number of Instances** | N/A |
| **Number of Features** | N/A |
| **Date Donated** | 2015 |
| **Source** | PHM Society |

## Dataset Informatio

This year’s prognostics topic focuses on the operation of a plant and the capability to detect plant failure events in advance. Data given represents: (a) time series of sensor measurements and control reference signals for each of a number of control components of the plant (e.g., 6 components); (b) time series data representing additional measurements of a fixed number of plant zones over the same period of time (e.g., 3 zones), where a zone may cover one or more plant components; (c) plant fault events, each characterized by a start time, an end time, and a failure code. Each plant is specific through its number of components and the number of zones. However, each plant logs faults from the same fixed set of faults. Only faults of type 1-5 are of interest, while code 6 represents all other faults not in focus. The frequency of measurements is approximately one sample every 15 minutes, and the time series data spans a period of approximately three to four years. The task is to predict future failure events of types 1-5 and the time of their occurrence from past data.

For example, the data set for Plant #1 is given by a collection of three [.csv] files: plant-1a.csv, plant-1b.csv, plant-1c.csv. Each of the (a), (b), and (c) files contains information as described above. More precisely the columns of each of the (a), (b), and (c) [.csv] files are:

Plant measurements per component: Component number “m”, time “t”, sensors “S1”-“S4”, and control references “R1”-“R4”
Additional plant measurements per zone in the plant: zone number “n”, time “t”, sensors “E1” and “E2”
Faults: Start time “t1”, end time “t2”, and fault code “F”.

Additionally, the following physical plant model information is provided:

Each plant component is controlled by a feedback loop system as represented in the figure below; plant components are disjoint
Each zone measures cumulative energy consumed (E1) and instantaneous power (E2) in disjoint sections of the plant covering one or more components
Faults are independent of one another. Also, a fault F is independent of data outside of a three hour window of time before the fault start time.

The participants will have access to the following data sets:
Training data for approximately thirty plants (e.g., see Plant 1 described above).
Test data for approximately ten plants. For each test plant, the first half of the fault file data is complete, while the second half is incomplete. Some faults of type 1-5 are missing.

## Tags

PHM, Fault detection, Prognostics, Industrial monitoring, Time-series analysis, Plant monitoring

## References

- [PHM Society Data Challenge](https://phmsociety.org/conference/annual-conference-of-the-phm-society/annual-conference-of-the-prognostics-and-health-management-society-2015/phm-data-challenge-3/)

[⬅️ Back to Index](../README.md)
