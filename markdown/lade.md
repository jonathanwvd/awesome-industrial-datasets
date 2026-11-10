# LaDe

Last-mile parcel pick-up and delivery records from five Chinese cities, with 10,677k packages handled by 21k couriers over six months of real operation in 2022.

- **Domain:** Logistics and retail
- **Modality:** Tabular; Geospatial and remote sensing
- **Task:** Forecasting; Regression; Other
- **Source Type:** Real production
- **Access:** Hugging Face
- **Size:** 10,677k packages from 21k couriers
- **Year:** 2024

## Description

LaDe is a last-mile delivery dataset drawn from real parcel operations in China and hosted on Hugging Face. Its paper appeared at the 30th ACM SIGKDD Conference on Knowledge Discovery and Data Mining in 2024. The data covers 10,677k packages handled by 21k couriers over six months, from 1 May to 31 October 2022.

It has two parts: LaDe-P for parcel pick-up and LaDe-D for delivery. Each part has one CSV file per city, for Shanghai, Hangzhou, Chongqing, Jilin and Yantai. Rows join package details, such as stop coordinates and required time windows, with task events that log when and where a courier accepts and completes each task. Road networks of the five cities and courier GPS trajectories are also included.

The authors test it on route prediction, spatio-temporal graph forecasting and estimated time of arrival prediction, with code on GitHub. The data may be used for research purposes.

## References

- [Hugging Face dataset](https://huggingface.co/datasets/Cainiao-AI/LaDe)
- [Preprint (arXiv)](https://arxiv.org/abs/2306.10675)
- [GitHub repository](https://github.com/wenhaomin/LaDe)
- [Industrial Atlas page](https://www.indatlas.com/datasets/lade/)

[⬅️ Back to Index](../README.md)
