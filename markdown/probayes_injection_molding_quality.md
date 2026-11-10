# Injection-Molding Production Data with Quality Labels

Sensor and quality-control data for 564 injection molded parts from a design of experiments in PP and ABS, with each part inspected as OK or NOK.

- **Domain:** Manufacturing
- **Modality:** Tabular
- **Task:** Quality prediction
- **Annotation:** Sample label
- **Source Type:** Lab or testbed
- **Access:** Direct download
- **Size:** 564 parts, 334 features
- **Year:** 2022
- **License:** CC BY

## Description

This dataset comes from the ProBayes research project, carried out by SKZ (German Plastics Center) and Fraunhofer IPA in 2021/2022 with funding from the Federal Ministry for Economic Affairs and Climate Action (BMWK) through AiF. Parts were made on a KraussMaffei 160-750PX injection molding machine.

A design of experiments was run for each of two materials, polypropylene (PP) and acrylonitrile butadiene styrene (ABS), giving 47 experimental points with 12 parts each, or 564 parts in total. Each row holds one part or cycle and is identified by its MachineCycleID. The 334 features come from 9 data sources, among them peripheral devices such as temperature control, dosing unit and dryer, and quality devices such as computer vision, a scale and an infrared camera.

Every part was inspected by hand and classified as OK or NOK, with some further labels. The record is version 2, published in 2022 under CC BY 4.0, with files named dataset_V2.parquet and data_description.pdf.

## References

- [Official page](https://b2share.eudat.eu/records/4c5692b886db419180f716acf895bf06)
- [Industrial Atlas page](https://www.indatlas.com/datasets/probayes-injection-molding-quality/)

[⬅️ Back to Index](../README.md)
