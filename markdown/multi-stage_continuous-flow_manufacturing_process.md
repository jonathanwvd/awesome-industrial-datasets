# Multi-stage continuous-flow manufacturing process

**Summary:** Real process data from a high-speed, continuous manufacturing line to predict output measurements from multiple stages.

| Parameter | Value |
| --- | --- |
| **Dataset** | Multi-stage continuous-flow manufacturing process |
| **Domain** | Manufacturing & Production; Chemical & Process |
| **Asset / Process** | Chemical Process |
| **Modality** | Time Series |
| **Task** | Regression; Process Monitoring |
| **Annotation** | Scalar Target |
| **Source Type** | Real Production / Field |
| **Access** | Kaggle; Login Required |
| **Size** | Information not available |
| **Year** | 2019 |
| **License** | Information not available |

## Description

This data was taken from an actual production line near Detroit, Michigan. The goal is to predict certain properties of the line's output from the various input data. The line is a high-speed, continuous manufacturing process with parallel and series stages.

The data comes from one production run spanning several hours. Liveline Technologies has a large quantity of this type of data from multiple production lines in various locations.

The process consists of multiple stages: In the first stage, Machines 1, 2, and 3 operate in parallel, feeding outputs into a combining step. Output from the combiner is measured in 15 locations around the material's outer surface, constituting the primary measurements to predict. Next, the output flows into a second stage where Machines 4 and 5 process the material in series. Measurements are again made in the same 15 locations after Machine 5, known as the secondary measurements to predict.

## References

- [Kaggle Dataset](https://www.kaggle.com/datasets/supergus/multistage-continuousflow-manufacturing-process)
- [Liveline Technologies](https://www.liveline.tech)

[⬅️ Back to Index](../README.md)
