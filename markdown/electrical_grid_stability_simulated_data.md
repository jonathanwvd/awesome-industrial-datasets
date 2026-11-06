# Electrical Grid Stability Simulated Data

10,000 simulated input sets for a 4-node star grid with the producer at the centre, each with a stability value and a stable or unstable label.

- **Domain:** Energy and power
- **Asset / Process:** Power grids and plants
- **Modality:** Tabular
- **Task:** Classification; Regression
- **Annotation:** Class label; Scalar target
- **Source Type:** Simulation
- **Access:** UCI repository
- **Size:** 10,000 instances
- **Year:** 2018
- **License:** CC BY

## Description

Electrical Grid Stability Simulated Data comes from a local stability analysis, repeated for different sets of input values, of a power grid that implements the Decentral Smart Grid Control concept. Its creator is Vadim Arzamasov, and it was donated to the UCI Machine Learning Repository in 2018. The analysis uses a method similar to that of Schäfer et al. (2016) on taming instabilities in power grid networks by decentralized control.

The 10,000 instances have 12 features: reaction times tau1 to tau4, nominal powers p1 to p4, with consumers between -0.5 and -2 s^-2 and p1 the absolute sum of the others, and coefficients g proportional to price elasticity. Averaging time (2 s), coupling strength (8 s^-2) and damping (0.1 s^-1) stay fixed.

Two goal fields support regression and classification: stab, the maximal real part of the characteristic equation root, and stabf, a stable or unstable label. There are no missing values. The data comes as one 2.3 MB CSV file under CC BY 4.0.

## References

- [DOI](https://doi.org/10.24432/C5PG66)
- [Industrial Atlas page](https://www.indatlas.com/datasets/electrical-grid-stability-simulated-data/)

[⬅️ Back to Index](../README.md)
