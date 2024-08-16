# Gas sensor arrays in open sampling settings

**Summary:** The dataset contains 18000 time-series recordings from a chemical detection platform at six different locations in a wind tunnel facility in response to ten high-priority chemical gaseous substances

| Parameter | Value |
| --- | --- |
| **Name** | Gas sensor arrays in open sampling settings |
| **Labeled** | Yes |
| **Time Series** | Yes |
| **Simulation** | No |
| **Missing Values** | No |
| **Dataset Characteristics** | Multivariate, Time-Series |
| **Feature Type** | Real |
| **Associated Tasks** | Classification |
| **Number of Instances** | 18000 |
| **Number of Features** | 1950000 |
| **Date Donated** | 2013-06-04 |
| **Source** | UCI Machine Learning Repository |

## Dataset Information

Number of instances:
18000 time-series measurements recorded from a 72 metal-oxide gas sensor array-based chemical detection platform.

Number of attributes (features):
Every measurement contains 72 time-series recorded during 260 seconds, each collected at a sample rate of 100 Hz (samples per second).
The dataset also contains time, temperature, and relative humidity information.
The resulting dataset ultimately includes 75-time series composed of 26000 points.

This archive contains 18000 time-series measurement recordings collected from an array of 72 metal-oxide gas sensors composing our sensing platform utilized in the detection and identification of potentially-dangerous chemical gaseous substances under complex environmental conditions, as reported in the related manuscript below. Our primary purpose is to make our dataset freely accessible online to the chemo-sensing research and machine-learning communities, as well as other interested communities, to develop alternative competitive solutions relevant to gas-sensing discrimination tasks in open sampling settings, such as the one pursued here, and/or navigation. The dataset can be used exclusively for research purposes. Commercial purposes are fully excluded.
The dataset was gathered from December 2010 to April 2012 (16 months) in a 2.5 m Ã— 1.2 m Ã— 0.4 m wind tunnel research test-bed facility situated at the BioCircuits Institute, University of California San Diego. Specifically, our customized research facility, endowed with a computer-supervised mass flow controller-based continuous flow gas delivery system, operates in a propulsion open-cycle mode, by continuously drawing external turbulent air into and throughout the tunnel and exhausting it back to the outside, thereby creating a relatively less-turbulent airflow moving downstream towards the end of the test field, which is particularly suitable for applications pursued here that require injecting chemical poisonous agents or explosive mixtures because it prevents saturation. Being operated by a fully computerized environment â€” controlled by a player/stage robot server software programmed on C++ on a PC fitted with the appropriate serial cards â€” and with minimum human intervention, the designed wind tunnel test-bed facility provides versatility for releasing the chemical substances of interest at the desired concentrations with high accuracy and in a highly reproducible manner during the entire experiment and simultaneously in preserving the appropriate environmental conditions to generate chemical gas plumes exhibiting turbulent patterns. A graphical illustration of the designed wind tunnel test-bed facility considered in this study along with the characteristics of the geometry of the problem as well as the exact locations of the chemical analyte source and chemo-sensory platform is presented in Figure 2 of the manuscript cited below. Actual pictures of the designed wind tunnel are also presented in the Supplementary Material, Figure S.1 of the accompanying manuscript.
The resulting dataset induces a ten-class gas discrimination problem, comprising recordings from ten distinct pure chemical gases, namely Acetone, Acetaldehyde, Ammonia, Butanol, Ethylene, Methane, Methanol, Carbon Monoxide, Benzene, and Toluene. The goal is to identify and discriminate the mentioned chemical hazards at relevant concentrations regardless of the location of the sensory system platform within the annotated wind tunnel research facility as well as the environmental and parametric conditions induced in the setting (Please see manuscript for more details). See Table 1 on Vergara et a. 2013 (manuscript below) for specifics on the identity of chemical analyte hazards as well as their nominal concentration values at the outlet of the gas source in parts-per-million by volume (ppmv). Please refer to the manuscript below for more details of the wind tunnel test-bed facility as well as for specifics on the collection procedure followed and the operating and environmental parameters utilized during the creation of the aforementioned dataset.

## Tags

Gas sensing, Sensor arrays, Environmental monitoring, Chemical detection, Open sampling settings

## References

- [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/Gas+sensor+arrays+in+open+sampling+settings)

[⬅️ Back to Index](../README.md)
