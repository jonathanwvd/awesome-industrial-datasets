# Robot Execution Failures

**Summary:** This dataset contains force and torque measurements on a robot after failure detection. Each failure is characterized by 15 force/torque samples collected at regular time intervals.

| Parameter | Value |
| --- | --- |
| **Name** | Robot Execution Failures |
| **Labeled** | Yes |
| **Time Series** | Yes |
| **Simulation** | No |
| **Missing Values** | No |
| **Dataset Characteristics** | Multivariate, Time-Series |
| **Feature Type** | Integer |
| **Associated Tasks** | Classification |
| **Number of Instances** | 463 |
| **Number of Features** | 90 |
| **Date Donated** | 1999-04-22 |
| **Source** | UCI Machine Learning Repository |

## Dataset Information

The donation includes 5 datasets, each of them defining a different learning problem:

    * LP1: failures in approach to grasp position
    * LP2: failures in transfer of a part
    * LP3: position of part after a transfer failure
    * LP4: failures in approach to ungrasp position
    * LP5: failures in motion with part

In order to improve classification accuracy, a set of five feature transformation strategies (based on statistical summary features, discrete Fourier transform, etc.) was defined and evaluated. This enabled an average improvement of 20% in accuracy. The most accessible reference is [Seabra Lopes and Camarinha-Matos, 1998].

## Tags

Robotics, Failure detection, Force and torque data, Time-series analysis, Machine learning

## References

- [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/Robot+Execution+Failures)

[⬅️ Back to Index](../README.md)
