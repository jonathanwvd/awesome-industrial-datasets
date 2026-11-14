# Valeo Anomaly Dataset (VAD)

Production-line images of one part class with 2,000 real defective samples spread over more than 20 defect subclasses, released with the SegAD method.

- **Domain:** Manufacturing
- **Modality:** Image
- **Task:** Defect detection
- **Source Type:** Real production
- **Access:** Direct download
- **Size:** 5,000 images
- **Year:** 2024
- **Benchmark:** Yes

## Description

The Valeo Anomaly Dataset (VAD) is an image set for visual inspection whose pictures all come from a real production line. It was released with the CVPR 2024 paper by Aimira Baitieva, David Hurych, Victor Besnier and Olivier Bernard that also introduces the SegAD (Segmentation-based Anomaly Detector) method.

The 5,000 images form a single class and include 2,000 real defective samples covering more than 20 defect subclasses, from obvious to very subtle. Training holds 1,000 bad and 2,000 good images; testing holds 1,000 bad and 1,000 good images, and 165 of the bad test images show rare defect types that never appear in training. The folder structure is similar to that of MVTec AD.

Unlike most anomaly detection sets, VAD gives defective examples for training, so it suits supervised and low-shot defect detection; a script builds the low-shot training split. The archive downloads from Google Drive, and the Anomalib library loads the one-class version.

## References

- [GitHub repository](https://github.com/abc-125/segad)
- [Preprint (arXiv)](https://arxiv.org/abs/2405.04953)
- [Industrial Atlas page](https://www.indatlas.com/datasets/valeo-anomaly-dataset/)

[⬅️ Back to Index](../README.md)
