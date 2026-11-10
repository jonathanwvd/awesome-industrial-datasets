# University of Ottawa Electric Motor Dataset

Vibration, acoustic and temperature signals from eight 3-phase motors, healthy and with seeded faults, at constant and variable speeds, loaded and unloaded.

- **Domain:** Manufacturing
- **Asset / Process:** Motors and drives; Bearings
- **Modality:** Vibration; Audio
- **Task:** Fault diagnosis
- **Annotation:** Class label
- **Source Type:** Lab or testbed
- **Access:** Mendeley Data
- **License:** CC BY
- **Publisher:** University of Ottawa

## Description

The University of Ottawa Electric Motor Dataset (UOEMD-VAFCVS) records vibration and acoustic fault signatures of electric motors under constant and variable speed. It comes from Mert Sehri and Patrick Dumond at the University of Ottawa and is described in a Data in Brief article from 2024.

Eight D396 Marathon Electric 3-phase motors of the same model ran on a SpectraQuest Machinery Fault & Rotor Dynamics Simulator, with faults created by SpectraQuest: rotor unbalance or misalignment, stator winding fault, voltage unbalance and single phasing, bowed rotor, broken rotor bars or faulty bearings. Speeds are 15 Hz or 60 Hz constant, a ramp from 15 to 45 Hz or back down, with and without load.

Three accelerometers, a microphone and a temperature channel were sampled at 42 kHz for 10 seconds, so each file holds 420,000 samples in CSV and MAT format. A four-part label marks the health state, speed and load of each sample. The data serve to train machine learning models for motor fault diagnosis and are released under CC BY 4.0.

## References

- [Mendeley Data](https://data.mendeley.com/datasets/msxs4vj48g)
- [pmc.ncbi.nlm.nih.gov](https://pmc.ncbi.nlm.nih.gov/articles/PMC11636780)
- [Industrial Atlas page](https://www.indatlas.com/datasets/uottawa-motor-vibration-acoustic/)

[⬅️ Back to Index](../README.md)
