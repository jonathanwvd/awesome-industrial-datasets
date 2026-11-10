# SMARTEOLE Wind Farm Control open dataset

One-minute SCADA, control logs and ground lidar data from a seven-turbine French wind farm during a 2020 wake steering field test.

- **Domain:** Energy and power
- **Asset / Process:** Wind turbines
- **Modality:** Time series
- **Task:** Energy optimization
- **Source Type:** Real production
- **Access:** Zenodo, Dataverse or Figshare
- **Size:** 7 turbines, 17 February to 25 May 2020
- **Year:** 2022
- **Publisher:** ENGIE Green

## Description

This dataset is the last of three field campaigns of the French national project SMARTEOLE, which tested a wake steering strategy to raise power production. Thomas Duc of ENGIE Green and Eric Simley of NREL published it on Zenodo in 2022 under the Etalab 2.0 open licence.

The data cover the 7 Senvion MM82 turbines (82 m rotor, 2.05 MW) of the Sole du Moulin Vieux wind farm in France, from 17 February to 25 May 2020, with wake steering applied on turbine SMV6. Files hold SCADA data from all turbines, control logs with the yaw offset applied at each time step, and a ground-based WindCube profiler lidar, all at 1-minute resolution.

Time steps with any turbine stopped were removed, and nacelle position and wind direction were corrected for north alignment. Static files add turbine coordinates, a farm map, guaranteed power and thrust curves and the transfer functions used in the related Wind Energy Science paper.

## References

- [DOI](https://doi.org/10.5281/zenodo.7342466)
- [Zenodo record](https://zenodo.org/records/7342466)
- [Industrial Atlas page](https://www.indatlas.com/datasets/smarteole-wind-farm/)

[⬅️ Back to Index](../README.md)
