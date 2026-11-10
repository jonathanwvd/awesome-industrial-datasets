# DiTEC-WDN

Machine-generated hydraulic scenarios for 36 water distribution networks, each with 1,000 scenarios stored as time series of directed graphs.

- **Domain:** Water and utilities
- **Asset / Process:** Water treatment and distribution
- **Modality:** Time series
- **Task:** Forecasting
- **Source Type:** Simulation
- **Access:** Hugging Face
- **Size:** 36 networks with 1,000 scenarios each
- **Year:** 2025
- **License:** CC BY

## Description

DiTEC-WDN is a collection of hydraulic scenarios for water distribution networks, described in a 2025 article in Scientific Data. The work is funded by the DiTEC project on digital twins for water networks (NWO 19454). The simulation metadata files (.INP) were collected from public resources; their hydraulic values were dropped and then re-synthesized by the authors' generator, so the data holds nothing from real systems.

The collection covers 36 networks, and every network has 1,000 scenarios with distinct characteristics. A scenario is a time series of directed graphs that share one topology, called states or snapshots. Nodes stand for reservoirs, junctions or tanks, and edges for pipes, pumps or valves. Configurations are named after the network, storage size, duration and component type.

On Hugging Face the data is tagged for graph machine learning and time-series forecasting. It is released under CC BY 4.0.

## References

- [Hugging Face dataset](https://huggingface.co/datasets/rugds/ditec-wdn)
- [nature.com](https://www.nature.com/articles/s41597-025-06026-0)
- [GitHub repository](https://github.com/DiTEC-project/DiTEC_WDN_dataset)
- [Industrial Atlas page](https://www.indatlas.com/datasets/ditec-wdn/)

[⬅️ Back to Index](../README.md)
