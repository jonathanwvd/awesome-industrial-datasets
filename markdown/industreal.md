# IndustReal

**Summary:** 84 egocentric HoloLens 2 videos of 27 participants assembling and maintaining a construction-toy model, labelled for procedure steps, actions and assembly states.

| Parameter | Value |
| --- | --- |
| **Domain** | Manufacturing |
| **Asset / Process** | — |
| **Modality** | Video; RGB-D and depth; Multimodal |
| **Task** | Classification; Object detection |
| **Annotation** | Class label; Bounding box |
| **Source Type** | Lab or testbed |
| **Access** | Direct download |
| **Size** | 84 videos from 27 participants |
| **Year** | 2023 |
| **License** | — |
| **Publisher** | Eindhoven University of Technology |

## Description

IndustReal is a dataset of egocentric videos in which participants carry out maintenance and assembly procedures on a 3D-printed construction-toy set based on STEMFIE parts. It accompanies a paper by Schoonbeek et al. on procedure step recognition with execution errors, presented at the 2024 IEEE/CVF Winter Conference on Applications of Computer Vision. Eindhoven University of Technology has published the data as zip and tar files on 4TU.ResearchData since October 2023.

The 84 videos show 27 participants and were recorded with a Microsoft HoloLens 2. Each recording holds RGB frames at 1080x720 and 10 FPS, left and right grayscale stereo frames at 640x480, colormapped depth and ambient light frames at 5 FPS, and gaze, hand and head pose tracking.

Labels cover action segments with start and end frames, assembly states in COCO format, and completed procedure steps, including wrongly executed ones. For action recognition the authors publish train, validation and test splits, and a significant part of the procedural and execution errors appears only in the validation and test sets. The release adds the 3D part geometries and trained model weights.

## References

- [GitHub repository](https://github.com/TimSchoonbeek/IndustReal)
- [data.4tu.nl](https://data.4tu.nl/datasets/b008dd74-020d-4ea4-a8ba-7bb60769d224)
- [Industrial Atlas page](https://www.indatlas.com/datasets/industreal/)

[⬅️ Back to Index](../README.md)
