# IV2V and iV2I+ Industrial Datasets

**Summary:** AI4Mobile industrial wireless datasets collected by Fraunhofer HHI in an industrial warehouse, covering iV2V (vehicle-to-vehicle) and iV2I+ (vehicle-to-infrastructure) 5G NR channel measurements for ML-based beam management and link quality prediction.

| Parameter | Value |
| --- | --- |
| **Associated Tasks** | Link Quality Prediction, Beam Management, Positioning, Channel Modeling, Machine Learning for Wireless Communications |
| **Data Source** | Real |
| **Dataset Characteristics** | Multivariate, Time-Series, Wireless Channel Measurements |
| **Date Donated** | 2021 |
| **Feature Type** | Real (channel metrics, position data) |
| **Labeled** | Yes |
| **Missing Values** | No |
| **Name** | IV2V and iV2I+ Industrial Datasets |
| **Number of Features** | Per measurement: RSRP (reference signal received power), RSRQ, SINR, position coordinates (x, y), beam index, timestamp; multiple antenna configurations |
| **Number of Instances** | Multiple measurement campaigns in an industrial warehouse environment; thousands of channel measurement snapshots per scenario |
| **Source** | Fraunhofer HHI (Heinrich Hertz Institute) / AI4Mobile H2020 EU Project / IEEE DataPort |
| **Time Series** | Yes |

## Description

The iV2V and iV2I+ datasets are part of the AI4Mobile project (H2020 EU research project) and were collected by Fraunhofer HHI (Heinrich Hertz Institute, Berlin) in an industrial warehouse environment. The datasets capture real 5G New Radio (NR) channel measurements between mobile industrial vehicles (forklifts) and fixed infrastructure points.

iV2V (industrial Vehicle-to-Vehicle): Measurements between two mobile nodes (forklifts) moving in a warehouse.
iV2I+ (industrial Vehicle-to-Infrastructure plus): Measurements between a mobile node (forklift) and fixed infrastructure access points, with multiple antenna configurations.

For each measurement snapshot, the dataset provides signal quality metrics (RSRP, RSRQ, SINR), precise position and trajectory data, beam indices, and timestamps. The data is intended for machine learning research in:
- Beam management and beam prediction
- Link quality estimation and prediction
- Positioning and localization
- Channel modeling for industrial wireless networks

Support code and documentation are available on GitHub (Fraunhofer HHI repository). The datasets are openly accessible via IEEE DataPort.

## Tags

5G NR, AI4Mobile, Beam Management, Channel Measurement, Fraunhofer HHI, Industrial Wireless, Link Quality Prediction, Vehicle-to-Infrastructure, Vehicle-to-Vehicle, Warehouse

## References

- [IEEE DataPort: AI4Mobile Industrial Wireless Datasets iV2V and iV2I+](https://ieee-dataport.org/open-access/ai4mobile-industrial-wireless-datasets-iv2v-and-iv2i)
- [GitHub Repository (Fraunhofer HHI)](https://github.com/fraunhoferhhi/ai4mobile-industrial)

[⬅️ Back to Index](../README.md)
