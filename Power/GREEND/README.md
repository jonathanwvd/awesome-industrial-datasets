## [GreenD: Energy metering data set](https://sourceforge.net/projects/greend/)

1.8GB (compressed)

GREEND is an energy dataset containing power measurements collected from multiple households in Austria and Italy. It provides detailed energy profiles on a per device basis with a sampling rate of 1 Hz.

![](https://img.shields.io/badge/sector-power-skyblue.svg) ![](https://img.shields.io/badge/labeled-implicit-green.svg) ![](https://img.shields.io/badge/simulation-no-red.svg) 

#### Data Set Information:

GREEND is the first 1Hz consumption dataset for Austria and Italy. The type and number of devices, as well as the number of monitored households significantly constraints the final application of the dataset. A statistical analysis of consumption behavior of residents would require a high number of households.

The measurement campaign was an ambitious aspect of the MONERGY project in which we monitored active power (Watts) at 1 Hz in selected households in the region of Carinthia (Austria) and Friuli-Venezia Giulia (Italy) for long term (1 year). We have been monitoring 8 households: 4 across the province of Udine (Italy) and 4 in the area of Klagenfurt (Austria).

The dataset was analyzed to model the energy demand in the regions and released to the research community for further studies. Each household(building0~7) is a different folder containing daily CSV files. Each file has the format timestamp, power for MAC1, power for MAC2, and so on, with MAC indicating in the header the network address of the Zigbee node used to collect the measurements.

In particular, the dataset was used for the following research areas:

1. Load disaggregation: identifying individual devices given an overall power measurement
2. Device usage modelling: predicting device operation in order to model users' preferences and plan control strategies
3. Occupancy modeling: given device usage inferring room and building occupancy, for instance to control thermostats
4. Autonomous device operation: learning controllers for small energy consumers/producers given power profiles and usage models extracted from real devices

#### Paper

[GREEND: An energy consumption dataset of households in Italy and Austria](https://www.researchgate.net/publication/262302322_GREEND_An_energy_consumption_dataset_of_households_in_Italy_and_Austria)

**Abstract**

Home energy management systems can be used to monitor and optimize consumption and local production from renewable energy. To assess solutions before their deployment, researchers and designers of those systems demand for energy consumption datasets. In this paper, we present the GREEND dataset, containing detailed power usage information obtained through a measurement campaign in households in Austria and Italy. We provide a description of consumption scenarios and discuss design choices for the sensing infrastructure. Finally, we benchmark the dataset with state-of-the-art techniques in load disaggregation, occupancy detection and appliance usage mining.

#### Citation Request

A. Monacchi, D. Egarter, W. Elmenreich, S. D’Alessandro, A. M. Tonello. GREEND: An Energy Consumption Dataset of Households in Italy and Austria. In proceedings of the 5th IEEE International Conference on Smart Grid Communications (SmartGridComm 14). November 2014, Venice, Italy.

**reference**

[kaggle dataset description](https://www.kaggle.com/p111110/greend-energy-dataset#dataset_2014-05-15.csv)