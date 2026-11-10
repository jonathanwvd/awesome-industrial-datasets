# Datasets of Man-in-the-middle Attacks Targeting Modbus TCP/IP and MMS protocols in the Smart Grid

Flow-based features for detecting eavesdropping man-in-the-middle attacks on Modbus TCP/IP and IEC 61850 MMS traffic at distributed energy resource sites.

- **Domain:** OT security
- **Asset / Process:** Control systems and networks; Power grids and plants
- **Modality:** Tabular; Network traffic
- **Task:** Intrusion detection; Classification
- **Access:** Zenodo, Dataverse or Figshare
- **Year:** 2023
- **License:** CC BY
- **Publisher:** KIOS Research and Innovation Center of Excellence, University of Cyprus

## Description

This collection from the KIOS Research and Innovation Center of Excellence at the University of Cyprus targets cyber attacks inside sites with distributed energy resources (DERs). At each site a local controller talks to the power equipment in the private area network over client-server protocols such as Modbus TCP/IP and IEC 61850 Manufacturing Message Specification (MMS), which often lack confidentiality and integrity protection.

The datasets serve to test methods that detect and classify eavesdropping man-in-the-middle attacks on MMS and Modbus TCP/IP traffic. Each sample is described by five flow-based features per connection: time to establish the connection, time to receive all responses, minimum and maximum time between requests, and number of requests. An ARP poisoning indicator is added as a further feature.

The data supports a 2023 paper in Sustainable Energy, Grids and Networks and is released under CC BY 4.0.

## References

- [DOI](https://doi.org/10.5281/zenodo.8375657)
- [Zenodo record](https://zenodo.org/records/8375657)
- [Industrial Atlas page](https://www.indatlas.com/datasets/mitm-modbus-mms-smart-grid/)

[⬅️ Back to Index](../README.md)
