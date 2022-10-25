## [ECO dataset](http://vs.inf.ethz.ch/res/show.html?what=eco-data)

![](https://img.shields.io/badge/sector-power-skyblue.svg) ![](https://img.shields.io/badge/labeled-yes-blue.svg) ![](https://img.shields.io/badge/simulation-no-red.svg)

The ECO (Electricity Consumption and Occupancy) data set is a comprehensive open-source (Creative Commons License CC BY 4.0) data set for non-intrusive load monitoring and occupancy detection research. It was collected in 6 Swiss households over a period of 8 months. For each of the households, the ECO data set provides:

- 1 Hz aggregate consumption data. Each measurement contains data on current, voltage, and phase shift for each of the three phases in the household.
- 1 Hz plug-level data measured from selected appliances.
- Occupancy information measured through a tablet computer (manual labeling) and a passive infrared sensor (in some of the households).

The files are coded in the following way. The first two digits (e.g., 01-06 identify the household). The next part {sm, plugs, occupancy} identifies the type of data (i.e., readings from the smart meter, the plugs and the occupancy ground truth). Lastly, where applicable, the suffix indicates the format of the data (either Matlab or plain CSV)

For each of the six households we collected aggregate electricity consumption data at 1 Hz using off-the-shelf smart meters. In total we collected more than 100 million measurements during the period of the deployment.

#### Variables

Household 1 : (1) Fridge, (2) dryer, (3) coffee machine, (4) kettle, (5) washing machine, (6) PC, (7) freezer.   
Household 2 : (1) Tablet, (2) dishwasher, (3) stove, (4) fridge, (5) TV, (6) stereo, (7) freezer, (8) kettle, (9) lamp, (10) laptops.  
Household 3 : (1) Tablet, (2) freezer, (3) coffee machine, (4) PC, (5) fridge, (6) kettle, (7) entertainment.  
Household 4 : (1) Fridge, (2) kitchen appliances3 , (3) lamp, (4) stereo & laptop, (5) freezer, (6) tablet, (7) entertainment, (8) microwave.  
Household 5 : (1) Tablet, (2) coffee machine, (3) kettle, (4) microwave, (5) fridge, (6) entertainment, (7) PC, router & printer, (8) fountain.  
Household 6 : (1) Lamp, (2) laptop & printer, (3) routers, (4) coffee machine, (5) en     

#### Paper

[The ECO Data Set and the Performance of Non-Intrusive Load Monitoring Algorithms](https://www.vs.inf.ethz.ch/publ/papers/beckel-2014-nilm.pdf)
