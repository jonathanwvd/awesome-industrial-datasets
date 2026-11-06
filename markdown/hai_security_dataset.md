# HAI Security Dataset

Time series of SCADA points with attack labels from an industrial control testbed coupled to a hardware-in-the-loop power generation simulator.

- **Domain:** OT security
- **Asset / Process:** Control systems and networks
- **Modality:** Time series
- **Task:** Intrusion detection; Anomaly detection
- **Annotation:** Event and time label; Normal-only training
- **Source Type:** Lab or testbed
- **Access:** Code repository
- **Year:** 2020
- **Publisher:** The Affiliated Institute of ETRI, South Korea
- **Benchmark:** Yes

## Description

The Affiliated Institute of ETRI in Daejeon, South Korea, publishes the HAI (HIL-based Augmented ICS) Security Dataset. Its testbed has four processes: a boiler on Emerson Ovation DCS, a turbine rotor kit on GE Mark VIe DCS, a water treatment process on a Siemens S7-300 PLC, and a dSPACE SCALEXIO simulation of steam-turbine and pumped-storage hydropower generation that ties the other three together.

Four versions have been released: HAI 20.07 (the bug-fixed HAI 1.0 of February 2020, with 38 attacks), 21.03, 22.04 and 23.05, plus HAIEnd 23.05 with points from the internal boiler DCS logic. Each version splits into normal-operation training files and attack test files. In every CSV the first column is a timestamp, followed by SCADA points and attack labels.

For scoring detectors the publisher strongly recommends the eTaPR metric. The data served two competitions, HAICon 2020 and HAICon 2021, and is obtained with git clone, using Git LFS from HAI 22.04 onward.

## References

- [GitHub repository](https://github.com/icsdataset/hai)
- [Industrial Atlas page](https://www.indatlas.com/datasets/hai-security-dataset/)

[⬅️ Back to Index](../README.md)
