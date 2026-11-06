# MVTec D2S

**Summary:** Instance-aware semantic segmentation benchmark of 21,000 high-resolution images showing groceries and everyday products from 60 categories.

| Parameter | Value |
| --- | --- |
| **Domain** | Logistics and retail |
| **Asset / Process** | — |
| **Modality** | Image |
| **Task** | Object detection |
| **Annotation** | Instance mask |
| **Source Type** | — |
| **Access** | — |
| **Size** | 21,000 images |
| **Year** | — |
| **License** | CC BY-NC-SA |
| **Publisher** | MVTec |

## Description

MVTec D2S (densely segmented supermarket) is a benchmark from MVTec for instance-aware semantic segmentation in an industrial domain. It is designed to resemble the setting of an automatic checkout, inventory or warehouse system.

It holds 21,000 high-resolution images with pixel-wise labels of every object instance, covering groceries and everyday products from 60 categories. Each training image shows objects of only one class against a homogeneous background. The validation and test scenes are more complex and diverse, taken under different lightings, rotations and backgrounds. The pixel-precise annotations allow crops of single instances to be used for artificial data augmentation.

The test annotations are not public. MVTec can score result files in COCO JSON format, with instance masks as RLE or bounding boxes, sent through its contact form. The data is released under CC BY-NC-SA 4.0, which does not allow commercial use.

## References

- [Official page](https://www.mvtec.com/company/research/datasets/mvtec-d2s)
- [Industrial Atlas page](https://www.indatlas.com/datasets/mvtec-d2s/)

[⬅️ Back to Index](../README.md)
