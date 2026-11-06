# Industrial Benchmark

**Summary:** Simulation environment for offline and online reinforcement learning with continuous, partially observable states, delayed effects and two opposing reward components.

| Parameter | Value |
| --- | --- |
| **Domain** | Cross-industrial |
| **Asset / Process** | — |
| **Modality** | Time series |
| **Task** | Simulation and control |
| **Annotation** | — |
| **Source Type** | Simulation |
| **Access** | Code repository |
| **Size** | — |
| **Year** | 2017 |
| **License** | Apache 2.0 |

## Description

The Industrial Benchmark is a reinforcement learning environment on GitHub for offline and online RL, meant to find the algorithms best suited to real-world applications. It is documented in "A benchmark environment motivated by industrial control problems" by D. Hein and co-authors, presented at the 2017 IEEE Symposium Series on Computational Intelligence (SSCI).

Its state and action spaces are continuous, and the state space is rather high-dimensional and only partially observable. Actions have three continuous components that act on three steerings, with delayed effects. Two reward components depend on the actions in opposing ways, the dynamics are heteroskedastic with state-dependent noise based on latent variables, and the optimal policy does not settle at a fixed operating point.

Java and Python versions are provided. The Python environment includes an OpenAI Gym compliant wrapper and installs from PyPI as industrial_benchmark_python. The code is licensed under Apache 2.0.

## References

- [GitHub repository](https://github.com/siemens/industrialbenchmark)
- [Industrial Atlas page](https://www.indatlas.com/datasets/openai-gym-industrial-benchmark/)

[⬅️ Back to Index](../README.md)
