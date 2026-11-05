# CSEM-MISD

**Summary:** Image stacks of 70 defective metal washers, each lit from 108 angles in a light dome, with hand-labelled defect masks for segmentation.

| Parameter | Value |
| --- | --- |
| **Dataset** | CSEM-MISD |
| **Domain** | Manufacturing & Production |
| **Asset / Process** | Casting / Metal Parts |
| **Modality** | Image |
| **Task** | Defect Segmentation; Defect Detection |
| **Annotation** | Pixel Mask |
| **Source Type** | Real Lab / Testbed |
| **Access** | Zenodo / Dataverse |
| **Size** | 70 parts with 108 images each |
| **Year** | 2021 |
| **License** | CC BY-NC-ND |

## Description

CSEM-MISD is a multi-illumination defect segmentation dataset acquired at CSEM (Centre Suisse d'Electronique et de Microtechnique); its creators are affiliated with CSEM and the École polytechnique fédérale de Lausanne (EPFL). Parts were captured in a half-spherical light dome that filters out ambient light and lights each part from 108 distinct angles: nine elevation levels with 12 azimuths each, 30 degrees apart.

The dataset covers three kinds of metallic parts, washers, screws and gears, of which only the washers are available for now. The washer set has 70 defective parts, split into 32 training and 38 test samples. Each sample holds 108 images, an automatically extracted foreground mask and a hand-labelled defect segmentation mask. Some defects, such as notches and holes, show in most illuminations, while others, such as scratches, appear in only a few.

The data accompanies the 2021 paper "Defect segmentation for multi-illumination quality control systems" in Machine Vision and Applications. It is released for research purposes under CC BY-NC-ND 4.0, and data loaders and training code are on GitHub.

## References

- [DOI](https://doi.org/10.5281/zenodo.5513768)
- [Zenodo record](https://zenodo.org/records/5513769)
- [GitHub repository](https://github.com/DawyD/illumination-preserving-rotations)

[⬅️ Back to Index](../README.md)
