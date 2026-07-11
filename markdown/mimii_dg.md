# MIMII DG: Sound Dataset for Malfunctioning Industrial Machine Investigation for Domain Generalization Task

**Summary:** The MIMII DG dataset comprises normal and abnormal operating sound recordings of five types of industrial machines organized into subsets corresponding to domain shifts. It is a subset of the DCASE 2022 Challenge Task 2 development dataset for unsupervised anomalous sound detection.

| Parameter | Value |
| --- | --- |
| **Dataset** | MIMII DG: Sound Dataset for Malfunctioning Industrial Machine Investigation for Domain Generalization Task |
| **Domain** | Manufacturing & Production |
| **Asset / Process** | Industrial Machines |
| **Modality** | Time Series; Audio |
| **Task** | Anomaly Detection; Fault Diagnosis; Condition Monitoring |
| **Annotation** | Normal-Only Training; Sample Label |
| **Source Type** | Real Lab / Testbed |
| **Access** | Repository; Zenodo / Dataverse; Competition |
| **Size** | Information not available |
| **Year** | 2022 |
| **License** | CC BY-NC-SA |

## Description

This dataset is a sound dataset for malfunctioning industrial machine investigation and inspection for domain generalization task (MIMII DG). The dataset consists of normal and abnormal operating sounds of five different types of industrial machines, i.e., fans, gearboxes, bearing, slide rails, and valves. The data for each machine type includes three subsets called "sections", and each section roughly corresponds to a type of domain shift. This dataset is a subset of the dataset for DCASE 2022 Challenge Task 2, so the dataset is entirely the same as data included in the development dataset.

Two simple baseline systems are available on the GitHub repositories autoencoder-based baseline and MobileNetV2-based baseline. The baseline systems provide a simple entry-level approach that gives a reasonable performance in the dataset. They are good starting points, especially for entry-level researchers who want to get familiar with the anomalous-sound-detection task.

This dataset was made by Hitachi, Ltd. and is available under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0) license. A paper will be published on the dataset and citation information will be announced; users are asked to cite it if they use this dataset.

## References

- [DCASE 2022 Challenge Task 2](https://dcase.community/challenge2022/task-unsupervised-anomalous-sound-detection-for-machine-condition-monitoring)
- [Development dataset](https://zenodo.org/record/6355122#.Ynt7rtrP2Uk)
- [Autoencoder-based baseline](https://github.com/Kota-Dohi/dcase2022_task2_baseline_ae)
- [MobileNetV2-based baseline](https://github.com/Kota-Dohi/dcase2022_task2_baseline_mobile_net_v2)

[⬅️ Back to Index](../README.md)
