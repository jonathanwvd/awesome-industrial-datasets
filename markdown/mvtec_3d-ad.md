# MVTec 3D-AD

**Summary:** Unsupervised 3D anomaly detection and localisation dataset with paired RGB images and 3D coordinate maps, plus ground-truth defect annotations across 10 industrial object categories.

| Parameter | Value |
| --- | --- |
| **Associated Tasks** | Anomaly Detection, 3D Anomaly Localisation, Segmentation |
| **Data Source** | Real |
| **Dataset Characteristics** | Image, 3D Point Cloud, Anomaly Detection |
| **Date Donated** | 2022 |
| **Feature Type** | 3D Coordinate Maps (XYZ) + RGB Images |
| **Labeled** | Yes |
| **Missing Values** | No |
| **Name** | MVTec 3D-AD |
| **Number of Features** | Information not available |
| **Number of Instances** | 4147 high-resolution scans across 10 categories |
| **Source** | https://www.mvtec.com/company/research/datasets/mvtec-3d-ad |
| **Time Series** | No |

## Description

MVTec 3D-AD is the first large-scale dataset dedicated to unsupervised 3D anomaly detection and localisation in industrial inspection scenarios. Each sample consists of paired data: a high-resolution 3D point cloud represented as XYZ TIFF coordinate maps and a corresponding RGB PNG image, allowing methods to exploit complementary 2D and 3D information.

The dataset spans 10 industrial object categories. For each category, defect-free samples are provided for training and validation, while the test set contains both normal and anomalous samples. Anomalous test samples are accompanied by pixel-precise ground truth masks indicating defect regions. The dataset includes calibration parameters to enable joint 2D/3D analysis. Total dataset size is approximately 13.2 GB.

MVTec 3D-AD was introduced at VISAPP 2022 and has since become a standard benchmark for evaluating 3D industrial inspection methods. It is licensed under CC BY-NC-SA 4.0 for non-commercial research use.

## Tags

3D Anomaly Detection, Defect Localisation, Industrial Inspection, MVTec, Point Clouds, RGB-D, Unsupervised Learning

## References

- [Dataset page](https://www.mvtec.com/company/research/datasets/mvtec-3d-ad)
- [Downloads](https://www.mvtec.com/company/research/datasets/mvtec-3d-ad/downloads)
- [Paper (VISAPP 2022)](https://doi.org/10.5220/0010865000003124)

[⬅️ Back to Index](../README.md)
