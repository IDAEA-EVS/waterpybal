# ***Visualization and outputs***

Generally, the dataset path loaded by WaterpyBal is the current project which could be changed if any other dataset is going to be used.

After defining the variable name and the desired time period, the excels or Figures of a specific coordination could be generated using the *Time series of a point* section.

The rasters or the maps of **each time step** could also be generated in *Maps* section. It is recommended to use short time periods to generate maps in .png format.

To clarify the water balance, the *Report* section allow to have the water balance variables integrated in an Excel report.
By introducing a raster, it is possible to have the water balance variables in each region or in the whole study area.

&nbsp;

>***IMPORTANT NOTE:*** All the rasters that is used in a WaterpyBal project have to have the exact same Geographic coordinate system, pixel resolution, length and width. We recommend [QGIS](https://www.qgis.org) as a free and Open Source software for shapefile to tif conversations, creating multiband tifs, raster resampling, etc. 