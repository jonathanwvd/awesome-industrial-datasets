# Job Shop Scheduling Benchmark: Environments and Instances for Learning and Non-learning Methods

**Summary:** Scheduling environments, problem instances and exact, heuristic and DRL solvers for job shop, flow shop, flexible job shop and online scheduling variants.

| Parameter | Value |
| --- | --- |
| **Dataset** | Job Shop Scheduling Benchmark: Environments and Instances for Learning and Non-learning Methods |
| **Domain** | Manufacturing & Production |
| **Asset / Process** | Information not available |
| **Modality** | Information not available |
| **Task** | Simulation / Control |
| **Annotation** | Information not available |
| **Source Type** | Information not available |
| **Access** | Repository |
| **Size** | Information not available |
| **Year** | 2026 |
| **License** | Information not available |

## Description

This repository from the AI for Decision Making group at TU/e collects environments and problem instances for machine scheduling. It covers job shop (JSP), flow shop (FSP) and flexible job shop scheduling (FJSP), FJSP with assembly constraints, FJSP with sequence-dependent setup times and the online FJSP with jobs arriving during operation.

The data folder holds the problem instances for each variant together with parsers that load them into the scheduling environment, whose core components are jobs, operations, machines and the job shop; a simulation environment handles dynamic problems with online arrivals. Solution methods include MILP and CP-SAT models, dispatching rules, a genetic algorithm and the deep reinforcement learning methods L2D, FJSP-DRL and DANIEL, each compatible with one or more variants.

Plotting functions draw precedence relations and Gantt charts. The work is described in a 2026 article in Annals of Mathematics and Artificial Intelligence, with a preprint on arXiv.

## References

- [GitHub repository](https://github.com/ai-for-decision-making-tue/Job_Shop_Scheduling_Benchmark_Environments_and_Instances)

[⬅️ Back to Index](../README.md)
