# ICS Sensor-Attack Dataset

Labelled attacks that corrupt the PLC's own level reading on a water-tank hardware-in-the-loop testbed, with 21 attack primitives in five families.

- **Domain:** OT security
- **Asset / Process:** Control systems and networks
- **Modality:** Time series
- **Task:** Intrusion detection; Classification
- **Annotation:** Event and time label
- **Source Type:** Lab or testbed
- **Year:** 2026
- **License:** CC BY

## Description

The ICS Sensor-Attack Dataset records attacks on the measurement layer of an industrial control system. It was captured on a closed-loop water-tank hardware-in-the-loop testbed and published on figshare by Rishabh Das in 2026.

The attacks corrupt the analog-to-digital converter reading of the level transducer inside the PLC's register space, while the controller itself keeps running normally under bang-bang control. There are 21 distinct corruption primitives grouped into five families: hard saturation, timing-based, slow drift or state-triggered, stealthy scaling, and statistical manipulation. Each attack runs over one contiguous time interval.

The data supports attack detection, anomaly classification and physics-aware monitoring of sensor channels, rather than the network or supervisory layers captured by sets such as SWaT and WADI. It is released under CC BY 4.0.

## References

- [DOI](https://doi.org/10.6084/m9.figshare.33134861)
- [api.figshare.com](https://api.figshare.com/v2/articles/33134861)
- [Industrial Atlas page](https://www.indatlas.com/datasets/ics-sensor-attack-dataset/)

[⬅️ Back to Index](../README.md)
