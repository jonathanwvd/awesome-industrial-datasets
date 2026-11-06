# SegWeldCT

**Summary:** Thirty high-resolution industrial CT volumes of butt and fillet welds made by MAG, MMA, TIG and oxyacetylene welding, for weld inspection research.

| Parameter | Value |
| --- | --- |
| **Domain** | Manufacturing |
| **Asset / Process** | Welding |
| **Modality** | X-ray and CT |
| **Task** | Defect detection; Classification |
| **Annotation** | — |
| **Source Type** | — |
| **Access** | Zenodo, Dataverse or Figshare |
| **Size** | 30 CT volumes |
| **Year** | 2026 |
| **License** | CC BY |
| **Publisher** | Brno University of Technology |

## Description

SegWeldCT is a set of high-resolution industrial computed tomography (CT) scans of welded joints from Brno University of Technology, with contributors from the Institute of Criminalistics. It was published on Zenodo in 2026 to support automated weld inspection, internal defect analysis and welding-process identification.

The 30 reconstructed 3D volumes come from specimens made with four welding processes, oxyacetylene, Manual Metal Arc (MMA), Metal Active Gas (MAG) and Tungsten Inert Gas (TIG), in both butt and fillet joints. Each volume is about 2 GB in MetaImage (.mha) format. Scans used a WidePIX A06-W0562-10 detector at a 40 keV energy threshold, 0.7 s exposure and a nominal voxel size of 0.055 mm, without filtering of the reconstructions.

The accompanying study annotated 90 2D slices for welding-process classification and binary defect segmentation; those slices and masks are not part of this release. Partitions for machine learning should be separated at the volume level. The data is licensed under CC BY 4.0.

## References

- [DOI](https://doi.org/10.5281/zenodo.23591479)
- [Zenodo record](https://zenodo.org/records/23591479)
- [Industrial Atlas page](https://www.indatlas.com/datasets/segweldct/)

[⬅️ Back to Index](../README.md)
