# PHM Data Challenge 18

| Parameter | Value |
| --- | --- |
| Data Set Characteristics | Multivariate |
| Attribute Characteristics | Real |
| Associated Tasks | Classification, Causal-Discovery |
| Number of Instances | 1567 |
| Number of Attributes | 591 |
| Date Donated | 2008-11-19 |
| Source | UCI Machine Learning Repository |
| Dataset size | 5.4MB |

## Data Set Information
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

## References
- [https://drive.google.com/open?id=15Jx9Scq9FqpIGn8jbAQB_lcHSXvIoPzb](https://drive.google.com/open?id=15Jx9Scq9FqpIGn8jbAQB_lcHSXvIoPzb)

