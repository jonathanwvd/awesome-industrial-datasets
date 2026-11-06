# MVTec MV-ball

Synthetic dataset for multi-view 6D pose estimation of a sphere whose pose only holistic multi-view methods can resolve reliably, with 112,042 training images.

- **Domain:** Robotics and automation
- **Modality:** Image
- **Task:** Pose estimation
- **Source Type:** Synthetic
- **Size:** 112,042 training images
- **Year:** 2026
- **License:** CC BY-NC-SA
- **Publisher:** MVTec

## Description

MVTec MV-ball is a public synthetic dataset from MVTec for evaluating multi-view 6D pose estimation methods. It was introduced with MVTOP, a multi-view transformer-based object pose estimation method by Lukas Ranftl, Felix Brendel, Bertram Drost and Carsten Steger, published in the VISAPP 2026 proceedings.

The object is a blue sphere whose surface carries a red hemisphere and a green hemisphere, set 90 degrees apart. Its pose cannot be determined from views that do not show both, and the dataset contains only such views, so only holistic multi-view methods can resolve the poses reliably. Each scene contains a single ball.

There are 112,042 training images and two evaluation splits: an easy split of 3,853 images, where at least 300 pixels of one hemisphere are visible, and a hard split of 3,458 images, where at least 10 are. The data is released under CC BY-NC-SA 4.0, which does not allow commercial use.

## References

- [Official page](https://www.mvtec.com/company/research/datasets/mvtec-mv-ball)
- [Industrial Atlas page](https://www.indatlas.com/datasets/mvtec-mv-ball/)

[⬅️ Back to Index](../README.md)
