# FEMTO (PRONOSTIA) Bearing Dataset

**Summary:** The FEMTO (PRONOSTIA) Bearing dataset is a collection of run-to-failure experiments on bearings under three operating conditions. It supports training and testing of prognostics models for remaining useful life prediction.

| Parameter | Value |
| --- | --- |
| **Dataset** | FEMTO (PRONOSTIA) Bearing Dataset |
| **Domain** | Manufacturing & Production |
| **Asset / Process** | Bearings |
| **Modality** | Time Series; Vibration |
| **Task** | Regression; RUL / Prognostics |
| **Annotation** | RUL Label; Scalar Target |
| **Source Type** | Real Lab / Testbed |
| **Access** | Repository; Competition |
| **Size** | Information not available |
| **Year** | 2012 |
| **License** | Information not available |

## Description

The FEMTO (PRONOSTIA) Bearing dataset comprises run-to-failure experiments on bearings, divided into three sub-datasets corresponding to distinct operating conditions. Sub-datasets 1 and 2 include two training runs and five test runs each, while sub-dataset 3 contains one test run. It was part of the 2012 IEEE Prognostics Challenge.

This reader constructs default splits by assigning runs to development, validation, and test sets, with customizable split assignments. The feature data consist of sliding windows with three channels, of which two acceleration channels are used due to missing temperature measurements in test runs. All features are standardized using a scaler fitted on the development data.

## References

- [tilman151/rul_datasets](https://github.com/tilman151/rul-datasets)

[⬅️ Back to Index](../README.md)
