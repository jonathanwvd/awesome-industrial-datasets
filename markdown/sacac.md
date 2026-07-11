# SACAC

**Summary:** Community-contributed industrial SISO PID control loop dataset repository with 25 datasets categorized by cause of poor performance (stiction, oscillation, saturation, sensor faults, etc.); designed as a benchmark for control loop performance monitoring research.

| Parameter | Value |
| --- | --- |
| **Dataset** | SACAC |
| **Domain** | Chemical & Process |
| **Asset / Process** | Valves / Actuators; Chemical Process |
| **Modality** | Time Series |
| **Task** | Fault Diagnosis; Process Monitoring; Simulation / Control |
| **Annotation** | Sample Label; Fault Type Label |
| **Source Type** | Real Production / Field |
| **Access** | Official Portal |
| **Size** | 25 SISO PID control loop datasets categorized by root cause of poor performance |
| **Year** | 2018 |
| **License** | Information not available |

## Description

The SACAC (South African Council for Automation and Control) data repository provides industrial process data for control loop performance monitoring (CLPM) research. It was established to address the lack of publicly available industrial datasets for testing and comparing CLPM methods.

The repository contains 25 SISO (single-input single-output) PID control loop datasets contributed by industry practitioners and academic researchers. Datasets are categorized according to the root causes of poor control performance as classified by Bauer et al. (2016), including:
- Valve stiction (most common)
- External oscillations and disturbances
- Aggressive tuning / oscillatory behavior
- Sensor faults and quantization
- Saturation and constraints
- Other causes

Each dataset provides time series of the process variable (PV) and manipulated variable (MV), enabling researchers to develop and benchmark methods for detecting, diagnosing, and ranking the severity of control loop problems. The dataset is described in the IFAC-PapersOnLine repository paper (2018) and is hosted on the SACAC resources page.

## References

- [SACAC Resources Page](https://sacac.org.za/resources/)
- [SACAC Repository Description Paper (IFAC-PapersOnLine, 2018)](https://www.sciencedirect.com/science/article/pii/S2405896318304701)
- [Bauer et al. (2016) - Cause categorization of poor control loop performance](http://www.sciencedirect.com/science/article/pii/S0959152415002127)
- [Valve Stiction Comparative Study (Bacci di Capaci et al., 2016)](https://www.sciencedirect.com/science/article/pii/S0959152416300907)

[⬅️ Back to Index](../README.md)
