# Appliances Energy Prediction

**Summary:** Ten-minute appliance energy readings from a low-energy house, paired with room temperature, humidity and airport weather data over about 4.5 months.

| Parameter | Value |
| --- | --- |
| **Domain** | Buildings and appliances |
| **Asset / Process** | HVAC and building systems |
| **Modality** | Time series |
| **Task** | Regression |
| **Annotation** | Scalar target |
| **Source Type** | Real production |
| **Access** | UCI repository |
| **Size** | 19,735 instances |
| **Year** | 2017 |
| **License** | CC BY |

## Description

Appliances Energy Prediction was created by Luis Candanedo and donated to the UCI Machine Learning Repository in 2017. Its measurements come from a low-energy house and serve to fit regression models of the energy that the appliances use. The introductory paper, by L. Candanedo, V. Feldheim and Dominique Deramaix, appeared in Energy and Buildings, volume 140.

The 19,735 records are spaced 10 minutes apart over about 4.5 months. A ZigBee wireless sensor network measured temperature and humidity in rooms such as the kitchen, living room and office, averaged to 10-minute periods. M-bus meters logged the target, appliance energy in Wh, and the energy of the light fixtures. Outdoor temperature, pressure, humidity, wind speed, visibility and dew point come from the Chievres Airport weather station in Belgium.

Two random variables are included to test regression models and filter out non-predictive attributes. The data has no missing values, comes as one 11.4 MB CSV file and is licensed under CC BY 4.0.

## References

- [UCI Machine Learning Repository](https://archive.ics.uci.edu/dataset/374/appliances+energy+prediction)
- [Industrial Atlas page](https://www.indatlas.com/datasets/appliances-energy-prediction/)

[⬅️ Back to Index](../README.md)
