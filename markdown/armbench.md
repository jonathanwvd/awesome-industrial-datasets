# ARMBench

Images, videos and tabular data from Amazon warehouse robots, annotated for five tasks including object segmentation, object identification and defect detection.

- **Domain:** Logistics and retail
- **Asset / Process:** Robots and manipulators
- **Modality:** Image; Video; Tabular
- **Task:** Defect detection; Other
- **Source Type:** Real production
- **Access:** Hugging Face
- **Size:** 6 dataset repositories covering 5 tasks
- **Year:** 2023
- **License:** CC BY
- **Publisher:** Amazon

## Description

ARMBench is a collection of datasets for perception and manipulation problems in Amazon Robotics systems, recorded in Amazon warehouses across a wide range of objects and configurations. It holds images, videos and tabular data from several stages of robotic manipulation, together with annotations. The paper on the first release was accepted at ICRA 2023, and a 2025 arXiv paper describes the stow data.

The data comes from two Amazon Robotics programs. Sparrow detects, selects and handles individual products in inventory; its datasets, released in March 2023, cover object segmentation, object identification and defect detection. Vulcan Stow places items into fabric-covered pods divided into compartments, sensing contact through force feedback. Its datasets add stow success prediction, released in August 2025, and blade insertion affordance prediction, released in June 2026 with about 29,000 cycles of RGBD images and 3D motion trajectories.

The five tasks are published on Hugging Face under the Amazon organization as six dataset repositories, licensed under CC BY 4.0.

## References

- [Official page](https://armbench.com/)
- [Industrial Atlas page](https://www.indatlas.com/datasets/armbench/)

[⬅️ Back to Index](../README.md)
