# Others 
## [Petrobras 3W](https://github.com/petrobras/3W/tree/master/dataset)
![](<https://img.shields.io/badge/sector-others-ff69b4.svg>)
![](<https://img.shields.io/badge/timestamp-yes-green.svg>)
### Data Set Information  
The 3W dataset consists of all CSV files in the subdirectories of the dataset directory and structured as detailed here.
### Attribute Information
- timestamp: observations - timestamps loaded into pandas - DataFrame as its index;
- P-PDG: pressure variable at the - Permanent Downhole Gauge (PDG);
- P-TPT: pressure variable at the - Temperature and Pressure - Transducer (TPT);
- T-TPT: temperature variable at the Temperature and Pressure - Transducer (TPT);
- P-MON-CKP: pressure variable upstream of the production choke (CKP);
- T-JUS-CKP: temperature variable downstream of the production choke (CKP);
- P-JUS-CKGL: pressure variable upstream of the gas lift choke (CKGL);
- T-JUS-CKGL: temperature variable upstream of the gas lift choke (CKGL);
- QGL: gas lift flow rate;
- class: observations labels associated with three types of periods (normal, fault transient, and faulty steady state).

Other information are also loaded into each pandas Dataframe:

- label: instance label (event type);
- well: well name. Hand-drawn and simulated instances have fixed names. Real instances have names masked with incremental id;
- id: instance identifier. -
- Hand-drawn and simulated instances have incremental id. 
- Each real instance has an id generated from its first timestamp.
### References
[Petrobras 3W](https://www.ufrgs.br/psebr/wp-content/uploads/2019/04/Abstract_A019_Vargas.pdf.) - R.E.V. Vargas, C.J. Munaro, P.M. Ciarelli. A methodology for generating datasets for development of anomaly detectors in oil wells based on Artificial Intelligence techniques. I Congresso Brasileiro em Engenharia de Sistemas em Processos. 2019. 