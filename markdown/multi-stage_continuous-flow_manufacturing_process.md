# Multi-Stage Continuous-Flow Manufacturing Process

**Summary:** Real production-line data from a multi-stage continuous-flow process near Detroit, for predicting output measurements taken at 15 surface locations.

| Parameter | Value |
| --- | --- |
| **Domain** | Manufacturing |
| **Asset / Process** | — |
| **Modality** | Time series; Tabular |
| **Task** | Regression; Quality prediction |
| **Annotation** | Scalar target |
| **Source Type** | Real production |
| **Access** | Kaggle |
| **Size** | — |
| **Year** | — |
| **License** | — |
| **Publisher** | Liveline Technologies |

## Description

This dataset holds real process data from a high-speed continuous manufacturing line near Detroit, Michigan, whose stages run both in parallel and in series. It comes from Liveline Technologies and covers a single production run lasting several hours.

In the first stage, Machines 1, 2 and 3 work in parallel and feed a combiner, whose output is measured at 15 locations around the outer surface of the exiting material. The flow then passes through Machines 4 and 5 in series, after which the same 15 locations are measured again. The data comes as one CSV file with a text file of notes.

The primary target is the first-stage output measurements and the secondary target is the second-stage output. Liveline Technologies uses such models to develop real-time process controllers in simulation environments and to detect anomalies by comparing predictions with actual outputs.

## References

- [Kaggle dataset](https://www.kaggle.com/datasets/supergus/multistage-continuousflow-manufacturing-process)
- [Industrial Atlas page](https://www.indatlas.com/datasets/multi-stage-continuous-flow-manufacturing-process/)

[⬅️ Back to Index](../README.md)
