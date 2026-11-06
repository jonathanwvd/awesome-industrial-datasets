# BSData

**Summary:** 1,104 images of ball screw drive surfaces with labelme pitting annotations, including 27 wear development sequences and a script for three data splits.

| Parameter | Value |
| --- | --- |
| **Domain** | Manufacturing |
| **Asset / Process** | — |
| **Modality** | Image |
| **Task** | Defect detection; Defect segmentation; Condition monitoring |
| **Annotation** | Instance mask; Sample label |
| **Source Type** | — |
| **Access** | Code repository |
| **Size** | 1,104 images, 394 image annotations |
| **Year** | 2021 |
| **License** | CC BY-SA |

## Description

BSData is an image dataset of surface defects on ball screw drives, a machine tool element, intended for instance segmentation and industrial wear forecasting. It is described in the publication "Industrial Machine Tool Element Surface Defect Dataset" and distributed through a GitHub repository.

The dataset holds 1,104 three-channel JPEG images and 394 image annotations of the surface damage type pitting, drawn with labelme and stored as JSON, convertible to VOC and COCO. The images show two ball screw drive types: one in 69 images with 55 image sizes, clean or soiled, and one in 325 images with two sizes, recorded over time with evolving soiling. A label key marks whether an image contains pitting, and file names carry a timestamp.

A script creates three splits: an 80/20 train and test split used for the included baseline model, the 27 wear development sequences, and a split by drive type. The data is released under CC BY-SA 4.0.

## References

- [GitHub repository](https://github.com/2Obe/BSData)
- [Industrial Atlas page](https://www.indatlas.com/datasets/bsdata/)

[⬅️ Back to Index](../README.md)
