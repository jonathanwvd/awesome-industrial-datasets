# SIT Large-Format LiFePO4 Battery Degradation Dataset (50 Ah Prismatic Cells)

**Summary:** Aging data from 22 prismatic 50 Ah LiFePO4 cells cycled for about 18 months at several rates and temperatures, logged at 1-second resolution with per-cell surface temperature.

| Parameter | Value |
| --- | --- |
| **Domain** | Energy and power |
| **Asset / Process** | Batteries |
| **Modality** | Time series |
| **Task** | Condition monitoring; RUL and prognostics |
| **Annotation** | — |
| **Source Type** | Lab or testbed |
| **Access** | Zenodo, Dataverse or Figshare |
| **Size** | 22 cells, about 14,800 data files |
| **Year** | 2026 |
| **License** | CC BY |
| **Publisher** | Singapore Institute of Technology |

## Description

This degradation dataset from the Singapore Institute of Technology (SIT) follows 22 large-format prismatic lithium iron phosphate cells (Narada FE50B, 50 Ah, 3.2 V nominal) over a campaign of about 18 months, from October 2022 to March 2024. The study was supported by the Singapore Energy Market Authority (EMA) under its Exploiting Distributed Generation Programme.

Testing used Repower and Chroma battery cyclers and a Sanwood environmental chamber. Protocols include full charge and discharge cycles at 1C and 2C and partial micro-cycles around 50% state of charge, at ambient temperature and in a chamber held at 40 °C. Up to 878 cycles per cell were recorded at 1-second resolution, in approximately 14,800 data files.

Each cycle workbook has charge and discharge sheets with voltage, current, capacity, energy, time and surface temperature from one or two thermocouple channels per cell. Per-cell capacity summaries track fade; after about 800 cycles at 1C and ambient temperature, ten cells keep between 6.7% and 87.6% of their capacity. A Python loader and Jupyter notebooks are included, and the data is released under CC BY 4.0.

## References

- [DOI](https://doi.org/10.57760/sciencedb.34754)
- [DOI](https://doi.org/10.25447/sit.32101523.v2)
- [Industrial Atlas page](https://www.indatlas.com/datasets/sit-lfp-50ah-degradation/)

[⬅️ Back to Index](../README.md)
