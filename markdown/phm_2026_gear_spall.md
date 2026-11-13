# PHM North America 2026 Conference Data Challenge

Vibration signals, condition indicators and tooth images from seven accelerated life tests of a spur gear, for estimating spall damage from sensor data alone.

- **Domain:** Manufacturing
- **Asset / Process:** Gears and gearboxes
- **Modality:** Vibration; Image; Time series
- **Task:** Condition monitoring; Regression
- **Annotation:** Unlabeled
- **Source Type:** Lab or testbed
- **Access:** Direct download
- **Size:** Seven accelerated life experiments
- **Year:** 2026
- **Benchmark:** Yes

## Description

The PHM North America 2026 Conference Data Challenge, hosted on the PHM Society data repository, concerns spall damage in gear teeth. Teams estimate damage progression from inexpensive sensor measurements, while close-up images of the tooth surfaces are available only for training. The damage of interest moves from wear to micro-pitting, pitting and spall formation.

In seven accelerated life experiments, A to G, a spur gear with 28 teeth runs in a simple gearbox with a one-to-one ratio until failure, after about 30 to 90 hours. Axial and radial accelerometers and an encoder are sampled at 102.4 kHz, and torque, speed and temperature at 1 Hz. One-minute HDF5 files also hold condition indicators such as FM4, NA4, M6a and ALR, time synchronous averages and in-line oil sensor data.

Three experiments are for training, with images of all 28 teeth at 6-hour intervals, and two each for test and validation. No ground truth is shared: teams derive damage labels from the images, and predicted trajectories are scored by mean squared error after an optimal monotonic rescaling.

## References

- [Official page](https://data.phmsociety.org/phm-north-america-2026-conference-data-challenge/)
- [Industrial Atlas page](https://www.indatlas.com/datasets/phm-2026-gear-spall/)

[⬅️ Back to Index](../README.md)
