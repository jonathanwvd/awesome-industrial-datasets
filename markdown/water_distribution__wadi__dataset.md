# Water Distribution (WaDi)

Sensor and actuator data from the iTrust water distribution testbed, with 14 days of normal operation and 2 days in which 15 cyber-physical attacks were launched.

- **Domain:** OT security
- **Asset / Process:** Water treatment and distribution
- **Modality:** Time series; Network traffic
- **Task:** Intrusion detection
- **Annotation:** Event and time label
- **Source Type:** Lab or testbed
- **Size:** 16 days; 123 sensors and actuators
- **Publisher:** iTrust

## Description

WaDi is a water distribution testbed run by iTrust, and its first dataset, WaDi.A1, covers 16 days of continuous operation: 14 under normal operation and 2 with attack scenarios. Data comes from all 123 sensors and actuators. The 15 attacks launched in those 2 days follow attack models from the iTrust research team that treat the intent space of a cyber-physical system as the attack model.

The WaDi.A2 update removed readings from periods when the plant was unstable and added a new CSV file, a second CSV file that labels each reading as attack (-1) or no attack (1), and an attack table with corrected dates.

A later release from December 2023, WaDi.A3, holds 105 hours of normal operation of the SWaT and WaDi testbeds, the last 100 of them in CrossOver mode, with no attacks. It includes PCAP files (335 GB for WaDi), historian data and an incomplete set of NetFlow logs.

## References

- [Official page](https://www.sutd.edu.sg/itrust/itrust-labs/datasets/dataset-characteristics/wadi/)
- [itrust.sutd.edu.sg](https://itrust.sutd.edu.sg/itrust-labs_datasets/dataset_info/)
- [Industrial Atlas page](https://www.indatlas.com/datasets/water-distribution-wadi-dataset/)

[⬅️ Back to Index](../README.md)
