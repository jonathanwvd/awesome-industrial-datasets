# Detecting Anomalies in Wafer Manufacturing

**Summary:** Anonymised machine data from semiconductor wafer manufacturing with 1,558 features and good or anomalous labels, in 1,763 training and 756 test rows.

| Parameter | Value |
| --- | --- |
| **Domain** | Electronics and semiconductors |
| **Asset / Process** | Semiconductor wafers and process tools |
| **Modality** | Tabular |
| **Task** | Classification; Quality prediction |
| **Annotation** | Sample label |
| **Source Type** | Real production |
| **Access** | Kaggle |
| **Size** | 1,763 training rows and 756 test rows |
| **Year** | — |
| **License** | — |

## Description

This dataset comes from a hackathon built on a use case from an Indian manufacturer of semiconductor wafers. Each row describes a product through attributes collected from the manufacturing machine, and the feature names are anonymised. Anomalous products are rare, so the two classes are strongly imbalanced.

The training file has 1,763 rows and 1,559 columns: Feature_1 to Feature_1558 plus a Class column with 0 for good and 1 for anomalous products. The test file has 756 rows with the 1,558 features only, and a sample submission file shows the expected output format.

The hackathon asks for a machine learning or deep learning model that classifies the anomalous products and generalises to the unseen test data, scored by the area under the curve (AUC). The high number of anonymised features is part of the challenge.

## References

- [Kaggle dataset](https://www.kaggle.com/datasets/arbazkhan971/anomaly-detection)
- [Industrial Atlas page](https://www.indatlas.com/datasets/detecting-anomalies-in-wafer-manufacturing/)

[⬅️ Back to Index](../README.md)
