# AssetOpsBench

Benchmark and framework from IBM for evaluating AI agents on industrial asset operations and maintenance scenarios across nine asset classes.

- **Domain:** Cross-industrial
- **Modality:** Text and documents; Time series
- **Task:** Question answering
- **Source Type:** Simulation
- **Access:** Code repository
- **Year:** 2025
- **Publisher:** IBM Research
- **Benchmark:** Yes

## Description

AssetOpsBench, maintained by IBM on GitHub, is a unified framework in which AI agents specific to a domain are built, orchestrated and evaluated, aimed at Industry 4.0 asset operations and maintenance. Its paper, "AssetOpsBench: A Benchmark for Industrial Asset Operations Agents" by D. Patel, S. Lin and colleagues, was accepted at KDD 2026 in the Datasets and Benchmarks Track.

The scenarios cover nine asset classes; the first release, in June 2025, held 141 industrial scenarios, which are also published as a Hugging Face dataset. Agents run multi-step workflows in simulated industrial environments over sensor data, failure modes, alerts and work orders, through five domain MCP servers: IoT, FMSR, TSFM, WO and Vibration. Example tasks include listing the assets of a site and generating a work order for a chiller anomaly.

Agent trajectories are scored by an LLM judge (Llama-4-Maverick-17B) on six criteria for reasoning, execution and data handling. The benchmark also ran the AssetOpsBench-Live competition at CODS 2025, which drew 365 participants and more than 500 agent submissions.

## References

- [GitHub repository](https://github.com/IBM/AssetOpsBench)
- [Industrial Atlas page](https://www.indatlas.com/datasets/assetopsbench/)

[⬅️ Back to Index](../README.md)
