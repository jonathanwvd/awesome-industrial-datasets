# CNC Mill Tool Wear

Machining data from 18 CNC milling experiments on wax blocks at the University of Michigan, varying tool condition, feed rate and clamp pressure.

- **Domain:** Manufacturing
- **Asset / Process:** CNC machining and tool wear
- **Modality:** Time series
- **Task:** Classification; Condition monitoring
- **Annotation:** Class label; Event and time label
- **Source Type:** Lab or testbed
- **Access:** Kaggle
- **Size:** 18 experiments
- **License:** CC0 and public domain

## Description

This dataset comes from machining experiments on a CNC milling machine in the System-level Manufacturing and Automation Research Testbed (SMART) at the University of Michigan. Wax blocks of 2 x 2 x 1.5 inches were milled into parts with an S carved into the top face while tool condition, feed rate and clamping pressure were varied.

The 18 experiments each have a time series file sampled every 100 ms, with readings from the four motors of the X, Y and Z axes and the spindle, extracted with Rockwell Cloud Collector Agent Elastic. A Machining_Process column labels each reading with the active operation, such as "Layer 1 Up" or "Layer 3 Down". Some readings do not reflect the machine state, for example when M1_CURRENT_FEEDRATE reads 50.

Each experiment's outputs are the tool condition and whether the experiment passed visual inspection. Eight experiments used an unworn tool and ten a worn one, and clamp pressures were 2.5, 3.0 and 4.0 bar. The publisher proposes tool wear detection and detection of inadequate clamping as classification studies. The data is released under CC0.

## References

- [Kaggle dataset](https://www.kaggle.com/shasun/tool-wear-detection-in-cnc-mill)
- [Industrial Atlas page](https://www.indatlas.com/datasets/cnc-mill-tool-wear/)

[⬅️ Back to Index](../README.md)
