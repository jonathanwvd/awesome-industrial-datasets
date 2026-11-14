# Gym Electric Motor

Python toolbox of Gymnasium environments that simulate electric drive trains, for classical control design and reinforcement learning on motor control.

- **Domain:** Energy and power
- **Asset / Process:** Motors and drives
- **Modality:** Simulator
- **Task:** Simulation and control
- **Source Type:** Simulation
- **Access:** Code repository
- **Year:** 2021
- **License:** MIT
- **Publisher:** Paderborn University

## Description

Gym Electric Motor (GEM) is a Python package for simulating and controlling electric motors, developed at the LEA department of Paderborn University. Built on Farama Gymnasium, it serves both classical control simulation and reinforcement learning. Its overview paper appeared in the Journal of Open Source Software in 2021, and a companion paper on reinforcement learning was published in IEEE Transactions on Neural Networks and Learning Systems.

An environment assembles a drive train from a voltage supply, a converter, an electric motor and a load model, with utilities for reference generation, reward calculation and visualization. Besides DC motor models, it covers permanent magnet synchronous, synchronous reluctance, externally excited synchronous, squirrel cage induction and doubly-fed induction motors. Converters take duty cycles (continuous control set) or switching commands (finite control set).

Any decision-making algorithm can be plugged in, from linear feedback control to DDPG agents, and an automated framework builds PI-based control structures. Example notebooks cover Stable-Baselines3 DDPG and DQN agents and model predictive control. GEM installs from PyPI and is MIT-licensed.

## References

- [GitHub repository](https://github.com/upb-lea/gym-electric-motor)
- [Industrial Atlas page](https://www.indatlas.com/datasets/gym-electric-motor/)

[⬅️ Back to Index](../README.md)
