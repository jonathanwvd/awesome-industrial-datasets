# MulSen-AD

Anomaly detection dataset that pairs RGB images, infrared thermography and laser-scanned 3D point clouds for 15 objects with 14 manually created anomaly types.

- **Domain:** Manufacturing
- **Modality:** Multimodal; Image; 3D point cloud
- **Task:** Anomaly detection; Anomaly localization
- **Annotation:** Sample label; Pixel mask
- **Source Type:** Lab or testbed
- **Access:** Hugging Face
- **Size:** 2,035 samples
- **Year:** 2025
- **Benchmark:** Yes

## Description

MulSen-AD is a multi-sensor anomaly detection dataset by Wenqiao Li and co-authors, presented at CVPR 2025 (arXiv 2412.14592). Each object is captured three ways: RGB images from cameras, gray-scale infrared images from lock-in infrared thermography and high-resolution 3D point clouds from laser scanners, so that surface appearance, geometric deformation and internal defects are all covered.

The 2,035 samples cover 15 objects made of metal, plastic, fiber, rubber, semiconductor and composite materials. The authors created 14 anomaly types by hand, among them cracks, holes, squeeze, creases, scratches, foreign bodies, bent parts and internal detachments. Each modality has train, test and ground-truth mask folders, the training data hold only normal objects, and object-level labels sit in CSV files.

MulSen-AD Bench evaluates multi-sensor methods; an object counts as anomalous when any of the three modalities is. A single 3D setting labels objects from the point cloud alone. The archive downloads from Hugging Face.

## References

- [GitHub repository](https://github.com/ZZZBBBZZZ/MulSen-AD)
- [Preprint (arXiv)](https://arxiv.org/abs/2412.14592)
- [Hugging Face dataset](https://huggingface.co/datasets/orgjy314159/MulSen_AD)
- [openaccess.thecvf.com](https://openaccess.thecvf.com/content/CVPR2025/html/Li_Multi-Sensor_Object_Anomaly_Detection_Unifying_Appearance_Geometry_and_Internal_Properties_CVPR_2025_paper.html)
- [Preprint (arXiv)](https://arxiv.org/html/2412.14592v1)
- [Industrial Atlas page](https://www.indatlas.com/datasets/mulsen-ad/)

[⬅️ Back to Index](../README.md)
