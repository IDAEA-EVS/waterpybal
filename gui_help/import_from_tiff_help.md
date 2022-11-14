# ***Import data from tiff archives***


>***IMPORTANT NOTE:*** All the rasters that is used in a WaterpyBal project have to have the exact same Geographic coordinate system, pixel resolution, length and width. We recommend [QGIS](https://www.qgis.org) as a free and Open Source software for shapefile to tif conversations, creating multiband tifs, raster resampling, etc.

&nbsp;


>***NOTE: The info introduced from a Geotiff arhchive overwrite the already existing variables.***

To introduce the data from a folder to the WaterpyBal dataset, each tif file name have to be the date of the data in the YYYY-MM-DD-HH format.

Similar to the *Variable introduction and spatial interpolation* step, **in case the .tif time intervals and the dataset time interval are different, the variable values will be devided or integrated to match the WaterpyBal dataset time interval.**
