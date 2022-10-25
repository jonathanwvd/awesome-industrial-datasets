## [Condition Based Maintenance of Naval Propulsion Systems](https://archive.ics.uci.edu/ml/datasets/Condition+Based+Maintenance+of+Naval+Propulsion+Plants#)

567.1KB (compressed)

Data have been generated from a sophisticated simulator of a Gas Turbines (GT), mounted on a Frigate characterized by a COmbined Diesel eLectric And Gas (CODLAG) propulsion plant type.

 ![](https://img.shields.io/badge/sector-mechanical-purple.svg)  ![](https://img.shields.io/badge/labeled-yes-blue.svg)  ![](https://img.shields.io/badge/time--series-no-red.svg)  ![](<https://img.shields.io/badge/simulation-yes-blue.svg>)

#### Data Set Information

| Data Set Characteristics | Attribute Characteristics | Associated Tasks |
| ------------------------ | ------------------------- | ---------------- |
| Multivariate             | Real                      | Regression       |

| Number of Instances | Number of Attributes |      |      |
| ------------------- | -------------------- | ---- | ---- |
| 11934               | 16                   |      |      |

> The experiments have been carried out by means of a numerical simulator of a naval vessel (Frigate) characterized by a Gas Turbine (GT) propulsion plant.
>
> The different blocks forming the complete simulator (Propeller, Hull, GT, Gear Box and Controller) have been developed and fine tuned over the year on several similar real propulsion plants.
>
> In this release of the simulator it is also possible to take into account the performance decay over time of the GT components such as GT compressor and turbines. The propulsion system behaviour has been described with this parameters:

- Ship speed (linear function of the lever position lp). 
- Compressor degradation coefficient kMc. 
- Turbine degradation coefficient kMt. 

so that each possible degradation state can be described by a combination of this triple (lp,kMt,kMc). 

The range of decay of compressor and turbine has been sampled with an uniform grid of precision 0.001 so to have a good granularity of representation. In particular for the compressor decay state discretization the kMc coefficient has been investigated in the domain [1; 0.95], and the turbine coefficient in the domain [1; 0.975]. Ship speed has been investigated sampling the range of feasible speed from 3 knots to 27 knots with a granularity of representation equal to three knots. 

A series of measures (16 features) which indirectly represents of the state of the system subject to performance decay has been acquired and stored in the dataset over the parameter's space. 

Ship speed has been investigated sampling the range of feasible speed from 3 knots to 27 knots with a granularity of representation equal to three knots.

A series of measures (16 features) which indirectly represents of the state of the system subject to performance decay has been acquired and stored in the dataset over the parameter's space. 

#### Variables

A 16-feature vector containing the GT measures at steady state of the physical asset:   

1 - Lever position (lp) [ ]  
2 - Ship speed (v) [knots]   
3 - Gas Turbine shaft torque (GTT) [kN m]  
4 - Gas Turbine rate of revolutions (GTn) [rpm]  
5 - Gas Generator rate of revolutions (GGn) [rpm]  
6 - Starboard Propeller Torque (Ts) [kN]  
7 - Port Propeller Torque (Tp) [kN]  
8 - HP Turbine exit temperature (T48) [C]  
9 - GT Compressor inlet air temperature (T1) [C]  
10 - GT Compressor outlet air temperature (T2) [C]  
11 - HP Turbine exit pressure (P48) [bar]  
12 - GT Compressor inlet air pressure (P1) [bar]  
13 - GT Compressor outlet air pressure (P2) [bar]  
14 - Gas Turbine exhaust gas pressure (Pexh) [bar]  
15 - Turbine Injecton Control (TIC) [%]  
16 - Fuel flow (mf) [kg/s]  

17 - GT Compressor decay state coefficient. (kMc, 0.95~1) 

17 - GT Compressor decay state coefficient. (kMc) 

18 - GT Turbine decay state coefficient. (kMt)

**NOTE**

- Features are not normalized
- Each feature vector is a row on the text file (18 elements in each row)

#### Paper

[Condition-Based Maintenance of Naval Propulsion Systems with supervised Data Analysis](https://github.com/makinarocks/awesome-industrial-machine-datasets/blob/master/data-explanation/Naval%20Propulsion%20Plants/Cipollini_etal_OE_2018_Condition_based_maintenance_of_naval_propulsion_systems_with_supervised_data_analysis.pdf) 

**highlights**

- A real-data validated model for the performance decay assessment of the main propulsion plant systems is presented.
- Data-Driven models to investigate the problem of performing Condition-Based Maintenance on a ship propulsion system.
- Several state-of-the-art supervised learning techniques are adopted.
- Unsupervised [learning algorithms](https://www.sciencedirect.com/topics/engineering/learning-algorithm) for [anomaly detection](https://www.sciencedirect.com/topics/engineering/anomaly-detection).
- The results confirm that it is possible to treat a CBM problem in a supervised fashion adopting regression techniques.

Abstract

Depending on the adopted strategy, impact of maintenance on overall expenses can remarkably vary.

The behavior and interaction of the [main components](https://www.sciencedirect.com/topics/engineering/main-component) of Ship [Propulsion](https://www.sciencedirect.com/topics/earth-and-planetary-sciences/propulsion) Systems cannot be easily modeled with a priori physical knowledge, considering the large amount of variables influencing them. Data-Driven Models (DDMs), instead, exploit advanced statistical techniques to build models directly on the large amount of historical data collected by on-board [automation systems](https://www.sciencedirect.com/topics/engineering/automation-system), **without requiring any a [priori knowledge](https://www.sciencedirect.com/topics/engineering/priori-knowledge)**. DDMs are extremely useful when it comes to continuously monitoring the propulsion equipment and take decisions based on the [actual condition](https://www.sciencedirect.com/topics/engineering/actual-condition) of the propulsion plant. In this paper, the authors investigate the problem of performing Condition-Based Maintenance through the use of DDMs. In order to conceive this purpose, several state-of-the-art [supervised learning](https://www.sciencedirect.com/topics/earth-and-planetary-sciences/supervised-learning) techniques are adopted, which require labeled sensor data in order to be deployed. **A [naval vessel](https://www.sciencedirect.com/topics/engineering/naval-vessels), characterized by a combined diesel-electric and gas propulsion plant, has been exploited to collect such data and show the effectiveness of the proposed approaches.** Because of confidentiality constraints with the Navy the authors used a real-data validated [simulator](https://www.sciencedirect.com/topics/engineering/simulators) and the [dataset](https://www.sciencedirect.com/topics/engineering/dataset) has been published for free use through the UCI repository.

#### Citation Request:

[1] A. Coraddu, L. Oneto, A. Ghio, S. Savio, D. Anguita, M. Figari, Machine Learning Approaches for Improving Condition?Based Maintenance of Naval Propulsion Plants, Journal of Engineering for the Maritime Environment, 2014, DOI: 10.1177/1475090214540874, (In Press) 

@article{Coraddu2013Machine, 
author={Coraddu, Andrea and Oneto, Luca and Ghio, Alessandro and 
Savio, Stefano and Anguita, Davide and Figari, Massimo}, 
title={Machine Learning Approaches for Improving Condition?Based Maintenance of Naval Propulsion Plants}, 
journal={Journal of Engineering for the Maritime Environment}, 
volume={--}, 
number={--}, 
pages={--}, 
year={2014} 
}