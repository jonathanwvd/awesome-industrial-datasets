### [Experiments on Li-ion batteries](https://ti.arc.nasa.gov/tech/dash/groups/pcoe/prognostic-data-repository/#battery)

56.5MB, 11.1MB, 93.7MB, 14.7MB, 8.7MB, 24.9MB(Data Set1~6, compressed)

 ![](https://img.shields.io/badge/sector-battery-ff69b4.svg)  ![](https://img.shields.io/badge/labeled-no-red.svg)  ![](https://img.shields.io/badge/time--series-yes-blue.svg)  ![](<https://img.shields.io/badge/simulation-no-red.svg>)

#### Data Set Information

| Data Set Characteristics | Attribute Characteristics | Associated Tasks |
| ------------------------ | ------------------------- | ---------------- |
| Multivariate             | Real                      | Regression       |

A set of four Li-ion batteries were run through 3 different operational profiles (charge, discharge and impedance) at room temperature (24 deg C).

**Charge**

Charging was carried out in a constant current (CC) mode at 1.5A until the battery voltage reached 4.2V and then continued in a constant voltage (CV) mode until the charge current dropped to 20mA. 

**Discharge**

Discharge was carried out using a 0.05Hz square wave loading profile of 4A amplitude and 50% duty cycle until the battery voltage fell to 2.0V, 2.2V, 2.5V and 2.7V for batteries 25, 26, 27 and 28 respectively.

**Impedance**

Impedance measurement was carried out through an electrochemical impedance spectroscopy (EIS) frequency sweep from 0.1Hz to 5kHz. 

#### Variables

type : operation  type, can be charge, discharge or impedance
ambient_temperature : ambient temperature (degree C)
time : the date and time of the start of the cycle, in MATLAB  date vector format
**charge**
Voltage_measured : Battery terminal voltage (Volts)
Current_measured : Battery output current (Amps)
Temperature_measured : Battery temperature (degree C)
Current_charge : Current measured at charger (Amps)
Voltage_charge : Voltage measured at charger (Volts)
Time : Time vector for the cycle (secs)
**discharge**
Voltage_measured : Battery terminal voltage (Volts)
Current_measured : Battery output current (Amps)
Temperature_measured : Battery temperature (degree C)
Current_charge : Current measured at load (Amps)
Voltage_charge : Voltage measured at load (Volts)
Time : Time vector for the cycle (secs)
Capacity : Battery capacity (Ahr) for discharge till 2.7V 
**impedance**
Sense_current : Current in sense branch (Amps)
Battery_current : Current in battery branch (Amps)
Current_ratio : Ratio of the above currents 
Battery_impedance : Battery impedance (Ohms) computed from raw data
Rectified_impedance : Calibrated and smoothed battery impedance (Ohms) 
Re : Estimated electrolyte resistance (Ohms)
Rct : Estimated charge transfer resistance (Ohms)

#### Paper

1. **Verification of a Remaining Flying Time Prediction System for Small Electric Aircraft***, Edward F. Hogge, Brian M. Bole, Sixto L. Vazquez, Jose Celaya*, Annual Conference of the Prognostics and Health Management, 2015
2. **Adaptation of an Electrochemistry-based Li-Ion Battery Model to Account for Deterioration Observed Under Randomized Use***, Bole, B. and Kulkarni, C. and Daigle, M.*, Annual Conference of the Prognostics and Health Management Society, 2014
3. **Particle-filtering-based prognosis framework for energy storage devices with a statistical characterization of state-of-health regeneration phenomena***, Olivares, Benjam{\'\i}n E and Munoz, Cerda and Orchard, Marcos E and Silva, Jorge F*, Instrumentation and Measurement, IEEE Transactions on, Vol. 62 No. 2, 364--376, 2013
4. **Major Challenges in Prognostics: Study on Benchmarking Prognostics Datasets***, Eker, OF and Camci, F and Jennions, IK*, European Conference of Prognostics and Health Management Society, 2012
5. **Lithium-ion battery remaining useful life estimation based on nonlinear ar model combined with degradation feature***, Liu, Datong and Luo, Yue and Peng, Yu and Peng, Xiyuan and Pecht, Michael*, Annual Conference of the Prognostics and Health Management Society 2012, 24--27, 2012
6. **Data-driven prognostics for lithium-ion battery based on Gaussian process regression***, Liu, Datong and Pang, Jingyue and Zhou, Jianbao and Peng, Yu*, Prognostics and System Health Management (PHM), 2012 IEEE Conference on, 1--5, 2012
7. **Health monitoring and remaining useful life estimation of lithium-ion aeronautical batteries***, Penna, JAM and Nascimento, CL and Ramos Rodrigues, L*, Aerospace Conference, 2012 IEEE, 1--12, 2012
8. **Designing data-driven battery prognostic approaches for variable loading profiles: Some lessons learned***, Saxena, Abhinav and Celaya, Jos{\'e} R and Roychoudhury, Indranil and Saha, Sankalita and Saha, Bhaskar and Goebel, Kai*, Eur. Conf. Prognost. Health Manag. Soc, 2012
9. **Dynamic battery remaining useful life estimation: An on-line data-driven approach***, Zhou, Jianbao and Liu, Datong and Peng, Yu and Peng, Xiyuan*, Instrumentation and Measurement Technology Conference (I2MTC), 2012 IEEE International, 2196--2199, 2012
10. **Model adaptation for prognostics in a particle filtering framework***, Saha, Bhaskar and Goebel, Kai*, International Journal of Prognostics and Health Management, Vol. 2 No. 1, 10, 2011
11. **Study on impedance model of Li-ion battery***, Luo, Weilin and Lv, Chao and Wang, Lixin and Liu, Chao*, Industrial Electronics and Applications (ICIEA), 2011 6th IEEE Conference on, 1943--1947, 2011
12. **An integrated health and contingency management case study on an autonomous ground robot***, Tang, Liang and Zhang, Bin and DeCastro, Jonathan and Hettler, Eric*, Control and Automation (ICCA), 2011 9th IEEE International Conference on, 584--589, 2011
13. **Transient behavior modeling and physical meaning analysis for Battery***, Xiangyang, Gao and Jun, Zhang and Ning, Ning*, Computer Application and System Modeling (ICCASM), 2010 International Conference on, V2--383, 2010
14. **Comparison of prognostic algorithms for estimating remaining useful life of batteries***, Saha, Bhaskar and Goebel, Kai and Christophersen, Jon*, Transactions of the Institute of Measurement and Control, Vol. 31 No. Wed Mar 04 2015 00:00:00 GMT-0800 (PST), 293--308, 2009
15. **Prognostics methods for battery health monitoring using a Bayesian framework***, Saha, Bhaskar and Goebel, Kai and Poll, Scott and Christophersen, Jon*, Instrumentation and Measurement, IEEE Transactions on, Vol. 58 No. 2, 291--296, 2009
16. **Modeling Li-ion battery capacity depletion in a particle filtering framework***, Saha, Bhaskar and Goebel, Kai*, Proceedings of the annual conference of the prognostics and health management society, 2009

#### Citation

B. Saha and K. Goebel (2007). "Battery Data Set", NASA Ames Prognostics Data Repository (http://ti.arc.nasa.gov/project/prognostic-data-repository), NASA Ames Research Center, Moffett Field, CA
