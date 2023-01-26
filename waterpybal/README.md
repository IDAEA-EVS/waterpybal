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