# [Data-driven prediction of battery cycle life before capacity degradation](https://data.matr.io/1/)

2.82GB , 1.8GB, 3.01GB

This dataset, used in “Data-driven prediction of battery cycle life before capacity degradation”, consists of 124 commercial lithium-ion batteries cycled to failure under fast-charging conditions. These lithium-ion phosphate (LFP)/graphite cells, manufactured by A123 Systems (APR18650M1A), were cycled in horizontal cylindrical fixtures on a 48-channel Arbin LBT potentiostat in a forced convection temperature chamber set to 30°C. The cells have a nominal capacity of 1.1 Ah and a nominal voltage of 3.3 V.

**objective**

The objective of this work is to optimize fast charging for lithium-ion batteries. As such, all cells in this dataset are charged with a one-step or two-step fast-charging policy. 

 ![](https://img.shields.io/badge/sector-battery-ff69b4.svg)  ![](https://img.shields.io/badge/labeled-no-red.svg)  ![](https://img.shields.io/badge/time--series-yes-blue.svg)  ![](<https://img.shields.io/badge/simulation-no-red.svg>)

#### Data Set Information

| Data Set Characteristics | Attribute Characteristics | Associated Tasks |
| ------------------------ | ------------------------- | ---------------- |
| Multivariate             | Real                      | Regression       |

**How to make data set**

"C1(A1)-C2"

- C1,C2 : first and second constant-current steps, respectively
- Q1 : the state-of-charge (SOC, %) at which the currents switch

The second current step ends at 80% SOC, after which the cells charge at 1C CC-CV. The upper and lower cutoff potentials are 3.6 V and 2.0 V, respectively, which are consistent with the manufacturer’s specifications. These cutoff potentials are fixed for all current steps, including fast charging; after some cycling, the cells may hit the upper cutoff potential during fast charging, leading to significant constant-voltage charging. All cells discharge at 4C.

The dataset is divided into three “batches”, representing approximately 48 cells each. Each batch is defined by a “batch date”, or the date the tests were started. Each batch has a few irregularities, as detailed on the page for each batch.

The temperature measurements are performed by attaching a Type T thermocouple with thermal epoxy (OMEGATHERM 201) and Kapton tape to the exposed cell can after stripping a small section of the plastic insulation. Note that the temperature measurements are not perfectly reliable; the thermal contact between the thermocouple and the cell can may vary substantially, and the thermocouple sometimes loses contact during cycling.

Internal resistance measurements were obtained during charging at 80% SOC by averaging 10 pulses of ±3.6C with a pulse width of 30 ms (2017-05-12 and 2017-06-30) or 33 ms (2018-04-12).

The following repository contains some starter code to load the datasets in either MATLAB or python:

<https://github.com/rdbraatz/data-driven-prediction-of-battery-cycle-life-before-capacity-degradation>

**Experimental design**

- All cells were cycled with one-step or two-step charging policies. The charging time varies from ~8 to 13.3 minutes (0-80% SOC). There are generally two cells tested per policy, with the exception of 3.6C(80%).
- 1 minute and 1 second rests were placed after reaching 80% SOC during charging and after discharging, respectively.
- We cycle to 80% of nominal capacity (0.88 Ah).
- An initial C/10 cycle was performed in the beginning of each test.
- The cutoff currents for the constant-voltage steps were C/50 for both charge and discharge.
- The pulse width of the IR test is 30 ms.

**Experimental notes**

- The computer automatically restarted twice. As such, there are some time gaps in the data.
- The temperature control is somewhat inconsistent, leading to variability in the baseline chamber temperature.
- The tests in channels 4 and 8 did not successfully start and thus do not have data.
- The thermocouples for channels 15 and 16 were accidentally switched.

**Data notes**

- Cycle 1 data is not available in the struct. The sampling rate for this cycle was initially too high, so we excluded it from the data set to create more manageable file sizes.
- The cells in Channels 1, 2, 3, 5, and 6 (3.6C(80%) and 4C(80%) policies) were stopped at the end of this batch and resumed in the 2017-06-30 batch. This pause in cycling lead to a rise in capacity upon resuming the tests.
- The tests in channels 13, 19, 21, 22, and 31 were terminated before the cells reached 80% of nominal capacity.

#### Paper

[Data-driven prediction of battery cycle life before capacity degradation](https://www.nature.com/articles/s41560-019-0356-8)

abstract

Accurately predicting the lifetime of complex, nonlinear systems such as lithium-ion batteries is critical for accelerating technology development. However, diverse aging mechanisms, significant device variability and dynamic operating conditions have remained major challenges. We generate a comprehensive dataset consisting of 124 commercial lithium iron phosphate/graphite cells cycled under fast-charging conditions, with widely varying cycle lives ranging from 150 to 2,300 cycles. Using discharge voltage curves from early cycles yet to exhibit capacity degradation, we apply machine-learning tools to both predict and classify cells by cycle life. Our best models achieve 9.1% test error for quantitatively predicting cycle life using the first 100 cycles (exhibiting a median increase of 0.2% from initial capacity) and 4.9% test error using the first 5 cycles for classifying cycle life into two groups. This work highlights the promise of combining deliberate data generation with data-driven modelling to predict the behaviour of complex dynamical systems.

#### Citation

Severson *et al*. Data-driven prediction of battery cycle life before capacity degradation. *Nature Energy* volume 4, pages 383–391 (2019).