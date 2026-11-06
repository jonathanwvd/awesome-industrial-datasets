# ToyADMOS2

Toy car and toy train operating sounds under normal and damaged conditions, with a mixer tool that builds anomalous sound detection sets under domain shift.

- **Domain:** Cross-industrial
- **Modality:** Audio
- **Task:** Anomaly detection
- **Annotation:** Sample label
- **Source Type:** Lab or testbed
- **Access:** Zenodo, Dataverse or Figshare
- **Size:** 149 GB of source recordings
- **Year:** 2021
- **License:** Academic or non-commercial terms

## Description

ToyADMOS2 is a dataset for anomaly detection in machine operating sounds (ADMOS) under domain shift conditions, published on Zenodo in 2021 by Noboru Harada and colleagues at NTT and presented at the DCASE2021 Workshop in Barcelona. Following ToyADMOS, it records miniature machines, a toy car and a toy train, under normal conditions and under anomaly conditions created by deliberately damaging them.

Each of the two sub-datasets holds over 27k normal and over 8k anomalous samples at 48 kHz, stored as MPEG-4 ALS files; the source recordings total 149 GB. Domain shifts include different machine models and part configurations, operating speeds and microphone arrangements. A subset was used in DCASE 2021 Challenge Task 2.

The recordings are source material rather than a ready-made set. A mixer tool in the GitHub repository compiles new datasets from Excel recipe files, either clean or at a signal-to-noise ratio of 6 dB; one recipe rebuilds the benchmark set evaluated in Table 3 of the paper. The data is released under a non-commercial license.

## References

- [Zenodo record](https://zenodo.org/records/4580270)
- [GitHub repository](https://github.com/nttcslab/ToyADMOS2-dataset)
- [Industrial Atlas page](https://www.indatlas.com/datasets/toyadmos2-dataset-another-dataset-of-miniature-machine-operating-sounds/)

[⬅️ Back to Index](../README.md)
