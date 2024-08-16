# Bosch Production Line Performance

**Summary:** This dataset from Bosch is aimed at reducing production line failures. It contains extensive data on manufacturing processes, focusing on minimizing testing errors and maximizing production line performance.

| Parameter | Value |
| --- | --- |
| **Name** | Bosch Production Line Performance |
| **Labeled** | Yes |
| **Time Series** | No |
| **Simulation** | No |
| **Missing Values** | Yes |
| **Dataset Characteristics** | Multivariate |
| **Feature Type** | Real, Binary |
| **Associated Tasks** | Classification |
| **Number of Instances** | N/A |
| **Number of Features** | N/A |
| **Date Donated** | 2016 |
| **Source** | Kaggle |

## Dataset Information

The data for this competition represents measurements of parts as they move through Bosch's production lines. Each part has a unique Id. The goal is to predict which parts will fail quality control (represented by a 'Response' = 1).

The dataset contains an extremely large number of anonymized features. Features are named according to a convention that tells you the production line, the station on the line, and a feature number. E.g., L3_S36_F3939 is a feature measured on line 3, station 36, and is feature number 3939.

On account of the large size of the dataset, we have separated the files by the type of feature they contain: numerical, categorical, and finally, a file with date features. The date features provide a timestamp for when each measurement was taken. Each date column ends in a number that corresponds to the previous feature number. E.g., the value of L0_S0_D1 is the time at which L0_S0_F0 was taken.

In addition to being one of the largest datasets (in terms of number of features) ever hosted on Kaggle, the ground truth for this competition is highly imbalanced. Together, these two attributes are expected to make this a challenging problem.

## Tags

Manufacturing, Production line, Quality control, Industrial data, Machine learning

## References

- [Kaggle Competition](https://www.kaggle.com/c/bosch-production-line-performance)
- [Kaggle - Bosch Production Line Performance Data](https://www.kaggle.com/competitions/bosch-production-line-performance/data)

[⬅️ Back to Index](../README.md)
