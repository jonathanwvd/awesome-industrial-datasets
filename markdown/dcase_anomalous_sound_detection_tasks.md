# DCASE Anomalous Sound Detection Tasks

**Summary:** Machine sound challenge in which detectors train on normal clips only and must handle domain shifts and machine types unseen during development.

| Parameter | Value |
| --- | --- |
| **Dataset** | DCASE Anomalous Sound Detection Tasks |
| **Domain** | Manufacturing & Production |
| **Asset / Process** | Information not available |
| **Modality** | Audio |
| **Task** | Anomaly Detection |
| **Annotation** | Normal-Only Training; Sample Label |
| **Source Type** | Information not available |
| **Access** | Competition |
| **Size** | Information not available |
| **Year** | 2024 |
| **License** | Information not available |

## Description

DCASE 2024 Task 2, First-Shot Unsupervised Anomalous Sound Detection for Machine Condition Monitoring, continues the anomalous sound detection tasks run from DCASE 2020 to DCASE 2023. Systems decide whether the sound of a machine is normal or anomalous after training on normal sounds only, under domain shifts and without hyperparameter tuning on new machine types.

The development dataset covers seven machine types, among them fan, gearbox, bearing and valve. Each type has one section with 990 normal source-domain clips, ten normal target-domain clips and 100 normal and 100 anomalous test clips, each a single-channel 10-second recording. Anomalous sounds come from deliberately damaged machines, and every clip mixes the machine sound with environmental noise recorded in several real factory environments. A separate machine set forms the additional training and evaluation datasets.

Scoring uses AUC and partial AUC with p = 0.1, combined by harmonic mean into an official score. An evaluator holds the ground truth for the evaluation dataset.

## References

- [Official page](https://dcase.community/challenge2024/task-first-shot-unsupervised-anomalous-sound-detection-for-machine-condition-monitoring)

[⬅️ Back to Index](../README.md)
