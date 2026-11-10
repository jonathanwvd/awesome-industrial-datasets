# MixedWM38

About 38,000 wafer maps from die probe tests in 38 single and mixed defect patterns, partly generated with a GAN to balance the classes.

- **Domain:** Electronics and semiconductors
- **Asset / Process:** Semiconductor wafers and process tools
- **Modality:** Image
- **Task:** Classification
- **Annotation:** Class label
- **Source Type:** Mixed
- **Size:** About 38,000 wafer maps
- **Year:** 2020

## Description

MixedWM38 is a wafer map dataset for recognising mixed-type defect patterns, published on GitHub with a paper by J. Wang and co-authors on deformable convolutional networks in IEEE Transactions on Semiconductor Manufacturing. The maps were collected in a wafer manufacturing plant by testing the electrical performance of each die with probes.

The real maps were unevenly spread over the patterns, so a generative adversarial network generated additional maps to balance them, for a total of about 38,000. The 38 patterns are one normal pattern, 8 single defect patterns and 29 mixed ones that combine two, three or four basic defects.

Each map is a 52 × 52 array in which 0 marks a blank spot, 1 a die that passed the electrical test and 2 a die that failed it. Labels are one-hot vectors over the 8 basic defect types, C2 to C9; Uzma Batool of the University of Technology Malaysia corrected the C7 and C9 labels. The data are downloadable from Kaggle, Google Drive and Baidu.

## References

- [GitHub repository](https://github.com/Junliangwangdhu/WaferMap)
- [Industrial Atlas page](https://www.indatlas.com/datasets/mixedwm38-wafer-maps/)

[⬅️ Back to Index](../README.md)
