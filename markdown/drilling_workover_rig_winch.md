# Vibration Dataset of a Drilling and Workover Rig Winch Under Complex Operating Conditions

Vibration records from the winch of a drilling and workover rig, each labelled with its operating condition, for diagnosis under load and speed changes.

- **Domain:** Oil and gas
- **Modality:** Vibration
- **Task:** Classification; Condition monitoring
- **Access:** IEEE DataPort
- **Publisher:** Northeast Electric Power University

## Description

This dataset, published on IEEE DataPort by authors from Northeast Electric Power University, contains vibration signals measured on the winch of a drilling and workover rig. They were gathered to study condition monitoring and automated diagnosis when load varies, speed fluctuates, and impacts and background noise disturb the measurements.

Each original record has 4096 sampling points and carries a label for its operating condition. The authors suggest cutting each record into windows of 1024 points with a step of 64, which yields 49 overlapping windows per record. To avoid leakage between overlapping windows, records should be assigned to training, validation and test subsets before the windowing, and normalisation parameters taken from the training subset only.

The documentation that accompanies the data describes the files, label definitions, signal dimensions and preprocessing. The authors list uses such as condition classification, feature extraction, mode decomposition, deep-learning diagnosis and robustness evaluation.

## References

- [DOI](https://doi.org/10.21227/4cb8-6471)
- [IEEE DataPort](https://ieee-dataport.org/documents/winch-data-set)
- [Industrial Atlas page](https://www.indatlas.com/datasets/drilling-workover-rig-winch/)

[⬅️ Back to Index](../README.md)
