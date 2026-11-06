# Textures Classification Dataset

Surface texture set of 8,674 images in 64 classes merged from the KTH, Kyberge and UIUC texture datasets and split in half for training and validation.

- **Domain:** Materials and metrology
- **Asset / Process:** Surfaces and textures
- **Modality:** Image
- **Task:** Classification
- **Annotation:** Class label
- **Access:** Direct download
- **Size:** 8,674 images
- **Year:** 2019

## Description

The Textures Classification Dataset combines surface texture images from three public texture datasets into one set of 64 classes. It accompanies the paper "A compact convolutional neural network for surface defect inspection", a paper its authors describe as upcoming; the repository was created in 2019.

All 8,674 images are resized to 331 x 331 pixels. Eleven classes (3,194 images) come from the KTH surface dataset, including KTH-TIPS and KTH-TIPS2, 28 classes (4,480 images without rotated patches) from the Kyberge dataset and 25 classes (1,000 images) from the UIUC dataset. The textures are real-world surfaces such as wood, blanket, cloth and leather.

The images are split at random into two halves, one for training and one for validation. The set is meant for evaluating the capacity of models or for pretraining CNN models for surface defect inspection. It is downloaded from Baidu, with an extraction code, or from Google Drive.

## References

- [GitHub repository](https://github.com/abin24/Textures-Dataset)
- [Industrial Atlas page](https://www.indatlas.com/datasets/textures-classification-dataset/)

[⬅️ Back to Index](../README.md)
