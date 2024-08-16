# Gas sensor array under dynamic gas mixtures

**Summary:** The data set contains the recordings of 16 chemical sensors exposed to two dynamic gas mixtures at varying concentrations. For each mixture, signals were acquired continuously during 12 hours.

| Parameter | Value |
| --- | --- |
| **Name** | Gas sensor array under dynamic gas mixtures |
| **Labeled** | Yes |
| **Time Series** | Yes |
| **Simulation** | No |
| **Missing Values** | No |
| **Dataset Characteristics** | Multivariate, Time-Series |
| **Feature Type** | Real |
| **Associated Tasks** | Classification, Regression |
| **Number of Instances** | 417850 |
| **Number of Features** | 19 |
| **Date Donated** | 2015-03-1 |
| **Source** | UCI Machine Learning Repository |

## Dataset Information

This data set contains the acquired time series from 16 chemical sensors exposed to gas mixtures at varying concentration levels. In particular, we generated two gas mixtures: Ethylene and Methane in air, and Ethylene and CO in air. Each measurement was constructed by the continuous acquisition of the 16-sensor array signals for a duration of about 12 hours without interruption.

The data set was collected in a gas delivery platform facility at the ChemoSignals Laboratory in the BioCircuits Institute, University of California San Diego. The measurement system platform provides versatility for obtaining the desired concentrations of the chemical substances of interest with high accuracy and in a highly reproducible manner.

The sensor array included 16 chemical sensors (Figaro Inc., US) of 4 different types: TGS-2600, TGS-2602, TGS-2610, TGS-2620 (4 units of each type). The sensors were integrated with customized signal conditioning and control electronics. The operating voltage of the sensors, which controls the sensors' operating temperature, was kept constant at 5 V for the whole duration of the experiments. The sensors' conductivities were acquired continuously at a sampling frequency of 100 Hz. The sensor array was placed in a 60 ml measurement chamber, where the gas sample was injected at a constant flow of 300 ml/min.

Each measurement was constructed by the continuous acquisition of the 16-sensor array signals while concentration levels changed randomly. For each measurement (each gas mixture), the signals were acquired continuously for about 12 hours without interruption.

The concentration transitions were set at random times (in the interval 80-120s) and to random concentration levels. The data set was constructed such that all possible transitions are present: increasing, decreasing, or setting to zero the concentration of one volatile while the concentration of the other volatile is kept constant (either at a fixed or at zero concentration level). At the beginning, ending, and approximately every 10,000 s, we inserted additional predefined concentration patterns with pure gas mixtures.

The concentration ranges for Ethylene, Methane, and CO were selected such that the induced magnitudes of the sensor responses were similar. Moreover, for gas mixtures, lower concentration levels were favored. Therefore, the multivariate response of the sensors to the presented set of stimuli is challenging since none of the configurations (single gas or mixture presentation) can be easily identified from the magnitude of sensors' responses. In particular, Ethylene concentration ranges from 0-20 ppm; 0-600 ppm for CO; and 0-300 ppm for Methane.

The primary purpose of making this data set freely accessible online is to provide extensive and continuous time series acquired from chemical sensors to the sensor and artificial intelligence research communities to develop and test strategies to solve a wide variety of tasks. In particular, the data set may be useful to develop algorithms for continuous monitoring or improve response time of sensory systems. Also, the repetition of the same type of sensors in the array will allow further investigation on sensor variability (reproducibility of sensors of the same kind). Other interesting topics may include sensor failure (to what extent system predictions degrade when sensors start failing) or calibration transfer (whether the model for one sensor can be extended to other sensors).

More information on the generated data set can be found in Fonollosa et al. 'Reservoir Computing compensates slow response of chemosensor arrays exposed to fast varying gas concentrations in continuous monitoring'; Sensors and Actuators B, 2015.

The data set can be used exclusively for research purposes. Commercial purposes are fully excluded.

## Tags

Gas sensors, Dynamic mixtures, Sensor data, Time-series data, Chemical sensors

## References

- [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/Gas+sensor+array+under+dynamic+gas+mixtures)

[⬅️ Back to Index](../README.md)
