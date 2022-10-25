## Mechanical   

### [PHM DATA Challenge 17](<https://www.phmsociety.org/events/conference/phm/17/data-challenge>): predict faulty regimes of operation of a train car using the data provided and physics-based modeling methods.       

Training and testing data sets are provided. The data given represents spectral features over non-overlapping frequency bands calculated from filtered sensor signals in sequential time frames, for typical frequencies discussed in the literature. One experiment consists of a matrix of 90 feature values over time.    

![](https://img.shields.io/badge/sector-mechanical-purple.svg)
![](https://img.shields.io/badge/labeled-implicit-green.svg)
![](https://img.shields.io/badge/time--series-yes-blue.svg) ![](<https://img.shields.io/badge/simulation-yes-blue.svg>)          

#### Data Set Information    

Timestamp: May 24, 2017 - 12:18pm    

__Training data__   

The training data consists of 200 csv files. Training data will be given in a collection of files "*Training-ddd.csv*" representing instances for all 90 features (*f101*,…,*f190*) described in Table 1 for all experiments described in Table 2. __It only represents nominal operation, where all systems and subsystems operate in a healthy manner__.           

- 200 'train' files consist of 90 columns. The information of 90 columns is as follows.         

  *Table 1: The following table indicates the available features and the sensor underlying the raw data for each feature. Five features are given as a feature set for each sensor, representing spectral information in non-overlapping frequency bands for increasing frequencies. The k-th (k=1...5) feature in each feature set is computed in the same way across sensors.*   

| Feature set per sensor | Sensors |
| ---------------------- | ------- |
| f101 - f105            | azs_1   |
| f106 - f110            | azp_1r  |
| f111 - f115            | azp_1l  |
| f116 - f120            | azp_2r  |
| f121 - f125            | azp_2l  |
| f126 - f130            | az_1r   |
| f131 - f13             | az_1l   |
| f136 - f140            | az_2r   |
| f141 - f145            | az_2l   |
| f146 - f150            | azs_2   |
| f151 - f155            | azp_3r  |
| f156 - f160            | azp_3l  |
| f161 - f165            | azp_4r  |
| f166 - f170            | azp_4l  |
| f171 - f175            | az_3r   |
| f176 - f180            | az_3l   |
| f181 - f185            | az_4r   |
| f186 - f190            | az_4l   |

​	*Table 2: Experiments provided.* 

| ExperimentID | Payload | Speed | Track | State   |
| ------------ | ------- | ----- | ----- | ------- |
| 1            | 1.02    | 1.04  | 1     | healthy |
| 2            | 1.96    | 1.03  | 1     | healthy |
| 3            | 0.89    | 1.03  | 2     | healthy |
| ...          |         |       |       |         |

​	*Table 3: Faults of interest.*    

| Number | Bogie            | Component        | Position |
| :----- | :--------------- | :--------------- | :------- |
| 1      | leading          | Primary Spring   | *czp_1r* |
| 2      | Primary Spring   | *czp_1l*         |          |
| 3      | Primary Spring   | *czp_2r*         |          |
| 4      | Primary Spring   | *czp_2l*         |          |
| 5      | Primary Damper   | *dzp_1r*         |          |
| 6      | Primary Damper   | *dzp_1l*         |          |
| 7      | Primary Damper   | *dzp_2r*         |          |
| 8      | Primary Damper   | *dzp_2l*         |          |
| 9      | Secondary Spring | *czs_1*          |          |
| 10     | Secondary Damper | *dzs_1r*         |          |
| 11     | Secondary Damper | *dzs_1l*         |          |
| 12     | trailing         | *Primary Spring* | *czp_3r* |
| 13     | Primary Spring   | *czp_3l*         |          |
| 14     | Primary Spring   | *czp_4r*         |          |
| 15     | Primary Spring   | *czp_4l*         |          |
| 16     | Primary Damper   | *dzp_3r*         |          |
| 17     | Primary Damper   | *dzp_3l*         |          |
| 18     | Primary Damper   | *dzp_4r*         |          |
| 19     | Primary Damper   | *dzp_4l*         |          |
| 20     | Secondary Spring | *czs_2*          |          |
| 21     | Secondary Damper | *dzs_2r*         |          |
| 22     | Secondary Damper | *dzs_2l*         |          |

__Test data__    

- The test data consists of 200 csv files. It consists of 24 columns. Testing data will be given in a collection of files "*Testing-ddd.csv*" analogous to the training data. It includes both nominal and faulty regimes of operation. No fault number or position information will be provided for faulty regimes.           

#### Objectives          

1. The primary objective of this challenge is to **predict faulty regimes of operation** of a train car using the data provided and physics-based modeling methods (e.g. inspired in any relevant reference such as the ones included in this document)       

#### Paper     

1. T. X. Mei & X. J. Ding (2009): Condition monitoring of rail vehicle suspensions based on changes in system dynamic interactions, Vehicle System Dynamics, 47:9, 1167-1181.  
2. S. Bruni , J. Vinolas , M. Berg , O. Polach & S. Stichel (2011): Modelling of suspension components in a rail vehicle dynamics context. , Vehicle System Dynamics, 49:7, 1021-1072.  
3. S. Iwnicki (1998): Manchester Benchmark for Rail Vehicle Simulation. Vehicle System Dynamics, 30:7, 295-313.     

##### Data Download Link     

<https://www.phmsociety.org/events/conference/phm/17/data-challenge>     

Data Capacity(Compressed) : 19.38 MB        

