# Industrial screw driving dataset collection: Time series data for process monitoring and anomaly detection

Over 34,000 screw driving runs into plastic parts across six experimental scenarios, with torque and angle series and class labels per run.

- **Domain:** Manufacturing
- **Modality:** Time series
- **Task:** Classification; Process monitoring
- **Annotation:** Class label
- **Source Type:** Lab or testbed
- **Access:** Zenodo, Dataverse or Figshare
- **Size:** Over 34,000 screw driving operations
- **Year:** 2025
- **License:** CC BY
- **Publisher:** TU Dortmund University

## Description

This collection holds time series from screw driving operations in plastic components, built for research on process monitoring, anomaly detection and quality control. Nikolai West and Jochen Deuse of TU Dortmund University publish it on Zenodo under CC BY 4.0 and described it in a 2025 arXiv paper.

Over 34,000 operations are split into six scenarios: thread degradation over repeated use (5,000 runs, one class), surface friction under lubricants, treatments and contamination (12,500 runs, 8 classes), two sets of assembly conditions with washer, thread and alignment faults (1,700 and 5,000 runs, 26 and 25 classes), and injection molding variations of the upper and lower workpieces (2,400 and 7,482 runs, 42 and 44 classes).

Each scenario archive holds the raw runs in JSON, a labels.csv file and a README. The PyScrew Python package downloads, validates and prepares the data and handles torque, angle, time, gradient and step measurements.

## References

- [DOI](https://doi.org/10.5281/zenodo.14729547)
- [Zenodo record](https://zenodo.org/records/14729547)
- [GitHub repository](https://github.com/nikolaiwest/pyscrew)
- [Industrial Atlas page](https://www.indatlas.com/datasets/industrial-screw-driving-dataset-collection/)

[⬅️ Back to Index](../README.md)
