# Milling Wear

**Summary:** NASA milling machine tool wear dataset with 16 experiments across varying speeds, feeds, and depths of cut; records spindle motor currents, vibrations, and acoustic emission alongside flank wear (VB) measurements for tool wear prediction research.

| Parameter | Value |
| --- | --- |
| **Dataset** | Milling Wear |
| **Domain** | Manufacturing & Production |
| **Asset / Process** | CNC / Machining |
| **Modality** | Time Series; Vibration; Audio |
| **Task** | RUL / Prognostics; Condition Monitoring; Regression |
| **Annotation** | RUL Label; Scalar Target |
| **Source Type** | Real Lab / Testbed |
| **Access** | Kaggle; Login Required |
| **Size** | 16 experimental cases with 167 total measurement runs; ~15 MB compressed |
| **Year** | 2007 |
| **License** | Information not available |

## Description

The NASA Milling Wear dataset (Agogino & Goebel, 2007) was collected at the UC Berkeley Emergent Space Tensegrities (BEST) Lab and contributed to NASA's Prognostics Center of Excellence Data Repository. Experiments were conducted on a milling machine under 16 different combinations of cutting speed, feed rate, material type, and depth of cut. For each case, multiple experimental runs were recorded with measurements taken at irregular intervals.

Six sensor channels are recorded synchronously: two spindle motor current signals (AC and DC), two vibration signals (table and spindle), and two acoustic emission signals (table and spindle). Additionally, the flank wear measurement (VB) of the milling insert is recorded at irregular intervals throughout the experiments. Operational parameters (depth of cut, feed, material type) are also stored. Data is provided in MATLAB struct array format (.mat), with a CSV version also available on Kaggle.

The primary task is to predict milling insert flank wear (VB) from the sensor signals, supporting preventive maintenance and remaining useful life estimation for cutting tools. This dataset has been widely used for tool condition monitoring research.

## References

- [NASA Open Data Portal - Milling Wear](https://data.nasa.gov/dataset/milling-wear)
- [NASA PCoE Data Repository](https://www.nasa.gov/intelligent-systems-division/discovery-and-systems-health/pcoe/pcoe-data-set-repository/)
- [Agogino & Goebel (2007) - Original citation](https://data.phmsociety.org/nasa/)

[⬅️ Back to Index](../README.md)
