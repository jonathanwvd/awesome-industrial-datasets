# Car Evaluation

**Summary:** Derived from simple hierarchical decision model, this database may be useful for testing constructive induction and structure discovery methods.

| Parameter | Value |
| --- | --- |
| **Name** | Car Evaluation |
| **Labeled** | Yes |
| **Time Series** | No |
| **Simulation** | No |
| **Missing Values** | No |
| **Dataset Characteristics** | Multivariate |
| **Feature Type** | Categorical |
| **Associated Tasks** | Classification |
| **Number of Instances** | 1728 |
| **Number of Features** | 6 |
| **Date Donated** | 1997-05-31 |
| **Source** | UCI Machine Learning Repository |

## Dataset Information

Car Evaluation Database was derived from a simple hierarchical decision model originally developed for the demonstration of DEX, M. Bohanec, V. Rajkovic: Expert system for decision making. Sistemica 1(1), pp. 145-157, 1990.). The model evaluates cars according to the following concept structure:

CAR                      car acceptability
. PRICE                  overall price
. . buying               buying price
. . maint                price of the maintenance
. TECH                   technical characteristics
. . COMFORT              comfort
. . . doors              number of doors
. . . persons            capacity in terms of persons to carry
. . . lug_boot           the size of luggage boot
. . safety               estimated safety of the car

Input attributes are printed in lowercase. Besides the target concept (CAR), the model includes three intermediate concepts: PRICE, TECH, COMFORT. Every concept is in the original model related to its lower level descendants by a set of examples (for these examples sets see http://www-ai.ijs.si/BlazZupan/car.html).

The Car Evaluation Database contains examples with the structural information removed, i.e., directly relates CAR to the six input attributes: buying, maint, doors, persons, lug_boot, safety.

Because of known underlying concept structure, this database may be particularly useful for testing constructive induction and structure discovery methods.

## Tags

Automobile evaluation, Decision-making, Categorical data, Multivariate data, Classification task

## References

- [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/Car+Evaluation)

[⬅️ Back to Index](../README.md)
