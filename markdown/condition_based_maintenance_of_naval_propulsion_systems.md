# Condition Based Maintenance of Naval Propulsion Systems

**Summary:** Data have been generated from a sophisticated simulator of a Gas Turbines (GT), mounted on a Frigate characterized by a COmbined Diesel eLectric And Gas (CODLAG) propulsion plant type.

| Parameter | Value |
| --- | --- |
| **Dataset** | Condition Based Maintenance of Naval Propulsion Systems |
| **Domain** | Energy & Power; Aerospace & Defense |
| **Asset / Process** | Gears / Gearboxes; Turbines / Engines |
| **Modality** | Tabular |
| **Task** | Regression; RUL / Prognostics; Predictive Maintenance; Simulation / Control |
| **Annotation** | Scalar Target |
| **Source Type** | Simulation |
| **Access** | UCI |
| **Size** | 11934 |
| **Year** | 2014 |
| **License** | Information not available |

## Description

The experiments have been carried out by means of a numerical simulator of a naval vessel (Frigate) characterized by a Gas Turbine (GT) propulsion plant. The different blocks forming the complete simulator (Propeller, Hull, GT, Gear Box and Controller) have been developed and fine tuned over the year on several similar real propulsion plants. In view of these observations the available data are in agreement with a possible real vessel.

In this release of the simulator it is also possible to take into account the performance decay over time of the GT components such as GT compressor and turbines. The propulsion system behaviour has been described with this parameters: - Ship speed (linear function of the lever position lp). - Compressor degradation coefficient kMc. - Turbine degradation coefficient kMt. so that each possible degradation state can be described by a combination of this triple (lp,kMt,kMc). The range of decay of compressor and turbine has been sampled with an uniform grid of precision 0.001 so to have a good granularity of representation.

In particular for the compressor decay state discretization the kMc coefficient has been investigated in the domain [1; 0.95], and the turbine coefficient in the domain [1; 0.975]. Ship speed has been investigated sampling the range of feasible speed from 3 knots to 27 knots with a granularity of representation equal to tree knots. A series of measures (16 features) which indirectly represents of the state of the system subject to performance decay has been acquired and stored in the dataset over the parameter's space. Check the README.txt file for further details about this dataset.

## References

- [UCI Machine Learning Repository Citation](https://doi.org/10.24432/C5K31K)
- [UCI Machine Learning Repository Dataset Page](https://archive.ics.uci.edu/ml/datasets/Condition+Based+Maintenance+of+Naval+Propulsion+Plants#)

[⬅️ Back to Index](../README.md)
