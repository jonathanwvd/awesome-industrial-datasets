## Power  
### [BLUE dataset](<http://portoalegre.andrew.cmu.edu:88/BLUED/>)   

 The dataset consists of voltage and current measurements for a single-family residence in the United States, sampled at 12 kHz for a whole week.  Every state transition of each appliance in the
home during this time was labeled and time-stamped, providing the necessary ground truth for the evaluation of event-based algorithms. 

![](https://img.shields.io/badge/sector-semicon-blue.svg)  ![](https://img.shields.io/badge/sector-power-lightblue.svg)  ![](https://img.shields.io/badge/labeled-yes-blue.svg)![](https://img.shields.io/badge/time--series-yes-blue.svg)   

#### Data Set Information         

| Index | Name                                               | Average Power Consumption (W) | Number of events | Phase |
| ----- | -------------------------------------------------- | ----------------------------- | ---------------- | ----- |
| 1     | Desktop Lamp                                       | 30                            | 26               | B     |
| 2     | Tall Desk Lamp                                     | 30                            | 25               | B     |
| 3     | Garage Door                                        | 530                           | 24               | B     |
| 4     | Washing Machine                                    | 130-700                       | 95               | B     |
| 5     | Kitchen music                                      | 0                             | -                | -     |
| 6     | Kitchen Aid Chopper                                | 1500                          | 16               | A     |
| 7     | Tea Kettle                                         | -                             | 0                | -     |
| 8     | Toaster Oven                                       | -                             | 0                | -     |
| 9     | Fridge                                             | 120                           | 616              | A     |
| 10    | A/V Living room                                    | 45                            | 8                | B     |
| 11    | Sub-woofer Living<br/>room                         | 0                             | -                | -     |
| 12    | Computer A                                         | 60                            | 45               | B     |
| 13    | Laptop B                                           | 40                            | 14               | B     |
| 14    | Dehumidifier                                       | -                             | 0                | -     |
| 15    | Vacuum Cleaner                                     | -                             | 0                | -     |
| 16    | DVR, A/V Receiver,<br/>Blueray Player<br/>Basement | 55                            | 34               | B     |
| 17    | Sub-woofer<br/>Basement                            | 0                             | -                | -     |
| 18    | Apple TV<br/>Basement                              | 0                             | -                | -     |
| 19    | Air Compressor                                     | 1130                          | 20               | A     |
| 20    | LCD Monitor A                                      | 35                            | 77               | B     |
| 21    | TV Basement                                        | 190                           | 54               | B     |
| 22    | Harddrive B                                        | -                             | 0                | -     |
| 23    | Printer                                            | 930                           | 150              | B     |
| 24    | Hair Dryer                                         | 1600                          | 8                | A     |
| 25    | Iron                                               | 1400                          | 40               | B     |
| 26    | Empty living room<br/>socket                       | 60                            | 2                | B     |
| 27    | Empty living room<br/>socket                       | -                             | 0                | -     |
| 28    | Monitor B                                          | 40                            | 150              | B     |
| 29    | Backyard lights                                    | 60                            | 16               | A     |
| 30    | Washroom light                                     | 110                           | 6                | A     |
| 31    | Office Lights                                      | 30                            | 54               | B     |
| 32    | Closet lights                                      | 20                            | 22               | B     |
| 33    | Upstairs hallway<br/>light                         | 25                            | 17               | B     |
| 34    | Hallways Stairs<br/>lights                         | 110                           | 58               | B     |
| 35    | Kitchen Hallway<br/>light                          | 15                            | 6                | B     |
| 36    | Kitchen overhead<br/>light                         | 65                            | 56               | B     |
| 37    | Bathroom upstairs<br/>lights                       | 65                            | 98               | A     |
| 38    | Dining room<br/>overhead light                     | 65                            | 32               | B     |
| 39    | Bedroom Lights                                     | 190                           | 19               | A     |
| 40    | Basement Light                                     | 35                            | 39               | B     |
| 41    | Microwave                                          | 1550                          | 70               | B     |
| 42    | Air Conditioner                                    | -                             | 0                | A+B   |
| 43    | Dryer                                              | -                             | 0                | A+B   |

Table shows the list of appliances in the home that were monitored, along with their average power consumption (estimated from turn-on events), the number of events associated with them and the phase (A or B) that they were feeding from.   

#### Paper     

1. [BLUED: A Fully Labeled Public Dataset for Event-Based
   Non-Intrusive Load Monitoring Research](<https://pdfs.semanticscholar.org/ed1b/8fc3074ec5d7bb7cf83e233d3b130637706f.pdf>)          

#### Citations    

The BibTeX reference for the paper is the following:  

@inproceedings{anderson_blued:_2012, 
  address = {Beijing, China},
  title = {{BLUED:} A Fully Labeled Public Dataset for {Event-Based} {Non-Intrusive} Load Monitoring Research},
  booktitle = {Proceedings of the 2nd {KDD} Workshop on Data Mining Applications in Sustainability {(SustKDD)}},
  author = {Anderson, Kyle and Ocneanu, Adrian and Benitez, Diego and Carlson, Derrick and Rowe, Anthony and Berges, Mario},
  month = aug, year = {2012} },  


##### Data Download Link   
[http://archive.ics.uci.edu/ml/machine-learning-databases/secom/](http://archive.ics.uci.edu/ml/machine-learning-databases/secom/)    

Data Capacity     

- [Data Dictionary](http://portoalegre.andrew.cmu.edu:88/BLUED/location_001_datadictionary.txt) [txt] [1 kB]  
- [Dataset 001](http://portoalegre.andrew.cmu.edu:88/BLUED/location_001_dataset_001.tar) [bzip, tar] [3.5 GB]  
- [Dataset 002](http://portoalegre.andrew.cmu.edu:88/BLUED/location_001_dataset_002.tar) [bzip, tar] [3.5 GB]  
- [Dataset 003](http://portoalegre.andrew.cmu.edu:88/BLUED/location_001_dataset_003.tar) [bzip, tar] [3.5 GB]  
- [Dataset 004](http://portoalegre.andrew.cmu.edu:88/BLUED/location_001_dataset_004.tar) [bzip, tar] [3.5 GB]  
- [Dataset 005](http://portoalegre.andrew.cmu.edu:88/BLUED/location_001_dataset_005.tar) [bzip, tar] [3.5 GB]  
- [Dataset 006](http://portoalegre.andrew.cmu.edu:88/BLUED/location_001_dataset_006.tar) [bzip, tar] [3.5 GB]  
- [Dataset 007](http://portoalegre.andrew.cmu.edu:88/BLUED/location_001_dataset_007.tar) [bzip, tar] [3.5 GB]  
- [Dataset 008](http://portoalegre.andrew.cmu.edu:88/BLUED/location_001_dataset_008.tar) [bzip, tar] [3.5 GB]  
- [Dataset 009](http://portoalegre.andrew.cmu.edu:88/BLUED/location_001_dataset_009.tar) [bzip, tar] [3.5 GB]  
- [Dataset 010](http://portoalegre.andrew.cmu.edu:88/BLUED/location_001_dataset_010.tar) [bzip, tar] [3.5 GB]  
- [Dataset 011](http://portoalegre.andrew.cmu.edu:88/BLUED/location_001_dataset_011.tar) [bzip, tar] [3.5 GB]  
- [Dataset 012](http://portoalegre.andrew.cmu.edu:88/BLUED/location_001_dataset_012.tar) [bzip, tar] [3.5 GB]  
- [Dataset 013](http://portoalegre.andrew.cmu.edu:88/BLUED/location_001_dataset_013.tar) [bzip, tar] [3.5 GB]  
- [Dataset 014](http://portoalegre.andrew.cmu.edu:88/BLUED/location_001_dataset_014.tar) [bzip, tar] [3.5 GB]  
- [Dataset 015](http://portoalegre.andrew.cmu.edu:88/BLUED/location_001_dataset_015.tar) [bzip, tar] [3.5 GB]  
- [Dataset 016](http://portoalegre.andrew.cmu.edu:88/BLUED/location_001_dataset_016.tar) [bzip, tar] [3.5 GB]  