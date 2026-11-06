# Li-ion Battery Aging Datasets

**Summary:** Run-to-failure charge, discharge and impedance records of Li-ion 18650 cells, aged on a NASA Ames prognostics testbed until a 30% capacity fade.

| Parameter | Value |
| --- | --- |
| **Domain** | Energy and power |
| **Asset / Process** | Batteries |
| **Modality** | Time series |
| **Task** | RUL and prognostics |
| **Annotation** | RUL label |
| **Source Type** | Lab or testbed |
| **Access** | Official portal |
| **Size** | — |
| **Year** | — |
| **License** | — |
| **Publisher** | NASA Ames Prognostics Center of Excellence (PCoE) |

## Description

The NASA Ames Prognostics Center of Excellence (PCoE) recorded the Li-ion Battery Aging Datasets on a battery prognostics testbed it built for the purpose. Commercial Li-ion 18650 cells went through charge, discharge and Electrochemical Impedance Spectroscopy (EIS) profiles at different ambient temperatures, and the repeated cycling accelerated their aging. The testbed uses programmable DC loads and power supplies, an environmental chamber and MATLAB-based acquisition at about 10 Hz.

Discharges ran at several current loads until the voltage fell to preset thresholds, some below the 2.7 V the manufacturer recommends, to induce deep-discharge aging. Tests stopped at an end-of-life criterion of 30% capacity fade, from 2 Ah to 1.4 Ah. Charge and discharge cycles hold measured voltage, current and temperature, discharge cycles add capacity, and impedance cycles add battery impedance and estimated electrolyte and charge-transfer resistances.

The run-to-failure series support prognostic algorithm development. Differing depth of discharge, rest periods and cell variability leave no two cells at the same state of life at the same cycle, the setting for remaining useful life prediction at end of discharge and end of life.

## References

- [Official page](https://data.nasa.gov/dataset/li-ion-battery-aging-datasets)
- [Industrial Atlas page](https://www.indatlas.com/datasets/li-ion-battery-aging-datasets/)

[⬅️ Back to Index](../README.md)
