# [Dynamic Gas Mixtures](https://archive.ics.uci.edu/ml/datasets/Gas+sensor+array+under+dynamic+gas+mixtures) 

![](https://img.shields.io/badge/sector-chemical-red.svg)
![](https://img.shields.io/badge/labeled-yes-blue.svg)
![](https://img.shields.io/badge/time--series-yes-blue.svg) 
![](<https://img.shields.io/badge/simulation-yes-blue.svg>)    

Parameter | Value
---- | ----
Data Set Characteristics | Multivariate, Time-Series
Attribute Characteristics	| Real
Associated Tasks	| Classification
Number of Instances	| 4178504
Number of Attributes	| 19
Date Donated | 2015-03-20
Source | UCI Machine Learning Repository
Dataset size | 352MB (compressed)


## Source

Creators: Jordi Fonollosa (fonollosa '@'ucsd.edu)\
BioCircutis Institute\
University of California San Diego\
San Diego, California, USA

Donors of the Dataset:\
Jordi Fonollosa (fonollosa '@'ucsd.edu)\
Ramon Huerta (rhuerta '@' ucsd.edu)

## Data Set Information  

This data set contains the acquired time series from 16 chemical sensors exposed to gas mixtures at varying concentration levels. In particular, we generated two gas mixtures: Ethylene and Methane in air, and Ethylene and CO in air. Each measurement was constructed by the continuous acquisition of the 16-sensor array signals for a duration of about 12 hours without interruption.

The data set was collected in a gas delivery platform facility at the ChemoSignals Laboratory in the BioCircuits Institute, University of California San Diego. The measurement system platform provides versatility for obtaining the desired concentrations of the chemical substances of interest with high accuracy and in a highly reproducible manner.

The sensor array included 16 chemical sensors (Figaro Inc., US) of 4 different types: TGS-2600, TGS-2602, TGS-2610, TGS-2620 (4 units of each type). The sensors were integrated with customized signal conditioning and control electronics. The operating voltage of the sensors, which controls the sensorsâ€™ operating temperature, was kept constant at 5 V for the whole duration of the experiments. The sensorsâ€™ conductivities were acquired continuously at a sampling frequency of 100 Hz. The sensor array was placed in a 60 ml measurement chamber, where the gas sample was injected at a constant flow of 300 ml/min.

Each measurement was constructed by the continuous acquisition of the 16-sensor array signals while concentration levels changed randomly. For each measurement (each gas mixture), the signals were acquired continuously for about 12 hours without interruption.

The concentration transitions were set at random times (in the interval 80-120s) and to random concentration levels. The data set was constructed such that all possible transitions are present: increasing, decreasing, or setting to zero the concentration of one volatile while the concentration of the other volatile is kept constant (either at a fixed or at zero concentration level). At the beginning, ending, and approximately every 10,000 s, we inserted additional predefined concentration patterns with pure gas mixtures.

The concentration ranges for Ethylene, Methane, and CO were selected such that the induced magnitudes of the sensor responses were similar. Moreover, for gas mixtures, lower concentration levels were favored. Therefore, the multivariate response of the sensors to the presented set of stimuli is challenging since none of the configurations (single
gas or mixture presentation) can be easily identified from the magnitude of sensorsâ€™ responses. In particular Ethylene concentration ranges from 0-20 ppm; 0-600 ppm for CO; and 0-300 ppm for Methane.

The primary purpose of making this data set freely accessible on-line is to provide extensive and continuous time series acquired from chemical sensors to the sensor and artificial intelligence research communities to develop and test strategies to solve a wide variety of tasks. In particular, the data set may be useful to develop algorithms for continuous monitoring or improve response time of sensory systems. Also, the repetition of the same type of sensors in the array will allow further investigation on sensor variability (reproducibility of sensors of the same kind). Other interesting topics may include sensor failure (to what extent system predictions degrade when sensors start failing) or calibration transfer (whether the model for one sensor can be extended to other sensors).

More information on the generated data set can be found in Fonollosa et al. 'Reservoir Computing compensates slow response of chemosensor arrays exposed to fast varying gas concentrations in continuous monitoring'; Sensors and Actuators B, 2015.

The data set can be used exclusively for research purposes. Commercial purposes are fully excluded.   

## Attribute Information

The data is presented in two different files: Each file contains the data from one mixture. The file ethylene_CO.txt contains the recordings from the sensors when exposed to mixtures of Ethylene and CO in air. The file ethylene_methane.txt contains the acquired time series induced by the mixture of Methane and Ethylene in air.

The structure of the files is the same: Data is distributed in 19 columns. First column represents time (in seconds), second column represents Methane (or CO) concentration set point (in ppm), third column details Ethylene concentration set point (in ppm), and the following 16 columns show the recordings of the sensor array.

Files include a header (one line) with the information of each column:

Time (seconds), Methane conc (ppm), Ethylene conc (ppm), sensor readings (16 channels)

The order of the sensors in the files is as follows:
TGS2602; TGS2602; TGS2600; TGS2600; TGS2610; TGS2610; TGS2620; TGS2620; TGS2602; TGS2602; TGS2600; TGS2600; TGS2610; TGS2610; TGS2620; TGS2620

Sensors' readings can be converted to KOhms by 40.000/S_i, where S_i is the value provided in the text files.


## References

- [UCI](https://archive.ics.uci.edu/ml/datasets/Gas+sensor+array+under+dynamic+gas+mixtures): Database source link.

- [A wireless sensor data-based coal mine gas monitoring algorithm with least squares support vector machines optimized by swarm intelligence techniques](<https://journals.sagepub.com/doi/full/10.1177/1550147718777440>): There is a part of experiment with gas sensor array drift data.

## Citation Request

1. Citation of Fonollosa et al. 'Reservoir Computing compensates slow response of chemosensor arrays exposed to fast varying gas concentrations in continuous monitoring'; Sensors and Actuators B, 2015 is required.     