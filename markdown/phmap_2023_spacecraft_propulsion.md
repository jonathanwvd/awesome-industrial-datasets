# PHM Asia-Pacific 2023 Conference Data Challenge

Simulated pressure signals from a spacecraft propulsion system, built with JAXA, for diagnosing bubble anomalies, solenoid valve faults and unforeseen anomalies.

- **Domain:** Aerospace and defense
- **Asset / Process:** Valves and actuators
- **Modality:** Time series
- **Task:** Fault diagnosis; Classification; Regression
- **Annotation:** Class label; Scalar target
- **Source Type:** Simulation
- **Access:** Direct download
- **Size:** 177 training cases
- **Year:** 2023
- **Benchmark:** Yes

## Description

The PHM Asia-Pacific 2023 Conference Data Challenge uses data from a simulator of a simplified spacecraft propulsion system developed with the cooperation of the Japan Aerospace Exploration Agency (JAXA). In the modelled system, water pressurized to 2 MPa leaves through four solenoid valves that stand in for thrusters, and opening and closing them causes water hammer and acoustic pressure fluctuations.

Each case is a CSV file of pressure at measurement points P1 to P7, sampled at 1 kHz over 1200 ms while the valve sequence runs three times. Anomalies are air bubbles at eight possible locations and solenoid valves that open only partly; the test data also hold unforeseen anomalies. The 177 training cases come from spacecraft 1 to 3, and the test cases from spacecraft 1 and 4.

Teams label each test case as normal or abnormal, name the anomaly type, the bubble location or the failed valve, and predict its opening ratio. Points are given per task, and scores for spacecraft 4 count double.

## References

- [Official page](https://data.phmsociety.org/phmap-2023-data-challenge/)
- [Industrial Atlas page](https://www.indatlas.com/datasets/phmap-2023-spacecraft-propulsion/)

[⬅️ Back to Index](../README.md)
