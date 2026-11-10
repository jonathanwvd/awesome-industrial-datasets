# Grid2Op

Python platform from RTE France that simulates power grid operation for sequential decision making and reinforcement learning, and runs the L2RPN competitions.

- **Domain:** Energy and power
- **Asset / Process:** Power grids and plants
- **Modality:** Simulator
- **Task:** Simulation and control
- **Source Type:** Simulation
- **Access:** Code repository
- **Year:** 2020
- **Publisher:** RTE France

## Description

Grid2Op (Grid To Operate) is a modular Python platform for operating a power grid in simulation, copyrighted by RTE France. It serves as the library behind the Learning To Run a Power Network (L2RPN) competitions and is used in reinforcement learning research on power systems. It is cited as a 2020 software release by B. Donnot.

The platform emulates grids of any size, provided a backend is implemented, with AC or DC power flow. Its default solver is PandaPower, and lightsim2grid, powsybl and PowerModels backends are available. The framework supports operations from changing generator setpoints and load values to load shedding, maintenance, storage units, redispatching and curtailment, and topology changes beyond connecting or disconnecting lines. Maintenance, hazards and attacks act as external events that can disconnect powerlines.

The interface follows gymnasium, and a Runner class assesses how well an agent performs. Grid2Op installs from PyPI or Docker and is released under the Mozilla Public License (MPL) v2.

## References

- [GitHub repository](https://github.com/Grid2Op/grid2op)
- [grid2op.readthedocs.io](https://grid2op.readthedocs.io/)
- [Industrial Atlas page](https://www.indatlas.com/datasets/grid2op/)

[⬅️ Back to Index](../README.md)
