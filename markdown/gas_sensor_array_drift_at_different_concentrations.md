# Gas Sensor Array Drift at Different Concentrations

13,910 measurements from 16 chemical sensors exposed to six gases over 36 months, each labelled with the gas and its concentration in ppmv.

- **Domain:** Chemical and process
- **Modality:** Tabular
- **Task:** Classification; Regression
- **Annotation:** Class label; Scalar target
- **Source Type:** Lab or testbed
- **Access:** UCI repository
- **Size:** 13,910 measurements
- **Year:** 2013
- **License:** Academic or non-commercial terms

## Description

Gas Sensor Array Drift at Different Concentrations extends the Gas Sensor Array Drift Dataset with the concentration level of each measurement. The data was gathered from January 2008 to February 2011 (36 months) on a gas delivery platform at the ChemoSignals Laboratory, BioCircuits Institute, University of California San Diego. Its creator is Alexander Vergara, and it was donated to the UCI Machine Learning Repository in 2013.

The 13,910 measurements come from 16 chemical sensors exposed to Ammonia, Acetaldehyde, Acetone, Ethylene, Ethanol and Toluene at gas-specific concentration ranges in ppmv. Each 16-channel sensor response becomes a 128-dimensional vector: per sensor, the steady-state resistance change, its normalised version and six exponential moving average transients with alpha 0.1, 0.01 and 0.001.

The data is split into ten batch files in libsvm-style format, each line giving the gas class, the concentration and the features. It is meant for tasks such as sensor drift, classification and regression, among others. Use is limited to research, and citing Vergara et al. and Rodriguez-Lujan et al. (2014) is required.

## References

- [DOI](https://doi.org/10.24432/C5MK6M)
- [Industrial Atlas page](https://www.indatlas.com/datasets/gas-sensor-array-drift-at-different-concentrations/)

[⬅️ Back to Index](../README.md)
