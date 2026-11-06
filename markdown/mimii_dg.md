# MIMII DG

**Summary:** Machine sound dataset for anomalous sound detection under domain shift, with five machine types and three shift scenarios each, used in the DCASE 2022 challenge.

| Parameter | Value |
| --- | --- |
| **Domain** | Manufacturing |
| **Asset / Process** | — |
| **Modality** | Audio |
| **Task** | Anomaly detection; Condition monitoring |
| **Annotation** | Normal-only training; Sample label |
| **Source Type** | — |
| **Access** | Zenodo, Dataverse or Figshare |
| **Size** | — |
| **Year** | 2022 |
| **License** | CC BY-NC-SA |

## Description

MIMII DG is a machine sound dataset for benchmarking domain generalization techniques in anomalous sound detection, described by Kota Dohi and colleagues in the proceedings of the DCASE2022 Workshop, held in Nancy, France, in November 2022. It consists of five machine types with three domain shift scenarios for each type.

Task 2 of the DCASE 2022 Challenge uses MIMII DG together with ToyADMOS2. The challenge data covers seven machine types (fan, gearbox, bearing, slide rail, valve, ToyCar and ToyTrain) as single-channel 10-second clips. Its anomalous sounds come from deliberately damaged machines, environmental noise was recorded in several real factories, and domain shifts include operating speed, machine load, environmental noise and microphone location.

In the challenge development dataset, each section holds 990 normal source-domain clips and ten normal target-domain clips for training, plus 100 normal and 100 anomalous test clips. Each section of the challenge evaluation dataset has 200 test clips without normal or anomaly labels. The development dataset, created jointly by Hitachi and NTT, is published on Zenodo. Challenge systems are ranked by the harmonic mean of AUC and pAUC.

## References

- [Official page](https://dcase.community/challenge2022/task-unsupervised-anomalous-sound-detection-for-machine-condition-monitoring)
- [Zenodo record](https://zenodo.org/records/6355122)
- [Industrial Atlas page](https://www.indatlas.com/datasets/mimii-dg-sound-dataset-for-malfunctioning-industrial-machine-investigation/)

[⬅️ Back to Index](../README.md)
