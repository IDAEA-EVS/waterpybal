# ***WaterpyBal Studio***

WaterpyBal Studio is the user interface of [Waterpybal Python Library](https://github.com/IDAEA-EVS/waterpybal).

WaterpyBal Studio contains the more frequently used capabilities of the Waterpybal Python Library.

---
---

## **How to calculate water balance of a study area?**
*From measured input data to the Spatio-temporal water balance model:*

&nbsp;

WaterpyBal library uses a single netCDF database to store the input and calculated data. In this document, the word *dataset* is used to describe the aformentioned database.

The first step is to create a **WaterPyBal dataset** or **Open an existing WaterPyBal dataset**.


In case of creatinng a new dataset, the spatial-temporal properties of the dataset have to be identified.

In case of opening an existing dataset, the model time step interval and a raster file that determines the study area have to be introduced.

After this stage, the steps that are indicated from 1 to 6 have to be followed based on the needs of each study and the available data.

If a variable is already available, they can be directly introduced in step one and the respective step to calculate them have to be skipped. In case of calculating these variables using WaterpyBal, the calculated data overwrites the introduced data. For example, infiltration data in some study areas are already available. In these cases, they can be introduced in the dataset in step one and the step 4 have to be skipped. Calculating the infiltration again using WaterpyBal will overwrite the introduced data.

After the completion of step 1 - 6, the *Visualization and outputs* option allows the generation of different forms of outputs based on the user needs. This step could be used for visualing any netCDF file.

&nbsp;

>***IMPORTANT NOTE:*** All the rasters that is used in a WaterpyBal project have to have the exact same Geographic coordinate system, pixel resolution, length and width. We recommend [QGIS](https://www.qgis.org) as a free and Open Source software for shapefile to tif conversations, creating multiband tifs, raster resampling, etc. 

&nbsp;


More information on each step are available in each section.

The Waterpybal and Waterpybal Studio manual is also available in [Github](https://github.com/IDAEA-EVS/waterpybal).