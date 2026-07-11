# IV2V and iV2I+ Industrial Datasets

**Summary:** AI4Mobile industrial wireless datasets collected by Fraunhofer HHI in an industrial warehouse, covering iV2V (vehicle-to-vehicle) and iV2I+ (vehicle-to-infrastructure) 5G NR channel measurements for ML-based beam management and link quality prediction.

| Parameter | Value |
| --- | --- |
| **Dataset** | IV2V and iV2I+ Industrial Datasets |
| **Domain** | Transportation & Mobility; Logistics & Retail |
| **Asset / Process** | Vehicles / Fleets |
| **Modality** | Time Series |
| **Task** | Forecasting; Classification |
| **Annotation** | Sample Label |
| **Source Type** | Real Production / Field |
| **Access** | Repository; IEEE DataPort |
| **Size** | Multiple measurement campaigns in an industrial warehouse environment; thousands of channel measurement snapshots per scenario |
| **Year** | 2021 |
| **License** | Information not available |

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

## References

- [IEEE DataPort: AI4Mobile Industrial Wireless Datasets iV2V and iV2I+](https://ieee-dataport.org/open-access/ai4mobile-industrial-wireless-datasets-iv2v-and-iv2i)
- [GitHub Repository (Fraunhofer HHI)](https://github.com/fraunhoferhhi/ai4mobile-industrial)

[⬅️ Back to Index](../README.md)
