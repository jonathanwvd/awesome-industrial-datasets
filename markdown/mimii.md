# MIMII Dataset: Sound Dataset for Malfunctioning Industrial Machine Investigation and Inspection

**Summary:** Eight-channel sound recordings of normal and anomalous valves, pumps, fans and slide rails, mixed with background noise recorded in real factories.

| Parameter | Value |
| --- | --- |
| **Domain** | Manufacturing |
| **Asset / Process** | Valves and actuators; Pumps, compressors and fans |
| **Modality** | Audio |
| **Task** | Anomaly detection; Fault diagnosis |
| **Annotation** | Sample label |
| **Source Type** | — |
| **Access** | Zenodo, Dataverse or Figshare |
| **Size** | — |
| **Year** | 2019 |
| **License** | CC BY-SA |
| **Publisher** | Hitachi, Ltd. |

## Description

The MIMII dataset collects sounds of malfunctioning industrial machines for investigation and inspection. Hitachi, Ltd. published version public 1.0 on Zenodo in 2019, and the data is described in a 2019 arXiv preprint and a paper at the 4th DCASE workshop by Harsh Purohit and colleagues.

It covers four machine types: valves, pumps, fans and slide rails. This version contains four product models per type (IDs 00, 02, 04 and 06). Each model has 5000 to 10000 seconds of normal sound and about 1000 seconds of anomalous sound, such as contamination, leakage, rotating unbalance and rail damage. An eight-channel microphone array recorded at 16 kHz and 16 bit, and background noise from several real factories was mixed in, with archives at -6, 0 and 6 dB.

The dataset targets sound-based machine fault diagnosis, including unsupervised anomaly detection, transfer learning and noise robustness. A deep autoencoder baseline on GitHub reports AUC per machine model and noise level. The license is CC BY-SA 4.0.

## References

- [Zenodo record](https://zenodo.org/records/3384388)
- [GitHub repository](https://github.com/MIMII-hitachi/mimii_baseline/)
- [Industrial Atlas page](https://www.indatlas.com/datasets/mimii-dataset-sound-dataset-for-malfunctioning-industrial-machine-investigation/)

[⬅️ Back to Index](../README.md)
