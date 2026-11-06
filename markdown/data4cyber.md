# Data4Cyber

Labelled 1 Hz process telemetry and OT packet captures from a distribution-grid management system with distributed energy resources, across seven primary scenarios.

- **Domain:** OT security
- **Asset / Process:** Power grids and plants; Control systems and networks
- **Modality:** Time series; Network traffic
- **Task:** Intrusion detection
- **Annotation:** Sample label; Event and time label
- **Access:** Zenodo, Dataverse or Figshare
- **Size:** 14,354 rows
- **Year:** 2026
- **License:** CC BY

## Description

Data4Cyber supports cyber-physical security work on systems that manage distribution grids with distributed energy resources (DER), combining several data types organised by scenario. Its creators work at the Fraunhofer Institute for Applied Information Technology, the Fraunhofer Institute for Communication, Information Processing and Ergonomics, and Panasonic. It was published on Zenodo in May 2026 under CC BY 4.0.

Of seven primary scenarios, one is a benign baseline. Two manipulate Modbus in the style of Industroyer, targeting the photovoltaic (PV) and battery storage (BSS) units; three inject false meter readings through ARP-spoofing man-in-the-middle attacks; and one compromises the MQTT price signal as a supply-chain attack. Each scenario folder holds a 1 Hz process telemetry table of 151 to 158 columns, separate benign-only and attack-only files, a state log in IPAL-compatible form, pcapng captures, attack-phase annotations and Modbus-register mappings.

Labels include a binary attack_active flag, an attack_phase field with one label per row and a multi-label attack_phase_all field that covers overlapping phases. The 14,354 rows, collected on 5 and 6 March 2026, split into 5,880 benign and 8,474 attack rows.

## References

- [DOI](https://doi.org/10.5281/zenodo.20004612)
- [Zenodo record](https://zenodo.org/records/20004612)
- [Industrial Atlas page](https://www.indatlas.com/datasets/data4cyber/)

[⬅️ Back to Index](../README.md)
