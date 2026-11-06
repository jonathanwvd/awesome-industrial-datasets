# Job Shop Scheduling Benchmark: Environments and Instances for Learning and Non-learning Methods

Scheduling environments, problem instances and exact, heuristic and DRL solvers for job shop, flow shop, flexible job shop and online scheduling variants.

- **Domain:** Manufacturing
- **Modality:** Problem instances; Simulator
- **Task:** Scheduling and optimization; Simulation and control
- **Access:** Code repository
- **Year:** 2026
- **Publisher:** AI for Decision Making, TU/e

## Description

This repository from the AI for Decision Making group at TU/e collects environments and problem instances for machine scheduling. It covers job shop (JSP), flow shop (FSP) and flexible job shop scheduling (FJSP), FJSP with assembly constraints, FJSP with sequence-dependent setup times and the online FJSP with jobs arriving during operation.

The data folder holds the problem instances for each variant together with parsers that load them into the scheduling environment, whose core components are jobs, operations, machines and the job shop; a simulation environment handles dynamic problems with online arrivals. Solution methods include MILP and CP-SAT models, dispatching rules, a genetic algorithm and the deep reinforcement learning methods L2D, FJSP-DRL and DANIEL, each compatible with one or more variants.

Plotting functions draw precedence relations and Gantt charts. The work is described in a 2026 article in Annals of Mathematics and Artificial Intelligence, with a preprint on arXiv.

## References

- [GitHub repository](https://github.com/ai-for-decision-making-tue/Job_Shop_Scheduling_Benchmark_Environments_and_Instances)
- [Industrial Atlas page](https://www.indatlas.com/datasets/tue-job-shop-scheduling-benchmark/)

[⬅️ Back to Index](../README.md)
