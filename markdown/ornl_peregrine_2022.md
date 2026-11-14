# Peregrine v2022-10

Multi-modal layer-wise powder bed images from laser powder bed fusion and binder jet printers, with ground truth pixel masks for training and baseline predictions for evaluation.

- **Domain:** Manufacturing
- **Asset / Process:** Additive manufacturing
- **Modality:** Image; Multimodal
- **Task:** Defect segmentation; Anomaly detection
- **Annotation:** Pixel mask
- **Access:** Registration required
- **Size:** 6 datasets from 2 powder bed printing technologies
- **Year:** 2023
- **Publisher:** Oak Ridge National Laboratory

## Description

Peregrine v2022-10 is a release of six datasets from Oak Ridge National Laboratory that hold layer-wise powder bed images from two printing technologies. An ExOne M-Flex printer supplied the binder jet data, while EOS M290 and AddUp FormUp 350 machines supplied the laser powder bed fusion data. The release has two records, v2022-10 (DOI 10.13139/ORNLNCCS/1896716) and v2022-10.1 (DOI 10.13139/ORNLNCCS/1923043); the second lists GammaPrint-700 where the first lists DMREF.

The images combine several sensor modalities: visible light, temporally integrated near-infrared (long exposure) and wide-band infrared. Materials include 17-4 PH stainless steel, GammaPrint-700, Inconel 718, maraging steel and H13 steel. Training data comes with ground truth pixel masks, while evaluation data carries baseline prediction masks produced by a trained neural network.

The release targets the development and testing of computer vision and machine learning methods for anomaly and defect detection. Files are transferred through Globus, which requires a Globus account and endpoint. Luke Scime, Chase Joslin, Ryan Duncan, Frank Brinkley, Christopher Ledford, Derek Siddel and Vincent Paquit are the authors.

## References

- [Official page](https://www.osti.gov/dataexplorer/biblio/dataset/1923043)
- [osti.gov](https://www.osti.gov/dataexplorer/biblio/dataset/1896716)
- [Industrial Atlas page](https://www.indatlas.com/datasets/ornl-peregrine-2022/)

[⬅️ Back to Index](../README.md)
