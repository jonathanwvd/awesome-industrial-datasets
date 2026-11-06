# Screening Datasets for Laser Welded Steel-Copper Lap Joints

Definitive screening experiments on laser welded steel-copper lap joints, with 360 evaluated cross sections recording weld metal size and cracking.

- **Domain:** Manufacturing
- **Asset / Process:** Welding
- **Modality:** Tabular
- **Task:** Quality prediction; Regression
- **Annotation:** Sample label; Scalar target
- **Source Type:** Lab or testbed
- **Access:** Mendeley Data
- **Size:** 360 cross sections (version V1)

## Description

Published on Mendeley Data, these tables come from laser welding trials on lap joints with a steel sheet over a copper sheet. A definitive screening design varies six factors at three levels in 18 parameter combinations: laser beam power, welding speed, angular position in the welding direction, focal position, gas flow rate and steel sheet thickness. The setup uses a Trumpf TruDisc 16002 beam source, 1.4301 steel, DHP copper and Argon 5.0 shielding gas.

In V1, every combination was repeated five times and every sheet cut four times, giving 360 cross sections, one per row. Each row holds the weld metal dimensions and a yes/no cracking column; V1.1 adds average crack length and crack count. V2 repeats the trials with adjusted laser power so every combination reaches sufficient weld depth, and gives the average copper weld depth per combination. V2.1 gives copper dilution instead.

V1 does not support precise weld-depth prediction, but its link between cracking and copper weld depth fits a binomial logistic regression. V2 supports estimating factor effects and a simple linear model of weld depth.

## References

- [Mendeley Data](https://data.mendeley.com/datasets/2s5m3crbkd/2)
- [Industrial Atlas page](https://www.indatlas.com/datasets/laser-welding/)

[⬅️ Back to Index](../README.md)
