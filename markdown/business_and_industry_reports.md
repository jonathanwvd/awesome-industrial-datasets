# Business and Industry Reports

**Summary:** 7,000 economics time series from 16 US Census Bureau economic reports covering the period 1956-2017.

| Parameter | Value |
| --- | --- |
| **Dataset** | Business and Industry Reports |
| **Domain** | Business & Economics |
| **Asset / Process** | Business / Economic Indicators |
| **Modality** | Time Series; Text / Documents |
| **Task** | Forecasting; Regression |
| **Annotation** | Scalar Target |
| **Source Type** | Public Records |
| **Access** | Kaggle; Repository; Login Required |
| **Size** | 10952 unique time series codes approximately |
| **Year** | 2017 |
| **License** | Information not available |

## Description

Along with their core mission of counting the US population, the United States Census Bureau gathers a wide range of economic data. This dataset comprises 16 different economic reports and surveys from the Census Bureau, covering numerous economic indicators.

The data is provided in a long format CSV, with a time_series_code column linking the data to a metadata CSV. The time series data includes error codes for some series, reflecting confidence intervals and other measures. Dates are stored as complete beginning of period dates, with series at monthly, quarterly, or annual resolutions. Multiple series exist under given categories, often split by states or tax types.

Values with non-numeric entries, such as 'Less than .05 percent', should be filtered out for numerical analysis. The dataset has been reformatted from original Census Bureau presentations to enhance usability, and the data preparation script is also provided.

## References

- [Kaggle Dataset Page](https://www.kaggle.com/datasets/census/business-and-industry-reports)
- [United States Census Bureau data sets](https://www.census.gov/data/datasets.html)
- [Data Preparation Script on GitHub](https://gist.github.com/SohierDane/2c1b36f653724fbc7d8f26501ef4b88d)

[⬅️ Back to Index](../README.md)
