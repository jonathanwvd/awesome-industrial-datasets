# Annotated Image Dataset for Shielded Metal Arc Welding (SMAW) Surface Defect Detection

448 annotated images of SMAW joints on SS45 medium-carbon steel showing spatter, slag inclusion and undercut, with COCO annotations and an 80:20 train-test split.

- **Domain:** Manufacturing
- **Asset / Process:** Welding
- **Modality:** Image
- **Task:** Defect detection; Object detection; Defect segmentation
- **Annotation:** Bounding box; Instance mask
- **Access:** Mendeley Data
- **Size:** 448 annotated images
- **Year:** 2026
- **License:** CC BY
- **Benchmark:** Yes

## Description

This Mendeley Data record, contributed by Mubessirul Ummah, contains images of shielded metal arc welding (SMAW) joints made on SS45 medium-carbon steel. It targets three surface weld defects: spatter, slag inclusion and undercut. It is the companion dataset to an article on detection transformer (DETR) models for defect identification in SMAW plate joints.

Photos come from a 50-megapixel smartphone camera on a tripod held 15 cm from the weld. A certified welding inspector reviewed and verified the 71 starting images of 3456×3456 px, which were annotated with polygon and bounding-box tools in Roboflow, resized to 640×640 px and tiled into a 5×5 grid. The outcome is 448 samples with COCO-format JSON annotations.

The samples are split 80:20 into 358 training and 90 test images. The training subset is augmented to 3,580 images and divided into five cross-validation folds. Version 1 appeared in August 2026 under CC BY 4.0.

## References

- [Mendeley Data](https://data.mendeley.com/datasets/f7j76vz53p)
- [Industrial Atlas page](https://www.indatlas.com/datasets/smaw-surface-defects/)

[⬅️ Back to Index](../README.md)
