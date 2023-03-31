# ***WaterpyBal***

This repository contains an open source Python library for water balance modelling.

---



## ***Package information:***
\
Name: WaterpyBal

version: 1.0.0

Author: Ashkan Hassanzadeh   

Email: ashkan.hassanzadeh@gmail.com

python: 3.*

License: agpl-3.0

---



## ***Installation:***
\
pip can be used for the installation:

`pip install waterpybal`

Alternatively, download the waterpybal folder from the github repository and add it to lib folder in python path alongside other python libraries.

---



## ***documentation:***
\
Waterpybal documentation can be found in [readthedocs](https://waterpybal.readthedocs.io)
---



## ***Jupyter Notebook:***
\
There is a notebook in [WaterpyBal's github repository](https://github.com/IDAEA-EVS/waterpybal) that explains an example of implementing WaterpyBal on spatial and isotopic data


---



## ***WaterpyBal Studio: Graphic User interface of WaterpyBal***

The GUI of WaterpyBal (WaterpyBal Studio), alongside the installation guide and the user manual can be foud [here](http://hdl.handle.net/10261/305226)


# waterpyBal and waterpyBal Studio

***waterpyBal*** is an open-souce Python library to calculate the spatial-temporal water cycle variables. WaterpyBal can be used to:

- Generate spatio-temporal netCDF database of desired variables in hourly, daily or monthly time-steps.

- In study areas using GeoTIFFs, or in a single point. 

- Various modes of introducing variables: numpy arrays, .CSV files or netCDF files and interpolating the available measurments.

- Possibility to import data from Geotiff archives

- Soil water reserve calculation based on Rasters

- Calculating infiltration for daily datasets based on the Curve number method

- Curve number corrections

- Possibility to use advance Curve number options such as customized curve number tables, changing the coefficients of the main Curve number formulas (such as Landa) and customizing the Curve number correction formulas

- Urban Curve number corrections

- A novel urban water cycle calculation

- Various methods of Evapotranspiration Calculation

- calculates the water balance in of a spatio-temporal dataset.

- Post-processing: Visualization of the results in form of excel outputs, rasters, figures or netCDF files. Generating Water balance reports.


***waterpyBal Studio*** is the user-interface of the waterpybal API. It contains the more frequently used capabilities of the Waterpybal Python Library.

&nbsp;

>***IMPORTANT NOTE:*** All the rasters that is used in a WaterpyBal project (waterpyBal and waterpyBal Studio) have to have the exact same Geographic coordinate system, pixel resolution, length and width. We recommend [QGIS](https://www.qgis.org) as a free and Open Source software for shapefile to tif conversations, creating multiband tifs, raster resampling, etc. 