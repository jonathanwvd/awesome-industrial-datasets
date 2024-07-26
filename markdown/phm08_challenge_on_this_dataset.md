# PHM08 Challenge on this dataset

| Parameter | Value |
| --- | --- |

## Data Set Information
Data sets consist of multiple multivariate time series. Each data set is further divided into training and test subsets. Each time series is from a different engine – i.e., the data can be considered to be from a fleet of engines of the same type. Each engine starts with different degrees of initial wear and manufacturing variation which is unknown to the user. This wear and variation is considered normal, i.e., it is not considered a fault condition. There are three operational settings that have a substantial effect on engine performance. These settings are also included in the data. The data are contaminated with sensor noise.
The engine is operating normally at the start of each time series, and starts to degrade at some point during the series. In the training set, the degradation grows in magnitude until a predefined threshold is reached beyond which it is not preferable to operate the engine. In the test set, the time series ends some time prior to complete degradation.  
The objective of the competition is to predict the number of remaining operational cycles before in the test set, i.e., the number of operational cycles after the last cycle that the engine will continue to operate properly.  
The data are provided as a zip-compressed text file with 26 columns of numbers, separated by spaces. Each row is a snapshot of data taken during a single operational cycle; each column is a different variable.

## Attribute Information
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


- Data Set  
  train.txt, test.txt, final_test.txt     
  Train trjectories: 218   
  Test trajectories: 218   
  final_test trajectoris: 435    
  'Train / Test' is used to create the model, and 'finally final_test' to calculate the final score.    
  (Once algorithms are trained to satisfaction, users can apply them to the final test dataset contained in the file named final_test.txt. )  
  The final score is the weighted sum of the RUL errors.

## References

