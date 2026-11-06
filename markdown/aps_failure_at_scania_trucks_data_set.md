# APS Failure at Scania Trucks

Operational data from heavy Scania trucks, labelled by whether a failure involves the Air Pressure System, with a cost-based metric from a 2016 challenge.

- **Domain:** Transportation and mobility
- **Asset / Process:** Vehicles and fleets
- **Modality:** Tabular
- **Task:** Classification
- **Annotation:** Class label
- **Source Type:** Real production
- **Access:** UCI repository
- **Size:** 60,000 training and 16,000 test examples
- **Year:** 2016
- **Publisher:** Scania CV AB
- **Benchmark:** Yes

## Description

APS Failure at Scania Trucks was created by Scania CV AB in Sweden, donated by Tony Lindgren and Jonas Biteus, and used in the Industrial Challenge 2016 at the 15th International Symposium on Intelligent Data Analysis (IDA). The data was collected from heavy Scania trucks in everyday use, and its focus, the Air Pressure System (APS), supplies pressurised air for truck functions such as braking and gear changes.

The positive class holds failures of a specific APS component, while the negative class holds trucks with failures in components unrelated to the APS. The data is a subset of all available data, selected by experts. The training set has 60,000 examples, 59,000 negative and 1,000 positive, and the test set has 16,000. The 171 anonymized attributes combine single numerical counters with histograms whose bins cover different conditions; 7 of them are histogram variables. Missing values are marked 'na'.

The challenge scores a model by its total misclassification cost: an unnecessary workshop check costs 10 and a missed faulty truck costs 500.

## References

- [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/APS+Failure+at+Scania+Trucks)
- [Industrial Atlas page](https://www.indatlas.com/datasets/aps-failure-at-scania-trucks/)

[⬅️ Back to Index](../README.md)
