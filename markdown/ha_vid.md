# HA-ViD

Multi-view RGB-D videos of people assembling a box of 35 parts common in industrial assembly, with action, tool, collaboration and error annotations.

- **Domain:** Manufacturing
- **Modality:** Video; RGB-D and depth
- **Task:** Other
- **Annotation:** Bounding box
- **Source Type:** Lab or testbed
- **Year:** 2023
- **License:** CC BY-NC

## Description

HA-ViD is a video dataset of people assembling the Generic Assembly Box (GAB), an object designed to stand for real-world industrial assembly. The 250x250x250mm box has 35 standard and non-standard parts commonly found in industrial assembly, needs four standard tools and has three plates with different task precedence and collaboration requirements. A 2023 arXiv paper by Hao Zheng, Regina Lee and Yuqian Lu describes it; CAD files, a bill of materials and instructions for building the box are available.

Three Azure Kinect RGB+D cameras on the assembly workbench film each participant from the left, front and top. Assembly runs in three stages, discovery with minimal exploded views, instruction with detailed steps and practice without instructions, to capture how procedural knowledge is learnt. Temporal labels follow the Human-Robot Shared Assembly Taxonomy (HR-SAT), covering subjects, actions, manipulated and target objects, tools, collaboration status, pauses and errors; subjects, objects and tools also carry frame-by-frame bounding boxes.

The data is benchmarked on four video understanding tasks and licensed under CC BY-NC 4.0.

## References

- [Official page](https://iai-hrc.github.io/ha-vid)
- [Industrial Atlas page](https://www.indatlas.com/datasets/ha-vid/)

[⬅️ Back to Index](../README.md)
