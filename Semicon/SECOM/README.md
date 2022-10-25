## Semicon  
### [SECOM](http://archive.ics.uci.edu/ml/datasets/secom): Semiconductor manufacturing process data.    

FAB data collected from 590 sensors in the semiconductor manufacturing process. Data consists of two files, 'secom.data' and 'secom_labels.data'. The 'secom.data' file consists of 1567 * 590 matrices with 590 features and 1567 examples. 'secom_labels.data' file contains classifications value and data time stamp value for each 1567 data. In 'secom_labels.data' file, -1 indicates pass (normal) and 1 indicates fail (abnormal).       

![](https://img.shields.io/badge/sector-semicon-blue.svg)
![](https://img.shields.io/badge/labeled-yes-blue.svg)
![](https://img.shields.io/badge/time--series-yes-blue.svg)
![](https://img.shields.io/badge/feature_selection-gray.svg) ![](<https://img.shields.io/badge/simulation-no-red.svg>)         

#### Data Set Information      


- Note      

There is no distinction between training data and test data in the data file.   
590 __variables__ -> 590 __sensors__      
[On the UCI homepage](http://archive.ics.uci.edu/ml/datasets/secom), the number of features was specified as 591, but as a result of directly loading the data, the shape of 'secom.data' converted to dataframe had a shape of (1567, 590). Big Data Technologies and Applications (Springer International Publishing. (2018)) also identified 590 features.      

- Data Summary       

| Data Set Characteristics | Attribute Characteristics | Associated Tasks                   |
| ------------------------ | ------------------------- | ---------------------------------- |
| Multivariate             | Real                      | Classification, Casual - Discovery |

| Number of Instances | Number of Attributes | Number of Missing Values(NaN) in secom.data |
| ------------------- | -------------------- | ------------------------------------------- |
| 1567                | 590                  | 41951(# of NA in 1567 by 590 matrix)        |

- \# of each class    

| Number of pass | Number of fail | total |
| -------------- | -------------- | ----- |
| 1463           | 104            | 1567  |

#### Paper     

1. [redictive Models for Equipment Fault Detection in the Semiconductor Manufacturing Process](http://www.ijetch.org/vol8/898-T10023.pdf)    
2. [Machine learning for sensor-based manufacturing processes](https://ieeexplore.ieee.org/document/8116997) : keywords: feature selection, random forest, gradient boosted trees , PCA, Logistic Regression    
3. [Rare Class Discovery Techniques for Highly Imbalanced Data](<http://www.iaeng.org/publication/IMECS2013/IMECS2013_pp269-272.pdf>)     
4. [Feature Selection and Boosting Techniques to Improve Fault Detection Accuracy in the Semiconductor Manufacturing Process](<http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.421.3370&rep=rep1&type=pdf>)      
5. [Data Imbalance Problem solving for SMOTE Based Oversampling: Study on Fault Detection Prediction
   Model in Semiconductor Manufacturing Process](<https://pdfs.semanticscholar.org/df3b/537f5912bef4dca1659bae8ef360bbf69782.pdf>)        

#### Citations    

McCann, M. and Johnston, A. (2008). UCI Machine Learning Repository [<http://archive.ics.uci.edu/ml/datasets/secom>].        


##### Data Download Link   
[http://archive.ics.uci.edu/ml/machine-learning-databases/secom/](http://archive.ics.uci.edu/ml/machine-learning-databases/secom/)    

Data Capacity     

secom.data : 5.13MB    

secom.names : 5KB    

secom_labels.data :   40KB   