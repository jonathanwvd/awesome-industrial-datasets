# Quality Prediction in a Mining Process

**Summary:** Explore real industrial data and help manufacturing plants to be more efficient.

| Parameter | Value |
| --- | --- |
| **Name** | Quality Prediction in a Mining Process |
| **Labeled** | Yes |
| **Time Series** | Yes |
| **Simulation** | No |
| **Missing Values** | No |
| **Dataset Characteristics** | Multivariate, Time-Series |
| **Feature Type** | Real |
| **Associated Tasks** | Regression |
| **Number of Instances** | INA |
| **Number of Features** | INA |
| **Date Donated** | INA |
| **Source** | Kaggle |

## Dataset Information

It is not always easy to find databases from real world manufacturing plants, especially mining plants. So, I would like to share this database with the community, which comes from one of the most important parts of a mining process: a flotation plant!

PLEASE HELP ME GET MORE DATASETS LIKE THIS FILLING A 30s SURVEY:

The main goal is to use this data to predict how much impurity is in the ore concentrate. As this impurity is measured every hour, if we can predict how much silica (impurity) is in the ore concentrate, we can help the engineers, giving them early information to take actions (empowering!). Hence, they will be able to take corrective actions in advance (reduce impurity, if it is the case) and also help the environment (reducing the amount of ore that goes to tailings as you reduce silica in the ore concentrate).

## Content

The first column shows time and date range (from March of 2017 until September of 2017). Some columns were sampled every 20 seconds. Others were sampled on an hourly basis.

The second and third columns are quality measures of the iron ore pulp right before it is fed into the flotation plant. Columns 4 through 8 are the most important variables that impact the ore quality at the end of the process. From column 9 until column 22, we can see process data (level and air flow inside the flotation columns, which also impact ore quality). The last two columns are the final iron ore pulp quality measurement from the lab.
The target is to predict the last column, which is the percentage of silica in the iron ore concentrate.

## Tags

Mining industry, Process optimization, Quality control, Predictive analytics, Operational efficiency

## References

- [Kaggle Dataset](https://www.kaggle.com/datasets/edumagalhaes/quality-prediction-in-a-mining-process)

[⬅️ Back to Index](../README.md)
