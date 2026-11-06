# Design of Experiments for Cyclic Aging of LFP 18650 Cells

**Summary:** Cycling data at 1 Hz from 15 LFP 18650 cells in a factorial design that varies charge rate, discharge rate and depth of discharge at 25 °C.

| Parameter | Value |
| --- | --- |
| **Domain** | Energy and power |
| **Asset / Process** | Batteries |
| **Modality** | Time series |
| **Task** | Condition monitoring |
| **Annotation** | — |
| **Source Type** | Lab or testbed |
| **Access** | Official portal |
| **Size** | 15 test cells |
| **Year** | — |
| **License** | — |

## Description

This dataset holds experimental data from a Design of Experiments (DoE) study of the cyclic aging of lithium iron phosphate (LFP) 18650 cells. It is credited to Florian Rzepka, with Mano Schmitz as contributor. The study uses both full factorial and fractional factorial designs.

Three factors vary: the charge rate from 0.5C to 0.9C (0.9 to 1.62 A), the discharge rate from 1C to 2.5C (1.8 to 4.5 A) and the depth of discharge from 45% to 65% (0.81 to 1.17 Ah). All cycling ran at a controlled ambient temperature of 25 °C. The plan assigns 15 test cells to eight factor combinations, and each cell went through several aging loops.

Voltage, current, temperature and auxiliary parameters are sampled at 1 Hz across several test steps and stored as partitioned Parquet files. The data supports the study of capacity fade, impedance growth and state-of-health degradation under controlled cycling.

## References

- [DOI](https://doi.org/10.14279/depositonce-24800)
- [Industrial Atlas page](https://www.indatlas.com/datasets/tu-berlin-lfp-18650-doe-aging/)

[⬅️ Back to Index](../README.md)
