# A 2.5-year campus-level smart meter database with equipment data for energy analytics

Electricity readings from over 1,400 meters in more than 20 HKUST campus buildings over 2.5 years, with equipment metadata in the Brick Schema.

- **Domain:** Buildings and appliances
- **Modality:** Time series
- **Task:** Forecasting; Energy optimization
- **Source Type:** Real production
- **Access:** Direct download
- **Size:** 1394 raw meter files, 1.43 GB
- **Year:** 2024

## Description

This database records electricity use on the campus of the Hong Kong University of Science and Technology (HKUST) in Sai Kung District, Hong Kong. It covers over 1,400 meters in more than 20 buildings, with detailed data on internal equipment, from 1 January 2022 to 27 May 2024. The metadata follows the Brick Schema.

The raw part holds 1394 Excel files, one per metering point, plus a Turtle file that describes locations, equipment and their relationships. The clean part resamples the series to 15-minute, 30-minute, hourly and daily intervals, with 403, 645, 255 and 26 files respectively; 65 files were excluded because data were missing or only zeros.

The authors intend the data for load pattern recognition, fault detection, demand response and load forecasting. A companion GitHub repository has scripts for preprocessing, lighting analysis, missing-rate analysis and SPARQL queries. The 1.43 GB version was released on Dryad in August 2024.

## References

- [Official page](https://datadryad.org/dataset/doi:10.5061/dryad.k3j9kd5h6)
- [GitHub repository](https://github.com/LiMingchen159/HKUST_Meter_Brick)
- [Industrial Atlas page](https://www.indatlas.com/datasets/campus-smart-meter-equipment/)

[⬅️ Back to Index](../README.md)
