# MIMII DUE

Operating sounds of fans, gearboxes, pumps, slide rails and valves recorded by Hitachi, split into source and target domains to test anomalous sound detection under domain shift.

- **Domain:** Manufacturing
- **Asset / Process:** Pumps, compressors and fans; Gears and gearboxes; Valves and actuators
- **Modality:** Audio
- **Task:** Anomaly detection
- **Access:** Zenodo, Dataverse or Figshare
- **Size:** Five machine types, six sections each
- **Year:** 2021
- **License:** CC BY-NC-SA
- **Publisher:** Hitachi, Ltd.

## Description

MIMII DUE is a collection of operating sounds from industrial machines, made and released by Hitachi, Ltd. It was built to test anomalous sound detection when the operating and environmental conditions during use differ from those seen in training, a situation known as domain shift. The data is a subset of the DCASE 2021 Challenge Task 2 data and is identical to its development and additional training sets.

Five machine types are covered: fans, gearboxes, pumps, slide rails and valves. Each type has six sections, and a section roughly matches one product. Each section holds data from a source domain and a target domain, which differ in conditions such as operating speed and environmental noise, and the dataset as a whole contains both normal and abnormal sounds. Experiments in the accompanying paper show large performance gaps between the two domains.

The files are on Zenodo under CC BY-NC-SA 4.0, and two baseline systems are published on GitHub as starting points for the anomalous sound detection task.

## References

- [Zenodo record](https://zenodo.org/records/4740355)
- [Preprint (arXiv)](https://arxiv.org/abs/2105.02702)
- [Industrial Atlas page](https://www.indatlas.com/datasets/mimii-due/)

[⬅️ Back to Index](../README.md)
