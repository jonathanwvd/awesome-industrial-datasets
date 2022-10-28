# [Gas Sensor Array Drift](https://archive.ics.uci.edu/ml/datasets/Gas+Sensor+Array+Drift+Dataset+at+Different+Concentrations)  


![](https://img.shields.io/badge/sector-chemical-red.svg)
![](https://img.shields.io/badge/labeled-yes-blue.svg)
![](https://img.shields.io/badge/time--series-yes-blue.svg)
![](<https://img.shields.io/badge/simulation-yes-blue.svg>)       

Parameter | Value
---- | ----
Data Set Characteristics | Multivariate, Time-Series
Attribute Characteristics	| Real
Associated Tasks	| Classification, Regression, Clustering
Number of Instances	| 13910
Number of Attributes	| 129
Date Donated | 2013-10-23
Source | UCI Machine Learning Repository
Dataset size | 9.6MB (compressed)


## Source:

- Creators: 
     - Alexander Vergara (vergara '@' ucsd.edu)
BioCircutis Institute
University of California San Diego
San Diego, California, USA
- Donors of the Dataset:
    - Alexander Vergara (vergara '@' ucsd.edu)
    - Jordi Fonollosa (fonollosa '@'ucsd.edu)
    - Irene Rodriguez-Lujan (irrodriguezlujan '@' ucsd.edu)
    - Ramon Huerta (rhuerta '@' ucsd.edu)

## Data Set Information    

This data set contains 13,910 measurements from 16 chemical sensors exposed to 6 gases at different concentration levels. This dataset is an extension of the Gas Sensor Array Drift Dataset ([Web Link]), providing now the information about the concentration level at which the sensors were exposed for each measurement. The primary purpose of making this dataset freely accessible on-line is to provide an extensive dataset to the sensor and artificial intelligence research communities to develop and test strategies to solve a wide variety of tasks, including sensor drift, classification, regression, among others.

The dataset can be used exclusively for research purposes. Commercial purposes are fully excluded. Citation of both Vergara et al. 'Chemical gas sensor drift compensation using classifier ensembles' and Rodriguez-Lujan et al. â€œOn the calibration of sensor arrays for pattern recognition using the minimal number of experimentsâ€ is required (see below).

The dataset was gathered during the period of January 2008 to February 2011 (36 months) in a gas delivery platform facility situated at the ChemoSignals Laboratory in the BioCircuits Institute, University of California San Diego. The measurement system platform provides versatility for obtaining the desired concentrations of the chemical substances of interest with high accuracy and in a highly reproducible manner, minimizing thereby the common mistakes caused by human intervention and making it possible to exclusively concentrate on the chemical sensors. See reference 1 for more details on the experimental setup.

The resulting dataset comprises recordings from six distinct pure gaseous substances, namely Ammonia, Acetaldehyde, Acetone, Ethylene, Ethanol, and Toluene, dosed at a wide variety of concentration levels in the intervals (50,1000), (5,500), (12,1000), (10,300), (10,600), and (10,100) ppmv, respectively.

Attribute Information 
Why 128-element feature vector per measurement? MOX gas sensors typically describe a monotonically smooth change in the conductance of the sensing layer due to the adsorption/desorption reaction processes of the exposed chemical analyte substance. We represented each time series with an aggregate of __eight features__ reflecting the sensor response. In particular, we considered two distinct types of features in the creation of this dataset: __two steady-state features__ and __six features__ reflecting the sensor dynamics. The steady-state features include the amplitude of the resistance change, and its normalized value. The transient features were extracted based on the exponential moving average (EMA) to reflect the sensor dynamics of the increasing/decaying transient portion of the sensor responses. The EMA transform evaluates the rising/decaying portions of the sensor resistance by considering the maximum/minimum values of y[k] of the following first-order digital filter:  y[k] = (1-a)y[k-1] + a(x[k] - x[k-1])     

where 0 < α < 1 is the smoothing parameter of the filter and x[k] is the acquired value at time k. Since different values of α provide different feature values and different information of the transient response, we computed the EMA filter for three values of α = 0.1, 0.01, 0.001 for both the rising and the decaying stages. Therefore, each of the __16 sensors__ used in the study contributes with __8 features__, thereby yielding a __128-element feature vector__ per measurement.     

   
## Sources   
- [UCI](https://archive.ics.uci.edu/ml/datasets/Gas+Sensor+Array+Drift+Dataset+at+Different+Concentrations): Database source link.

- [Data Science project with Python Notebooks](https://github.com/miltongneto/Gas-Sensor-Array-Drift): This project consists of building a solution following all the steps of CRISP-DM (CRoss Industry Standard Process for Data Mining). (Repository in portuguese).

## Citation  
1. A Vergara, S Vembu, T Ayhan, M Ryan, M Homer, R Huerta. "Chemical gas sensor drift compensation using classifier ensembles." Sensors and Actuators B: Chemical 166 (2012): 320-329.

2. I Rodriguez-Lujan, J Fonollosa, A Vergara, M Homer, R Huerta. "On the calibration of sensor arrays for pattern recognition using the minimal number of experiments." Chemometrics and Intelligent Laboratory Systems 130 (2014): 123-134.