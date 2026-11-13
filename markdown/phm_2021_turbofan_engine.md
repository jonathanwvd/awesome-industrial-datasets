# 2021 PHM Conference Data Challenge

Run-to-failure flight data from the N-CMAPSS turbofan engine simulation set, for estimating remaining useful life under varied flight conditions and failure modes.

- **Domain:** Aerospace and defense
- **Asset / Process:** Turbines and engines
- **Modality:** Time series
- **Task:** RUL and prognostics; Regression
- **Annotation:** RUL label
- **Source Type:** Simulation
- **Access:** Competition
- **Size:** Flight data for 100 aircraft
- **Year:** 2021
- **Benchmark:** Yes

## Description

The 2021 PHM Conference Data Challenge, hosted on the PHM Society data repository, deals with remaining useful life (RUL) prediction for a fleet of aircraft engines under high variability in the flight envelope and multiple failure modes. It uses a subset of the run-to-failure trajectories of N-CMAPSS, the Turbofan Engine Degradation Simulation Data Set-2.

Full flight profile data cover 100 aircraft whose slowly developing faults start at some point in their flight history. The development set holds 90 units, and in its training and test parts every unit runs from cycle 1 until failure. The validation set has units that are partly degraded and have not yet failed, with flight scenario descriptors, measurements and auxiliary data.

The training and test data come from the NASA prognostics data repository, and the validation set was released for a one-time assessment at the end of the challenge. Teams may split the development data as they choose, and a web interface scores train, test and validation results.

## References

- [Official page](https://data.phmsociety.org/2021-phm-conference-data-challenge/)
- [Industrial Atlas page](https://www.indatlas.com/datasets/phm-2021-turbofan-engine/)

[⬅️ Back to Index](../README.md)
