# Dataset of Hyperspectral Melt Pool Signatures and Thermal Anomalies in DED of 316L steel

**Summary:** In-situ hyperspectral NIR melt pool images from directed energy deposition of 316L steel, labelled into six thermal anomaly classes.

| Parameter | Value |
| --- | --- |
| **Dataset** | Dataset of Hyperspectral Melt Pool Signatures and Thermal Anomalies in DED of 316L steel |
| **Domain** | Manufacturing & Production |
| **Asset / Process** | Additive Manufacturing |
| **Modality** | Image |
| **Task** | Classification; Process Monitoring |
| **Annotation** | Class Label |
| **Source Type** | Real Lab / Testbed |
| **Access** | Zenodo / Dataverse |
| **Size** | 561,861 hyperspectral images |
| **Year** | 2023 |
| **License** | CC BY |

## Description

This dataset from Vrije Universiteit Brussel contains in-situ melt pool signatures, recorded as hyperspectral near-infrared (NIR) images, from directed energy deposition (DED) of 316L steel. Samples were printed on the university's MiCLAD machine with a 600 W laser, and thermal anomalies were created by varying the scanning speed between 500 and 1300 mm/min.

A 3D-One Avior AX-M25NIR camera with a 5x5 hyperspectral filter layout records 25 wavelengths per image. The accompanying paper counts 561,861 images from four thin-wall samples. A CSV file lists the filename, sample, label, time, X and Z position and local scanning speed of every signature, with six labels: baseline, edge, underheat, strong underheat, overheat and strong overheat.

The raw .tif images come in ZIP archives with a Python debayering function that retrieves the spectral bands. The paper trains convolutional neural networks to classify the melt pool class. The data is released under CC BY 4.0.

## References

- [DOI](https://doi.org/10.5281/zenodo.10409569)
- [Zenodo record](https://zenodo.org/records/10409569)
- [DOI](https://doi.org/10.1109/ACCESS.2024.3507370)

[⬅️ Back to Index](../README.md)
