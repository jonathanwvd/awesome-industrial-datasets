# [ISDB - International Stiction Data Base](https://sites.ualberta.ca/~bhuang/Stiction-Book.htm)

![](https://img.shields.io/badge/sector-control_loop-darkgreen.svg)
![](https://img.shields.io/badge/labeled-yes-blue.svg)
![](https://img.shields.io/badge/time--series-yes-blue.svg) 
![](<https://img.shields.io/badge/simulation-no-red.svg>)

 Parameter | Value
---------- | -----
Data Set Characteristics | Time-series
Attribute Characteristics | Real
Associated Tasks | Classification
Number of Instances	| 
Number of Attributes |
Date Donated | 
Source | University of Alberta
Dataset size | 13.7 MB (compressed)

## Source
The industrial data were provided by courtesy of: 
- Ashish Singhal and Timothy Salsbury for loops BAS 1−8; 
- Alexander Horch for loops CHEM 1−3 and PAP 1−10; 
- Peter He and Joe Qin for loops CHEM 4−6; 
- Biao Huang for loops CHEM 7−12; 
- Nina Thornhill for loops CHEM 13−17 and CHEM 40−64; 
- Claudio Scali for loops CHEM 18−28 and CHEM 32−39; 
- Shoukat Choudhury and Sirish Shah for loops CHEM 29−31, PAP 11−13, POW 1−5 and MIN 1.

## Data Set Information  
This is an international database of industrial control loops (most of them suffering from stiction) from different fields. It was an outcome of a project initiated by Mohieddine Jelali during the writing of the book [Detection and Diagnosis of Stiction in Control Loops: State of the Art and Advanced Methods](https://sites.ualberta.ca/~bhuang/Stiction-Book.htm).

The data were provided by different international Colleagues (called Stiction Group) who have contributed to the book.
The Stiction Group has decided to publish the database to enable other researchers working on the field to test their own methods on industrial data.


## Attribute Information
The data are stored in a structure cdata that contains substructures.

Each data set contains: comments; brief comments; type (0: self-regulating; 1: integrating); sampling period [s]; and the data: t (time) [s], SP (set point), PV (process variable), OP (controller output), and (only for some loops) Kc (proportional gain), Ti (integration time constant), en (normalised control error SP − PV).

Example: PV for the chemical loop no. 19: pv = cdata.chemicals.loop19.PV.

## References

## Citation Request
1. M. Jelali, B. Huang (Eds.): Detection and Diagnosis of Stiction in Control Loops: State of the Art and Advanced Methods. Springer-Verlag London, 2010.
