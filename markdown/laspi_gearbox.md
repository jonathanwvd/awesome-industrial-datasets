# LASPI: Detection and diagnostics of gearbox faults

Current, voltage and vibration recordings from a motor-driven gearbox test bench in France, covering seven bearing and gear health states.

- **Domain:** Manufacturing
- **Asset / Process:** Gears and gearboxes; Bearings
- **Modality:** Vibration; Time series
- **Task:** Fault diagnosis
- **Annotation:** Class label
- **Source Type:** Lab or testbed
- **Access:** Official portal
- **Size:** 84 experiments
- **Year:** 2023
- **Publisher:** Signal and Industrial Process Analysis Laboratory (LASPI)

## Description

The LASPI dataset records an electromechanical drive on a test bench at the Signal and Industrial Process Analysis Laboratory in Roanne, France. An inverter supplies and controls a 1.5 kW three-phase induction motor, which turns a three-shaft gearbox; an electromagnetic brake on the gearbox adds load. The bearings and gears under study sit on the intermediate shaft.

Three current and voltage sensors at the inverter output and an accelerometer close to the studied parts feed National Instruments 9234 cards. Acquisitions last 10 seconds at 25.6 kHz, and the CSV files have seven columns: three phase currents, the vibration signal and three phase voltages.

The page reports 84 experiments over 7 health states: healthy, a gear surface fault, a gear half-tooth breakage, inner and outer bearing ring faults, and two combined faults. Each state runs at three speeds and four load levels. The data was made available in 2023 with two slide files of the bench; the papers listed with it study fault detection from motor current signals.

## References

- [DOI](https://doi.org/10.25666/DATAUBFC-2023-03-06)
- [search-data.ubfc.fr](https://search-data.ubfc.fr/FR-13002091000019-2023-03-06_LASPI-Detection-and-diagnostics-of-gearbox.html)
- [Industrial Atlas page](https://www.indatlas.com/datasets/laspi-gearbox/)

[⬅️ Back to Index](../README.md)
