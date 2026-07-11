# ManyWells

**Summary:** The ManyWells datasets contain simulations of multiphase (gas, oil, water) flow in thousands of wells to support research on data-driven methodologies and industrial applications of machine learning and AI.

| Parameter | Value |
| --- | --- |
| **Dataset** | ManyWells |
| **Domain** | Oil & Gas |
| **Asset / Process** | Oil Wells / Reservoirs |
| **Modality** | Time Series |
| **Task** | Classification; Regression; Simulation / Control |
| **Annotation** | Sample Label; Class Label; Scalar Target |
| **Source Type** | Simulation |
| **Access** | Repository; Hugging Face |
| **Size** | 3006000 |
| **Year** | 2025 |
| **License** | Information not available |

## Description

The ManyWells datasets contain simulations of multiphase (gas, oil, water) flow in thousands of wells. The datasets were created and shared by Solution Seeker AS to support research on data-driven methodologies and industrial applications of machine learning and AI.

There are currently three datasets for three different operating conditions: manywells-sol-1 with stationary boundary conditions and open-loop control (no feedback), manywells-nsol-1 with non-stationary boundary conditions and open-loop control (no feedback), and manywells-nscl-1 with non-stationary boundary conditions and closed-loop control (with feedback). Each dataset contains one million data points from 2000 vertical wells (500 data points per well). Each data point corresponds to one simulation performed by the simulator code available on the ManyWells GitHub repository.

The datasets include unique well identifiers called "ID". Note that IDs are unique only within each dataset, so well 1 in one dataset differs from well 1 in another. The simulation parameters can be found in configuration files named [dataset-name]_config.zip, stored as dictionaries with well IDs as keys. The datasets do not contain any personal, sensitive, or private information.

## References

- [ManyWells GitHub repository](https://github.com/solution-seeker-as/manywells)
- [ManyWells on Hugging Face](https://huggingface.co/datasets/solution-seeker-as/manywells)

[⬅️ Back to Index](../README.md)
