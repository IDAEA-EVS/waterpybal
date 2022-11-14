# ***Infiltration Calculation***

Calculating Infiltration using Curve Number is available if the WaterpyBal dataset time interval is daily. If not, the infiltration have to be introduced directly in step 1.
A multi band raster have to be used to introduce the data needed to calculate Curve Number.

HSG: Hydrologic Soil Group

LU: Land use

&nbsp;

>***IMPORTANT NOTE:*** All the rasters that is used in a WaterpyBal project have to have the exact same Geographic coordinate system, pixel resolution, length and width. We recommend [QGIS](https://www.qgis.org) as a free and Open Source software for shapefile to tif conversations, creating multiband tifs, raster resampling, etc. 

&nbsp;


If the WaterpyBal dataset is a single point, the Curve Number value is limited to be introduced directly. 

Urban infiltration could be calculated by the Composite Curve number correction, Urban Cycle or both. Details of the Urban Cycle can be found in [this article](https://github.com/IDAEA-EVS).

The variables to calculate the Urban water cycle could be determined as a constant, from a raster or from WaterpyBal dataset.
If it is from a raster, the path have to be introduced in the table.
If it is from the WaterpyBal dataset, the *Value or path* field have to be left empty.

&nbsp;


A maximum infiltration threshold value could be determined to limit the infiltration.