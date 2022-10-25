## Mechanical    
### [C-MAPSS](https://ti.arc.nasa.gov/tech/dash/groups/pcoe/prognostic-data-repository/) 
#### Turbofan Engine Degradation Simulation Data Set    

This data set was generated with the C-MAPSS simulator.  C-MAPSS stands for 'Commercial Modular Aero-Propulsion System Simulation' and it is a tool for the simulation of realistic large commercial turbofan engine data. Each data set is divided into a train and a test set. Each time-series data set is a data set obtained from another engine. A dataset is data from the same type of engine. The four data sets are multivariate time-series data obtained with different operational conditions (ONE, SIX) and fault modes (ONE, TWO), respectively. There are three operational settings that affect engine performance. For each test data, RUL (Remaining Useful Life) values are provided. In the training set, the degradation increases until it reaches the predefined threshold, which is deemed bad for operating the engine. In the test set, the time series data is terminated before it is completely degraded. For each data set, there is a column of 26 sensors.      

Response surfaces of all sensors are generated via a thermo-dynamical simulation model for the engine as a function of variations of flow and efficiency of the modules of interest.  

![](https://img.shields.io/badge/sector-mechanical-purple.svg)
![](https://img.shields.io/badge/labeled-implicit-green.svg)
![](https://img.shields.io/badge/time--series-yes-blue.svg)  
![](https://img.shields.io/badge/time--to--failure-gray.svg) ![](<https://img.shields.io/badge/simulation-yes-blue.svg>)     

#### Data Set Information  

- Data Explanation     

Each engine initially has some wear and there is a manufacturing variation, but this is considered normal.   
There are three operational settings that affect engine performance.   
Data was contaminated by sensor noise.    
At the beginning of each time series data collection, the engine starts at normal state, and a fault occurs at any time point.   
In the training set, the fault grows until a system failure occurs.     
In the test set, the time series ends to some extent before a system failure occurs.    

- Purpose of Competition     
predicting the number of remaining operational cycles before a system failure occurs in the test set.   


- Summary of each dataset        

| Data Set | Train trajectories | Test trajectories | Conditions     | Fault modes                           |
| -------- | ------------------ | ----------------- | -------------- | ------------------------------------- |
| FD001    | 100                | 100               | One(sea level) | One(HPD Degradation)                  |
| FD002    | 260                | 259               | Six            | One(HPC degradation)                  |
| FD003    | 100                | 100               | One            | Two(HPC degradation, fan degradation) |
| FD004    | 249                | 248               | Six            | Two(HPC degradation, fan degradation) |

| Train Data Set | Number of row | Test Data Set | Number of row | RUL Data Set | Number of row |
| -------------- | ------------- | ------------- | ------------- | ------------ | ------------- |
| FD001          | 20631         | FD001         | 13096         | FD001        | 100           |
| FD002          | 53759         | FD002         | 33991         | FD002        | 259           |
| FD003          | 24720         | FD003         | 16596         | FD003        | 100           |
| FD004          | 61249         | FD004         | 41214         | FD004        | 248           |


- Attributes Explanation    

Each dataset has 26 columns.     
The columns correspond to:  

1)	unit number  
2)	time, in cycles  
3)	operational setting 1  
4)	operational setting 2  
5)	operational setting 3  
6)	sensor measurement  1  
7)	sensor measurement  2  
...  
26)	sensor measurement  26   

- train/test data set __N/A__   
  __None__       

#### Paper    

1. [Long Short-Term Memory Network for Remaining
   Useful Life Estimation](<http://www.hitachi-america.us/rd/about_us/bdl/docs/LSTM_RUL.PDF>)   

   keywords: LSTM,  Multi-Layer Perceptron (MLP), Support Vector Regression (SVR), Relevance Vector Regression (RVR) and Convolutional Neural Network (CNN)   

2. [Remaining Useful Life Estimation Using Functional
   Data Analysis](<https://arxiv.org/pdf/1904.06442.pdf>)   

   keywords: LSTM, CNN, MLP    

#### Citations  

A. Saxena and K. Goebel (2008). "Turbofan Engine Degradation Simulation Data Set", NASA Ames Prognostics Data Repository (http://ti.arc.nasa.gov/project/prognostic-data-repository), NASA Ames Research Center, Moffett Field, CA    

##### Data Download Link  
[https://ti.arc.nasa.gov/c/6/](https://ti.arc.nasa.gov/c/6/)   

Data Capacity(Compressed):  

11.9MB       