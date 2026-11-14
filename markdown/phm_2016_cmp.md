# PHM 2016 CMP Data Challenge

Time series from a wafer chemical-mechanical planarization tool, paired with average material removal rates, for predicting removal rate as pad and dresser wear.

- **Domain:** Electronics and semiconductors
- **Asset / Process:** Semiconductor wafers and process tools
- **Modality:** Time series
- **Task:** Regression; Condition monitoring
- **Annotation:** Scalar target
- **Access:** Competition
- **Year:** 2016
- **Benchmark:** Yes

## Description

The PHM 2016 Data Challenge, held with the PHM 2016 Conference, centres on a wafer chemical-mechanical planarization (CMP) tool that polishes material off the wafer surface. Teams predict the average rate at which material is removed at given tool settings while the tool degrades over time.

The tool has a rotating table with a replaceable polishing pad, a wafer carrier, a slurry dispenser and a dresser that conditions the pad; pad and dresser both lose effectiveness with use and are eventually replaced. Each row of the time series holds all measurement variables at one instant of a run, and a separate table gives the average removal rate per wafer ID and stage, derived from thickness measured before and after polishing.

Training, test and validation sets were released, and the answers for the test and validation sets were later published. Mean squared error carries 90% of the final score and the physics-based modeling approach the other 10%.

## References

- [Official page](https://phmsociety.org/conference/annual-conference-of-the-phm-society/annual-conference-of-the-prognostics-and-health-management-society-2016/phm-data-challenge-4/)
- [Industrial Atlas page](https://www.indatlas.com/datasets/phm-2016-cmp/)

[⬅️ Back to Index](../README.md)
