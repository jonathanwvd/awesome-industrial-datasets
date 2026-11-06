# Spatiotemporally Registered In-Situ and Ex-Situ Datasets for Laser-based Blown Powder Directed Energy Deposition

**Summary:** In situ melt pool video and toolpath coordinates from eight Inconel 718 DED builds, registered to post-build X-ray CT of each part.

| Parameter | Value |
| --- | --- |
| **Domain** | Manufacturing |
| **Asset / Process** | Additive manufacturing |
| **Modality** | Video; X-ray and CT; Multimodal |
| **Task** | Process monitoring |
| **Annotation** | — |
| **Source Type** | — |
| **Access** | Official portal |
| **Size** | eight DED builds |
| **Year** | 2024 |
| **License** | — |
| **Publisher** | Oak Ridge National Laboratory |

## Description

This Oak Ridge National Laboratory dataset covers laser-based blown powder directed energy deposition (DED) of Inconel 718. It was released in November 2024 under sponsorship of the Advanced Manufacturing Office of the Office of Energy Efficiency and Renewable Energy (EERE).

Eight builds share one test coupon geometry with bulk deposition, thin walls and overhangs, each under a different printing condition: nominal, +15% scan speed, +12% laser power, +42% powder feed rate, +100% jerk limit, +10% layer height, +20% hatch spacing and +20% carrier gas flow. In situ data consist of xyz coordinates at 100 Hz and on-axis melt pool camera video at 60 Hz, synchronized in time so the camera data maps onto positions.

Post-build X-ray computed tomography (XCT) of each coupon is spatially registered to the recorded coordinates, so melt pool camera data can be compared with flaws found in the XCT data. The files are read with an HDF5 reader and are downloaded through Globus.

## References

- [DOI](https://doi.org/10.13139/OLCF/2446626)
- [osti.gov](https://www.osti.gov/dataexplorer/biblio/dataset/2446626)
- [Industrial Atlas page](https://www.indatlas.com/datasets/ornl-ded-in718-registered/)

[⬅️ Back to Index](../README.md)
