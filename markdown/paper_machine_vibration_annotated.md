# Condition monitoring vibration data annotated with technical language from paper machines in northern Sweden

A year of vibration spectra from two kraftliner paper machines, each paired with Swedish maintenance notes written by on-site experts, for fault diagnosis from technical language.

- **Domain:** Manufacturing
- **Modality:** Vibration; Text and documents
- **Task:** Fault diagnosis; Condition monitoring
- **Annotation:** Text and QA label
- **Source Type:** Real production
- **Size:** 21,090 signal and annotation pairs
- **Publisher:** Luleå University of Technology

## Description

Labelled industrial data is scarce in prognostics and health management research. This dataset from Luleå University of Technology fills that gap with signals and annotations from two large paper machines at a kraftliner producer in northern Sweden.

It holds 21,090 signal and annotation pairs from one year of production. The signals are mostly accelerometer vibration measurements, recorded with SKF CMSS 2200 and CMSS 2207 sensors on an SKF IMx system. The annotations are in Swedish and were written by on-site experts. Each note is linked to every signal from the ten days before its date, and the data does not say which sensor or machine part a sample came from.

The data is a Pandas dataframe saved as pickle and JSON files with four columns: an id, the FFT and envelope spectra, the notes, and sentence embeddings from Swedish SentenceBERT. Contributors include SCA Munksund, Smurfit Kappa and SKF. Signed notes keep pseudonymised personal data, and the catalogue record marks access to the dataset as restricted.

## References

- [Official page](https://researchdata.se/en/catalogue/dataset/2023-246)
- [Industrial Atlas page](https://www.indatlas.com/datasets/paper-machine-vibration-annotated/)

[⬅️ Back to Index](../README.md)
