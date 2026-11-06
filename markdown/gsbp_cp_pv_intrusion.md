# GSBP-CP

**Summary:** Cross-layer intrusion detection data from an operational grid-tied PV installation in Morocco, with Modbus/TCP inverter telemetry, MQTT meter readings and packet captures.

| Parameter | Value |
| --- | --- |
| **Domain** | OT security |
| **Asset / Process** | Solar PV; Control systems and networks |
| **Modality** | Network traffic; Time series; Tabular |
| **Task** | Intrusion detection |
| **Annotation** | Event and time label |
| **Source Type** | Lab or testbed |
| **Access** | Zenodo, Dataverse or Figshare |
| **Size** | 223,215 time-aligned records |
| **Year** | 2026 |
| **License** | CC BY |

## Description

GSBP-CP is a cyber-physical dataset from Morocco: researchers turned a grid-tied photovoltaic system in operation in the Green & Smart Building Park of Mohammed VI Polytechnic University (UM6P) into a cybersecurity testbed. A transparent proxy relays Modbus/TCP polling of a production Huawei SUN2000L-5KTL inverter, a separate Shelly 3EM meter reports over MQTT, and a mirror port on the switch records packets, with one NTP clock for all three.

The scenarios follow MITRE ATT&CK for ICS: normal operation over three diurnal cycles, reconnaissance, denial of service, three variants of false-data injection in Modbus responses, replay, ARP spoofing and MQTT injection of falsified meter readings. Each scenario has inverter telemetry with per-register response latencies, three-phase meter data and pcapng traffic captures.

A fused table of 223,215 time-aligned records has 66 numeric features (78 in an extended variant) and a ground-truth attack log. Code for fusion, feature engineering and split generation and a notebook with the authors' results come with the data, released under CC BY 4.0.

## References

- [DOI](https://doi.org/10.5281/zenodo.23198408)
- [Zenodo record](https://zenodo.org/records/23198408)
- [Industrial Atlas page](https://www.indatlas.com/datasets/gsbp-cp-pv-intrusion/)

[⬅️ Back to Index](../README.md)
