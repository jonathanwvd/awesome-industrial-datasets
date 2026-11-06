# PCAD

Multi-view RGB images of five electronic assembly groups with 6D poses, CAD models and defect masks for missing or interchanged components.

- **Domain:** Manufacturing
- **Asset / Process:** PCBs and electronic assemblies
- **Modality:** Image
- **Task:** Anomaly detection; Anomaly localization
- **Annotation:** Normal-only training; Pixel mask; Pose and keypoints
- **Source Type:** Mixed
- **Access:** Direct download
- **Size:** 1,440 defect-free and 4,744 defective samples
- **Year:** 2025
- **Publisher:** Institute for TMDT, University of Wuppertal

## Description

PCAD (Pose-agnostic Anomaly Detection using CAD Models) is an image dataset for anomaly detection in industrial assembly inspection, published by the Institute for TMDT at the University of Wuppertal. Products from a manufacturing facility for industry-grade electronic devices were captured with a dedicated hardware setup that records each sample from several viewpoints together with its 6D pose.

Five assembly groups are covered, with two defect kinds: missing components and interchanged components. The final set holds 1,440 defect-free and 4,744 defective samples, with binary defect masks rendered from the CAD models. CAD models, synthetic renderings, the raw images and a sparse set with shifted lighting are included as well.

In the accompanying paper, models are trained on defect-free samples of each product and scored with image-level AUROC, pixel-level AUROC and pixel-level AUPRO. The data and the generation pipeline are shared through the repository.

## References

- [GitHub repository](https://github.com/tmdt-buw/pcad-dataset)
- [openaccess.thecvf.com](https://openaccess.thecvf.com/content/WACV2025W/ASTAD/papers/Maack_PCAD_A_Real-World_Dataset_for_6D_Pose_Industrial_Anomaly_Detection_WACVW_2025_paper.pdf)
- [Industrial Atlas page](https://www.indatlas.com/datasets/pcad/)

[⬅️ Back to Index](../README.md)
