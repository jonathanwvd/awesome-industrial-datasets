# Contamination Isolation Scenarios in Water Distribution Networks

Simulated chlorine sensor readings over 14 days for contamination events in a water network, with ground truth on the source node and intensity.

- **Domain:** Water and utilities
- **Asset / Process:** Water treatment and distribution
- **Modality:** Time series
- **Task:** Process monitoring
- **Annotation:** Event and time label
- **Source Type:** Simulation
- **Access:** Zenodo, Dataverse or Figshare
- **Year:** 2026
- **License:** CC BY
- **Publisher:** KIOS Research and Innovation Center of Excellence, University of Cyprus

## Description

This dataset of simulated contamination events in water distribution networks (WDNs) comes from authors at the KIOS Research and Innovation Center of Excellence and the University of Cyprus. Each scenario injects a contaminant into the network and records the chlorine readings of the deployed sensors.

Readings were taken every hour over a simulated period of 14 days. Each sample holds the chlorine concentration time series of all deployed sensors in the WDN together with ground-truth metadata on the event, including the contamination node, its intensity, and the sensor indices and locations. The scenarios are MATLAB v7.3 (HDF5) files, read in Python with h5py, and the example code loads a scenario of the L-TOWN network. Everything ships as one tar archive.

Suggested tasks are isolating the contamination source, detecting events from sensor data, estimating injection start, duration and intensity, and testing robustness under realistic demand variability. The data was published in 2026 under CC BY 4.0.

## References

- [DOI](https://doi.org/10.5281/zenodo.20462263)
- [Zenodo record](https://zenodo.org/records/20462263)
- [Industrial Atlas page](https://www.indatlas.com/datasets/wdn-contamination-isolation-scenarios/)

[⬅️ Back to Index](../README.md)
