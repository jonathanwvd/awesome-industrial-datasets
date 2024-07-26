# [3W](https://github.com/petrobras/3W/tree/master/dataset)

![](https://img.shields.io/badge/sector-oil_and_gas-darkblue.svg)
![](https://img.shields.io/badge/labeled-yes-blue.svg)
![](<https://img.shields.io/badge/timestamp-yes-green.svg>)
![](<https://img.shields.io/badge/simulation-simulated_and_real-green.svg>)

Parameter | Value
---- | ----
Data Set Characteristics | Multivariate and Time-Series
Attribute Characteristics | Real
Associated Tasks	| Classification, Regression, Clustering
Number of Instances	| 1981
Number of Attributes | 10
Date Donated | 2019-07-01
Source | Github
Dataset size | 681MB (compressed)

## Data Set Information  
The 3W dataset consists of all CSV files in the subdirectories of the dataset directory and structured as detailed here.

To the best of its authors' knowledge, this is the first realistic and public dataset with rare undesirable real events in oil wells that can be readily used as a benchmark dataset for development of machine learning techniques related to inherent difficulties of actual data.

For more information about the theory behind this dataset, refer to the paper A realistic and public dataset with rare undesirable real events in oil wells published in the Journal of Petroleum Science and Engineering [link here](). Specific challenges (benchmarks) that practitioners and researchers can use together with the 3W dataset are defined and proposed in this paper.

## Attribute Information
The 3W dataset consists of 1,981 CSV files structured as follows. The subdirectory names are the instances' labels. Each file represents one instance. The filename reveals its source. All files are standardized as follow. There are one observation per line and one series per column. Columns are separated by commas and decimals are separated by periods. The first column contains timestamps, the last one reveals the observations' labels, and the other columns are the Multivariate Time Series (MTS) (i.e. the instance itself).

- timestamp: observations - timestamps loaded into pandas - DataFrame as its index;
- P-PDG: pressure variable at the - Permanent Downhole Gauge (PDG);
- P-TPT: pressure variable at the - Temperature and Pressure - Transducer (TPT);
- T-TPT: temperature variable at the Temperature and Pressure - Transducer (TPT);
- P-MON-CKP: pressure variable upstream of the production choke (CKP);
- T-JUS-CKP: temperature variable downstream of the production choke (CKP);
- P-JUS-CKGL: pressure variable upstream of the gas lift choke (CKGL);
- T-JUS-CKGL: temperature variable upstream of the gas lift choke (CKGL);
- QGL: gas lift flow rate;
- class: observations labels associated with three types of periods (normal, fault transient, and faulty steady state).

Other information are also loaded into each pandas Dataframe:

- label: instance label (event type);
- well: well name. Hand-drawn and simulated instances have fixed names. Real instances have names masked with incremental id;
- id: instance identifier.
- Hand-drawn and simulated instances have incremental id. 
- Each real instance has an id generated from its first timestamp.

## References
- [Github](https://github.com/petrobras/3W/blob/master/3W_TOOLKIT_STRUCTURE.md) - official data source. 
- [Kaggle](https://www.kaggle.com/datasets/afrniomelo/3w-dataset) - Kaggle page with the dataset and codes.

## Citation Request 
1. [Vargas, Ricardo Emanuel Vaz, et al. "A realistic and public dataset with rare undesirable real events in oil wells." Journal of Petroleum Science and Engineering 181 (2019): 106223.](https://www.sciencedirect.com/science/article/abs/pii/S0920410519306357?via%3Dihub)
