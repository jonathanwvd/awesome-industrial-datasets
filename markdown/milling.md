# Milling

**Summary:** NASA milling machine tool wear dataset with 16 experiments on a milling machine; records spindle motor currents, vibrations, and acoustic emissions alongside measured flank wear (VB) for tool condition monitoring and remaining useful life research.

| Parameter | Value |
| --- | --- |
| **Associated Tasks** | Tool Wear Prediction, Remaining Useful Life, Regression, Prognostics |
| **Data Source** | Real |
| **Dataset Characteristics** | Multivariate, Time-Series |
| **Date Donated** | 2007 |
| **Feature Type** | Real |
| **Labeled** | Yes |
| **Missing Values** | No |
| **Name** | Milling |
| **Number of Features** | 8 sensor channels (AC/DC spindle motor current, table/spindle vibration, table/spindle acoustic emission, flank wear VB) plus operational parameters |
| **Number of Instances** | 16 experimental cases; 167 measurement runs total |
| **Source** | NASA Ames Prognostics Center of Excellence (PCoE) Data Repository |
| **Time Series** | Yes |

## Description

The NASA Milling dataset is part of the NASA Prognostics Center of Excellence (PCoE) Data Repository, contributed by A. Agogino and K. Goebel from UC Berkeley in 2007. The dataset was collected from a milling machine under 16 different experimental conditions varying cutting speed, feed rate, depth of cut, and material type. Each experiment produces multiple measurement runs with flank wear (VB) values recorded at irregular intervals.

Sensor channels include: AC spindle motor current, DC spindle motor current, table vibration, spindle vibration, acoustic emission at the table, and acoustic emission at the spindle. Operational parameters such as depth of cut, feed rate, and workpiece material are also provided. The data is stored as a MATLAB struct array; a CSV version is available on Kaggle and Hugging Face.

The primary research application is tool condition monitoring: predicting the current or future flank wear value (VB) from the sensor time series. The dataset has been used extensively in prognostics and health management research, including deep learning approaches for RUL estimation of cutting tools.

## Tags

Acoustic Emission, Milling Machine, NASA, Predictive Maintenance, Prognostics, Tool Wear, Vibration

## References

- [NASA PCoE Data Repository](https://ti.arc.nasa.gov/tech/dash/groups/pcoe/prognostic-data-repository/)
- [Milling dataset on Kaggle (CSV format)](https://www.kaggle.com/datasets/vinayak123tyagi/milling-data-set-prognostic-data)

[⬅️ Back to Index](../README.md)
