# Maintenance of Naval Propulsion Plants Data Set

**Summary:** Predicting Gas Turbine propulsion plant's decay state coefficient.

| Parameter | Value |
| --- | --- |
| **Name** | Maintenance of Naval Propulsion Plants Data Set |
| **Labeled** | Yes |
| **Time Series** | No |
| **Simulation** | Yes |
| **Missing Values** | No |
| **Dataset Characteristics** | Multivariate |
| **Feature Type** | Real |
| **Associated Tasks** | Regression, Classification |
| **Number of Instances** | 11934 |
| **Number of Features** | 16 |
| **Date Donated** | INA |
| **Source** | Kaggle |

## Dataset Information

The experiments have been carried out by means of a numerical simulator of a naval vessel (Frigate) characterized by a Gas Turbine (GT) propulsion plant. The different blocks forming the complete simulator (Propeller, Hull, GT, Gear Box, and Controller) have been developed and fine-tuned over the year on several similar real propulsion plants. In view of these observations, the available data are in agreement with a possible real vessel.
In this release of the simulator, it is also possible to take into account the performance decay over time of the GT components such as GT compressor and turbines.
The propulsion system behaviour has been described with these parameters:

- Ship speed (linear function of the lever position lp).
- Compressor degradation coefficient kMc.
- Turbine degradation coefficient kMt.
so that each possible degradation state can be described by a combination of this triple (lp,kMt,kMc).
The range of decay of compressor and turbine has been sampled with a uniform grid of precision 0.001 to have a good granularity of representation.
In particular for the compressor decay state discretization, the kMc coefficient has been investigated in the domain [1; 0.95], and the turbine coefficient in the domain [1; 0.975].
Ship speed has been investigated by sampling the range of feasible speed from 3 knots to 27 knots with a granularity of representation equal to three knots.
A series of measures (16 features) which indirectly represents the state of the system subject to performance decay has been acquired and stored in the dataset over the parameter's space.
Check the README.txt file for further details about this dataset.

## Attribute Information

A 16-feature vector containing the GT measures at steady state of the physical asset:
- Lever position (lp) []
- Ship speed (v) [knots]
- Gas Turbine (GT) shaft torque (GTT) [kN m]
- GT rate of revolutions (GTn) [rpm]
- Gas Generator rate of revolutions (GGn) [rpm]
- Starboard Propeller Torque (Ts) [kN]
- Port Propeller Torque (Tp) [kN]
- High Pressure (HP) Turbine exit temperature (T48) [°C]
- GT Compressor inlet air temperature (T1) [°C]
- GT Compressor outlet air temperature (T2) [°C]
- HP Turbine exit pressure (P48) [bar]
- GT Compressor inlet air pressure (P1) [bar]
- GT Compressor outlet air pressure (P2) [bar]
- GT exhaust gas pressure (Pexh) [bar]
- Turbine Injection Control (TIC) [%]
- Fuel flow (mf) [kg/s]
- GT Compressor decay state coefficient
- GT Turbine decay state coefficient.

## Tags

Naval propulsion, Predictive maintenance, Operational efficiency, System performance, Maritime data

## References

- [Kaggle Dataset](https://www.kaggle.com/datasets/elikplim/maintenance-of-naval-propulsion-plants-data-set)

[⬅️ Back to Index](../README.md)
