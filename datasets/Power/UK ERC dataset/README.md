## [UK-DALE dataset](http://jack-kelly.com/data/)

3.5GB(compressed)

This dataset records the power demand from five houses. In each house we record both the whole-house mains power demand every six seconds as well as power demand from individual appliances every six seconds. In three of the five houses (houses 1, 2 and 5) we also record the whole-house voltage and current at 16 kHz.

![](https://img.shields.io/badge/sector-power-skyblue.svg) ![](https://img.shields.io/badge/labeled-yes-blue.svg)  ![](https://img.shields.io/badge/time--series-yes-blue.svg) ![](https://img.shields.io/badge/simulation-no-red.svg)

#### Data Set Information:

All five homes have whole-home power recorded every six seconds; and appliance-level data is at six second resolution. Homes 1, 2 and 5 also have whole-home active power and apparent power at 1 second resolution. The six-second and one-second data is stored in CSV files where the first column is the UNIX timestamp.

UK-DALE uses a data format similar to that used by the first public disaggregation dataset, the Reference
Energy Disaggregation Data Set (REDD)10.
There are five directories, one per house. The directories are named house_ox> where x is an integer between 1 and 5.
Each directory contains a set of channel_oi>.dat CSV files (one file per electricity meter i) and a labels.dat file which is a CSV file which maps from channel number i to appliance name. All CSV files in UK-DALE use a single space as the column separator (as per REDD).
One way in which UK-DALE differs from REDD is that UK-DALE includes a set of detailed metadata files. These follow the NILM Metadata schema37.

The metadata files are in YAML text file format (YAML is a superset of the JSON format). This metadata describes properties such as the specifications of each appliance; the mains wiring between the meters and between meters and appliances; exactly which measurements are provided by each meter; which room each appliance belongs in etc.

The labels.dat file in each directory is redundant and is only included to provide compatibility with REDD. All data in UK-DALE as of January 2015 are available from the UK Energy Research Council’s Energy Data Centre. 

The latter source will be updated as we collect more data. There are three forms of data in UK-DALE:

- The 6 second data from the Current Cost meters (Data Citation 1).
- The 1 second data from our sound card power meter (Data Citation 1). 
- The 16 kHz data recorded by our sound card power meter (Data Citation 2). The complete set of 16
  kHz files requires 4 TBytes of storage. The 16 kHz data is supplied as a set of 200 MByte files. Each file
  records 1 h of data.

#### Paper

[The UK-DALE dataset, domestic appliance-level electricity demand and whole-house demand from five UK homes](https://www.nature.com/articles/sdata20157)

#### Citation Request

Kelly J., Knottenbelt W. 2015. UKERC Energy Data Centre. <http://dx.doi.org/10.5286/UKERC.EDC.000001>

Kelly J., Knottenbelt W. 2015. UKERC Energy Data Centre. <http://dx.doi.org/10.5286/UKERC.EDC.000002>

This data is made freely available under Creative Commons Attribution 4.0 International (CC BY 4.0). See more at <https://creativecommons.org/licenses/by/4.0/>
