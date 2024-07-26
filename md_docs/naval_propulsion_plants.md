# Naval Propulsion Plants

| Parameter | Value |
| --- | --- |
| Data Set Characteristics | Attribute Characteristics | Associated Tasks | |
| Attribute Characteristics | Associated Tasks | |
| Associated Tasks | | ------------------------ | ------------------------- | ---------------- | |
| Number of Instances | Number of Attributes |      |      | |
| Number of Attributes | |      | |

## Data Set Information
| Data Set Characteristics | Attribute Characteristics | Associated Tasks |
| ------------------------ | ------------------------- | ---------------- |
| Multivariate             | Real                      | Regression       |

| Number of Instances | Number of Attributes |      |      |
| ------------------- | -------------------- | ---- | ---- |
| 11934               | 16                   |      |      |

567.1KB (compressed)


> The experiments have been carried out by means of a numerical simulator of a naval vessel (Frigate) characterized by a Gas Turbine (GT) propulsion plant.

> The different blocks forming the complete simulator (Propeller, Hull, GT, Gear Box and Controller) have been developed and fine tuned over the year on several similar real propulsion plants.

> In this release of the simulator it is also possible to take into account the performance decay over time of the GT components such as GT compressor and turbines. The propulsion system behaviour has been described with this parameters:

- Ship speed (linear function of the lever position lp). 
- Compressor degradation coefficient kMc. 
- Turbine degradation coefficient kMt. 

so that each possible degradation state can be described by a combination of this triple (lp,kMt,kMc). 

The range of decay of compressor and turbine has been sampled with an uniform grid of precision 0.001 so to have a good granularity of representation. In particular for the compressor decay state discretization the kMc coefficient has been investigated in the domain [1; 0.95], and the turbine coefficient in the domain [1; 0.975]. Ship speed has been investigated sampling the range of feasible speed from 3 knots to 27 knots with a granularity of representation equal to three knots. 

A series of measures (16 features) which indirectly represents of the state of the system subject to performance decay has been acquired and stored in the dataset over the parameter's space. 

Ship speed has been investigated sampling the range of feasible speed from 3 knots to 27 knots with a granularity of representation equal to three knots.

A series of measures (16 features) which indirectly represents of the state of the system subject to performance decay has been acquired and stored in the dataset over the parameter's space.

## Attribute Information
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

## References

