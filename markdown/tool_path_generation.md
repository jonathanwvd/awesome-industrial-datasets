# Self-optimizing tool path generation for 5-axis machining processes

Measured shape deviations on 5-axis machined pocket walls paired with simulated width of cut, depth of cut, material removal rate and feedrate per probed point.

- **Domain:** Manufacturing
- **Asset / Process:** CNC machining and tool wear
- **Modality:** Tabular
- **Task:** Regression
- **Annotation:** Scalar target
- **Source Type:** Mixed

## Description

This dataset accompanies the paper "Self-optimizing tool path generation for 5-axis machining processes". It pairs measured shape deviations of machined pocket walls with cutting conditions computed by a process-parallel material simulation; the experimental setup is described in the paper.

Each probed point carries the measured deviation in millimetres, the width and depth of cut, the projected distance from the surface point to the tool tip along the tool axis, the material removal rate in cm³/min, the feedrate in m/min, and the X, Y and Z position in workpiece coordinates.

The points come from two pockets, A and B, machined with and without compensation. Pocket A without compensation covers 9 sample parts, with a systematic selection of 128 points on the upper 5-axis wall and 61 on the lower wall plus 50 random points per wall. The other three sets come from 3 sample parts each with 100 random points per wall, and Pocket A with compensation also has the systematic selection.

## References

- [Mendeley Data](https://data.mendeley.com/datasets/smyg6cfwpk/1)
- [Industrial Atlas page](https://www.indatlas.com/datasets/tool-path-generation/)

[⬅️ Back to Index](../README.md)
