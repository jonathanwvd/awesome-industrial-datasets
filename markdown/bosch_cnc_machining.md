# CNC Machining Data

Tri-axial vibration recordings at 2 kHz from three brownfield CNC milling machines running 15 processes, labelled as normal or anomalous over 2018 to 2021.

- **Domain:** Manufacturing
- **Asset / Process:** CNC machining and tool wear
- **Modality:** Vibration
- **Task:** Process monitoring; Classification
- **Annotation:** Sample label
- **Source Type:** Real production
- **Access:** Code repository
- **Size:** 3 machines, 15 processes each
- **License:** CC BY
- **Publisher:** Robert Bosch GmbH

## Description

CNC Machining Data is a set of real-world industrial vibration recordings from brownfield CNC milling machines, published by Robert Bosch GmbH. It is the companion material to a Procedia CIRP paper (volume 107) by Mohamed-Ali Tnani, Michael Feil and Klaus Diepold on a smart data collection system for machine monitoring.

A Bosch CISS tri-axial accelerometer mounted inside each machine records the X, Y and Z axes at 2 kHz. Normal and anomalous data were gathered over 6 timeframes of 6 months each between October 2018 and August 2021, and labelled accordingly. The data covers 3 machines (M01 to M03), each running 15 processes (OP00 to OP14), and each process folder splits its HDF5 files into good and bad examples.

Because the impact of anomalies differs, the data suits studies of model scalability and process variation. Python helpers and a notebook load and plot the files. The data is licensed under CC BY 4.0, and the code under BSD-3-Clause.

## References

- [GitHub repository](https://github.com/boschresearch/CNC_Machining)
- [Industrial Atlas page](https://www.indatlas.com/datasets/bosch-cnc-machining/)

[⬅️ Back to Index](../README.md)
