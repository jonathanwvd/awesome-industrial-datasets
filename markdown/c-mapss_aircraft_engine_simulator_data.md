# C-MAPSS Aircraft Engine Simulator Data

**Summary:** This dataset was generated with the C-MAPSS simulator, a tool for the simulation of realistic large commercial turbofan engine data. The data consists of a series of flights with a reasonable linear transition period to allow the engine to change from one flight condition to the next. The fault was injected at a given time in one of the flights and persists throughout the remaining flights, effectively increasing the age of the engine. The intent is to identify which flight and when in the flight the fault occurred.

| Parameter | Value |
| --- | --- |
| **Name** | C-MAPSS Aircraft Engine Simulator Data |
| **Labeled** | Yes |
| **Time Series** | Yes |
| **Simulation** | Yes |
| **Missing Values** | NIA |
| **Dataset Characteristics** | Time-Series, Multivariate |
| **Feature Type** | Real, Integer |
| **Associated Tasks** | Regression, Classification |
| **Number of Instances** | N/A |
| **Number of Features** | N/A |
| **Date Donated** | NIA |
| **Source** | NASA |

## Special Note

C-MAPSS and C-MAPSS40K ARE CURRENTLY UNAVAILABLE FOR DOWNLOAD. Glenn Research Center management is reviewing the availability requirements for these software packages. We are working with Center management to get the review completed and issues resolved in a timely manner. We will post updates on this website when the issues are resolved. We apologize for any inconvenience. Please contact Jonathan Litt, jonathan.s.litt@nasa.gov, if you have any questions in the meantime.

## Subject Area

Engine Health

## Description

This data set was generated with the C-MAPSS simulator. C-MAPSS stands for 'Commercial Modular Aero-Propulsion System Simulation' and it is a tool for the simulation of realistic large commercial turbofan engine data. Each flight is a combination of a series of flight conditions with a reasonable linear transition period to allow the engine to change from one flight condition to the next. The flight conditions are arranged to cover a typical ascent from sea level to 35K ft and descent back down to sea level. The fault was injected at a given time in one of the flights and persists throughout the remaining flights, effectively increasing the age of the engine. The intent is to identify which flight and when in the flight the fault occurred.

## How Data Was Acquired

The data provided is from a high fidelity system level engine simulation designed to simulate nominal and fault engine degradation over a series of flights. The simulated data was created with a Matlab Simulink tool called C-MAPSS.

## Sample Rates and Parameter Description

The flights are full flight recordings sampled at 1 Hz and consist of 30 engine and flight condition parameters. Each flight contains 7 unique flight conditions for an approximately 90 min flight including ascent to cruise at 35K ft and descent back to sea level. The parameters for each flight are the flight conditions, health indicators, measurement temperatures and pressure measurements.

## Faults/Anomalies

Faults arose from the inlet engine fan, the low pressure compressor, the high pressure compressor, the high pressure turbine, and the low pressure turbine.

## Tags

Aircraft engine, Simulator data, Engine performance, Sensor data, Prognostics

## References

- [NASA's Open Data Portal](https://data.nasa.gov/dataset/C-MAPSS-Aircraft-Engine-Simulator-Data/xaut-bemq/about_data)

[⬅️ Back to Index](../README.md)