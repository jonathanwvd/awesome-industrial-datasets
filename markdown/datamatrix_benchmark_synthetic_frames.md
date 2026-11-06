# DataMatrix readers on synthetic production-line frames

**Summary:** Synthetic test set of 1368 greyscale frames of DataMatrix codes that imitate a conveyor camera, each paired with its expected decoded string.

| Parameter | Value |
| --- | --- |
| **Domain** | Manufacturing |
| **Asset / Process** | — |
| **Modality** | Image |
| **Task** | Other |
| **Annotation** | Text and QA label |
| **Source Type** | Synthetic |
| **Access** | Code repository |
| **Size** | 1368 frames (PNG) |
| **Year** | 2026 |
| **License** | CC0 and public domain |
| **Publisher** | libscanner |

## Description

The set consists of 1368 synthetic images of DataMatrix (ECC 200) symbols, rendered to imitate a camera mounted over a conveyor. It is published by libscanner, the developer of the dmr reader, as the test data of an open comparison between dmr, zxing-cpp, ZXing and libdmtx. The symbols are produced with its own dmgen generator.

Each frame is a 720×540 greyscale image with one code on a white label, placed on a grey background under uneven light. Starting from nominal settings, one condition is changed at a time across 16 conditions, among them module size, rotation, blur, tilt, damage, and curved or crumpled labels. Every point holds 12 frames that cycle through 16×16, 22×22 and 40×40 symbols filled with random digits, and every frame comes with its expected string.

The frames ship as a ZIP archive in the v1 release on GitHub, and the generation script rebuilds the same set from a fixed seed. Frames and expected strings are released under CC0 1.0; the scripts and programs use MIT No Attribution.

## References

- [GitHub repository](https://github.com/libscanner/datamatrix-benchmark)
- [GitHub repository](https://github.com/libscanner/datamatrix-benchmark/releases/tag/v1)
- [Industrial Atlas page](https://www.indatlas.com/datasets/datamatrix-benchmark-synthetic-frames/)

[⬅️ Back to Index](../README.md)
