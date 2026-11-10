# PHM 2010 Milling Cutter Data Challenge

Force, vibration and acoustic emission records from a high-speed CNC milling machine, with wear measured after each cut, for estimating cutter remaining useful life.

- **Domain:** Manufacturing
- **Asset / Process:** CNC machining and tool wear
- **Modality:** Time series; Vibration
- **Task:** RUL and prognostics; Regression
- **Annotation:** Scalar target
- **Source Type:** Lab or testbed
- **Access:** Direct download
- **Size:** 6 cutter records, about 300 cuts each
- **Year:** 2010
- **Publisher:** PHM Society
- **Benchmark:** Yes

## Description

This dataset comes from the 2010 PHM Society Conference Data Challenge, which asked teams to estimate the remaining useful life of cutters on a high-speed CNC milling machine. The tool is a 6mm ball nose tungsten carbide cutter, and the signals come from a dynamometer, accelerometers and an acoustic emission sensor on an experimental setup.

There are six cutter records, c1 to c6. Records c1, c4 and c6 are training data: each holds a wear file with wear after every cut in 10^-3 mm and about 300 CSV files, one per cut. Each file has seven columns, force and vibration in X, Y and Z plus AE-RMS. The spindle ran at 10400 RPM with a feed rate of 1555 mm/min, sampled at 50 kHz per channel.

Records c2, c3 and c5 are the test data. The organisers outline a path from feature extraction to wear models and RUL prediction, checked with leave-one-out cross-validation. Each compressed record is about 800 MB and downloads directly from the challenge page.

## References

- [Official page](https://phmsociety.org/phm_competition/2010-phm-society-conference-data-challenge/)
- [Industrial Atlas page](https://www.indatlas.com/datasets/phm-2010-milling/)

[⬅️ Back to Index](../README.md)
