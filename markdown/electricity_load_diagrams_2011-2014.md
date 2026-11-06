# ElectricityLoadDiagrams20112014

**Summary:** Electricity consumption of 370 clients in kW for every 15 minutes, stored as one semicolon-separated text file with one column per client.

| Parameter | Value |
| --- | --- |
| **Domain** | Energy and power |
| **Asset / Process** | Power grids and plants |
| **Modality** | Time series |
| **Task** | Regression |
| **Annotation** | — |
| **Source Type** | Real production |
| **Access** | UCI repository |
| **Size** | 370 clients |
| **Year** | 2015 |
| **License** | CC BY |

## Description

ElectricityLoadDiagrams20112014 was created by Artur Trindade and donated to the UCI Machine Learning Repository in 2015. It is a time series data set whose associated tasks are regression and clustering.

The consumption of 370 points or clients sits in one text file, LD2011_2014.txt (678.1 MB, a 249.2 MB download), saved in CSV format with semicolons. The first column holds the date and time as 'yyyy-mm-dd hh:mm:ss', and each other column is one client, with 140,256 values per client. Values are in kW for each 15 minutes; dividing by 4 gives kWh.

Every day has 96 measures (24 x 4), and the time labels follow Portuguese hour. On the March time change day, values between 1:00 and 2:00 am are zero for all points; on the October one, the same hour aggregates the consumption of two hours. For clients created after 2011, the earlier consumption is set to zero, and there are no missing values. The license is CC BY 4.0.

## References

- [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/ElectricityLoadDiagrams20112014)
- [Industrial Atlas page](https://www.indatlas.com/datasets/electricity-load-diagrams-2011-2014/)

[⬅️ Back to Index](../README.md)
