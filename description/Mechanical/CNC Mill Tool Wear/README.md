## Mechanical    
### [CNC Mill Tool Wear](https://www.kaggle.com/shasun/tool-wear-detection-in-cnc-mill/data) 

CNC Mill Tool Wear data was provided to perform classification studies such as 'Tool wear detection' and 'Detection of inadequate clamping'.     

A series of machining experiments were run on 2" x 2" x 1.5" wax blocks in a CNC milling machine in the System-level Manufacturing and Automation Research Testbed (SMART) at the University of Michigan. Machining data was collected from a CNC machine for variations of tool condition, feed rate, and clamping pressure. Each experiment produced a finished wax part with an "S" shape - S for smart manufacturing - carved into the top face, as shown in `test_artifact.jpg` (included in the dataset).  

General data from each of the 18 different experiments are given in `train.csv`  Time series data was collected from the 18 experiments with a sampling rate of `100 ms` and are separately reported in files `experiment_01.csv` to `experiment_18.csv`. Each `experiment_xx.csv` file consists of 48 columns and the number of each row is from `experiment_01.csv` to `experiment_18.csv` (1056, 1669, 1522, 533, 463, 1297, 566, 606, 741, 1302, 2315, 2276 , 2234, 2333, 1382, 603, 2151, 2254). Time series data from 18 experiments is collected at a sampling rate of 100 ms.          

![](https://img.shields.io/badge/sector-mechanical-purple.svg)
![](https://img.shields.io/badge/labeled-meta--only-yellow.svg)
![](https://img.shields.io/badge/time--series-yes-blue.svg)  
![](https://img.shields.io/badge/tool_wear_detection-gray.svg)
![](https://img.shields.io/badge/detection_of_inadequate_clamping-gray.svg) ![](<https://img.shields.io/badge/simulation-yes-blue.svg>)      

#### Data Set Information  

- Data Set    


| Data Set          | Number of row | Data Set          | Number of row |
| ----------------- | ------------- | ----------------- | ------------- |
| experiment_01.csv | 1056          | experiment_10.csv | 1302          |
| experiment_02.csv | 1669          | experiment_11.csv | 2315          |
| experiment_03.csv | 1522          | experiment_12.csv | 2276          |
| experiment_04.csv | 533           | experiment_13.csv | 2234          |
| experiment_05.csv | 463           | experiment_14.csv | 2333          |
| experiment_06.csv | 1297          | experiment_15.csv | 1382          |
| experiment_07.csv | 566           | experiment_16.csv | 603           |
| experiment_08.csv | 606           | experiment_17.csv | 2151          |
| experiment_09.csv | 741           | experiment_18.csv | 2254          |
|                   |               | Train.csv         | 18            |



- Attribute explanation - `Train.csv`       

| Inputs(features)     | Description                                                  | Outputs(predictions)     | Description                                                  |
| -------------------- | ------------------------------------------------------------ | ------------------------ | ------------------------------------------------------------ |
| No.experiment number | -                                                            | tool_condition           | label for unworn and worn tools                              |
| material             | wax                                                          | machine_completed        | indicator for if machine was completed without the workspace moving out of the pneumatic vise |
| feed_rate            | relative velocity of the cutting tool along the workpiece(mm/s) | passed_visual_inspection | indicator for if the workpiece passed visual   inspection, only available for experiments where machining was completed |
| clamp_pressure       | pressure used to hold the workpiece in the wise(bar)         | -                        |                                                              |

The 'tool_condition' variable indicates whether the tool is unworn or worn. 

- Attributes explanation - `18 experiment_xx.csv`     

  There are a total of 48 attributes.   

  | Attribute name            | Type    | Description                                                  |
  | ------------------------- | ------- | ------------------------------------------------------------ |
  | X1_ActualPosition         | float64 | actual x position of part (mm)                               |
  | X1_ActualVelocity         | float64 | actual x velocity of part (mm/s)                             |
  | X1_ActualAcceleration     | float64 | actual x acceleration of part (mm/s/s)                       |
  | X1_CommandPosition        | float64 | reference x position of part (mm)                            |
  | X1_CommandVelocity        | float64 | reference x velocity of part (mm/s)                          |
  | X1_CommandAcceleration    | float64 | reference x acceleration of part (mm/s/s)                    |
  | X1_CurrentFeedback        | float64 | current (A)                                                  |
  | X1_DCBusVoltage           | float64 | voltage (V)                                                  |
  | X1_OutputCurrent          | float64 | current (A)                                                  |
  | X1_OutputVoltage          | float64 | voltage (V)                                                  |
  | X1_OutputPower            | float64 | power (kW)                                                   |
  | Y1_ActualPosition         | float64 | actual y position of part (mm)                               |
  | Y1_ActualVelocity         | float64 | actual y velocity of part (mm/s)                             |
  | Y1_ActualAcceleration     | float64 | actual y acceleration of part (mm/s/s)                       |
  | Y1_CommandPosition        | float64 | reference y position of part (mm)                            |
  | Y1_CommandVelocity        | float64 | reference y velocity of part (mm/s)                          |
  | Y1_CommandAcceleration    | float64 | reference y acceleration of part (mm/s/s)                    |
  | Y1_CurrentFeedback        | float64 | current (A)                                                  |
  | Y1_DCBusVoltage           | float64 | voltage (V)                                                  |
  | Y1_OutputCurrent          | float64 | current (A)                                                  |
  | Y1_OutputVoltage          | float64 | voltage (V)                                                  |
  | Y1_OutputPower            | float64 | power (kW)                                                   |
  | Z1_ActualPosition         | float64 | actual z position of part (mm)                               |
  | Z1_ActualVelocity         | float64 | actual z velocity of part (mm/s)                             |
  | Z1_ActualAcceleration     | float64 | actual z acceleration of part (mm/s/s)                       |
  | Z1_CommandPosition        | float64 | reference z position of part (mm)                            |
  | Z1_CommandVelocity        | float64 | reference z velocity of part (mm/s)                          |
  | Z1_CommandAcceleration    | float64 | reference z acceleration of part (mm/s/s)                    |
  | Z1_CurrentFeedback        | float64 | current (A)                                                  |
  | Z1_DCBusVoltage           | float64 | voltage (V)                                                  |
  | Z1_OutputCurrent          | float64 | current (A)                                                  |
  | Z1_OutputVoltage          | float64 | voltage (V)                                                  |
  | S1_ActualPosition         | float64 | actual position of spindle (mm)                              |
  | S1_ActualVelocity         | float64 | actual velocity of spindle (mm/s)                            |
  | S1_ActualAcceleration     | float64 | actual acceleration of spindle (mm/s/s)                      |
  | S1_CommandPosition        | float64 | reference position of spindle (mm)                           |
  | S1_CommandVelocity        | float64 | reference velocity of spindle (mm/s)                         |
  | S1_CommandAcceleration    | float64 | reference acceleration of spindle (mm/s/s)                   |
  | S1_CurrentFeedback        | float64 | current (A)                                                  |
  | S1_DCBusVoltage           | float64 | voltage (V)                                                  |
  | S1_OutputCurrent          | float64 | current (A)                                                  |
  | S1_OutputVoltage          | float64 | voltage (V)                                                  |
  | S1_OutputPower            | float64 | current (A)                                                  |
  | S1_SystemInertia          | float64 | torque inertia (kg*m^2)                                      |
  | M1_CURRENT_PROGRAM_NUMBER | float64 | number the program is listed under on the CNC                |
  | M1_sequence_number        | float64 | line of G-code being executed                                |
  | M1_CURRENT_FEEDRATE       | float64 | instantaneous feed rate of spindle                           |
  | Machining_Process         | object  | the current machining stage being performed. Includes preparation, tracing up  and down the "S" curve involving different layers, and repositioning of the spindle as it moves through the air to a certain starting point |


- Two ways to use CNC measurements   

  (1) Taking every CNC measurement as an independent observation where the operation being performed is given in the Machining_Process column. Active machining operations are labeled as "Layer 1 Up", "Layer 1 Down", "Layer 2 Up", "Layer 2 Down", "Layer 3 Up", and "Layer 3 Down".    

  (2) Taking each one of the 18 experiments (the entire time series) as an observation for time series classification     

#### Paper  

1. [CNC Machine Tool’s wear diagnostic and prognostic by
   using dynamic bayesian networks](<https://hal.archives-ouvertes.fr/hal-00672204/document>)      

keywords: dynamic bayesian networks, Diagnostic, Prognostic, Remaining Useful Life, Condition
Based Maintenance, Hidden Markov Models, Monitoring data, Tool wear     


##### Data Download Link   
Data Capacity(Compressed):   

2.56MB   

Data Capacity(Raw):   

11.6MB   