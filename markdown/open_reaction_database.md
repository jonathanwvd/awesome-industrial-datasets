# Open Reaction Database

**Summary:** Open-access chemical reaction database with over 1 million reactions, designed to support machine learning for reaction prediction, synthesis planning, and experiment design; uses Protocol Buffers schema and CC BY 4.0 license.

| Parameter | Value |
| --- | --- |
| **Associated Tasks** | Reaction Prediction, Retrosynthesis, Chemical Synthesis Planning, Yield Prediction, Experiment Design |
| **Data Source** | Real |
| **Dataset Characteristics** | Structured Chemical Reaction Data |
| **Date Donated** | 2021 |
| **Feature Type** | Mixed (SMILES strings, numerical reaction conditions, categorical) |
| **Labeled** | Yes |
| **Missing Values** | No |
| **Name** | Open Reaction Database |
| **Number of Features** | Per reaction: reactants, reagents, solvents, catalysts (as SMILES/InChI), conditions (temperature, pressure, time), yield, provenance, and references; stored in Protocol Buffers schema |
| **Number of Instances** | Over 1 million chemical reactions (growing community-contributed database) |
| **Source** | Open Reaction Database (ORD) Consortium — pharma, academia, and tech |
| **Time Series** | No |

## Description

The Open Reaction Database (ORD) is an open-access, community-driven chemical reaction database established in 2019 by a consortium of experts from the pharmaceutical industry, academia, and technology sector. It was created to address the lack of standardized, machine-readable repositories for chemical reaction data.

The database stores chemical reactions using a Protocol Buffers-based schema that captures: reactants, reagents, solvents, and products as SMILES or InChI strings; reaction conditions (temperature, pressure, reaction time, atmosphere); yields (percentage and absolute); experimental procedures; safety notes; and data provenance. The schema is designed to be both human- and machine-readable.

As of 2021, the database contains over 1 million reactions, contributed by pharmaceutical companies (Eli Lilly, Merck, AstraZeneca, etc.) and academic groups. The dataset is described in a 2021 JACS paper and is expected to serve as a foundation for ML models for reaction prediction, retrosynthesis, and automated synthesis planning.

Licensed under CC BY 4.0. Hosted on GitHub and accessible via a web interface.

## Tags

CC BY 4.0, Chemical Reactions, Cheminformatics, Open Access, Pharmaceutical, Protocol Buffers, Reaction Prediction, Retrosynthesis, SMILES, Synthesis Planning

## References

- [ORD Paper: An Open Database for Chemical Reactions (JACS 2021)](https://pubs.acs.org/doi/10.1021/jacs.1c09820)
- [C&EN article on ORD (2021)](https://cen.acs.org/physical-chemistry/computational-chemistry/new-database-machine-learning-research/99/web/2021/11)
- [GitHub: Open Reaction Database](https://github.com/open-reaction-database)

[⬅️ Back to Index](../README.md)
