# APS Failure at Scania Trucks

| Parameter | Value |
| --- | --- |
| Dataset Characteristics | Multivariate |
| Feature Type | Integer, Real |
| Associated Tasks | Classification |
| Number of Instances | 60000 |
| Number of Features | 171 |
| Date Donated | 2017-12-07 |
| Source | UCI Machine Learning Repository |

## Dataset Information
The datasets' positive class consists of component failures for a specific component of the APS system. The negative class consists of trucks with failures for components not related to the APS.

## Variable Information
Attribute Information:
   The attribute names of the data have been anonymized for proprietary reasons. It consists of both single numerical counters and histograms consisting of bins with different conditions. Typically the histograms have open-ended conditions at each end. For example, if we are measuring the ambient temperature 'T' then the histogram could be defined with 4 bins where: 

   bin 1 collect values for temperature T < -20
   bin 2 collect values for temperature T >= -20 and T < 0
   bin 3 collect values for temperature T >= 0 and T < 20
   bin 4 collect values for temperature T > 20

   The attributes are as follows: class, then anonymized operational data. The operational data have an identifier and a bin id, like 'Identifier_Bin'. In total there are 171 attributes, of which 7 are histogram variables. Missing values are denoted by 'na'.

## References
- [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/APS+Failure+at+Scania+Trucks)

