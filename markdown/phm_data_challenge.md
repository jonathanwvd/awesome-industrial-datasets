# PHM Data Challenge

Plant sensor, control reference and fault event logs from the 2015 PHM competition on detecting plant faults and localizing them in time.

- **Domain:** Manufacturing
- **Modality:** Time series
- **Task:** Fault diagnosis; RUL and prognostics
- **Annotation:** Event and time label; Class label
- **Access:** Competition
- **Size:** About thirty training plants and ten test plants
- **Year:** 2015
- **Benchmark:** Yes

## Description

The PHM Data Challenge was the competition of the PHM 2015 Conference, focused on fault detection and prognostics in industrial plant monitoring. Teams were scored on detecting plant faults from a set of possible faults and on localizing them in time, with the aim of predicting future failure events of types 1 to 5 and when they occur.

Each plant comes as three CSV files: per-component sensors S1 to S4 and control references R1 to R4, per-zone cumulative energy E1 and instantaneous power E2, and fault events with start time, end time and fault code. Code 6 groups the faults not in focus. Samples arrive about every 15 minutes over roughly three to four years.

Training data covers about thirty plants and test data about ten, and the second half of each test fault file is incomplete. A score rewards detections within one hour of the true fault time and penalizes false positives and false negatives.

## References

- [Official page](https://phmsociety.org/conference/annual-conference-of-the-phm-society/annual-conference-of-the-prognostics-and-health-management-society-2015/phm-data-challenge-3/)
- [Industrial Atlas page](https://www.indatlas.com/datasets/phm-data-challenge/)

[⬅️ Back to Index](../README.md)
