# Oil Well

**Summary:** Oil well operation parameters (2013-2021)

| Parameter | Value |
| --- | --- |
| **Name** | Oil Well |
| **Labeled** | Yes |
| **Time Series** | No |
| **Simulation** | No |
| **Missing Values** | No |
| **Dataset Characteristics** | Multivariate |
| **Feature Type** | Real |
| **Associated Tasks** | Regression |
| **Number of Instances** | INA |
| **Number of Features** | INA |
| **Date Donated** | INA |
| **Source** | Kaggle |

## Dataset Information

This dataset covers the main parameters of the oil well operation (well № 807). I work as a lead geologist in an oil field in Siberia and oversee the development of an oil field. Every day I collect real data on the work of oil wells. Let me introduce you a little bit and you become a little oilmen)😃 This well was drilled in 2013 at an oil field in the north of Russia. The depth of this well is 2400 meters. An oil reservoir contains oil and gas dissolved in it under high pressure. There is water in the reservoir below the oil. After the completion of the well construction, a pump is lowered into the well, into which a liquid containing oil, gas and water is supplied. On the surface of the well, a sample is taken every day, which shows how much water and oil is contained in this well in percent (column5 - "Water cut (%)"). From the well, the liquid enters the metering unit, which calculates how much fluid the well produces per day (column2 - "Volume of liquid (m3 / day)") and how much gas (column3 - "Gas volume (m3 / day)"). Knowing the above parameters, I calculate how much oil the well produces (column1 - "Oil volume (m3 / day)") and how much water (column4 - "Water volume (m3 / day)"). Also, data about the dynamic level (column7 - "Dynamic level (meters)") is taken every day. A sensor is installed in the pump, which is lowered into the well, which shows reservoir pressure in the well (column8 - "Reservoir pressure (atm)") As the well is operated, reservoir pressure begins to decrease, and oil production decreases accordingly. There is less oil and gas, more water - the oil field begins to deplete. The field's profitability is falling.

Why do we need to know all these parameters and how can we apply them?🤔

We build a 3D model of the field, graphs, on the basis of which we can understand at what stage of development this field is. We can understand how much oil has been produced and how much oil remains, its prospects. Based on these data, we can draw conclusions about the profitability of the well, whether it is profitable for the oil company or the well is unprofitable. Thus, having data on the well operation, we will be able to predict not only a decrease in oil production, but we will also know when and what measures and decisions to take to increase oil production!

## Tags

Oil well, Petroleum engineering, Production optimization, Operational data

## References

- [Kaggle Dataset](https://www.kaggle.com/datasets/ruslanzalevskikh/oil-well)

[⬅️ Back to Index](../README.md)
