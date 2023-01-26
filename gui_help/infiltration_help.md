# ***Infiltration Calculation***

Calculating Infiltration using Curve Number is available if the WaterpyBal dataset time interval is **daily**. If not, the infiltration has to be introduced directly in step 1.
A multi-band raster have to be used to introduce the data needed to calculate Curve Number, containing Land use, hydrologic soil group and hydrologic condition/Altitude (In case the curve number table is based on the slope groups).

HSG: Hydrologic Soil Group

LU: Land use

HC: Hydrologic Condition

The USGS recommended table is the default table, considering the Initial abstraction ratio of 0.2.

The **Advanced Curve Number Tuning** section allows the user to modify the Potential Maximum retention (S) formula as a polynomial equation of the curve numbre. Note that by chaging the S formula, the curve number table have to be modified respectively.

The **CN Calue** section is to choose a constant number as the curve number for the whole study area in all time-steps.

&nbsp;

>***IMPORTANT NOTE:*** All the rasters that is used in a WaterpyBal project have to have the exact same Geographic coordinate system, pixel resolution, length and width. We recommend [QGIS](https://www.qgis.org) as a free and Open Source software for shapefile to tif conversations, creating multiband tifs, raster resampling, etc. 

&nbsp;


If the WaterpyBal dataset is a single point, the Curve Number value is limited to be introduced directly. 

**Urban infiltration** could be calculated by the **Composite Curve number correction**, **Urban Cycle** or both. More details of the Urban Cycle can be found in [this article](https://github.com/IDAEA-EVS).

*The urban zone raster have to have the exact same Geographic coordinate system, pixel resolution, length and width as other rasters, with nodata (-9999) value in all the study area except the urban zone*

The variables to calculate the Urban water cycle could be determined as a constant, from a raster or from WaterpyBal dataset.
If it is from a raster, the path have to be introduced in the table.
If it is from the WaterpyBal dataset, the *Value or path* field have to be left empty.

&nbsp;


A maximum infiltration threshold value could be determined to limit the infiltration.