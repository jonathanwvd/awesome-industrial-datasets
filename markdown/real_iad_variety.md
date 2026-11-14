# Real-IAD Variety

Five-view industrial anomaly detection benchmark of 198,950 images over 160 object categories from 28 industries, with pixel-level defect masks.

- **Domain:** Manufacturing
- **Modality:** Image
- **Task:** Anomaly detection; Anomaly localization
- **Annotation:** Pixel mask; Normal-only training
- **Source Type:** Lab or testbed
- **Access:** Hugging Face
- **Size:** 198,950 images
- **Year:** 2026
- **License:** CC BY-NC-SA
- **Benchmark:** Yes

## Description

Real-IAD Variety is an industrial anomaly detection benchmark and the successor of Real-IAD, with about 5.3 times as many object categories. It is described in a 2026 Pattern Recognition article. Its 160 categories span 28 industries, 24 material types and 22 colour variations, and 27 defect types were introduced artificially, drawing on production line experience.

The 198,950 images come from five cameras per sample: one top-down unit at 5,328 by 3,040 pixels and four angled ones. Training holds 3,991 normal samples (19,955 images); testing holds 35,799 samples, of which 3,990 are normal and 31,809 anomalous. Defects carry pixel-level masks.

Results are reported with I-AUROC and P-AUPR for multi-class unsupervised, zero-shot and few-shot methods. Files are on Hugging Face behind a conditions form whose requests are approved automatically, under CC BY-NC-SA 4.0.

## References

- [Official page](https://realiad4ad.github.io/Real-IAD-Variety/)
- [Hugging Face dataset](https://huggingface.co/datasets/Real-IAD/Real-IAD_Variety)
- [Hugging Face dataset](https://huggingface.co/datasets/Real-IAD/Real-IAD_Variety/resolve/main/LICENSE.txt)
- [Industrial Atlas page](https://www.indatlas.com/datasets/real-iad-variety/)

[⬅️ Back to Index](../README.md)
