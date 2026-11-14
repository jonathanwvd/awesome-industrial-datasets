# Experimental Dataset of retired batteries (first-life, second-life and third-life) discharged at constant power rate

Constant-power discharge tests on six retired lithium-ion cells grouped by state of health, with 324 records of voltage, current, power and temperature at 1 Hz.

- **Domain:** Energy and power
- **Asset / Process:** Batteries
- **Modality:** Time series
- **Task:** Condition monitoring
- **Source Type:** Lab or testbed
- **Access:** IEEE DataPort
- **Size:** 324 discharge records in 36 CSV files

## Description

This dataset records constant-power discharge tests on six retired lithium-ion cells, grouped by state of health (SoH) into first-life, second-life and third-life batteries. It is meant for research on battery degradation, SoH estimation, second- and third-life applications, thermal behaviour and energy storage management.

First-life cells hold 1870 and 1804 mAh (SoH 85% and 82%), second-life cells 1320 and 990 mAh (60% and 45%), and third-life cells 530 and 490 mAh (24% and 22%). Each cell was charged to 4.2 V and discharged to 2.5 V at nine constant power levels from 2 W to 10 W in 1 W steps, six times over, giving 324 records.

Voltage, current, power, equivalent resistance and surface temperature are logged at 1 Hz by a Raspberry Pi 4 with an ADS1115 converter, an ACS712 5 A Hall-effect current sensor and 10 kΩ NTC thermistors. A ZIP archive holds 36 CSV files, one per cell and batch.

## References

- [DOI](https://doi.org/10.21227/qeqt-bh78)
- [IEEE DataPort](https://ieee-dataport.org/documents/experimental-dataset-retired-batteries-first-life-second-life-and-third-life-discharged-1)
- [Industrial Atlas page](https://www.indatlas.com/datasets/retired-batteries-multi-life/)

[⬅️ Back to Index](../README.md)
