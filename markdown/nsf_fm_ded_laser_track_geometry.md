# NSF Future Manufacturing Data Challenge: A Multimodal DED Dataset

**Summary:** Thermal image sequences, SEM tiles and height maps of single DED laser tracks on SS316L substrates, released for predicting local track geometry.

| Parameter | Value |
| --- | --- |
| **Domain** | Manufacturing |
| **Asset / Process** | Additive manufacturing |
| **Modality** | Image; Multimodal |
| **Task** | Regression; Quality prediction |
| **Annotation** | — |
| **Source Type** | — |
| **Access** | Zenodo, Dataverse or Figshare |
| **Size** | — |
| **Year** | 2026 |
| **License** | CC BY |
| **Publisher** | Texas A&M University |

## Description

This dataset from Texas A&M University supports the NSF Future Manufacturing Data Challenge. It holds multimodal measurements of single directed energy deposition (DED) laser tracks on SS316L substrates, made on an Optomec LENS MTS 500 hybrid manufacturing platform, and was published on Zenodo in 2026 with National Science Foundation grant FMRG-2328395.

There are three modalities: in-situ thermal image sequences, SEM images of the surrounding substrate morphology from a Zeiss EVO MA10, and full-field height maps from a Bruker ContourGT-K white-light profilometer. Thermal frames are 400 × 400 pixels at about 14 µm per pixel, recorded at 50 fps with a scan speed of 10 mm/s. The common analysis window runs from 20 to 100 mm in part coordinates.

The challenge task is to predict local geometric variation along each track, with local width from the height map as the primary target. A GitHub repository adds starter notebooks and loaders. The Zenodo record is licensed CC BY 4.0.

## References

- [DOI](https://doi.org/10.5281/zenodo.21285367)
- [Zenodo record](https://zenodo.org/records/21285367)
- [GitHub repository](https://github.com/abhishekhanchate/nsf-fmrg-data-challenge)
- [Industrial Atlas page](https://www.indatlas.com/datasets/nsf-fm-ded-laser-track-geometry/)

[⬅️ Back to Index](../README.md)
