## Semicon
### [PHM DATA Challenge 18](https://www.phmsociety.org/events/conference/phm/18/data-challenge): Etching tool fault detection (PdM)  

The data provided by PHM Data Challenge 18 was provided to investigate the fault behavior of ion mill etch tools in the wafer manufacturing process. It is a database that collects sensor data in time sequence from ion mill etching tools operating under various setting conditions.    

![](https://img.shields.io/badge/sector-semicon-blue.svg)
![](https://img.shields.io/badge/labeled-yes-blue.svg)
![](https://img.shields.io/badge/time--series-yes-blue.svg) ![](<https://img.shields.io/badge/simulation-no-red.svg>)        

#### Data Set Information    

__Training data__   

The training data consists of 60 csv files. It consists of 20 train files, which are training data, 20 train_fault files containing abnormal information only at abnormal points, and 20 train_ttf files, which show ttf information.   

- Data Summary   

| \# of abnormal data | \# of normal data | \# of total data |
| ------------------- | ----------------- | ---------------- |
| 1,236               | 82,188,204        | 82,189,440       |

- 20 'train' files consist of 82,189,440 rows and consist of 24 columns. The information of 24 columns is as follows.       

| ID#  | Parameter Name          | Type            | Description                                                  |
| ---- | ----------------------- | --------------- | ------------------------------------------------------------ |
| S1   | time                    | Numeric         | time                                                         |
| S2   | Tool                    | Categorical     | tool id                                                      |
| S3   | stage                   | Categorical     | processing stage of wafer                                    |
| S4   | Lot                     | Categorical     | wafer id                                                     |
| S5   | runnum                  | Numeric         | number of times tool has been run                            |
| S6   | recipe                  | Categorical     | describes tool settings used to process wafer                |
| S7   | recipe_step             | Categorical     | process step of a recipe                                     |
| S8   | IONGAUGEPRESSURE        | Numeric(Sensor) | pressure reading for the main process chamber when under vacuum |
| S9   | ETCHBEAMVOLTAGE         | Numeric         | voltage potential applied to the beam plate of the grid assembly |
| S10  | ETCHBEAMCURRENT         | Numeric         | ion current impacting the beam grid determining the amount of ions accelerated through the grid assembly to the wafer |
| S11  | ETCHSUPPRESSORVOLTAGE   | Numeric         | voltage potential applied to the suppressor plate of the grid assembly |
| S12  | ETCHSUPPRESSORCURRENT   | Numeric(Sensor) | ion current impacting the suppressor grid plate              |
| S13  | FLOWCOOLFLOWRATE        | Numeric         | rate of flow of helium through the flowcool circuit, controlled by mass flow controller |
| S14  | FLOWCOOLPRESSURE        | Numeric(Sensor) | resulting helium pressure in the flowcool circuit            |
| S15  | ETCHGASCHANNEL1READBACK | Numeric         | rate of flow of argon into the source assembly in the vacuum chamber |
| S16  | ETCHPBNGASREADBACK      | Numeric         | rate of flow of argon into the PBN assembly in the chamber   |
| S17  | FIXTURETILTANGLE        | Numeric         | wafer tilt angle setting                                     |
| S18  | ROTATIONSPEED           | Numeric         | wafer rotation speed setting                                 |
| S19  | ACTUALROTATIONANGLE     | Numeric(Sensor) | measure wafer rotation angle                                 |
| S20  | FIXTURESHUTTERPOSITION  | Numeric         | open / close shutter setting for wafer shielding             |
| S21  | ETCHSOURCEUSAGE         | Numeric         | counter of use for the grid assembly consumable              |
| S22  | ETCHAUXSOURCETIMER      | Numeric         | counter of the use for the chamber shields consumable        |
| S23  | ETCHAUX2SOURCETIMER     | Numeric         | counter of the use for the chamber shields consumable        |
| S24  | ACTUALSTEPDURATION      | Numeric(Sensor) | measured time duration for a particular step                 |

- 20 'train_fault' files consist of a total of 1,236 rows and consist of three columns.    

| ID#  | Parameter Name | Type        | Description                                                  |
| ---- | -------------- | ----------- | ------------------------------------------------------------ |
| F1   | time           | Numeric     | time                                                         |
| F2   | fault_name     | Categorical | name of the particular class of fault that occurred at the specified time |
| F3   | stage          | Categorical | -                                                            |

- 20 'train_ttf' files consist of a total of  82,189,440 rows and consist of four columns.      

| Parameter Name                                     | Type    |
| -------------------------------------------------- | ------- |
| time                                               | Numeric |
| TTF_FlowCool Pressure Dropped Below Limit          | Numeric |
| TTF_Flowcool Pressure Too High Check Flowcool Pump | Numeric |
| TTF_Flowcool leak                                  | Numeric |

__Test data__    

- The test data consists of 5 csv files. It consists of 7,198,948 rows and consists of 24 columns.      

####  Purpose of Data Challenge        

The purpose of this PHM data challenge is as follows.   

1. Diagnose failure(i.e detect and identify)  
2. Determine time remaining until next failure (i.e predict remaining useful life)  

#### Paper   

These are not the papers provided by PHM data Challenge 2018 , attached are some of the papers listed in this paper session of [2018 PHM Society Conference brochure (2018-09-22).pdf](<https://www.phmsociety.org/sites/phmsociety.org/files/2018%20PHM%20Society%20Conference%20brochure%20(2018-09-22).pdf>)     

1. [A Data Driven Health Monitoring Approach to Extending Small
   Sats Mission](https://www.phmpapers.org/index.php/phmconf/article/download/573/phmc_18_573) - Prognostics     

   keywords: anomaly detection, LSTM, Auto-Encoder, sensor   

2. [Automated Hyper-parameter Tuning for Machine Learning Models
   in Machine Health Prognostics](https://www.phmpapers.org/index.php/phmconf/article/download/490/phmc_18_490) - Diagnostics    

   keywords: data from PHM 2016 Data Challenge, Bayesian optimization algorithms, hyper-parameter optimization problem    

##### Data Download Link     
[https://drive.google.com/open?id=15Jx9Scq9FqpIGn8jbAQB_lcHSXvIoPzb](https://drive.google.com/open?id=15Jx9Scq9FqpIGn8jbAQB_lcHSXvIoPzb)    

Data Capacity(Compressed) : 5.0G    

