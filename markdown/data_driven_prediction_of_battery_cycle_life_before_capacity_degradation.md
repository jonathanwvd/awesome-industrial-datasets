# Data-driven prediction of battery cycle life before capacity degradation

**Summary:** This dataset facilitates the prediction of lithium-ion batteries' cycle life before they reach capacity degradation. It includes charge-discharge cycles and various operational parameters.

| Parameter | Value |
| --- | --- |
| **Name** | Data-driven prediction of battery cycle life before capacity degradation |
| **Labeled** | Yes |
| **Time Series** | Yes |
| **Simulation** | No |
| **Missing Values** | INA |
| **Dataset Characteristics** | Multivariate, Time-Series |
| **Feature Type** | Real |
| **Associated Tasks** | Regression |
| **Number of Instances** | INA |
| **Number of Features** | INA |
| **Date Donated** | INA |
| **Source** | Matr.io |

## Dataset Information

This dataset, used in our publication 'Data-driven prediction of battery cycle life before capacity degradation', consists of 124 commercial lithium-ion batteries cycled to failure under fast-charging conditions. These lithium-ion phosphate (LFP)/graphite cells, manufactured by A123 Systems (APR18650M1A), were cycled in horizontal cylindrical fixtures on a 48-channel Arbin LBT potentiostat in a forced convection temperature chamber set to 30°C. The cells have a nominal capacity of 1.1 Ah and a nominal voltage of 3.3 V.

The objective of this work is to optimize fast charging for lithium-ion batteries. As such, all cells in this dataset are charged with a one-step or two-step fast-charging policy. This policy has the format 'C1(Q1)-C2', in which C1 and C2 are the first and second constant-current steps, respectively, and Q1 is the state-of-charge (SOC, %) at which the currents switch. The second current step ends at 80% SOC, after which the cells charge at 1C CC-CV. The upper and lower cutoff potentials are 3.6 V and 2.0 V, respectively, which are consistent with the manufacturer's specifications. These cutoff potentials are fixed for all current steps, including fast charging; after some cycling, the cells may hit the upper cutoff potential during fast charging, leading to significant constant-voltage charging. All cells discharge at 4C.

The dataset is divided into three 'batches', representing approximately 48 cells each. Each batch is defined by a 'batch date', or the date the tests were started. Each batch has a few irregularities, as detailed on the page for each batch.

The data is provided in two formats. For each batch, a MATLAB struct is available. The struct provides a convenient data container in which the data for each cycle is easily accessible. This struct can be loaded in either MATLAB or python (via the h5py package). Pandas dataframes can be generated via the provided code. Additionally, the raw data for each cell is available as a CSV file. Note that the CSV files occasionally exhibit errors in both test time and step time in which the test time resets to zero mid-cycle; these errors are corrected for in the structs.

The temperature measurements are performed by attaching a Type T thermocouple with thermal epoxy (OMEGATHERM 201) and Kapton tape to the exposed cell can after stripping a small section of the plastic insulation. Note that the temperature measurements are not perfectly reliable; the thermal contact between the thermocouple and the cell can may vary substantially, and the thermocouple sometimes loses contact during cycling.

Internal resistance measurements were obtained during charging at 80% SOC by averaging 10 pulses of ±3.6C with a pulse width of 30 ms (2017-05-12 and 2017-06-30) or 33 ms (2018-04-12).

## Tags

Battery life prediction, Lithium-ion batteries, Charge-discharge cycles, Predictive maintenance, Energy storage

## References

- [Matr.io Dataset](https://data.matr.io/1/projects/5c48dd2bc625d700019f3204)

[⬅️ Back to Index](../README.md)
