# Mechanical Analysis

**Summary:** Fault diagnosis problem of electromechanical devices; also PUMPS DATA SET is newer version with domain theory and results

| Parameter | Value |
| --- | --- |
| **Name** | Mechanical Analysis |
| **Labeled** | Yes |
| **Time Series** | No |
| **Simulation** | No |
| **Missing Values** | No |
| **Dataset Characteristics** | Multivariate |
| **Feature Type** | Categorical, Integer, Real |
| **Associated Tasks** | Classification |
| **Number of Instances** | 209 |
| **Number of Features** | 8 |
| **Date Donated** | 1990-05-31 |
| **Source** | UCI Machine Learning Repository |

## Dataset Information

F. Bergadano supplied this database. Each instance contains many components, each of which has 8 attributes. Different instances in this database have different numbers of components. It was impossible to put one instance on one line. He originally had one instance per file, but this makes it difficult to ftp them (imagine ftp'ing 222 or so files!). I bundled the set of 209 instances into a single data file, prefixing each with the line:

              ===== Instance number 1: =====

where 'n' is a number in [1,221]. However, they are NOT, repeat NOT in sequential order. Twelve (12) of the instances are missing. Bergadano supplied these additional 12 instances (numbers 8,12,32,33,66,69,73,152,167,194,203,208) in a 'notused' sub-directory. I bundled these up with the same format in the 'notused-instances' file.

A quick scan of their file didn't reveal what the purpose is for these twelve instances.

## Tags

Fault diagnosis, Electromechanical devices, Component analysis, Classification tasks, Pump analysis

## References

- [UCI Machine Learning Repository](https://archive.ics.uci.edu/dataset/64/mechanical+analysis)

[⬅️ Back to Index](../README.md)
