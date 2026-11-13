# Swiss Railway Traction Network Load Forecasting Dataset with Operational Planning Context

Hourly load of the Swiss railway traction grid with weather forecasts and planned train operations from SBB, for day-ahead load forecasting.

- **Domain:** Energy and power
- **Asset / Process:** Power grids and plants
- **Modality:** Time series
- **Task:** Forecasting
- **Annotation:** Scalar target
- **Source Type:** Real production
- **Access:** Zenodo, Dataverse or Figshare
- **Size:** Two hourly CSV files covering 2018–2023 and 2020–2023
- **Year:** 2026
- **License:** CC BY
- **Publisher:** EPFL

## Description

This dataset supports day-ahead forecasting of the electrical load of the Swiss railway traction network, the dedicated 16.7 Hz power grid that Swiss Federal Railways (SBB) runs to supply electric trains. It was prepared at EPFL with data provided by SBB, within the INITIATE project funded by the Swiss Federal Office of Transport.

The target is the total traction grid load at hourly resolution. Inputs combine weather forecasts with operational planning variables that SBB forecasts for the next day, such as train counts, tonnage, train-kilometres and gross tonne-kilometres for freight, regional and long-distance trains. The Railway file spans 2018 to 2023 with 56 covariates, regional for four network sectors; the Railway-Agg file spans 2020 to 2023 with 16 nationally aggregated covariates.

Both variants share a 24-hour forecast horizon and target models that take planned future events as inputs. The record was published on Zenodo in March 2026 under CC BY 4.0.

## References

- [DOI](https://doi.org/10.5281/zenodo.18986666)
- [Zenodo record](https://zenodo.org/records/18986667)
- [Industrial Atlas page](https://www.indatlas.com/datasets/swiss-railway-traction-load/)

[⬅️ Back to Index](../README.md)
