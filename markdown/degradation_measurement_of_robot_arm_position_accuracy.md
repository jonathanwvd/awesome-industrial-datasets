# Degradation Measurement of Robot Arm Position Accuracy

**Summary:** Tool center position errors and 125 Hz joint controller data from a UR5 robot arm run under varied temperature, payload and speed, published by NIST.

| Parameter | Value |
| --- | --- |
| **Domain** | Robotics and automation |
| **Asset / Process** | Robots and manipulators |
| **Modality** | Time series |
| **Task** | Condition monitoring |
| **Annotation** | — |
| **Source Type** | Lab or testbed |
| **Access** | Direct download |
| **Size** | — |
| **Year** | 2017 |
| **License** | — |
| **Publisher** | National Institute of Standards and Technology |

## Description

Degradation Measurement of Robot Arm Position Accuracy is a NIST dataset on the positional health of a Universal Robot UR5 arm. It supports work on monitoring, diagnostics and prognostics (PHM) of robot accuracy and is linked to papers by G. Qiao, B. A. Weiss and C. Schlenoff from the 2017 ASME manufacturing conference and IEEE ICRA 2017.

The arm follows a programmed trajectory that stops at randomly selected points in its workspace under different temperatures, payloads and speeds. A 7-D measurement system built at NIST records the tool center position (x, y, z), and its differences from the nominal positions given by the kinematic parameters are stored. Controller data from each joint, collected at 125 Hz, add positions, velocities, currents, accelerations, torques and temperatures.

The controller CSV files cover half and full speed with 1.6 lb and 4.5 lb payloads, three tests each, plus cold-start runs with 4.5 lb. In one case the joints started near 25 degrees Celsius and reached about 35 after two hours.

## References

- [Official page](https://www.nist.gov/el/intelligent-systems-division-73500/degradation-measurement-robot-arm-position-accuracy)
- [data.nist.gov](https://data.nist.gov/od/id/754A77D9DA1E771AE0532457068179851962)
- [nist.gov](https://www.nist.gov/publications/accuracy-degradation-analysis-industrial-robot-systems)
- [Industrial Atlas page](https://www.indatlas.com/datasets/degradation-measurement-of-robot-arm-position-accuracy/)

[⬅️ Back to Index](../README.md)
