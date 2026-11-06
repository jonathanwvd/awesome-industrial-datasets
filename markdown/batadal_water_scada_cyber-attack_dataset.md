# BATADAL Water SCADA Cyber-Attack Dataset

**Summary:** Hourly SCADA data from a simulated water distribution network, C-Town, split into attack-free, partially labelled and unlabelled sets for comparing attack detectors.

| Parameter | Value |
| --- | --- |
| **Domain** | OT security |
| **Asset / Process** | Control systems and networks; Water treatment and distribution |
| **Modality** | Time series |
| **Task** | Intrusion detection |
| **Annotation** | Event and time label; Unlabeled |
| **Source Type** | Simulation |
| **Access** | Direct download |
| **Size** | Three hourly SCADA datasets |
| **Year** | 2016 |
| **License** | — |
| **Benchmark** | Yes |

## Description

BATADAL is a set of hourly historical SCADA operations data for C-Town, a simulated water distribution network, released for the BATADAL attack detection competition. The reference paper, "The Battle Of The Attack Detection Algorithms: Disclosing Cyber Attacks On Water Distribution Networks" by Riccardo Taormina, Stefano Galelli, Nils Ole Tippenhauer and many co-authors, appeared in the Journal of Water Resources Planning and Management in August 2018.

Training Dataset 1, released on 20 November 2016, comes from a one-year simulation of normal operation with no attacks. Training Dataset 2, released on 28 November 2016, is about six months long and holds several attacks, some approximately labelled, with a list of the attacks. The Test Dataset, released on 20 February 2017, spans three months with several attacks but no labels. Flows are in litres per second; pressures and water levels are in metres.

The Test Dataset is used to compare the performance of detection algorithms. Two earlier competition sets, formerly Dataset 1 and Dataset 2, were withdrawn because their demand patterns differed from the test data.

## References

- [Official page](https://www.batadal.net/data.html)
- [Industrial Atlas page](https://www.indatlas.com/datasets/batadal-water-scada-cyber-attack-dataset/)

[⬅️ Back to Index](../README.md)
