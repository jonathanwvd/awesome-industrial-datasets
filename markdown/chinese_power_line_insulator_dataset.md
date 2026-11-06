# Chinese Power Line Insulator Dataset

Power line insulator images with VOC2007 annotations, combining 600 normal images captured by UAVs and 248 synthetic images of defective insulators.

- **Domain:** Energy and power
- **Asset / Process:** Power grids and plants
- **Modality:** Image
- **Task:** Defect detection; Object detection
- **Annotation:** Bounding box
- **Source Type:** Mixed
- **Access:** Code repository
- **Size:** 600 normal and 248 defective images
- **Year:** 2018

## Description

The Chinese Power Line Insulator Dataset (CPLID) is a set of power line insulator images for defect detection, made by WANG Zi-Hao from images provided by the State Grid Corporation of China. It accompanies the 2018 article "Detection of Power Line Insulator Defects Using Aerial Images Analyzed With Convolutional Neural Networks" in IEEE Transactions on Systems, Man, and Cybernetics: Systems.

The Normal_Insulators folder holds 600 images of normal insulators captured by UAVs, with annotations of the insulators only. The Defective_Insulators folder holds 248 synthetic images whose annotations cover both the insulators and their defects. Each folder has an images and a labels subfolder, and the labels use the VOC2007 format.

The defective images were synthesized because few real defective insulators were available: TVSeg masks from part of the original images, augmented by affine transforms, trained a U-Net that segmented the remaining images, and the insulators were then attached to different backgrounds.

## References

- [GitHub repository](https://github.com/InsulatorData/InsulatorDataSet)
- [Industrial Atlas page](https://www.indatlas.com/datasets/chinese-power-line-insulator-dataset/)

[⬅️ Back to Index](../README.md)
