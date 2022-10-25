## Chemical    
### [Dynamic Gas Mixtures](https://archive.ics.uci.edu/ml/datasets/Gas+sensor+array+under+dynamic+gas+mixtures) 

This data set contains the acquired time series from 16 chemical sensors exposed to gas mixtures at varying concentration levels.      
For each measurement (each gas mixture), the signals were acquired continuously for about 12 hours without interruption.   

The data set was collected in a gas delivery platform facility at the ChemoSignals Laboratory in the BioCircuits Institute, University of California San Diego.   

![](https://img.shields.io/badge/sector-chemical-red.svg)
![](https://img.shields.io/badge/labeled-yes-blue.svg)
![](https://img.shields.io/badge/time--series-yes-blue.svg) ![](<https://img.shields.io/badge/simulation-yes-blue.svg>)    

#### Data Set Information  

- Data Summary      

| Data Set Characteristics  | Attribute Characteristics | Associated Tasks           |
| ------------------------- | ------------------------- | -------------------------- |
| Multivariate, Time-Series | Real                      | Classification, Regression |

| Number of Instances | Number of Attributes | Number of Missing Values(NaN/not available) |
| ------------------- | -------------------- | ------------------------------------------- |
| 4178504             | 19                   | 0                                           |


- Data Explanation     
The data consists of two files, each containing data for each gas mixture.    
Two kinds of gas mixtures = Ethylene and Methane in air / Ethylene and CO in air  
Each file consists of 19 columns = Time(seconds), Methane conc(or CO conc) (ppm), Ethylene conc (ppm), sensor readings (16 channels)  
Sequence of Sensors = TGS2602; TGS2602; TGS2600; TGS2600; TGS2610; TGS2610; TGS2620; TGS2620; TGS2602; TGS2602; TGS2600; TGS2600; TGS2610; TGS2610; TGS2620; TGS2620        

#### Paper  

1. [kaggle](<https://www.kaggle.com/uciml/gas-sensor-array-under-dynamic-gas-mixtures>)   

2. [A wireless sensor data-based coal mine gas monitoring algorithm with least squares support vector machines optimized by swarm intelligence techniques](<https://journals.sagepub.com/doi/full/10.1177/1550147718777440>): There is a part of experiment with gas sensor array drift data.     

   keywords: CNN, LSTM, LS-SVM    

#### Citation   

Citation of Fonollosa et al. 'Reservoir Computing compensates slow response of chemosensor arrays exposed to fast varying gas concentrations in continuous monitoring'; Sensors and Actuators B, 2015 is required.     


##### Data Download Link   
[https://archive.ics.uci.edu/ml/machine-learning-databases/00322/](https://archive.ics.uci.edu/ml/machine-learning-databases/00322/)   

Data Capacity(Compressed):   

352MB      