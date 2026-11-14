# HSU TwinFlow

Digital-twin simulation runs of a production facility with injected and repaired faults, labelled by component, fault type and time, for anomaly detection and diagnosis.

- **Domain:** Manufacturing
- **Asset / Process:** Robots and manipulators
- **Modality:** Time series
- **Task:** Fault diagnosis
- **Annotation:** Class label; Event and time label
- **Source Type:** Simulation
- **Access:** Zenodo, Dataverse or Figshare
- **Size:** Training and test scenario archives
- **Year:** 2026
- **License:** CC BY
- **Publisher:** Helmut Schmidt University
- **Benchmark:** Yes

## Description

HSU TwinFlow is a benchmark of simulation runs from a digital twin of a production facility with more than 100 interacting components, among them conveyors, robots, autonomous mobile robots, robot stations and workstations. It comes from Helmut Schmidt University in Hamburg with partners at Digital Twin Factory, Novatio Solutions and TU Graz, and accompanies a paper in the proceedings of DX 2026, the 37th International Conference on Principles of Diagnosis and Resilient Systems.

Scenario files inject faults into conveyors, mobile robots and six-axis robots, keep them active for set intervals and then repair them, so ground truth names the component, the fault type and the timestamps. Each scenario has Parquet files of measurements, fault values and configuration parameters on a shared time index. Training holds repeated nominal and low-fault-rate runs; the test set holds area-specific and simultaneous-fault runs.

The GitHub repository adds system knowledge files, detection and diagnosis baselines, evaluation scripts and a dashboard. Data is under CC BY 4.0 and code under MIT.

## References

- [DOI](https://doi.org/10.5281/zenodo.22943652)
- [Zenodo record](https://zenodo.org/records/23516670)
- [GitHub repository](https://github.com/imb-hsu/twinflow)
- [Industrial Atlas page](https://www.indatlas.com/datasets/hsu-twinflow/)

[⬅️ Back to Index](../README.md)
