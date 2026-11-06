# Wind Turbine Scada Dataset

SCADA records at 10-minute intervals from a working wind turbine in Turkey during 2018, pairing measured power with the theoretical power curve.

- **Domain:** Energy and power
- **Asset / Process:** Wind turbines
- **Modality:** Time series
- **Task:** Regression; Condition monitoring
- **Annotation:** Scalar target
- **Source Type:** Real production
- **Access:** Kaggle

## Description

The Wind Turbine Scada Dataset contains 2018 data from the SCADA system of a wind turbine that is in service and generating power in Turkey. On wind turbines, SCADA systems record quantities such as wind speed, wind direction and generated power at 10-minute intervals.

The single file, T1.csv, has one row per 10-minute interval and five columns. They give the timestamp, the active power the turbine produced at that moment in kW, the wind speed at hub height in m/s, which is the wind the turbine uses to generate electricity, the theoretical power the manufacturer specifies for that wind speed, and the wind direction at hub height in degrees, toward which the turbine turns automatically.

Each record pairs the measured active power with the manufacturer's theoretical power for the same wind speed.

## References

- [Kaggle dataset](https://www.kaggle.com/datasets/berkerisen/wind-turbine-scada-dataset)
- [Industrial Atlas page](https://www.indatlas.com/datasets/wind-turbine-scada-dataset/)

[⬅️ Back to Index](../README.md)
