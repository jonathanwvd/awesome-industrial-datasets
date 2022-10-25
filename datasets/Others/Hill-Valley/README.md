## [Hill-Valley Data Set](https://archive.ics.uci.edu/ml/datasets/Hill-Valley)

Hill_Valley_with_noise_Training.data (417.4KB)
Hill_Valley_with_noise_Testing.data (420.9KB)
Hill_Valley_without_noise_Training.data (722.7KB)
Hill_Valley_without_noise_Testing.data (722.8KB)

This is NOT a manufacturing dataset, but looks good for testing pattern detection methods.

Two simulated data sets, with and without noise. Each record represents 100 points on a twodimensional graph, where the algorithm must classify the series as either a Hill (a “bump” in the terrain) or a Valley (a “dip” in the terrain).

![](https://img.shields.io/badge/sector-etc-black.svg) ![](https://img.shields.io/badge/labeled-yes-blue.svg) ![](<https://img.shields.io/badge/simulation-no-red.svg>) ![](https://img.shields.io/badge/time--series-no-red.svg)

#### Data Set Information:

| Data Set Characteristics | Attribute Characteristics | Associated Tasks |
| ------------------------ | ------------------------- | ---------------- |
| Sequential               | Real                      | Classification   |

| Number of Instances | Number of Attributes | Number of Classes |      |
| ------------------- | -------------------- | ----------------- | ---- |
| 1212                | 101                  | 2                 |      |

feature : V1~V100, Class

- 100 predictive attributes, 1 goal attribute

- 1-100 : Labeled x##. Floating point values (numeric)
- 101 : Labeled class. Binary {0,1} representing {valley,hill} (nominal)

number of instance

- training 606, test 606

Each record represents 100 points on a two-dimensional graph. When plotted in order (from 1 through 100) as the Y co-ordinate, the points will create either a Hill (a “bump” in the terrain) or a Valley (a “dip” in the terrain). 

There are six files, as follows: 

(a) Hill_Valley_without_noise_Training.data (class distribution : 305/301)  
(b) Hill_Valley_without_noise_Testing.data (295/311)

These first two datasets (without noise) are a training/testing set pair where the hills or valleys have a smooth transition. 

(c) Hill_Valley_with_noise_Training.data (307/299)  
(d) Hill_Valley_with_noise_Testing.data (299/307)

These next two datasets (with noise) are a training/testing set pair where the terrain is uneven, and the hill or valley is not as obvious when viewed closely. 

(e) Hill_Valley_sample_arff.text 

The sample ARFF file is useful for setting up experiments, but is not necessary.

1~100 is numeric, class is {0,1}

(f) Hill_Valley_visual_examples.jpg 

This graphic file shows two example instances from the data. 

- Example of 'valley' instance from Hill-Valley without noise
- Example of 'hill' instance from Hill-Valley dataset with noise

#### Variables

1-100: Labeled “X##”. Floating point values (numeric) 
101: Labeled “class”. Binary {0, 1} representing {valley, hill} 

task : supervised classification on hill-valley

#### Citation Request:

Please refer to the Machine Learning Repository's [citation policy](https://archive.ics.uci.edu/ml/citation_policy.html)

**reference**

https://www.simonwenkel.com/2018/08/19/revisiting_ml_hill_valley_detection.html

https://www.openml.org/d/1566
