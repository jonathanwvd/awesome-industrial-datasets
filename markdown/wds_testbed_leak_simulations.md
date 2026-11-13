# Dataset of Leak Simulations in Experimental Testbed Water Distribution System

Acceleration, hydrophone and dynamic pressure signals from a 47 m PVC water distribution testbed with four induced leak types and no-leak runs.

- **Domain:** Water and utilities
- **Asset / Process:** Water treatment and distribution
- **Modality:** Vibration; Audio; Time series
- **Task:** Classification
- **Annotation:** Class label
- **Source Type:** Lab or testbed
- **Access:** Mendeley Data
- **Size:** Two hundred and eighty 30-second signals
- **Year:** 2022
- **License:** CC BY

## Description

This dataset holds signals recorded on a laboratory-scale water distribution testbed with induced leaks, for research on leak detection and localization. Its contributors are from the University of Texas at Austin and Texas A&M University. The testbed is 47 m long and built from PVC pipes 152.4 mm in diameter.

There are two hundred and eighty signals, each 30 seconds long, from two accelerometers, two hydrophones and two dynamic pressure sensors. Controlled runs vary the network layout (looped or branched), the leak type (longitudinal crack, circumferential crack, gasket leak, orifice leak or no leak), the background flow (0, 0.18 or 0.47 L/s, or a transient from 0.47 to 0 L/s at second 20), background noise, and sensor types and positions.

Accelerometer and pressure data come as CSV files and hydrophone data as raw files at 8000 Hz, with a Python script that turns them into a pandas DataFrame. Version 1 was published on Mendeley Data in December 2022 under CC BY 4.0.

## References

- [Mendeley Data](https://data.mendeley.com/datasets/tbrnp6vrnj)
- [Industrial Atlas page](https://www.indatlas.com/datasets/wds-testbed-leak-simulations/)

[⬅️ Back to Index](../README.md)
