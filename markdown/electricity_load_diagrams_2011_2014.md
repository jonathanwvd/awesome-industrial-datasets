# Electricity Load Diagrams 2011-2014

**Summary:** This data set contains electricity consumption of 370 points/clients.

| Parameter | Value |
| --- | --- |
| **Name** | Electricity Load Diagrams 2011-2014 |
| **Labeled** | Yes |
| **Time Series** | Yes |
| **Simulation** | No |
| **Missing Values** | No |
| **Dataset Characteristics** | Time-Series |
| **Feature Type** | Real |
| **Associated Tasks** | Regression, Clustering |
| **Number of Instances** | 370 |
| **Number of Features** | 140256 |
| **Date Donated** | 2015-03-12 |
| **Source** | UCI Machine Learning Repository |

## Dataset Information

Data set has no missing values.
Values are in kW of each 15 min. To convert values in kWh values must be divided by 4.
Each column represent one client. Some clients were created after 2011. In these cases consumption were considered zero.
All time labels report to Portuguese hour. However all days present 96 measures (24*4). Every year in March time change day (which has only 23 hours) the values between 1:00 am and 2:00 am are zero for all points.
Every year in October time change day (which has 25 hours) the values between 1:00 am and 2:00 am aggregate the consumption of two hours.

## Tags

Electricity consumption, Time-series data, Energy monitoring, Smart grid, Urban energy use

## References

- [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/ElectricityLoadDiagrams20112014)

[⬅️ Back to Index](../README.md)
