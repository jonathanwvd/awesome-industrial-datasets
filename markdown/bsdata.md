# BSData

**Summary:** KIT ball screw surface defect dataset with 1,104 segmentation images and 21,835 classification patches focusing on pitting defects; supports defect detection, instance segmentation, and prognostics research under CC BY-SA 4.0.

| Parameter | Value |
| --- | --- |
| **Associated Tasks** | Defect Classification, Instance Segmentation, Defect Detection, Prognostics |
| **Data Source** | Real |
| **Dataset Characteristics** | Image, Segmentation, Multiclass |
| **Date Donated** | 2021 |
| **Feature Type** | Image |
| **Labeled** | Yes |
| **Missing Values** | No |
| **Name** | BSData |
| **Number of Features** | RGB images of ball screw surfaces; instance segmentation masks for pitting defects |
| **Number of Instances** | 1,104 images with instance segmentation annotations; 21,835 image patches for classification |
| **Source** | Karlsruhe Institute of Technology (KIT) / GitHub |
| **Time Series** | No |

## Description

BSData (Ball Screw Dataset) was created at the Karlsruhe Institute of Technology (KIT) for research in surface defect detection, instance segmentation, and prognostics of ball screw drives. Ball screws are precision mechanical components widely used in industrial machinery; pitting defects on their surface are a primary failure mode.

The dataset contains 1,104 images with instance-level segmentation annotations marking individual pitting defects, and 21,835 smaller image patches extracted for classification tasks (defective vs. non-defective). Images were captured under controlled lighting from actual ball screw components with varying degrees of wear and pitting.

The dataset supports three main research tasks: (1) defect classification of image patches, (2) instance segmentation of defect regions in full images, and (3) prognostics to predict remaining useful life based on observed defect patterns. Published under the CC BY-SA 4.0 license, the dataset is hosted on GitHub and is one of the few publicly available datasets specifically for ball screw health monitoring.

## Tags

Ball Screw, CC BY-SA 4.0, Defect Classification, Instance Segmentation, KIT, Pitting, Predictive Maintenance, Prognostics, Surface Defect

## References

- [BSData GitHub Repository](https://github.com/2Obe/BSData)
- [BSData Paper (IEEE Access)](https://doi.org/10.1109/ACCESS.2021.3116068)

[⬅️ Back to Index](../README.md)
