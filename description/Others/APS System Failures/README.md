## [APS Failure at Scania Trucks Data Set](https://archive.ics.uci.edu/ml/datasets/APS+Failure+at+Scania+Trucks)

aps_failure_test_set.csv : 11.9MB (16,000)

aps_failure_training_set.csv : 44.7MB (60,000)

The datasets' positive class consists of component failures for a specific component of the APS system. The negative class consists of trucks with failures for components not related to the APS.

![](https://img.shields.io/badge/sector-etc-black.svg) ![](https://img.shields.io/badge/labeled-yes-blue.svg) ![](https://img.shields.io/badge/time--series-no-red.svg) ![](https://img.shields.io/badge/failure%20classification-gray.svg) ![](<https://img.shields.io/badge/simulation-no-red.svg>)

#### Data Set Information:

| Data Set Characteristics | Attribute Characteristics | Associated Tasks |
| ------------------------ | ------------------------- | ---------------- |
| Multivariate             | Integer, Real             | Classification   |

| Number of Instances | Number of Attributes |      |      |
| ------------------- | -------------------- | ---- | ---- |
| 60000               | 171                  |      |      |

**Introduction**
The dataset consists of data collected from heavy Scania trucks in everyday usage.

The system in focus is the Air Pressure system (APS) which generates pressurised air that are utilized in various functions in a truck, such as braking and gear changes.

- The positive class consists of component failures for a specific component of the APS system.
- The negative class consists of trucks with failures for components not related to the APS.

The data consists of a subset of all available data, selected by experts. (in order to guarantee the quality of the predictive model)

**Challenge metric**

Cost-metric of miss-classification: 

Predicted class | True class | 

| pos | neg | 

pos | - | Cost_1 | 

neg | Cost_2 | - | 

Cost_1(FP) = 10 and cost_2(FN) = 500 

The total cost of a prediction model the sum of 'Cost_1' multiplied by the number of Instances with type 1 failure(FP) and 'Cost_2' with the number of instances with type 2 failure(FN), resulting in a 'Total_cost'.

In this case Cost_1 refers to the cost that an unnecessary check needs to be done by an mechanic at an workshop, while Cost_2 refer to the cost of missing a faulty truck, which may cause a breakdown. 

Total_cost = Cost_1 * Num_Instances + Cost_2 * Num_Instances. 

**Number of Instances:**

The training set contains 60000 examples in total in which 59000 belong to the negative class and 1000 positive class. The test set contains 16000 examples.

**Attribute Information: **

The attribute names of the data have been **anonymized** for proprietary reasons. It consists of both single numerical counters and histograms consisting of bins with different conditions. Typically the histograms have open-ended conditions at each end. For example if we measuring the ambient temperature 'T' then the histogram could be defined with 4 bins where: 

bin 1 collect values for temperature T < -20 
bin 2 collect values for temperature T >= -20 and T < 0 
bin 3 collect values for temperature T >= 0 and T < 20 
bin 4 collect values for temperature T > 20 

| b1 | b2 | b3 | b4 | 

-20 0 20 

The attributes are as follows: class, then anonymized operational data. The operational data have an identifier and a bin id, like 'Identifier_Bin'. 
In total there are 171 attributes, of which **7 are histogram variables.** Missing values are denoted by 'na'.

#### Paper

[Prediction of Failures in the Air Pressure System of Scania Trucks using a Random Forest and Feature Engineering](https://www.researchgate.net/publication/309195602_Prediction_of_Failures_in_the_Air_Pressure_System_of_Scania_Trucks_Using_a_Random_Forest_and_Feature_Engineering)

This paper demonstrates an approach in data analysis to minimize overall maintenance costs for the air pressure system of Scania trucks. Feature creation on histograms was used. Randomly chosen subsets of attributes were then evaluated to generate an order and a final subset of features. Finally, a Random Forest was applied and finetuned. The results clearly show that data analysis in the field is beneficial and improves upon the naive approaches of checking every truck or no truck until failure.

**Data Understanding**

The data given to us contains a training set and a test set. The training set contains 60,000 rows, of which 1,000 belong to the positive class and 171 columns, of which one is the class column.

All attributes are numeric. **70 of these attributes belong to 7 histograms with ten bins each.** Based on visual inspection we guessed, that the sum across each histogram indicates the age of the APS.

Also, most failures could be predicted by using one or two features. It appeared that the hard part is to correctly predict failures for records that are actually very close to the non-failure class. Some visual inspection methods we used were:
– Box plots to get an overview of the variance of the values.
– Scatter plots to see how the classes are spread.
– Radar charts to recognize outliers.

[Combining Boosted Trees with Metafeature Engineering for Predictive Maintenance](https://www.researchgate.net/publication/313067390_Combining_Boosted_Trees_with_Metafeature_Engineering_for_Predictive_Maintenance)

The exploratory analysis of the data enabled to outlined two important conditions:

(1) high quantity of missing values

(2) high imbalance in the class distribution

#### Citation Request:

Please refer to the Machine Learning Repository's [citation policy](https://archive.ics.uci.edu/ml/citation_policy.html) 