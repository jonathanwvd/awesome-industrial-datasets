# Data-driven prediction of battery cycle life before capacity degradation

**Summary:** This dataset consists of 124 commercial lithium-ion batteries cycled to failure under fast-charging conditions to optimize fast charging for lithium-ion batteries.

| Parameter | Value |
| --- | --- |
| **Dataset** | Data-driven prediction of battery cycle life before capacity degradation |
| **Domain** | Energy & Power |
| **Asset / Process** | Batteries |
| **Modality** | Time Series |
| **Task** | Regression; RUL / Prognostics |
| **Annotation** | RUL Label; Scalar Target |
| **Source Type** | Real Lab / Testbed |
| **Access** | Repository |
| **Size** | 124 |
| **Year** | 2019 |
| **License** | Information not available |

## Description

This dataset, used in the publication “Data-driven prediction of battery cycle life before capacity degradation”, includes measurements from lithium-ion phosphate (LFP)/graphite cells manufactured by A123 Systems. The cells were cycled in a controlled temperature environment at 30°C with a one-step or two-step fast-charging policy, monitored until failure to study degradation patterns.

The dataset is divided into three batches, each with approximately 48 cells, distinguished by batch dates. Data is provided in MATLAB struct format or as raw CSV files, with some noted errors in the CSV files that are corrected in the structs. Measurements include temperature from thermocouples and internal resistance during charging at 80% state-of-charge using specific pulsing protocols.

Starter code for accessing and using the dataset is available on GitHub, along with structured data files and a zipped archive of the full dataset. The data aims to support optimization of fast-charging methods and battery life prediction.

## References

- [GitHub Repository](https://github.com/rdbraatz/data-driven-prediction-of-battery-cycle-life-before-capacity-degradation)
- [Original Publication - Nature Energy 2019](https://data.matr.io/1/projects/5c48dd2bc625d700019f3204)

[⬅️ Back to Index](../README.md)
