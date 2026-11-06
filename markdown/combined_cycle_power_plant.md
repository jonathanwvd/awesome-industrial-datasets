# Combined Cycle Power Plant

Hourly ambient readings and net electrical output from a combined cycle power plant at full load, 9,568 data points recorded from 2006 to 2011.

- **Domain:** Energy and power
- **Asset / Process:** Power grids and plants; Turbines and engines
- **Modality:** Tabular
- **Task:** Regression
- **Annotation:** Scalar target
- **Source Type:** Real production
- **Access:** UCI repository
- **Size:** 9,568 data points
- **Year:** 2014
- **License:** CC BY

## Description

The Combined Cycle Power Plant data set comes from a plant built from gas turbines, steam turbines and heat recovery steam generators, where the two turbine types are combined in one cycle to generate electricity. Its creators are Pınar Tüfekci and Heysem Kaya, and it was donated to the UCI Machine Learning Repository in 2014, with Tüfekci's paper in the International Journal of Electrical Power & Energy Systems as its introductory paper.

The data covers six years, 2006 to 2011, with the plant set to full load. Four hourly averaged ambient variables are the features: temperature (1.81 to 37.11 °C), ambient pressure, relative humidity and exhaust vacuum (25.36 to 81.56 cm Hg). The target is the net hourly electrical energy output, from 420.26 to 495.76 MW. Vacuum relates to the steam turbine, the other three variables to gas turbine performance. Values are not normalized and none are missing.

The 9,568 data points come shuffled five times so that 5x2-fold statistical tests can be run, in .xlsx and .ods files, under CC BY 4.0.

## References

- [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/Combined+Cycle+Power+Plant)
- [DOI](https://doi.org/10.24432/C5002N)
- [semanticscholar.org](https://www.semanticscholar.org/paper/f164ee353ada936ef97d0d379f8581336ddc9733)
- [Industrial Atlas page](https://www.indatlas.com/datasets/combined-cycle-power-plant/)

[⬅️ Back to Index](../README.md)
