# Reference Energy Disaggregation Data Set (REDD)

**Summary:** Whole-home 15 kHz current and voltage plus circuit- and plug-level power from homes near Boston, released by two MIT researchers for energy disaggregation research.

| Parameter | Value |
| --- | --- |
| **Domain** | Buildings and appliances |
| **Asset / Process** | HVAC and building systems |
| **Modality** | Time series |
| **Task** | Regression |
| **Annotation** | Scalar target |
| **Source Type** | Real production |
| **Access** | — |
| **Size** | 119 days of data from 10 homes |
| **Year** | 2011 |
| **License** | — |

## Description

REDD is a freely available data set of detailed power usage from real homes, presented by J. Zico Kolter and Matthew J. Johnson of the Massachusetts Institute of Technology. It serves research on energy disaggregation, also called non-intrusive load monitoring (NILM): inferring the individual appliance loads from an aggregate electricity signal.

Each house contributes the whole-home signal, with current on both phases and voltage on one phase at 15 kHz, up to 24 circuits labelled with their appliance category at 0.5 Hz, and up to 20 plug-level monitors at 1 Hz. As of June 2011 it covered 10 homes in the greater Boston area, 119 days of data, 268 monitors and more than 1 terabyte of raw data, with UTC timestamps.

The paper reports initial results with a Factorial Hidden Markov Model on two weeks of whole-home and circuit data from five houses, scored by the share of total energy correctly assigned: 64.5% when the models come from the same house and 47.7% on a house held out from training.

## References

- [Official page](https://zicokolter.com/publications/kolter2011redd.pdf)
- [redd.csail.mit.edu](http://redd.csail.mit.edu/)
- [Industrial Atlas page](https://www.indatlas.com/datasets/the-reference-energy-disaggregation-data-set-redd/)

[⬅️ Back to Index](../README.md)
