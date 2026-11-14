# PMSG-3phase-Dataset

Lab recordings of a permanent magnet synchronous generator under 24 short-circuit faults and a healthy state, at three torque levels and three speeds.

- **Domain:** Energy and power
- **Asset / Process:** Motors and drives
- **Modality:** Time series
- **Task:** Fault diagnosis; Condition monitoring
- **Annotation:** Class label
- **Source Type:** Lab or testbed
- **Access:** Zenodo, Dataverse or Figshare
- **Size:** 225 .mat files
- **Year:** 2025
- **License:** CC BY
- **Publisher:** University of São Paulo

## Description

This dataset records electrical signals from a three-phase permanent magnet synchronous generator (PMSG) on a test bench in the Real-Time Simulation Laboratory of the InnovaPower Hub at the University of São Paulo. It accompanies a Data in Brief article that presents it as a benchmark dataset of PMSG electrical signals for condition monitoring, and it is archived on Zenodo as a release of the MitDev-Eletrica repository.

The generator has 24 winding taps placed at set distances from the neutral point, which allow short circuits between turns and windings to be staged. The 225 MATLAB files cover 24 fault conditions and one healthy state, each run at three torque levels and three rotational speeds. Every test lasts three seconds at a 20 kHz sampling rate, and the fault tests capture the pre-fault, fault and post-fault periods. The files are labelled by test condition.

The files can be read in Python without MATLAB. The data is released under CC BY 4.0.

## References

- [DOI](https://doi.org/10.5281/zenodo.15741561)
- [Zenodo record](https://zenodo.org/records/15741561)
- [ncbi.nlm.nih.gov](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12475480/)
- [GitHub repository](https://github.com/InnovaPower/MitDev-Eletrica)
- [Industrial Atlas page](https://www.indatlas.com/datasets/mitdev-eletrica-pmsg/)

[⬅️ Back to Index](../README.md)
