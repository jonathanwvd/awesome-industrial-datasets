# SKZ Injection Molding Dataset (Viscometer, Euromap77, Quality Table)

Machine settings, Euromap77 machine data, quality table values and in-nozzle viscometer pressure curves from 68 ABS injection molding cycles at 17 settings.

- **Domain:** Manufacturing
- **Modality:** Time series; Tabular
- **Task:** Regression
- **Source Type:** Lab or testbed
- **Access:** Zenodo, Dataverse or Figshare
- **Size:** 68 cycles in 17 experiments (1.0 GB)
- **Year:** 2025
- **Publisher:** SKZ (German Plastics Center)

## Description

This dataset from SKZ, the German Plastics Center in Würzburg, comes from the research project LoKI, funded by the Bavarian collaborative research programme. A KraussMaffei 160-750PX injection molding machine was fitted with a Dynisco viscometer at the injection nozzle and used to mold standard parts of roughly 100 × 160 × 60 mm from Terluran GP-35 ABS.

It holds 68 cycles: 17 experiments with distinct machine settings, each repeated four times to capture statistical spread. Three subsets can be joined by experiment and run identifiers: machine setting parameters with Euromap77 machine data read over OPC UA after each cycle, time-resolved viscometer pressure data, and values from the machine's quality table, such as pressure and energy parameters measured by internal sensors.

The data was collected to test whether machine learning models can predict material viscosity during injection from internal OPC UA machine data, as an AI-based viscometer, and whether they can propose adjusted settings that offset viscosity swings between batches, for example with recyclate. Files are provided as CSV and Parquet on B2SHARE.

## References

- [Official page](https://b2share.eudat.eu/records/fkk68-zyf30)
- [b2share.eudat.eu](https://b2share.eudat.eu/records/fkk68-zyf30/files/Dataset%20description.pdf)
- [Industrial Atlas page](https://www.indatlas.com/datasets/skz-loki-injection-molding-viscometer/)

[⬅️ Back to Index](../README.md)
