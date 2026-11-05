# MILP Benchmarks CellphoneCo.

**Summary:** Mixed-integer linear programming instances in MPS format that model the weekly supply chain planning of a fictive cellphone and accessories company.

| Parameter | Value |
| --- | --- |
| **Dataset** | MILP Benchmarks CellphoneCo. |
| **Domain** | Logistics & Retail |
| **Asset / Process** | Information not available |
| **Modality** | Information not available |
| **Task** | Information not available |
| **Annotation** | Information not available |
| **Source Type** | Synthetic |
| **Access** | Repository |
| **Size** | Information not available |
| **Year** | 2023 |
| **License** | Apache-2.0 |

## Description

These instances, published by SAP in a GitHub repository, model the supply chain of a fictive company that produces and sells cellphones and accessories of different types. Each instance is a mixed-integer linear optimization problem in the standard MPS format, compressed as .gz, to be unpacked and solved with a mathematical programming solver.

The planning horizon is split into weekly time buckets over a network of warehouses, factories, distribution centers and customers. Components are procured and moved to the factory, final products consume components and restricted resources, and products flow through a main distribution center to local ones before delivery. Late delivery or non-delivery is allowed, and the objective minimizes total cost.

Three instance sets exist. public_mps varies network size and comes with .dec decompositions; vary_matrix_rhs_bounds holds 50 instances with 27710 variables and 16288 constraints each; unbd_semicont adds semi-continuous variables. The license is Apache 2.0.

## References

- [GitHub repository](https://github.com/SAP-samples/ibp-sop-benchmarks-milp-cellphoneco)

[⬅️ Back to Index](../README.md)
