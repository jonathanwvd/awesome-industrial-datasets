## Chemical Detection Platform    
### [Gas sensor arrays in open sampling settings Data Set](https://archive.ics.uci.edu/ml/datasets/Gas+sensor+arrays+in+open+sampling+settings)

The dataset contains 18000 time-series recordings from a chemical detection platform at six different locations in a wind tunnel facility in response to ten high-priority chemical gaseous substances.  
The resulting dataset induces a **ten-class** gas discrimination problem   
The dataset was gathered from December 2010 to April 2012(16 months) in wind tunnel research test-bed facility situated at the BioCircuits Institute, University of California San Diego.    

![](https://img.shields.io/badge/sector-chemical-red.svg)
![](https://img.shields.io/badge/labeled-yes-blue.svg)
![](https://img.shields.io/badge/time--series-yes-blue.svg) ![](<https://img.shields.io/badge/simulation-yes-blue.svg>)     

#### Data Set Information    

| Data Set Characteristics  | Attribute Characteristics | Associated Tasks |
| ------------------------- | ------------------------- | ---------------- |
| Multivariate, Time-Series | Real                      | Classification   |

| Number of Instances | Number of Attributes | Number of Missing Values(NaN/not available) |
| ------------------- | -------------------- | ------------------------------------------- |
| 18,000              | 1,950,000            | ?                                           |


  - Number of instances:  
    18,000 times-series measurements recorded from a 72 metal-oxide gas sensor array-based chemical detection platform.  
  
  - Number of attributes:  
    Every measurement contains 72 time-series recorded during 260 seconds, each collected at a sample rate of 100Hz (samples per second).
    The dataset also contains time, temperature, and relative humidity information.  
    72 metal-oxide gas sensors + time, temperature, relative humidity information = 75 measurement types  
    The resulting dataset ultimately includes 75-time series composed of 26000 points.  
    Number of Attributes = 75 * 260* 100 = 1,950,000     
  
  - 10 classes gas name:   
    Acetone, Acetaldehyde, Ammonia, Butanol, Ethylene, Methane, Methanol, Carbon Monoxide, Benzene, Toluene     
  
  - The goal of this data:  
    Identify and discriminate the mentioned chemical hazards at relevant concentrations regardless of the location of the sensory system platform within the annotated wind tunnel research facility as well as the environmental and parametric conditions induced in the setting (Please see manuscript for more details).    


#### Attribute Information  
- Explanation of folder name  

  - Data consists of 11 folders: number of measurements per chemical class identity + nomial concentration   
    ex. Toluene_200 = gas identity is 'Toluene', measured at a concentration of 200 ppmv       
  - Each of 11 folders consists of 6 subfolders.: represent the line location within the test area of the wind tunnel  
    ex. L1 means location 1, L6 means location 6 (where L1 is closest to the gas source)    
  - Each of six subfolders consists of 300 files: it has a number of measurements measured at the corresponding location in the tunnel
    Meaning of each file name = log information of each of the measurements  
    ex.  
    201106060617_board_setPoint_500V_fan_setPoint_060_mfc_setPoint_Toluene_200ppm_p7  
    201106060617 = year, month, day, time  
    board_setPoint_500V = fixed operating temperature value   
    fan_setPoint_060 = set-point value of the nomial rotational speeds of the multiple-step motor-driven exhaust fan utilized    
    mfc_setPoint_Tolune_200ppm = analyte identity and concentration value for each particular measurement   
    p7 = line point location at which the chemo-sensory platform was located in the wind tunnel  

- Meaning of each column     
  - Each data file has 92 columns. The meaning of each column is as follows.    
  - For example, if line 1 is,  
    22250 0 0 100 100 100 103 103 105 22.22 63.43 1 476 555 803 497 775 885 873 843 1 346 545 635 616 571 552 773 745 1 397 509 660 638     755 744 745 657 1 420 510 525 531 504 650 719 715 1 2201 449 652 1228 847 654 850 737 1 370 459 650 445 756 773 847 803 1 345 457 587   554 757 704 769 818 1 354 407 499 696 786 686 757 733 1 339 418 547 567 653 573 773 84  
    The meaning of the value corresponding to each column is as follows  
    22250 = measured at 22.25 seconds  
    0 0 = set point, measured value of the fan speed  
    100 100 100 103 103 105 = set point, actual measured values of the MFC  
    22.22 63.43 = temperature, humidity values  
    1 = boundary between each sensor module board  
    remaining 80 columns = actual time series values for each measurement -> The eight numbers 1 of them represent the boundary and the remaining 72 represent the 72 time series mentioned above.       
#### Paper          

N/A       

##### Ambiguous Parts     
\- The number of columns is 92 in each of the data files. The number of rows is different.   
\- 75 time-series(72 gas sensor + time, temperature, relative humidity information) * 26000 = 1950000    

Why '1950000' is the number of attributes(This is ambiguous. 72 gas sensors, time, temperature and humidity total 75 should be attribute)    

Why 1950000 is the number of attributes?  

Is there NA? -> The data file was too large to verify.       

#### Citations   

Alexander Vergara, Jordi Fonollosa, Jonas Mahiques, Marco Trincavelli, Nikolai Rulkov, RamÃ³n Huerta, On the performance of gas sensor arrays in open sampling systems using Inhibitory Support Vector Machines, Sensors and Actuators B: Chemical, Available online 18 May 2013, ISSN 0925-4005, 10.1016/j.snb.2013.05.027. [(Web Link)](<https://www.sciencedirect.com/science/article/pii/S092540051300590X>)   

##### Data Folder Link    

[https://archive.ics.uci.edu/ml/machine-learning-databases/00251/](https://archive.ics.uci.edu/ml/machine-learning-databases/00251/)  

Data Capacity(Compressed)     

7.8GB  