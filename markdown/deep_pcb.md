# DeepPCB

**Summary:** 1,500 aligned pairs of defect-free template and tested PCB images, with bounding boxes for six defect types and 1,000 images set aside for training.

| Parameter | Value |
| --- | --- |
| **Domain** | Electronics and semiconductors |
| **Asset / Process** | PCBs and electronic assemblies |
| **Modality** | Image |
| **Task** | Defect detection; Object detection |
| **Annotation** | Bounding box |
| **Source Type** | Mixed |
| **Access** | Code repository |
| **Size** | 1,500 image pairs |
| **Year** | 2018 |
| **License** | Academic or non-commercial terms |
| **Benchmark** | Yes |

## Description

DeepPCB is a printed circuit board defect dataset introduced with the paper "On-line PCB Defect Detector On A New PCB Defect Dataset". Its images come from a linear scan CCD at about 48 pixels per millimetre; the original images of around 16k by 16k pixels are cropped into 640 by 640 sub-images, aligned by template matching and binarized.

The 1,500 image pairs each combine a defect-free template with an aligned tested image. Because real tested images hold few defects, artificial defects were added by hand, giving around 3 to 12 defects per image. Each defect has an axis-aligned bounding box and one of six classes: open, short, mousebite, spur, pin hole and spurious copper.

The authors separate 1,000 images as the training set and keep the rest for testing. Evaluation uses mean average precision and F-score, counting a detection when its IoU with a ground truth box of the same class exceeds 0.33. The authors allow use of the dataset for research purposes only.

## References

- [GitHub repository](https://github.com/tangsanli5201/DeepPCB)
- [GitHub repository](https://github.com/Charmve/Surface-Defect-Detection/tree/master/DeepPCB)
- [Industrial Atlas page](https://www.indatlas.com/datasets/deep-pcb/)

[⬅️ Back to Index](../README.md)
