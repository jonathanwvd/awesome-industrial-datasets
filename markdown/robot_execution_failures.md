# Robot Execution Failures

Force and torque readings taken on a robot right after failure detection, 463 instances split into five learning problems with a class per failure.

- **Domain:** Robotics and automation
- **Asset / Process:** Robots and manipulators
- **Modality:** Time series
- **Task:** Classification
- **Annotation:** Class label
- **Access:** UCI repository
- **Size:** 463 instances
- **Year:** 1999
- **License:** CC BY

## Description

Robot Execution Failures holds force and torque measurements recorded on a robot after a failure has been detected. It was created by Luis Lopes and Luis Camarinha-Matos and donated to the UCI Machine Learning Repository in 1999.

The donation has five datasets, each a different learning problem: failures in approach to grasp position (LP1), failures in transfer of a part (LP2), position of a part after a transfer failure (LP3), failures in approach to ungrasp position (LP4) and failures in motion with a part (LP5).

Each of the 463 instances has a class and 15 force/torque samples taken at regular intervals over a 315 ms window, giving 90 integer-valued features: Fx, Fy, Fz, Tx, Ty and Tz at each step. There are no missing values. The task is classification, and the data is released under CC BY 4.0.

## References

- [DOI](https://doi.org/10.24432/C5M89N)
- [UCI Machine Learning Repository](https://archive.ics.uci.edu/dataset/138/robot+execution+failures)
- [Industrial Atlas page](https://www.indatlas.com/datasets/robot-execution-failures/)

[⬅️ Back to Index](../README.md)
