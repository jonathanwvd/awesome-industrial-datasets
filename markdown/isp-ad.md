# ISP-AD

Screen-printing inspection dataset of 559,049 samples that combine 711 real factory defects with 245,664 synthetic ones.

- **Domain:** Manufacturing
- **Asset / Process:** Surfaces and textures
- **Modality:** Image
- **Task:** Anomaly detection; Defect detection
- **Annotation:** Sample label
- **Source Type:** Mixed
- **Access:** Zenodo, Dataverse or Figshare
- **Size:** 559,049 samples
- **Year:** 2025
- **License:** CC BY-NC-SA
- **Publisher:** Polymer Competence Center Leoben
- **Benchmark:** Yes

## Description

ISP-AD (Industrial Screen Printing Anomaly Detection Dataset) comes from a real-world industrial screen-printing use case. It was published on Zenodo in 2025 by researchers from Polymer Competence Center Leoben and Burg Design GmbH in Austria, and is described in a 2026 article in the Journal of Intelligent Manufacturing.

Of the 559,049 samples, 312,674 are fault-free and 246,375 are defective. The defective part holds 711 real, weakly labeled defects collected on the factory floor and 245,664 synthetic defects. The files are organised into unsupervised and supervised splits, with extra fault-free data for work on defect synthesis.

The dataset is a benchmark for unsupervised, self-supervised and supervised defect detection under production conditions. PyTorch and Anomalib data loaders for the unsupervised split are published in the project's GitHub repository. Reuse is limited to non-commercial purposes under CC BY-NC-SA 4.0.

## References

- [DOI](https://doi.org/10.5281/zenodo.14911042)
- [Preprint (arXiv)](https://arxiv.org/abs/2503.04997)
- [GitHub repository](https://github.com/p4ulk/isp-ad)
- [Industrial Atlas page](https://www.indatlas.com/datasets/isp-ad/)

[⬅️ Back to Index](../README.md)
