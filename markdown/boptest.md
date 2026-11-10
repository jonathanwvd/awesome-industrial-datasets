# BOPTEST

Containerized building emulators with predefined test scenarios and KPI calculation for simulation-based benchmarking of building control strategies.

- **Domain:** Buildings and appliances
- **Asset / Process:** HVAC and building systems
- **Modality:** Simulator
- **Task:** Simulation and control; Energy optimization
- **Source Type:** Simulation
- **Access:** Code repository
- **Year:** 2021
- **Publisher:** International Building Performance Simulation Association (IBPSA)
- **Benchmark:** Yes

## Description

BOPTEST (Building Optimization Performance Tests) is a framework for simulation-based benchmarking of building control strategies, developed within IBPSA Project 1 and now IBPSA Project 2 of the International Building Performance Simulation Association. Its reference paper by D. Blum and co-authors appeared in the Journal of Building Performance Simulation in 2021.

Each test case is a Modelica building model wrapped as an FMU, with boundary conditions such as weather, schedules and energy prices, plus forecasts of them. The released cases include BESTEST Air, BESTEST Hydronic, BESTEST Hydronic Heat Pump, Single Zone Commercial Hydronic, Two Zone Apartment Hydronic, Multizone Residential Hydronic and three Multizone Office variants. Every case has predefined testing scenarios.

Controllers interact through a RESTful HTTP API that advances the simulation, reads measurements and returns key performance indicators, with baseline KPIs from each case's embedded control. BOPTEST runs locally with Docker or Podman or through a public web service, and an OpenAI-Gym interface is available.

## References

- [Official page](https://ibpsa.github.io/project1-boptest/)
- [GitHub repository](https://github.com/ibpsa/project1-boptest)
- [ibpsa.github.io](https://ibpsa.github.io/project1-boptest/testcases/index.html)
- [GitHub repository](https://github.com/ibpsa/project1-boptest/blob/master/license.md)
- [Industrial Atlas page](https://www.indatlas.com/datasets/boptest/)

[⬅️ Back to Index](../README.md)
