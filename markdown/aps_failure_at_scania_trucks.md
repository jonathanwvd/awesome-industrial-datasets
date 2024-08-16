# APS Failure at Scania Trucks

**Summary:** The datasets' positive class consists of component failures for a specific component of the APS system. The negative class consists of trucks with failures for components not related to the APS.

| Parameter | Value |
| --- | --- |
| **Name** | APS Failure at Scania Trucks |
| **Labeled** | Yes |
| **Time Series** | No |
| **Simulation** | No |
| **Missing Values** | Yes |
| **Dataset Characteristics** | Multivariate |
| **Feature Type** | Real, Integer |
| **Associated Tasks** | Classification |
| **Number of Instances** | 76000 |
| **Number of Features** | 171 |
| **Date Donated** | 2017-12-07 |
| **Source** | UCI Machine Learning Repository |

## Dataset Information

This file is part of APS Failure and Operational Data for Scania Trucks.

Copyright (c) <2016> <Scania CV AB>

This program (APS Failure and Operational Data for Scania Trucks) is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program.  If not, see <http://www.gnu.org/licenses/>.

------------------------------------------------------------------------

1. Title: APS Failure at Scania Trucks

2. Source Information
   -- Creator: Scania CV AB
               Vagnmakarvägen 1 
               151 32 Södertälje 
               Stockholm
               Sweden 
   -- Donor:   Tony Lindgren (tony@dsv.su.se) and Jonas Biteus (jonas.biteus@scania.com)
   -- Date:    September, 2016
 
3. Past Usage:
   Industrial Challenge 2016 at The 15th International Symposium on Intelligent Data Analysis (IDA) 
   -- Results:         
     The top three contestants                                                | Score | Number of Type 1 faults | Number of Type 2 faults
     ------------------------------------------------------------------------------------------------------------------------------------
     Camila F. Costa and Mario A. Nascimento                                  | 9920  | 542                     | 9
     Christopher Gondek, Daniel Hafner and Oliver R. Sampson                  | 10900 | 490                     | 12
     Sumeet Garnaik, Sushovan Das, Rama Syamala Sreepada and Bidyut Kr. Patra | 11480 | 398                     | 15

4. Relevant Information:
   -- Introduction
     The dataset consists of data collected from heavy Scania 
     trucks in everyday usage. The system in focus is the 
     Air Pressure system (APS) which generates pressurised 
     air that are utilized in various functions in a truck, 
     such as braking and gear changes. The datasets' 
     positive class consists of component failures 
     for a specific component of the APS system. 
     The negative class consists of trucks with failures 
     for components not related to the APS. The data consists 
     of a subset of all available data, selected by experts. 

   -- Challenge metric  

     Cost-metric of miss-classification:

     Predicted class |      True class       |
                     |    pos    |    neg    |
     -----------------------------------------
      pos            |     -     |  Cost_1   |
     -----------------------------------------
      neg            |  Cost_2   |     -     |
     -----------------------------------------
     Cost_1 = 10 and cost_2 = 500

     The total cost of a prediction model the sum of 'Cost_1' 
     multiplied by the number of Instances with type 1 failure 
     and 'Cost_2' with the number of instances with type 2 failure, 
     resulting in a 'Total_cost'.

     In this case Cost_1 refers to the cost that an unnecessary 
     check needs to be done by a mechanic at a workshop, while 
     Cost_2 refers to the cost of missing a faulty truck, 
     which may cause a breakdown.

     Total_cost = Cost_1*No_Instances + Cost_2*No_Instances.

5. Number of Instances: 
     The training set contains 60000 examples in total in which 
     59000 belong to the negative class and 1000 positive class. 
     The test set contains 16000 examples. 

6. Number of Attributes: 171 

7. Attribute Information:
   The attribute names of the data have been anonymized for 
   proprietary reasons. It consists of both single numerical 
   counters and histograms consisting of bins with different 
   conditions. Typically the histograms have open-ended 
   conditions at each end. For example if we measuring 
   the ambient temperature 'T' then the histogram could 
   be defined with 4 bins where: 

   bin 1 collect values for temperature T < -20
   bin 2 collect values for temperature T >= -20 and T < 0     
   bin 3 collect values for temperature T >= 0 and T < 20  
   bin 4 collect values for temperature T > 20 

   |  b1  |  b2  |  b3  |  b4  |   
   ----------------------------- 
         -20     0      20

  The attributes are as follows: class, then 
  anonymized operational data. The operational data have 
  an identifier and a bin id, like 'Identifier_Bin'.
  In total there are 171 attributes, of which 7 are 
  histogram variables. Missing values are denoted by 'na'.

## Tags

Scania trucks, APS system, Component failure, Predictive maintenance, Industrial data

## References

- [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/APS+Failure+at+Scania+Trucks)

[⬅️ Back to Index](../README.md)
