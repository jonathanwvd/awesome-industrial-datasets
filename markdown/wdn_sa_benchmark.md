# wdn-sa-benchmark

Python tool and assets that turn EPANET water networks into structural models, with simulated L-TOWN measurements that contain leaks, sensor faults and cyber attacks.

- **Domain:** Water and utilities
- **Asset / Process:** Water treatment and distribution
- **Modality:** Time series
- **Task:** Fault diagnosis; Intrusion detection
- **Source Type:** Simulation
- **Access:** Code repository
- **Year:** 2022

## Description

wdn-sa-benchmark is a Python tool with assets for creating water distribution network examples to benchmark structural analysis diagnosis algorithms. Its EpanetConverter turns an EPANET INP network file into a structural model for a chosen set of pressure sensors, flow sensors and leak locations, optionally with sensor faults, and an example script places sensors and leaks at random.

The repository holds network structures in INP format, including L-TOWN in an original and a skeletonized version, and structural models stored as JSON dictionaries of equations, known and unknown variables and faults. It also holds simulated measurements for the L-TOWN network with leaks, faults and cyber attacks, as XLSX files with YAML files that describe each configuration; they were produced by extending the BattLeDIM code.

Examples read the structural models in Python and compute MSO and MTES sets with faultdiagnosistoolbox, and Matlab examples are included. The repository is licensed under EUPL 1.2.

## References

- [GitHub repository](https://github.com/asztyber/wdn-sa-benchmark)
- [Industrial Atlas page](https://www.indatlas.com/datasets/wdn-sa-benchmark/)

[⬅️ Back to Index](../README.md)
