# MVTec ITODD

**Summary:** Industrial 3D object detection and 6D pose estimation dataset with multi-sensor acquisition per scene, including 3D range data, multiple grayscale cameras, and CAD models for 28 industrial objects.

| Parameter | Value |
| --- | --- |
| **Dataset** | MVTec ITODD |
| **Domain** | Robotics & Automation; Manufacturing & Production |
| **Asset / Process** | General Manufacturing |
| **Modality** | Image; 3D Point Cloud; RGB-D; Multimodal |
| **Task** | Object Detection; Pose Estimation; 3D Understanding |
| **Annotation** | Bounding Box; Pose / Keypoint Label; Split Metadata |
| **Source Type** | Real Lab / Testbed |
| **Access** | Direct Download |
| **Size** | 3500 labelled scenes across 28 object categories |
| **Year** | 2017 |
| **License** | CC BY-NC-SA |

## Description

MVTec ITODD (Industrial 3D Object Detection Dataset) is a benchmark dataset for 6D pose estimation of industrial objects in realistic factory settings. Each scene is captured simultaneously by five sensors: two 3D sensors producing range/XYZ images and three grayscale cameras (with and without projected pattern, and rectified/distorted variants). CAD models and camera calibration parameters are provided for all objects.

The dataset contains 28 objects and 3,500 labelled scenes, with downloads organised by modality. The base package includes 3D data and is approximately 150 MB, while individual grayscale camera packages are several GB each. This multi-modal and multi-sensor design distinguishes ITODD from simpler single-camera pose benchmarks and makes it relevant for robotic bin-picking and industrial assembly applications.

MVTec ITODD was introduced at the ICCV Workshops 2017 and is licensed under CC BY-NC-SA 4.0 for non-commercial research use. Users are encouraged to evaluate methods across all sensor modalities.

## References

- [Dataset page](https://www.mvtec.com/company/research/datasets/mvtec-itodd)
- [Downloads by modality](https://www.mvtec.com/company/research/datasets/mvtec-itodd/downloads)
- [Paper (ICCVW 2017)](https://openaccess.thecvf.com/content_ICCV_2017_workshops/papers/w31/Drost_Introducing_MVTec_ITODD_ICCV_2017_paper.pdf)

[⬅️ Back to Index](../README.md)
