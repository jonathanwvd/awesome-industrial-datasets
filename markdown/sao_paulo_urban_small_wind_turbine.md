# Operation SCADA Dataset of an Urban Small Wind Turbine in São Paulo, Brazil

One-minute inverter records of a rooftop Skystream 3.7 small wind turbine at the University of São Paulo, 2017 to 2022, with bit-coded fault and status flags.

- **Domain:** Energy and power
- **Asset / Process:** Wind turbines
- **Modality:** Time series
- **Task:** Other
- **Source Type:** Real production
- **Access:** Zenodo, Dataverse or Figshare
- **Size:** 6 yearly CSV files, 2017 to 2022
- **Year:** 2023
- **License:** CC BY
- **Publisher:** University of São Paulo, Institute of Energy and Environment

## Description

This dataset records the operation of a Skystream 3.7 small wind turbine on the roof of the High Voltage Laboratory of the Institute of Energy and Environment at the University of São Paulo, Brazil. Welson Bassi, Alcantaro Lemes Rodrigues and Ildo Luis Sauer of the institute published it on Zenodo in 2023 under CC BY 4.0.

The turbine's internal inverter controller logged one record per minute from 2017 to 2022, stored as one semicolon-separated CSV file per year. Electrical values include energy, grid voltages and currents and frequency; mechanical ones include rotation and wind speed, plus nacelle and inverter temperatures and internal DC bus voltages.

Turbine, grid and system status are bit-coded integers, so several causes can add up in one value. They flag conditions such as overspeed, braking, low or high grid voltage, frequency faults, grid disconnection and temperature shutdown. A text file describes the columns.

## References

- [DOI](https://doi.org/10.5281/zenodo.7348454)
- [Zenodo record](https://zenodo.org/records/7348454)
- [Industrial Atlas page](https://www.indatlas.com/datasets/sao-paulo-urban-small-wind-turbine/)

[⬅️ Back to Index](../README.md)
