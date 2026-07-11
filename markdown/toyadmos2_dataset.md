# ToyADMOS2 dataset: Another dataset of miniature-machine operating sounds for anomalous sound detection under domain shift conditions

**Summary:** ToyADMOS2 dataset is a large-scale dataset for anomaly detection in machine operating sounds under domain-shift conditions. It consists of two sub-datasets for fault diagnosis of toy car and toy train machines with over 27k normal and over 8k anomalous sound samples recorded at a 48-kHz sampling rate.

| Parameter | Value |
| --- | --- |
| **Dataset** | ToyADMOS2 dataset: Another dataset of miniature-machine operating sounds for anomalous sound detection under domain shift conditions |
| **Domain** | Manufacturing & Production |
| **Asset / Process** | Industrial Machines |
| **Modality** | Time Series; Audio |
| **Task** | Anomaly Detection; Fault Diagnosis; Condition Monitoring |
| **Annotation** | Sample Label; Class Label |
| **Source Type** | Real Lab / Testbed |
| **Access** | Repository |
| **Size** | 27 k samples |
| **Year** | 2021 |
| **License** | Information not available |

## Description

ToyADMOS2 dataset is a large-scale dataset for anomaly detection in machine operating sounds (ADMOS), designed for evaluating systems under domain-shift conditions. It consists of two sub-datasets for machine-condition inspection: fault diagnosis of machines with geometrically fixed tasks ("toy car") and fault diagnosis of machines with moving tasks ("toy train"). Domain shifts are represented by introducing several differences in operating conditions, such as the use of the same machine type but with different machine models and part configurations, different operating speeds, microphone arrangements, etc. Each sub-dataset contains over 27 k samples of normal machine-operating sounds and over 8 k samples of anomalous sounds recorded at a 48-kHz sampling rate.

What makes this dataset different from others is that it is not used as is, but in conjunction with the tool provided on GitHub. The mixer tool lets you create datasets with any combination of recordings by describing the amount you need in a recipe file.

The samples are compressed as MPEG-4 ALS (MPEG-4 Audio Lossless Coding) with a suffix of '.mp4' that you can load by using the audioread or librosa python module.

## References

- [GitHub Repository](https://github.com/nttcslab/ToyADMOS2-dataset)
- [ArXiv Paper](https://arxiv.org/abs/2106.02369)

[⬅️ Back to Index](../README.md)
