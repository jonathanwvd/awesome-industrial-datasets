## [Steel Plates Faults Data Set](http://archive.ics.uci.edu/ml/datasets/Steel+Plates+Faults)

Faults.NNA : 292KB

Faults27x7 var : 497Byte

 ![](https://img.shields.io/badge/sector-steal-gray.svg) ![](https://img.shields.io/badge/labeled-yes-blue.svg)  ![](<https://img.shields.io/badge/simulation-no-red.svg>) ![](https://img.shields.io/badge/time--series-no-red.svg)  ![](https://img.shields.io/badge/fault_classification-gray.svg)

#### Data Set Information

| Data Set Characteristics | Attribute Characteristics | Associated Tasks |
| ------------------------ | ------------------------- | ---------------- |
| Multivariate             | Real                      | Classification   |

| Number of Instances | Number of Attributes |      |      |
| ------------------- | -------------------- | ---- | ---- |
| 1941                | 27                   |      |      |

A dataset of steel plates’ faults, classified into 7 different types. The goal was to train machine learning for automatic pattern recognition.

Dataset has 7 binary features that describe the 27 features describing fault(location, size,...) and type of fault(one of 7: Pastry, Z_Scratch, K_Scatch, Stains, Dirtiness, Bumps, Other_Faults). The type part of t he fault is also used as a binary classification target('common' or 'other' fault).

The last 7 columns are one hot encoded classes, i.e. if the plate fault is classified as "Stains" there will be a 1 in that column and 0's in the other columns. If you are unfamiliar with one hot encoding, just know that the last seven columns are your class labels.

All dataset records indicate a superficial fault of stainless steel leaf. There are six types of faults: The fault description consists of 27 indicators that indicate the geometry of the fault and its outline.

#### Variables

27 Independent variables

X_Minimum  
X_Maximum  
Y_Minimum   
Y_Maximum  
Pixels_Areas  
X_Perimeter  
Y_Perimeter  
Sum_of_Luminosity  
Minimum_of_Luminosity  
Maximum_of_Luminosity  
Length_of_Conveyer  
TypeOfSteel_A300  
TypeOfSteel_A400  
Steel_Plate_Thickness  
Edges_Index  
Empty_Index  
Square_Index  
Outside_X_Index  
Edges_X_Index  
Edges_Y_Index  
Outside_Global_Index  
LogOfAreas  
Log_X_Index  
Log_Y_Index   
Orientation_Index  
Luminosity_Index  
SigmoidOfAreas   

Type of dependent variables(7 Types of Steel Plates Faults) - one hot encoding

**the last seven columns are class labels.**

Pastry  
Z_Scratch  
K_Scatch  
Stains  
Dirtiness  
Bumps  
Other_Faults  

#### paper

[MetaNet*: The Theory of Independent Judges](https://www.researchgate.net/publication/13731626_MetaNet_The_Theory_of_Independent_Judges)

**Classification of Six Types of Surface Defects in Stainless Steel Plates**

The goal is to accurately classify the types of surface defects in stainless steel plates with six possible types of defects

#### Citation Request:

dataset provided by Semeion, Research Center of Sciences of Communication, Via Sersale 117, 00128, Rome, Italy. www.semeion.it