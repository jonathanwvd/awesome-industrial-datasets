# CiP-DMD

Machine signals, metadata and quality measurements from a multi-stage process that machines piston rods and cylinder bottoms and assembles them into cylinders.

- **Domain:** Manufacturing
- **Asset / Process:** CNC machining and tool wear
- **Modality:** Time series; Vibration
- **Task:** Quality prediction; Fault diagnosis; Anomaly detection
- **Annotation:** Class label; Sample label; Scalar target
- **Access:** Code repository
- **Year:** 2023

## Description

CiP-DMD (Center for industrial Productivity Discrete Manufacturing Dataset) is a machine learning dataset from discrete manufacturing, released with an article for Procedia CIRP by Nicolas Jourdan, Tobias Biegel, Beatriz Bretones Cassoli and Joachim Metternich. Piston rods are turned on an Index C65 CNC lathe, cylinder bottoms are cut on a Kasto SBA 2 saw and milled on a DMC 50H machine, and both are assembled into cylinders.

Process data is stored in HDF5. Sawing, turning and milling each have internal PLC signals; milling adds accelerometer signals, and some milling folders add Pro-Micron spike sensory tool holder signals. CSV files map timestamps to milling subprocesses. Per-component JSON metadata links process data, start and end times, an anomaly class and quality measurements with pass flags.

Two of the most common errors behind faulty cylinder bottoms, misaligned raw material at the saw and uneven clamping in the milling jig, were provoked on purpose and form anomaly classes; a third marks miscellaneous errors not visible in process data. Unassembled piston rods with uneven edges may be used for an additional anomaly detection task.

## References

- [GitHub repository](https://github.com/HannesJoern/interq_data_acquisition_public)
- [Industrial Atlas page](https://www.indatlas.com/datasets/cip-dmd/)

[⬅️ Back to Index](../README.md)
