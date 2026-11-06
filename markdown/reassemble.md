# REASSEMBLE

Teleoperated robot demonstrations of assembly and disassembly on the NIST Assembly Task Board 1, with force-torque, event camera, audio and RGB video data.

- **Domain:** Robotics and automation
- **Asset / Process:** Robots and manipulators
- **Modality:** Multimodal; Video; Time series
- **Task:** Classification
- **Annotation:** Text and QA label
- **Source Type:** Lab or testbed
- **Access:** Official portal
- **Size:** 4,551 demonstrations
- **Year:** 2025

## Description

REASSEMBLE (Robotic assEmbly disASSEMBLy datasEt) is a multimodal dataset of contact-rich robotic manipulation on the NIST Assembly Task Board 1, distributed through TUData and presented at Robotics: Science and Systems 2025. After the board and object poses are randomized, a human operator drives the robot remotely through assembly and disassembly, narrating each action and marking segment boundaries with key presses.

The 4,551 demonstrations, 4,035 of them successful, span 781 minutes and cover four actions (pick, insert, remove and place) on 17 objects. Recordings combine robot proprioception, force-torque readings, event camera data, microphone audio and multi-view RGB video, stored in HDF5 without downsampling, with raw timestamps. JSON files hold the camera and board poses, measured by motion capture only at the beginning, since continuous tracking interferes with the event camera.

Action segments are labelled at two hierarchical levels, each with start and end times, a success flag and a natural language description. They support temporal action segmentation, motion policy learning, anomaly detection and task inversion. Text files list the training and validation recordings; MIT-licensed GitHub code loads, visualizes and converts them.

## References

- [DOI](https://doi.org/10.48436/0ewrv-8cb44)
- [tuwien-asl.github.io](https://tuwien-asl.github.io/REASSEMBLE_page/)
- [GitHub repository](https://github.com/TUWIEN-ASL/REASSEMBLE)
- [Industrial Atlas page](https://www.indatlas.com/datasets/reassemble/)

[⬅️ Back to Index](../README.md)
