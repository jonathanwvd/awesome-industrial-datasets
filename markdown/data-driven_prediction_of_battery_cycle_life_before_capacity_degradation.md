# Data-driven prediction of battery cycle life before capacity degradation

| Parameter | Value |
| --- | --- |
| Data Set Characteristics | Attribute Characteristics	| Real |
| Attribute Characteristics | Real |
| Associated Tasks | Number of Instances	| |
| Number of Instances | Number of Attributes	| |
| Number of Attributes | Date Donated | |
| Date Donated | Source | |
| Source | Dataset size | |
| Dataset size | ## Data Set Information |

## Data Set Information
- Data Set Characteristics: Multivariate
- Attribute Characteristic: Real
- Associated Tasks: Regression
- Size: 2.82GB , 1.8GB, 3.01GB

This dataset, used in “Data-driven prediction of battery cycle life before capacity degradation”, consists of 124 commercial lithium-ion batteries cycled to failure under fast-charging conditions.x

These lithium-ion phosphate (LFP)/graphite cells, manufactured by A123 Systems (APR18650M1A), were cycled in horizontal cylindrical fixtures on a 48-channel Arbin LBT potentiostat in a forced convection temperature chamber set to 30°C. The cells have a nominal capacity of 1.1 Ah and a nominal voltage of 3.3 V.

## Attribute Information
The data is presented in two different files: Each file contains the data from one mixture. The file ethylene_CO.txt contains the recordings from the sensors when exposed to mixtures of Ethylene and CO in air. The file ethylene_methane.txt contains the acquired time series induced by the mixture of Methane and Ethylene in air.

The structure of the files is the same: Data is distributed in 19 columns. First column represents time (in seconds), second column represents Methane (or CO) concentration set point (in ppm), third column details Ethylene concentration set point (in ppm), and the following 16 columns show the recordings of the sensor array.

Files include a header (one line) with the information of each column:

Time (seconds), Methane conc (ppm), Ethylene conc (ppm), sensor readings (16 channels)

The order of the sensors in the files is as follows:
TGS2602; TGS2602; TGS2600; TGS2600; TGS2610; TGS2610; TGS2620; TGS2620; TGS2602; TGS2602; TGS2600; TGS2600; TGS2610; TGS2610; TGS2620; TGS2620

Sensors' readings can be converted to KOhms by 40.000/S_i, where S_i is the value provided in the text files.

## References

