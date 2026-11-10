# PC-Gym

Open-source reinforcement learning environments for chemical process control, with constraint and disturbance handling and policy evaluation against NMPC oracles.

- **Domain:** Chemical and process
- **Asset / Process:** Chemical process units
- **Modality:** Simulator
- **Task:** Simulation and control
- **Source Type:** Simulation
- **Access:** Code repository
- **Year:** 2024
- **License:** MIT
- **Benchmark:** Yes

## Description

PC-Gym is an open-source Python tool for building and evaluating reinforcement learning (RL) algorithms in chemical process control. It is described in the 2024 preprint "PC-Gym: Benchmark Environments For Process Control Problems" by Maximilian Bloor and co-authors, and installs from PyPI as pcgym.

The simulated processes include a CSTR, a first order system, a multistage extraction column, nonsmooth control, a crystallisation reactor, a four tank system, a fluidized biofilm sand bed reactor and a photoproduction bioreactor. The models carry nonlinear dynamics, disturbances and constraints, and users can set setpoints, observation and action spaces, constraint handling, disturbance generation and the reward function.

A policy evaluation module computes performance and reproducibility metrics, such as mean and median performance, standard deviation and median absolute deviation, and compares RL policies with a nonlinear model predictive control (NMPC) oracle across scenarios. The code is released under the MIT license.

## References

- [GitHub repository](https://github.com/MaximilianB2/pc-gym)
- [maximilianb2.github.io](https://maximilianb2.github.io/pc-gym/)
- [Preprint (arXiv)](https://arxiv.org/abs/2410.22093)
- [maximilianb2.github.io](https://maximilianb2.github.io/pc-gym/API/evaluation_metrics/)
- [GitHub repository](https://github.com/MaximilianB2/pc-gym/blob/main/LICENSE)
- [Industrial Atlas page](https://www.indatlas.com/datasets/pc-gym/)

[⬅️ Back to Index](../README.md)
