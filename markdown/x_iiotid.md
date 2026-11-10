# X-IIoTID

Intrusion dataset for the Industrial Internet of Things from UNSW Canberra with 820,834 instances, 68 features and three label levels covering normal traffic and staged attacks.

- **Domain:** OT security
- **Asset / Process:** Control systems and networks
- **Modality:** Tabular; Network traffic
- **Task:** Intrusion detection
- **Annotation:** Class label
- **Access:** IEEE DataPort
- **Size:** 820,834 instances
- **Year:** 2021
- **Publisher:** UNSW Canberra

## Description

X-IIoTID is an intrusion dataset for the Industrial Internet of Things by Muna Al-Hawawreh, Elena Sitnikova and Neda Aboutorab of UNSW Canberra, with an accompanying research article. Its features are connectivity- and device-agnostic, meant to fit heterogeneous IIoT systems and their newer protocols such as MQTT, CoAP and WebSocket.

The traffic spans industrial control loop devices (sensors, actuators and controllers) as well as edge, mobile and cloud components. Features come from network traffic, system and application logs, device resources, and OSSEC and Zeek logs. The final version holds 820,834 instances, 421,417 normal and 399,417 attacks, described by 68 features.

Attacks range from scanning, WebSocket fuzzing and CoAP resource discovery to brute force, dictionary and insider attacks, reverse shell, man-in-the-middle, MQTT broker subscription, Modbus register reading, TCP relay, command and control, data exfiltration, false data injection, fake notifications and crypto-ransomware. Labels come in three levels: normal versus attack, attack sub-category and attack sub-sub-category.

## References

- [IEEE DataPort](https://ieee-dataport.org/documents/x-iiotid-connectivity-and-device-agnostic-intrusion-dataset-industrial-internet-things)
- [Industrial Atlas page](https://www.indatlas.com/datasets/x-iiotid/)

[⬅️ Back to Index](../README.md)
