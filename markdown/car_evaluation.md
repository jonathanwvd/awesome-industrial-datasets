# Car Evaluation

**Summary:** Derived from simple hierarchical decision model, this database may be useful for testing constructive induction and structure discovery methods.

| Parameter | Value |
| --- | --- |
| **Dataset** | Car Evaluation |
| **Domain** | Transportation & Mobility |
| **Asset / Process** | Vehicles / Fleets |
| **Modality** | Tabular |
| **Task** | Classification |
| **Annotation** | Sample Label; Class Label |
| **Source Type** | Real Lab / Testbed |
| **Access** | UCI |
| **Size** | 1728 |
| **Year** | 1997 |
| **License** | Information not available |

## Description

Car Evaluation Database was derived from a simple hierarchical decision model originally developed for the demonstration of DEX, M. Bohanec, V. Rajkovic: Expert system for decision making. Sistemica 1(1), pp. 145-157, 1990. The model evaluates cars according to the following concept structure:

CAR car acceptability
. PRICE overall price
. . buying buying price
. . maint price of the maintenance
. TECH technical characteristics
. . COMFORT comfort
. . . doors number of doors
. . . persons capacity in terms of persons to carry
. . . lug_boot the size of luggage boot
. . safety estimated safety of the car

Input attributes are printed in lowercase. Besides the target concept (CAR), the model includes three intermediate concepts: PRICE, TECH, COMFORT. Every concept is in the original model related to its lower level descendants by a set of examples (for these examples sets see http://www-ai.ijs.si/BlazZupan/car.html).

The Car Evaluation Database contains examples with the structural information removed, i.e., directly relates CAR to the six input attributes: buying, maint, doors, persons, lug_boot, safety. Because of known underlying concept structure, this database may be particularly useful for testing constructive induction and structure discovery methods.

## References

- [Knowledge acquisition and explanation for multi-attribute decision making (Bohanec, M. and Rajkovič, V. 1988)](https://www.semanticscholar.org/paper/KNOWLEDGE-ACQUISITION-AND-EXPLANATION-FOR-DECISION-Bohanec-Rajkovi%C4%8D/8bab443ae322ff47c3e609272bd93fd4650555bc)
- [UCI Machine Learning Repository - Car Evaluation](https://archive.ics.uci.edu/ml/datasets/Car+Evaluation)
- [DOI: 10.24432/C5JP48](https://doi.org/10.24432/C5JP48)

[⬅️ Back to Index](../README.md)
