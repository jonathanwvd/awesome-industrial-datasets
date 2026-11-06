# Condition Based Maintenance of Naval Propulsion Plants

11,934 steady-state measurement vectors from a simulated naval gas turbine plant, with compressor and turbine decay coefficients as regression targets.

- **Domain:** Transportation and mobility
- **Asset / Process:** Turbines and engines
- **Modality:** Tabular
- **Task:** Regression; Condition monitoring
- **Annotation:** Scalar target
- **Source Type:** Simulation
- **Access:** UCI repository
- **Size:** 11,934 instances
- **Year:** 2014
- **License:** CC BY

## Description

Condition Based Maintenance of Naval Propulsion Plants comes from a numerical simulator of a frigate with a COmbined Diesel eLectric And Gas (CODLAG) gas turbine propulsion plant. Its creators are Andrea Coraddu, Luca Oneto, Alessandro Ghio, Stefano Savio, Davide Anguita and Massimo Figari, and it was donated to the UCI Machine Learning Repository in 2014.

The simulator joins propeller, hull, gas turbine, gear box and controller blocks tuned on similar real plants, and models performance decay of the compressor and turbines. Ship speed was sampled from 3 to 27 knots, the compressor decay coefficient kMc over [1; 0.95] and the turbine coefficient kMt over [1; 0.975], on a grid of 0.001.

Each of the 11,934 instances is a 16-feature vector of steady-state measures, such as shaft torque, revolutions, propeller torques, temperatures, pressures and fuel flow, plus both decay coefficients. There are no missing values, and the data is released under CC BY 4.0.

## References

- [DOI](https://doi.org/10.24432/C5K31K)
- [Industrial Atlas page](https://www.indatlas.com/datasets/condition-based-maintenance-of-naval-propulsion-plants/)

[⬅️ Back to Index](../README.md)
