# Magnetic Tile Defect

**Summary:** Real-world magnetic tile surface defect dataset with 1,344 grayscale images across 6 defect categories and one defect-free class; includes pixel-level segmentation annotations for surface defect detection research.

| Parameter | Value |
| --- | --- |
| **Associated Tasks** | Defect Detection, Image Classification, Semantic Segmentation |
| **Data Source** | Real |
| **Dataset Characteristics** | Image, Multiclass, Segmentation |
| **Date Donated** | 2018 |
| **Feature Type** | Image |
| **Labeled** | Yes |
| **Missing Values** | No |
| **Name** | Magnetic Tile Defect |
| **Number of Features** | Grayscale images with pixel-level segmentation masks |
| **Number of Instances** | 1,344 images across 6 classes (MT_Blowhole, MT_Break, MT_Crack, MT_Fray, MT_Uneven, MT_Free) |
| **Source** | GitHub (abin24) / Northeastern University |
| **Time Series** | No |

## Description

The Magnetic Tile Defect dataset contains surface defect images of magnetic tiles collected from an industrial production line. It includes 1,344 images split across six defect categories: MT_Blowhole (blowhole defects), MT_Break (breakage), MT_Crack (surface cracks), MT_Fray (fraying), MT_Uneven (uneven surface), and MT_Free (defect-free samples used as the negative class).

Each image comes with a corresponding binary segmentation mask that identifies the defect region at the pixel level, enabling both classification and segmentation tasks. Images are grayscale and were acquired under controlled industrial conditions. The dataset was introduced alongside the paper 'A compact convolutional neural network for surface defect inspection' and has become a standard benchmark for industrial surface defect detection.

The dataset is hosted on GitHub and is widely used in quality control and automated visual inspection research. Tasks supported include binary defect detection, multi-class defect classification, and semantic segmentation of defect regions.

## Tags

Computer Vision, Defect Detection, Grayscale Images, Industrial Inspection, Magnetic Tile, Quality Control, Semantic Segmentation, Surface Defect

## References

- [GitHub: Magnetic Tile Defect Datasets (abin24)](https://github.com/abin24/Magnetic-tile-defect-datasets)
- [Paper: A compact convolutional neural network for surface defect inspection](https://doi.org/10.1016/j.measurement.2018.06.010)

[⬅️ Back to Index](../README.md)
