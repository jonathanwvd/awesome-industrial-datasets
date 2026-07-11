# Gas sensor array temperature modulation

**Summary:** A chemical detection platform composed of 14 temperature-modulated metal oxide (MOX) gas sensors was exposed during 3 weeks to mixtures of carbon monoxide and humid synthetic air in a gas chamber.

| Parameter | Value |
| --- | --- |
| **Dataset** | Gas sensor array temperature modulation |
| **Domain** | Chemical & Process; Electronics & Semiconductor |
| **Asset / Process** | Chemical Process |
| **Modality** | Time Series |
| **Task** | Classification; Regression |
| **Annotation** | Class Label; Scalar Target |
| **Source Type** | Real Lab / Testbed |
| **Access** | UCI |
| **Size** | 4095000 |
| **Year** | 2019 |
| **License** | Information not available |

## Description

A chemical detection platform composed of 14 temperature-modulated metal oxide semiconductor (MOX) gas sensors was exposed to dynamic mixtures of carbon monoxide (CO) and humid synthetic air in a gas chamber. The acquired time series of the sensors and the measured values of CO concentration, humidity and temperature inside the gas chamber are provided.

The chemical detection platform consists of 14 MOX gas sensors, 7 units of TGS 3870-A04 sensors by Figaro Engineering and 7 units of SB-500-12 by FIS. The operating temperature of the sensors was controlled by a modulated heater voltage cycling between 0.2-0.9 V. Sensors were pre-heated for one week before experiments. The sensors' output voltage was sampled at 3.5 Hz using an Agilent DAQ system.

Dynamic gas mixtures were generated with mass flow controllers controlling streams of CO, wet and dry air delivered into a small PTFE test chamber. The CO concentration ranged from 0 to 20 ppm with relative humidity between 15% and 75%. Each experiment included 100 measurements, lasting approximately 25 hours per experiment, replicated across 13 working days over 17 calendar days. The dataset is contained in 13 text files corresponding to each measurement day.

## References

- [UCI Machine Learning Repository Dataset Page](https://archive.ics.uci.edu/dataset/487/gas+sensor+array+temperature+modulation)
- [Dataset DOI](https://doi.org/10.24432/C5S302)

[⬅️ Back to Index](../README.md)
