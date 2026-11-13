# SyDDD - Synthetic Deep Drawing Dataset

LS-Dyna deep drawing simulations over varied tool geometries and blank holder forces, with meshes, point clouds and per-face sheet thickness of formed parts.

- **Domain:** Manufacturing
- **Modality:** 3D point cloud; Tabular
- **Task:** Other
- **Source Type:** Simulation
- **Access:** Zenodo, Dataverse or Figshare
- **Size:** 2,490 simulation results, 7.4 GB ZIP
- **Year:** 2025
- **License:** CC BY

## Description

SyDDD is a set of numerical deep drawing simulations, run in LS-Dyna, in which the tool geometry and the blank holder force vary. Its authors work at Helmut-Schmidt-Universität Hamburg and Technische Universität Dresden, and it is cited by a 2025 Journal of Physics: Conference Series paper on a data-driven approach to designing deep drawing tools. Funding comes from the DFG through SPP 2422.

Each geometry folder holds die, blank holder and punch files plus one formed part file per blank holder force, all as NumPy archives with triangular meshes and 100,000 sampled surface points. Part files also give the sheet thickness of every triangle. A parameters table lists the 2,490 simulation results with their geometric tool parameters, blank holder force and minimum sheet thickness.

PyTorch loaders read both the point cloud and the mesh form. The 7.4 GB archive is on the DaRUS repository under CC BY 4.0.

## References

- [DOI](https://doi.org/10.18419/DARUS-5158)
- [Industrial Atlas page](https://www.indatlas.com/datasets/synthetic-deep-drawing/)

[⬅️ Back to Index](../README.md)
