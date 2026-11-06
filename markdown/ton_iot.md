# TON_IoT

Telemetry, network, Linux and Windows datasets from a UNSW Canberra IoT and IIoT testbed, with normal and attack records labelled for AI-based intrusion detection.

- **Domain:** OT security
- **Asset / Process:** Control systems and networks
- **Modality:** Network traffic; Time series
- **Task:** Intrusion detection
- **Annotation:** Class label; Event and time label
- **Source Type:** Lab or testbed
- **Access:** Direct download
- **Year:** 2019
- **License:** Academic or non-commercial terms
- **Publisher:** UNSW Canberra

## Description

TON_IoT is a set of Industry 4.0, IoT and Industrial IoT (IIoT) datasets from UNSW Canberra at the Australian Defence Force Academy, for evaluating AI-based cybersecurity applications such as intrusion detection. The data was gathered on a testbed network at the Cyber Range and IoT Labs, where Windows, Linux and Kali machines link IoT, cloud and edge/fog layers.

Four sources were recorded in parallel under normal operation and attacks such as DoS, DDoS and ransomware: telemetry from more than 10 IoT and IIoT sensors, including weather and Modbus sensors; network traffic as pcap files and Zeek (Bro) logs; Linux audit traces from Ubuntu 14 and 18; and Windows 7 and 10 Performance Monitor data.

Processed CSV files add standard features and labels. A train and test folder holds selected CSV samples of the four datasets, a statistics folder counts normal and attack records, and a ground-truth folder lists security events with timestamps, labelled by attacker IP address. Free academic use is granted in perpetuity; commercial use is allowed after asking the author, Dr Nour Moustafa.

## References

- [Official page](https://research.unsw.edu.au/projects/toniot-datasets)
- [Industrial Atlas page](https://www.indatlas.com/datasets/ton-iot/)

[⬅️ Back to Index](../README.md)
