# Wind Turbine SCADA Data For Early Fault Detection

SCADA time series from 36 turbines in three wind farms, split into 95 datasets of which 45 lead up to a labelled fault, with the CARE score for evaluation.

- **Domain:** Energy and power
- **Asset / Process:** Wind turbines
- **Modality:** Time series
- **Task:** Anomaly detection
- **Annotation:** Event and time label
- **Source Type:** Real production
- **Access:** Zenodo, Dataverse or Figshare
- **Size:** 95 datasets from 36 turbines
- **Year:** 2024
- **License:** CC BY-SA
- **Publisher:** Fraunhofer Institute for Energy Economics and Energy System Technology (IEE)
- **Benchmark:** Yes

## Description

This dataset, known by the title of its paper, CARE to Compare, gathers SCADA time series from 36 wind turbines in three wind farms for early fault detection. Christian Gück and Cyriana Roelofs of the Fraunhofer Institute for Energy Economics and Energy System Technology published it on Zenodo in 2024, under CC BY-SA 4.0.

The 95 datasets add up to 89 years of operation. Farm A, onshore in Portugal with 5 turbines, comes from the EDP open data platform and its fault logbook; farms B and C are anonymized offshore farms in Germany. They have 86, 257 and 957 features. In the current version, 45 datasets end in a turbine fault preceded by an anomaly and 50 show normal operation. Each data point carries a turbine-status label.

The accompanying paper defines the CARE score (Coverage, Accuracy, Reliability and Earliness) for comparing anomaly detection models. Later versions corrected some labels, and the record lists known implausible Min, Max and Std values, advising Avg signals only for most analyses of wind farm B.

## References

- [DOI](https://doi.org/10.5281/zenodo.14958989)
- [Zenodo record](https://zenodo.org/records/14958989)
- [Zenodo record](https://zenodo.org/records/14006163)
- [Preprint (arXiv)](https://arxiv.org/abs/2404.10320)
- [Industrial Atlas page](https://www.indatlas.com/datasets/care-to-compare-wind-turbine/)

[⬅️ Back to Index](../README.md)
