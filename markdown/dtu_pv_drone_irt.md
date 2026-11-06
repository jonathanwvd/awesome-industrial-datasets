# DTU PV plant - Drone Infrared Thermography Dataset: Influence of Irradiance and Altitude

Drone infrared thermography images of defective PV modules at DTU's Risø plant, taken at four altitudes and irradiances, with EL images and IV curves.

- **Domain:** Energy and power
- **Asset / Process:** Solar PV
- **Modality:** Image; Multimodal
- **Task:** Defect detection
- **Annotation:** Class label
- **Access:** Zenodo, Dataverse or Figshare
- **Year:** 2025

## Description

This dataset holds drone infrared thermography (IRT) images of photovoltaic modules at DTU's PV plant at Risø, collected in the SOLARIS project. It gathers the measurements behind the publication "Advancing Drone Infrared Thermography for Photovoltaic Plant Inspections Defect Detection: Influence of Altitude and Environmental Conditions" and was posted in 2025 by Rodrigo Del Prado Santamaria.

Each module under study was imaged from the drone at four altitudes and irradiances. The ZIP archive is organised by defect type, with one folder per module. A module folder holds an EL image in NEF format, or a visible image for the soiling cases, plus IRT images as PNG files for viewing and as raw float32 temperature files sampled to 363x605 pixels.

Each module folder also has its IV curve as a CSV file of measured voltage and current, the average of three measurements at standard test conditions. For two soiling modules, the IV curves were measured in the field with a portable IV tracer.

## References

- [Official page](https://data.dtu.dk/articles/dataset/DTU_PV_plant_-_Drone_Infrared_Thermography_Dataset_Influence_of_Irradiance_and_Altitude/29665346/1)
- [Industrial Atlas page](https://www.indatlas.com/datasets/dtu-pv-drone-irt/)

[⬅️ Back to Index](../README.md)
