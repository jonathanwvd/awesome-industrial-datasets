# [Superconductivty DataSet](http://archive.ics.uci.edu/ml/datasets/Superconductivty+Data)

8.3MB(compressed)

![](https://img.shields.io/badge/sector-semicon-blue.svg) ![](https://img.shields.io/badge/labeled-yes-blue.svg) ![](https://img.shields.io/badge/time--series-no-red.svg)  ![](<https://img.shields.io/badge/simulation-no-red.svg>)

#### Paper

[A data-driven statistical model for predicting the critical temperature of a superconductor](https://www.sciencedirect.com/science/article/pii/S0927025618304877?via%3Dihub)

#### Data Set Information:

| Data Set Characteristics | Attribute Characteristics | Associated Tasks |
| ------------------------ | ------------------------- | ---------------- |
| Multivariate             | Real                      | Regression       |

| Number of Instances | Number of Attributes |
| ------------------- | -------------------- |
| 21263               | 81                   |

1. train.csv 

- contains 81 features extracted from 21263 superconductors along with the critical temperature in the 82nd column,

2. unique_m.csv contains the chemical formula broken up for all the 21263 superconductors from the train.csv file. The last two columns have the critical temperature and chemical formula. The original data comes from [[Web Link\]](http://supercon.nims.go.jp/index_en.html) which is public. The goal here is to predict the critical temperature based on the features extracted.

The database contains a large list of superconductors, their critical temperatures, and the source references mostly from journal articles.

#### Variables

The key columns (variables) were “element”, the chemical formula of the material, and
“Tc”, the critical temperature. Variable “num” was a unique identifier for each row. Column “refno” contained links to the referenced source.

#### Paper

[A data-driven statistical model for predicting the critical temperature of a superconductor](https://www.sciencedirect.com/science/article/pii/S0927025618304877?via%3Dihub)

#### Citation Request:

Hamidieh, Kam, A data-driven statistical model for predicting the critical temperature of a superconductor, Computational Materials Science, Volume 154, November 2018, Pages 346-354, [[Web Link\]](https://doi.org/10.1016/j.commatsci.2018.07.052)