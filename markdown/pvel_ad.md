# PVEL-AD

36,543 near-infrared electroluminescence images of solar cells with 40,358 bounding boxes over 12 defect types, from cracks and finger interruptions to short circuits.

- **Domain:** Energy and power
- **Asset / Process:** Solar PV
- **Modality:** Image
- **Task:** Defect detection; Object detection
- **Annotation:** Bounding box
- **Access:** Request or approval
- **Size:** 36,543 images, 40,358 bounding boxes
- **Year:** 2021
- **Publisher:** Hebei University of Technology and Beihang University
- **Benchmark:** Yes

## Description

PVEL-AD, the Photovoltaic Electroluminescence Anomaly Detection dataset, is a collection of electroluminescence images of solar cells released jointly by Hebei University of Technology and Beihang University. Its reference article, by Binyi Su, Zhong Zhou and Haiyong Chen, appeared in IEEE Transactions on Industrial Informatics.

The 36,543 near-infrared images show internal defects against heterogeneous backgrounds. Besides one anomaly-free class there are 12 defect categories, including cracks of line and star shape, short circuits, black core, thick lines, finger interruptions, horizontal or vertical dislocation, printing errors, scratches, fragments and corner defects. A total of 40,358 ground truth bounding boxes mark the defects, with a long-tailed spread: finger interruptions have 2958 boxes in trainval and 22638 in test, scratches only 5 and 3.

The task is framed as long-tail object detection over trainval and test sets, scored with an AP50-5-95 script; test annotations, first evaluated through a Kaggle competition, are now released too. Access requires a hand-signed request form sent from an institutional email address.

## References

- [GitHub repository](https://github.com/binyisu/PVEL-AD)
- [Industrial Atlas page](https://www.indatlas.com/datasets/pvel-ad/)

[⬅️ Back to Index](../README.md)
