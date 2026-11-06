# Gas sensor array under dynamic gas mixtures

**Summary:** About 12 hours of continuous recordings per mixture from a 16-sensor chemical array exposed to Ethylene-Methane and Ethylene-CO mixtures at randomly changing concentrations.

| Parameter | Value |
| --- | --- |
| **Domain** | Chemical and process |
| **Asset / Process** | — |
| **Modality** | Time series |
| **Task** | Regression |
| **Annotation** | Scalar target |
| **Source Type** | Lab or testbed |
| **Access** | UCI repository |
| **Size** | 4,178,504 instances in two files |
| **Year** | 2015 |
| **License** | Academic or non-commercial terms |
| **Publisher** | ChemoSignals Laboratory, BioCircuits Institute, University of California San Diego |

## Description

This dataset was recorded on a gas delivery platform at the ChemoSignals Laboratory of the BioCircuits Institute, University of California San Diego. Its creator, Jordi Fonollosa, donated it to the UCI Machine Learning Repository in 2015. Two mixtures in air were presented to the sensors: Ethylene with Methane, and Ethylene with CO.

The array has four units each of the Figaro TGS-2600, TGS-2602, TGS-2610 and TGS-2620 sensors, sampled at 100 Hz in a 60 ml chamber with a flow of 300 ml/min. Each mixture ran for about 12 hours while concentrations jumped to random levels every 80 to 120 s, within 0-20 ppm Ethylene, 0-600 ppm CO and 0-300 ppm Methane.

Each of the two text files has 19 columns: time, the two concentration set points and the 16 sensor readings, for 4,178,504 instances in total. The authors propose it for continuous monitoring, faster sensor response, and studies of sensor variability, sensor failure and calibration transfer. It is described in Fonollosa et al., Sensors and Actuators B, 2015.

## References

- [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/Gas+sensor+array+under+dynamic+gas+mixtures)
- [Industrial Atlas page](https://www.indatlas.com/datasets/gas-sensor-array-under-dynamic-gas-mixtures/)

[⬅️ Back to Index](../README.md)
