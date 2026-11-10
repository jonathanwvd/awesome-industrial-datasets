# Production Data Set for Five-Axis CNC Milling with Multiple Changeovers

One-second NC control data from a five-axis milling machine making three products with every changeover between them, labelled by production, changeover and interruption phases.

- **Domain:** Manufacturing
- **Asset / Process:** CNC machining and tool wear
- **Modality:** Time series; Tabular
- **Task:** Process monitoring; Other
- **Annotation:** Event and time label
- **Source Type:** Lab or testbed
- **Access:** Zenodo, Dataverse or Figshare
- **Size:** 52,026 rows, 170 features and ten label sets
- **Year:** 2024
- **License:** CC BY
- **Publisher:** Technical University of Applied Sciences Würzburg-Schweinfurt

## Description

This dataset follows a five-axis milling machine, a Spinner U5-620 with a Siemens 840D-SL control, through production and changeovers. It was recorded over three days in March 2024 in the machine tool laboratory of the Institute of Digital Engineering at the Technical University of Applied Sciences Würzburg-Schweinfurt, and it is described in a Scientific Data paper.

The machine made three products, a keychain, a bottle opener and a coordinate system model, and every one of the six possible changeovers between them was recorded. Five repetitions gave 30 manufacturing sessions and five full changeover matrices. Control data came through a Softing uaGate 840D interface, sent each second when a value changed.

The single CSV file has 52,026 rows with a timestamp, 170 features and ten label sets. Features include door, coolant and program status, feed rate, axis positions and errors, spindle speed, tool data, and current, torque, temperature and power for each axis. Labels mark production, changeover and interruption phases, for modelling the process and human interaction with the machine. The data is on Zenodo under CC BY 4.0.

## References

- [Zenodo record](https://zenodo.org/records/14094887)
- [pmc.ncbi.nlm.nih.gov](https://pmc.ncbi.nlm.nih.gov/articles/PMC12185752/)
- [Industrial Atlas page](https://www.indatlas.com/datasets/five-axis-cnc-milling-changeovers/)

[⬅️ Back to Index](../README.md)
