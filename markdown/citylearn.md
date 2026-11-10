# CityLearn

Gymnasium environment for demand response and energy coordination of building communities, with shared scenarios, baseline controllers and KPI scorecards.

- **Domain:** Buildings and appliances
- **Asset / Process:** HVAC and building systems; Batteries; Solar PV
- **Modality:** Simulator
- **Task:** Simulation and control; Energy optimization
- **Source Type:** Simulation
- **Access:** Code repository
- **Year:** 2019
- **License:** MIT
- **Benchmark:** Yes

## Description

CityLearn is an open-source Gymnasium environment for coordinating building energy use, demand response and reinforcement learning control. CityLearn v1.0 introduced the control environment; v2 was described in the Journal of Building Performance Simulation, and v3 in an arXiv preprint.

Version 3 models renewable energy communities with buildings and thermal systems, PV, batteries, electric vehicles and flexible loads, together with electrical limits, local energy sharing, changing members and assets, and data or equipment failures. Public datasets, such as the CityLearn Challenge 2022 set with EVs, download on first use.

Controllers are tested on the same scenarios, interfaces and performance indicators. Built-in baselines such as a business-as-usual agent serve as references, and the KPIs report district cost, grid import, EV departure feasibility and electrical phase violations. The code is distributed under the MIT license.

## References

- [Official page](https://www.citylearn.net/)
- [GitHub repository](https://github.com/citylearn-project/CityLearn)
- [citylearn.net](https://www.citylearn.net/publications.html)
- [Industrial Atlas page](https://www.indatlas.com/datasets/citylearn/)

[⬅️ Back to Index](../README.md)
