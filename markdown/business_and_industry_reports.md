# Business and Industry Reports

**Summary:** 7,000 economics time series for 1956-2017.

| Parameter | Value |
| --- | --- |
| **Name** | Business and Industry Reports |
| **Labeled** | Yes |
| **Time Series** | No |
| **Simulation** | No |
| **Missing Values** | No |
| **Dataset Characteristics** | Tabular |
| **Feature Type** | Real, Integer, Categorical |
| **Associated Tasks** | Analysis |
| **Number of Instances** | INA |
| **Number of Features** | INA |
| **Date Donated** | INA |
| **Source** | Kaggle |

## Dataset Information

Along with their core mission of counting the US population, the United States Census Bureau gathers a wide range of economic data. This dataset covers 16 of their economic reports and surveys:

- Advance Monthly Sales for Retail and Food Services
- Construction Spending
- Housing Vacancies and Homeownership
- Manufactured Housing Survey (1980-2013)
- Manufactured Housing Survey (Current)
- Manufacturers' Shipments, Inventories, and Orders
- Manufacturing and Trade Inventories and Sales
- Monthly Retail Trade and Food Services
- Monthly Wholesale Trade: Sales and Inventories
- New Home Sales
- New Residential Construction
- Quarterly Financial Report
- Quarterly Services Survey
- Quarterly Summary of State & Local Taxes
- Quarterly Survey of Public Pensions
- U.S. International Trade in Goods and Services

## Content

The data csv is arranged in a long format, with the time_series_code column tying it back to the metadata csv. If you're trying to figure out what data is available, you'll want to start with the metadata. Just over a third of the time series store error codes, usually confidence intervals, rather than actual values. The metadata for these time series will have values in the columns et_code, et_desc, and et_unit. All of the dates are stored as complete beginning of the period dates, but all of the time series are at either monthly, quarterly, or annual resolution. Exact days and months are provided for convenience when aligning time series and so that you don't have to unpack period codes like 'Q22009'. There may be many time series bundled under a given data category or description. For example, the largest category (taxes) contains dozens of types of tax categories, and each of those contains a separate time series for each state in the country. Two of the error code time series have non-numeric values. To convert the values column into reasonable units you'll need to drop all entries equal to the string 'Less than .05 percent'. The data have been substantially reformatted from how they are provided by the Census Bureau. You can find the script I used to prepare the data here.

## Tags

Economic data, Industry reports, Business statistics, Market analysis, U.S. Census data

## References

- [Kaggle Dataset](https://www.kaggle.com/datasets/census/business-and-industry-reports)

[⬅️ Back to Index](../README.md)