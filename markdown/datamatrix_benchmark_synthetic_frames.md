# DataMatrix Benchmark Synthetic Frames

**Summary:** Synthetic grayscale frames of DataMatrix (ECC 200) codes on labels over a conveyor, with 16 controlled degradations and the expected decoded string for every frame.

| Parameter | Value |
| --- | --- |
| **Dataset** | DataMatrix Benchmark Synthetic Frames |
| **Domain** | Manufacturing & Production; Logistics & Retail |
| **Asset / Process** | Retail / Logistics Items |
| **Modality** | Image |
| **Task** | Benchmark Suite |
| **Annotation** | Text / QA Label |
| **Source Type** | Synthetic |
| **Access** | Repository; Direct Download |
| **Size** | 1,368 images; 59 MB |
| **Year** | 2026 |
| **License** | CC0 |

## Description

The DataMatrix Benchmark Synthetic Frames set is designed to test how 2D DataMatrix (ECC 200) code readers behave on production-line images used for product marking and traceability. Each 720 x 540 grayscale frame shows one code on a white label against a grey background with uneven lighting, imitating a camera mounted over a conveyor.

Starting from nominal conditions (4 pixels per module, random rotation, high print contrast and low noise), one condition is changed at a time across 16 conditions: module size, in-plane rotation, defocus, motion blur, noise, print contrast, JPEG quality, label tilt, dot gain, data-area damage with and without padding, cylinder bend, wave, crumpled paper, plastic film with folds and glare, and inverted polarity. Each test point has 12 frames using 16 x 16, 22 x 22 and 40 x 40 symbols filled with random digits.

The file expected.csv lists, for every frame, the condition, its value, the symbol size and the encoded string, so a decoder can be scored on correct, missed and wrong reads. The frames and expected strings are released under CC0 as a versioned GitHub release with SHA-256 checksums, and the repository includes MIT-0 measurement scripts and published results for several open-source and commercial readers.

## References

- [datamatrix-benchmark GitHub repository](https://github.com/libscanner/datamatrix-benchmark)
- [Frames release v1](https://github.com/libscanner/datamatrix-benchmark/releases/tag/v1)

[⬅️ Back to Index](../README.md)
