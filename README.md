# VNAReader
GUI for visualization and analysis of the reflection scattering parameter S11 registered in biosensors setups.

The current version is designed for S11 values registered as Real and Imaginary components with a DG8-SAQ Vector Network Analyzer (VNA, SDR-Kits). Implementation to load data from different VNAs or formats should be easy.

I will add more detailed instructions as soon as I have the time. For the time being, just have a look at the Quick Start section below.

## Requiremenets
Tested with python 3.7 - 3.9

The libraries required can be found in requirements.txt.

## Quick Start
The easiest way to run the program is within a virtual environment. First, create it e.g.:
```
python -m venv env
```

and then activate it:

In Linux:
```
source env/bin/activate
```

In Windows:
```
.\env\Scripts\activate
```

Then, install packaged using requirements.txt, e.g.:
```
python -m pip install -r requirements.txt
```

Then, for running the program:
```
python -m vnareader
```

This should open the following GUI:

![image](./Tutorial_Data/Figure1.png)

Go to File -> Open to load the VNA S11 file, then you will see Real and Imaginary components of this quantity in the figure axis:

![image](./Tutorial_Data/Figure2.png)

You can change the S11 representation using the buttons in the bottom of the GUI for the selected Plot (which you can select in the upper right corner of the GUI)

If the data corresponds to a single antenna connected to the VNA, you can analyze it by going to Analysis -> Single Antenna. This should take you to the following GUI:

![image](./Tutorial_Data/Figure3.png)

If the data corresponds instead to two coupled antennas, one of them being the reader antenna, and the other one being the tag antenna which is itself connected to a sensing element, you can analyze it by going to Analysis -> Coupled Antennas. This should take you to the following GUI:

![image](./Tutorial_Data/Figure4.png)

## Author
[Javier Sotres](https://github.com/JSotres)
