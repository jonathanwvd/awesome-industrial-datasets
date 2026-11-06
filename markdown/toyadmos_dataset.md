# ToyADMOS dataset

**Summary:** Miniature-machine operating sounds from NTT, about 540 hours normal and over 12,000 anomalous samples, recorded with a toy car, a toy conveyor and a toy train.

| Parameter | Value |
| --- | --- |
| **Domain** | Manufacturing |
| **Asset / Process** | — |
| **Modality** | Audio |
| **Task** | Anomaly detection; Fault diagnosis |
| **Annotation** | Sample label |
| **Source Type** | Lab or testbed |
| **Access** | Zenodo, Dataverse or Figshare |
| **Size** | about 540 hours normal and over 12,000 anomalous sound samples |
| **Year** | 2019 |
| **License** | Academic or non-commercial terms |
| **Publisher** | NTT Media Intelligence Laboratories |

## Description

The ToyADMOS dataset holds operating sounds of miniature machines for research on anomaly detection in machine operating sounds (ADMOS). It was prepared by Yuma Koizumi and colleagues at NTT Media Intelligence Laboratories and introduced in "ToyADMOS: A Dataset of Miniature-Machine Operating Sounds for Anomalous Sound Detection" at WASPAA 2019.

It contains approximately 540 hours of normal sounds and over 12,000 anomalous samples, recorded with four microphones at 48 kHz; the anomalous sounds come from deliberately damaged components. Three sub-datasets match three tasks: product inspection with a toy car, fault diagnosis of a fixed machine with a toy conveyor and fault diagnosis of a moving machine with a toy train.

The data is downloaded from Zenodo under a non-commercial license. It exceeds 440 GB in total, so each sub-dataset, approximately 60 GB compressed, is split into 7 to 9 7-zip files. Python code for building small training and test sets and testing a simple autoencoder comes with it.

## References

- [Zenodo record](https://zenodo.org/records/3351307)
- [GitHub repository](https://github.com/YumaKoizumi/ToyADMOS-dataset)
- [Industrial Atlas page](https://www.indatlas.com/datasets/toyadmos-dataset/)

[⬅️ Back to Index](../README.md)
