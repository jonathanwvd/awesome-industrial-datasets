# InsPLAD

10,607 drone colour images of seventeen asset types on operating power lines, labelled for asset detection, defect classification and anomaly detection.

- **Domain:** Energy and power
- **Asset / Process:** Power grids and plants
- **Modality:** Image
- **Task:** Object detection; Fault diagnosis
- **Annotation:** Bounding box; Class label
- **Source Type:** Real production
- **Access:** Mendeley Data
- **Size:** 10,607 images, 28,933 asset instances
- **Year:** 2023
- **License:** CC BY-NC
- **Publisher:** Universidade Federal de Pernambuco Centro de Informatica
- **Benchmark:** Yes

## Description

InsPLAD is a set of high-resolution colour images taken by unmanned aerial vehicles over real-world operating power lines. It was introduced in a 2023 article in the International Journal of Remote Sensing and is also used in a WACV paper on attention modules for image-level anomaly detection in industrial inspection.

The 10,607 images show seventeen kinds of power line asset, with 28,933 annotated instances. Five of the assets carry six defects: four forms of corrosion, a broken component and the presence of a bird's nest. Each asset is labelled at image level as normal or by its defect name. InsPLAD-det serves asset detection with bounding boxes; InsPLAD-fault crops the objects into a supervised fault classification set, with two to three classes per asset and an unsupervised anomaly detection set.

The authors evaluate object detection with AP, defect classification with balanced accuracy and anomaly detection with AUROC. The data are distributed through Mendeley Data under CC BY-NC 3.0, and the code repository holds the documentation.

## References

- [Mendeley Data](https://data.mendeley.com/datasets/5n3fjgvfyz/1)
- [GitHub repository](https://github.com/andreluizbvs/InsPLAD)
- [Industrial Atlas page](https://www.indatlas.com/datasets/insplad/)

[⬅️ Back to Index](../README.md)
