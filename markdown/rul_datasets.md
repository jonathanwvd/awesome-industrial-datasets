# RUL Datasets

**Summary:** Python library that wraps five remaining useful lifetime datasets, including C-MAPSS, FEMTO and XJTU-SY, as PyTorch Lightning data modules with one shared API.

| Parameter | Value |
| --- | --- |
| **Domain** | Cross-industrial |
| **Asset / Process** | Bearings; Turbines and engines |
| **Modality** | Time series |
| **Task** | RUL and prognostics |
| **Annotation** | — |
| **Source Type** | — |
| **Access** | Code repository |
| **Size** | — |
| **Year** | 2022 |
| **License** | — |

## Description

RUL Datasets is a Python library that provides datasets for remaining useful lifetime (RUL) estimation as LightningDataModules, ready to use in PyTorch Lightning. It lives in the tilman151/rul-datasets repository on GitHub, created in 2022, and installs with pip.

Five datasets are supported: the C-MAPSS turbofan degradation dataset, the FEMTO (PRONOSTIA) bearing dataset, the XJTU-SY bearing dataset, the N-C-MAPSS new turbofan degradation dataset and a tiny dummy dataset for debugging. All of them share one API, so an experiment written for one dataset runs on the others without code changes.

Higher-order data modules take one or more of these basic modules and adapt them for transfer learning, unsupervised domain adaptation and semi-supervised learning experiments.

## References

- [GitHub repository](https://github.com/tilman151/rul-datasets)
- [Industrial Atlas page](https://www.indatlas.com/datasets/rul-datasets/)

[⬅️ Back to Index](../README.md)
