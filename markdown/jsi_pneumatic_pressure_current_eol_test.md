# Pneumatic Pressure and Electrical Current Time Series in Manufacturing

Seven days of pneumatic pressure and actuator current at 100 Hz from an end-of-line test machine for small electric drives, labelled by processing step.

- **Domain:** Manufacturing
- **Asset / Process:** Valves and actuators
- **Modality:** Time series
- **Task:** Classification; Process monitoring
- **Annotation:** Event and time label; Class label
- **Source Type:** Real production
- **Access:** Mendeley Data
- **Size:** About 150 pieces, 3,674 labelled segments
- **Year:** 2024
- **License:** CC BY
- **Publisher:** Jožef Stefan Institute

## Description

This dataset comes from a real discrete manufacturing shopfloor: a machine that tests assembled small electric drives at the end of the line, at a large European drive supplier. Researchers from the Jožef Stefan Institute and the University of Ljubljana collected it and described it in Data in Brief.

A pressure sensor on the pneumatic line powering the machine and a current sensor on the combined supply of its actuators were both sampled at 100 Hz. The recordings span seven days and about 150 processed pieces. Each timestamp is tagged with one of the 24 processing steps the machine performs per piece, taken from transitions in its internal state machine.

Cutting the series into runs of constant step label gives 3,674 labelled segments, each with a characteristic pressure and current signature. The labels support supervised time series classification and the validation of clustering and segmentation methods for non-invasive process monitoring. Files are CSV with Python pickle versions and demonstration notebooks.

## References

- [Mendeley Data](https://data.mendeley.com/datasets/ypzswhhzh9)
- [pmc.ncbi.nlm.nih.gov](https://pmc.ncbi.nlm.nih.gov/articles/PMC11239481/)
- [Industrial Atlas page](https://www.indatlas.com/datasets/jsi-pneumatic-pressure-current-eol-test/)

[⬅️ Back to Index](../README.md)
