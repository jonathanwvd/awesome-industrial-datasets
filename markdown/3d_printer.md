# 3D Printer Dataset for Mechanical Engineers

Results of 3D printing tests that link nine printer setting parameters to measured roughness, ultimate tensile strength and elongation.

- **Domain:** Manufacturing
- **Asset / Process:** Additive manufacturing
- **Modality:** Tabular
- **Task:** Regression; Quality prediction; Classification
- **Annotation:** Scalar target; Class label
- **Source Type:** Lab or testbed
- **Access:** Kaggle

## Description

This dataset links the setting parameters of a 3D printer to the quality, accuracy and strength of the parts it prints. It originates from research at the Mechanical Engineering department of Selcuk University and uses the settings and filaments of an Ultimaker S5 printer.

Each record holds nine settings: layer height, wall thickness, infill density, infill pattern, nozzle temperature, bed temperature, print speed, material and fan speed. Three measured outputs follow: surface roughness in micrometres, ultimate tensile strength in MPa and elongation in percent. Material and strength tests were run on a Sincotec tester rated to pull 20 kN.

The stated aim of the study is to find how strongly each setting affects print quality, accuracy and strength. A second stated goal is to estimate the filament material from the input and output parameters with kNN and DNN algorithms.

## References

- [Kaggle dataset](https://www.kaggle.com/datasets/afumetto/3dprinter)
- [Industrial Atlas page](https://www.indatlas.com/datasets/3d-printer/)

[⬅️ Back to Index](../README.md)
