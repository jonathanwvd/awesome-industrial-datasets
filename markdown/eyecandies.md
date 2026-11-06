# Eyecandies

**Summary:** Synthetic dataset of photo-realistic rendered candies in ten classes for unsupervised anomaly detection and localization, with RGB, depth and normal maps.

| Parameter | Value |
| --- | --- |
| **Domain** | Manufacturing |
| **Asset / Process** | — |
| **Modality** | Image; RGB-D and depth; Multimodal |
| **Task** | Anomaly detection; Anomaly localization |
| **Annotation** | Normal-only training; Pixel mask |
| **Source Type** | Synthetic |
| **Access** | — |
| **Size** | — |
| **Year** | 2022 |
| **License** | — |
| **Publisher** | Eyecan.ai |

## Description

Eyecandies was released by Eyecan.ai with the paper "The Eyecandies Dataset for Unsupervised Multimodal Anomaly Detection and Localization" by Luca Bonfiglioli, Marco Toschi, Davide Silvestri, Nicola Fioraio and Daniele De Gregorio, presented at ACCV 2022.

Each candy is generated procedurally and rendered on a simulated conveyor, lit by four single spotlights, all spotlights together or a global light box, with RGB, depth and surface-normal images. The ten classes include candy cane, gummy bear, lollipop and marshmallow. Key rendering parameters are drawn at random, which spreads the appearance within each class. Defects are inserted during rendering, so their pixel masks are produced automatically.

Training and validation samples are free of anomalies; anomalous samples and their ground truth appear only in the test set. Per-class baseline results cover methods such as PADIM, STFPM and GANomaly, and a leaderboard ranks results on a private test set, with metrics computed from submitted heatmaps. The data is formatted as a Pipelime underfolder.

## References

- [Official page](https://eyecan-ai.github.io/eyecandies/)
- [Industrial Atlas page](https://www.indatlas.com/datasets/eyecandies/)

[⬅️ Back to Index](../README.md)
