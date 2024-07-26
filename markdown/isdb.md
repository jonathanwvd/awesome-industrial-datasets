# ISDB

| Parameter | Value |
| --- | --- |
| Data Set Characteristics | Time-series |
| Attribute Characteristics | Real |
| Associated Tasks | Classification |
| Number of Instances | Number of Attributes | |
| Number of Attributes | Date Donated | |
| Date Donated | Source | University of Alberta |
| Source | University of Alberta |
| Dataset size | 13.7 MB (compressed) |

## Data Set Information
This is an international database of industrial control loops (most of them suffering from stiction) from different fields. It was an outcome of a project initiated by Mohieddine Jelali during the writing of the book [Detection and Diagnosis of Stiction in Control Loops: State of the Art and Advanced Methods](https://sites.ualberta.ca/~bhuang/Stiction-Book.htm).

The data were provided by different international Colleagues (called Stiction Group) who have contributed to the book.
The Stiction Group has decided to publish the database to enable other researchers working on the field to test their own methods on industrial data.

## Attribute Information
The data are stored in a structure cdata that contains substructures.

Each data set contains: comments; brief comments; type (0: self-regulating; 1: integrating); sampling period [s]; and the data: t (time) [s], SP (set point), PV (process variable), OP (controller output), and (only for some loops) Kc (proportional gain), Ti (integration time constant), en (normalised control error SP − PV).

Example: PV for the chemical loop no. 19: pv = cdata.chemicals.loop19.PV.

## References

