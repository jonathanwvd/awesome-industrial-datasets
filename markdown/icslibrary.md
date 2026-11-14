# ICSLibrary: A Dataset and Benchmark for Identifying Internet-Facing Industrial Control System Devices

Network traffic and device records from repeated probing of 2,205 Internet-facing ICS endpoints, labelled with vendor, type and model across 165 models.

- **Domain:** OT security
- **Asset / Process:** Control systems and networks
- **Modality:** Network traffic
- **Task:** Classification
- **Annotation:** Class label
- **Access:** Zenodo, Dataverse or Figshare
- **Size:** 2,205 labeled endpoints
- **Year:** 2026
- **License:** CC BY
- **Publisher:** Shenyang Institute of Automation, Chinese Academy of Sciences

## Description

ICSLibrary is a collection for identifying industrial control system devices that are reachable from the Internet, released on Zenodo in 2026 by researchers at the Shenyang Institute of Automation, Chinese Academy of Sciences. It targets device identification by vendor, type and model for asset inventory, vulnerability assessment and exposure monitoring.

The data was built by discovering Internet-facing ICS services and then probing them repeatedly with protocol-specific requests from different scanner locations and at different times. It covers 2,205 labelled endpoints and 165 device models speaking Modbus/TCP, EtherNet/IP or S7comm.

The release holds the captured network traffic, scanning logs, device information, the scanners and a benchmark archive, along with paired traffic views that separate instance details from explicit model identifiers. The authors report that recognising known endpoints does not reliably carry over to new endpoints of the same model. It is licensed under CC BY 4.0.

## References

- [DOI](https://doi.org/10.5281/zenodo.14984907)
- [Zenodo record](https://zenodo.org/records/23414401)
- [Industrial Atlas page](https://www.indatlas.com/datasets/icslibrary/)

[⬅️ Back to Index](../README.md)
