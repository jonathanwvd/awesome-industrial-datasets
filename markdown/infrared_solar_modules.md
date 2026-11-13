# InfraredSolarModules

20,000 small infrared images of solar modules from solar farms, each labelled with one of 11 anomaly classes such as hot spots, cracking or soiling, or as no anomaly.

- **Domain:** Energy and power
- **Asset / Process:** Solar PV
- **Modality:** Image
- **Task:** Classification
- **Annotation:** Class label
- **Source Type:** Real production
- **Access:** Code repository
- **Size:** 20,000 infrared images
- **Year:** 2020
- **Publisher:** Raptor Maps, Inc.

## Description

InfraredSolarModules is a labelled machine learning dataset of real-world infrared imagery showing anomalies on solar modules in solar farms. Raptor Maps released it, and it was first published at the AI for Earth Sciences workshop of ICLR 2020.

Its 20,000 infrared images measure 24 by 40 pixels each and fall into 12 classes. Half of them, 10,000 images, show nominal modules in the No-Anomaly class. The other 11 classes cover anomalies such as hot spots in a single cell (1,877 images) or in several cells, cracking, hot spots on thin film modules, shadowing, one or more activated bypass diodes (1,499 for a single diode), vegetation (1,639), soiling and offline modules, where the entire module is heated (828).

A single zip archive holds the images directory and a module_metadata.json file that records the file path and anomaly class of every image, which supports anomaly classification of solar PV modules.

## References

- [GitHub repository](https://github.com/RaptorMaps/InfraredSolarModules)
- [Industrial Atlas page](https://www.indatlas.com/datasets/infrared-solar-modules/)

[⬅️ Back to Index](../README.md)
