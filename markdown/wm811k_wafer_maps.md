# WM811K Wafer Maps

**Summary:** Large-scale real wafer map dataset from TSMC with 811,457 wafer maps (172,950 labeled) covering 9 failure pattern classes; standard benchmark for semiconductor yield diagnosis and defect pattern recognition.

| Parameter | Value |
| --- | --- |
| **Associated Tasks** | Defect Pattern Classification, Failure Mode Recognition |
| **Data Source** | Real |
| **Dataset Characteristics** | Image, Multiclass |
| **Date Donated** | 2014 |
| **Feature Type** | Image (wafer map binary/ternary maps) |
| **Labeled** | Yes |
| **Missing Values** | No |
| **Name** | WM811K Wafer Maps |
| **Number of Features** | Variable-size binary/ternary wafer maps encoding die pass/fail status on a 2D grid |
| **Number of Instances** | 811,457 wafer maps total; 172,950 labeled across 9 classes; 638,507 unlabeled |
| **Source** | TSMC / MIR Lab (Ming Chuan University) |
| **Time Series** | No |

## Description

The WM-811K dataset (also called WM811K) contains 811,457 real wafer maps collected from TSMC (Taiwan Semiconductor Manufacturing Company) production lines, contributed by Ming-Ju Wu, Jyh-Shing Roger Jang, and Jui-Long Chen. Each wafer map encodes the pass/fail test results of individual dies on a silicon wafer as a 2D grid (ternary values: pass, fail, edge die).

Of the 811,457 maps, 172,950 have been manually labeled into one of 9 failure pattern categories:
1. Center — failures concentrated in the center
2. Donut — ring-shaped failure pattern
3. Edge-Loc — edge localized failures
4. Edge-Ring — full ring around edge
5. Loc — localized cluster of failures
6. Near-Full — nearly all dies failed
7. Random — random distributed failures
8. Scratch — linear scratch pattern
9. None — no apparent pattern

The remaining 638,507 maps are unlabeled and can be used for semi-supervised or unsupervised learning. The dataset is available under a CC0 (public domain) license. It is a standard benchmark for yield diagnosis, failure mode classification, and transfer learning in semiconductor manufacturing.

## Tags

CC0, Defect Pattern, Failure Mode Classification, Large-scale, Semi-supervised Learning, Semiconductor Manufacturing, TSMC, Wafer Map, Yield Diagnosis

## References

- [IEEE Transactions on Semiconductor Manufacturing - WM-811K Paper (2014)](https://doi.org/10.1109/TSM.2014.2364237)
- [MIR Lab Dataset Page](http://mirlab.org/dataSet/public/)
- [Kaggle Mirror](https://www.kaggle.com/datasets/qingyi/wm811k-wafer-map)

[⬅️ Back to Index](../README.md)
