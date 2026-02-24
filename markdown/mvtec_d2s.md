# MVTec D2S

**Summary:** Instance-aware segmentation benchmark for industrial retail and warehouse scenarios with 21,000 high-resolution images and pixel-wise instance labels across 60 product categories.

| Parameter | Value |
| --- | --- |
| **Associated Tasks** | Instance Segmentation, Semantic Segmentation, Object Detection |
| **Data Source** | Real |
| **Dataset Characteristics** | Image, Instance Segmentation |
| **Date Donated** | 2018 |
| **Feature Type** | Images + COCO-format Annotations |
| **Labeled** | Yes |
| **Missing Values** | No |
| **Name** | MVTec D2S |
| **Number of Features** | Information not available |
| **Number of Instances** | 21000 images across 60 object categories |
| **Source** | https://www.mvtec.com/company/research/datasets/mvtec-d2s |
| **Time Series** | No |

## Description

MVTec D2S (Densely Segmented Supermarket Dataset) is an industrial vision benchmark targeting automated checkout, inventory management, and intralogistics applications. The dataset contains 21,000 high-resolution images of product objects in varied lighting, rotations, and background conditions, closely mimicking real-world warehouse and retail checkout scenarios.

All 60 product categories are annotated with pixel-precise instance segmentation labels in COCO JSON format. The dataset provides labelled training and validation splits; test set annotations are withheld and evaluation requires submitting results in COCO JSON format to the official evaluation server. Images are approximately 6.0 GB and annotations approximately 40 MB.

MVTec D2S was introduced at ECCV 2018 and is a standard benchmark for dense instance segmentation in operational industrial settings. It is licensed under CC BY-NC-SA 4.0 for non-commercial research use.

## Tags

COCO Format, Industrial Vision, Instance Segmentation, Intralogistics, MVTec, Retail Automation, Warehouse Vision

## References

- [Dataset page](https://www.mvtec.com/company/research/datasets/mvtec-d2s)
- [Downloads](https://www.mvtec.com/company/research/datasets/mvtec-d2s/downloads)
- [Paper (ECCV 2018)](https://openaccess.thecvf.com/content_ECCV_2018/papers/Patrick_Follmann_D2S_Densely_Segmented_ECCV_2018_paper.pdf)

[⬅️ Back to Index](../README.md)
