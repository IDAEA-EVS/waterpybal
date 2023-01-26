# <p align="center">***WaterpyBal Studio***</p> 


# <p align="center">![](light_theme_2_resized.png)  </p>

# <p align="center"> **Ashkan Hassanzadeh - Enric Vázquez-Suñé**

<p align="center"> 2023

<div style="page-break-after: always;"></div>

&nbsp;

WaterpyBal Studio is the user interface of [Waterpybal Python Library](https://github.com/IDAEA-EVS).

WaterpyBal Studio contains the more frequently used capabilities of the Waterpybal Python Library.

---

## *Waterpybal Studio General Information*

- Version:
    
    alpha.1

- Developer:

    Ashkan Hassanzadeh
    
    IDAEA - CSIC

- Contact Information:

    ahskan.hassanzadeh@gmail.com


## *Waterpybal Studio Installation*

Follow the instruction shown in the ***WaterpyBal_Studio_Installation_Guide.pdf*** file.

## *Waterpybal Studio capabilities*


- Generating spatio-temporal netCDF database of desired variables in hourly, daily or monthly time-steps.

- It can be used in study areas using GeoTIFFs, or in a single point. 

- Various modes of introducing variables from .CSV files or netCDF files and interpolating the available measurments.

- Possibility to import data from Geotiff archives

- Soil water reserve calculation based on Rasters

- Calculating infiltration for daily datasets based on the Curve number method

- Curve number corrections

- Possibility to use advance Curve number options such as customized curve number tables, changing the coefficients of the main Curve number formulas (such as Landa) and customizing the Curve number correction formulas

- Urban Curve number corrections

- A novel urban water cycle calculation

- Various methods of Evapotranspiration Calculation

- calculates the water balance in of a spatio-temporal dataset.

- Visualization of the results in form of excel outputs, rasters, figures or netCDF files. 



## **How to calculate water balance of a study area?**
*From measured input data to the Spatio-temporal water balance model:*

&nbsp;

WaterpyBal library uses a single netCDF database to store the input and calculated data. In this document, the word *dataset* is used to describe the aformentioned database.

The first step is to create a **WaterPyBal dataset** or **Open an existing WaterPyBal dataset**.


In case of creatinng a new dataset, the spatial-temporal properties of the dataset have to be identified.

In case of opening an existing dataset, the time step and a raster file, determining the study area of the dataset have to be introduced.

After this stage, the steps that are indicated from 1 to 6 have to be followed based on the needs of each study and the available data.

If a variable is already available, they can be directly introduced in step one and the respective step to calculate them have to be skipped. In case of calculating these variables using WaterpyBal, the calculated data overwrites the introduced data. For example, infiltration data in some study areas are already available. In these cases, they can be introduced in the dataset in step one and the step 4 have to be skipped.

After the completion of step 1 - 6, the *Visualization and outputs* option allows the generation of different forms of outputs based on the user needs. This step could be used for visualing any netCDF file.

&nbsp;

>***IMPORTANT NOTE:*** All the rasters that is used in a WaterpyBal project have to have the exact same Geographic coordinate system, pixel resolution, length and width. We recommend [QGIS](https://www.qgis.org) as a free and Open Source software for shapefile to tif conversations, creating multiband tifs, raster resampling, etc. 

&nbsp;


More information on each step are available in each section.

The Waterpybal and Waterpybal Studio manual is also available in [Github](https://github.com/IDAEA-EVS).

---

# ***WaterpyBal Studio intro window***

Click on **Enter WaterpyBal Studio** button. The program is available in light and dark themes.

![](gui_help/screenshots/intro.png)

---
# ***New WaterpyBal Studio dataset properties***

&nbsp;

![](gui_help/screenshots/spat_temp_prop.png)

&nbsp;

## Spatial properties:



If the project contains a study area, a sample raster (.tif) have to be introduced. If it is just in one point, ***Single point*** option have to be selected.
If the Urban water balance calculations (Urban water cycle or curve number urban corrections) have to be done in a part of the study area, the respective option have to  be selected.

&nbsp;

>***IMPORTANT NOTE:*** All the rasters that is used in a WaterpyBal project have to have the exact same Geographic coordinate system, pixel resolution, length and width. We recommend [QGIS](https://www.qgis.org) as a free and Open Source software for shapefile to tif conversations, creating multiband tifs, raster resampling, etc. 

&nbsp;

## Temporal properties:

WaterpyBal dataset is a netCDF file that could be created in *hourly, daily or monthly* time intervals.
The dataset accepts the data from 1970-01-01 00:00:00 UTC.

&nbsp;

## Additional Variables:

Any variable could be added to the dataset. This capability is included in the WaterpyBal Studio since the netCDFs could be used to store the data of a study area, even if the data is not related to the water balance. More, introduction, interpolation and visualization of these variables could  also be done using  WaterpyBal Studio.

The main additional variables related to the water balance that have to be added to the dataset are in case the **evapotranspiration** values have to be calculated using WaterpyBal Studio. In this case, the variables that are needed to calculate evapotanspiration and change in time have to be added to the dataset.
Note that if the variable value is the same in the whole study area or it could be introduced in form of a raster (not changes in time), there is no need to add it to the dataset and they can be introduced exactly in **evapotranspiration** callculation step.

&nbsp;

>***IMPORTANT NOTE:*** The variable names have to be exactly the same (Case Sensitive) as it is mentioned in this guide. The WaterpyBal evapotranspiration calculation incorporate the [**pyet python library**](https://pyet.readthedocs.io/en/latest/api/index.html). To keep the consistency between pyet and WaterpyBal, the variable names are unchanged.
The units of the variables could be found [here](https://pyet.readthedocs.io/en/latest/methods/units.html).

&nbsp;

Aformentioned variables vary based on the method that is going to be used for evapotranspiration calculation. The correct method have to be selected by the user based on the ** dataset time interval**, available data, etc.
The variables mentioned as **Mandatory** have to be present in each method to calculate the evapotranspiration.

&nbsp;

### Combination evapotranspiration calculation methods:

&nbsp;


- ***Kimberly Penman:***

    tmean: **Mandatory**, wind: **Mandatory**, rs: Optional, rn: Optional, g: 0, tmax: Optional, tmin: Optional, rhmax: Optional, rhmin: Optional, rh: Optional, pressure: Optional, elevation: Optional, lat: Optional, n: Optional, nn: Optional, rso: Optional, a: 1.35, b: -0.35

- ***Penman:***
    
    tmean: **Mandatory**, wind: **Mandatory**, rs: Optional, rn: Optional, g: 0, tmax: Optional, tmin: Optional, rhmax: Optional, rhmin: Optional, rh: Optional, pressure: Optional, elevation: Optional, lat: Optional, n: Optional, nn: Optional, rso: Optional, aw: 2.6, bw: 0.536, a: 1.35,b: -0.35

- ***FAO-56 Penman-Monteith:***

    tmean: **Mandatory**, wind: **Mandatory**, rs: Optional, rn: Optional, g: 0, tmax: Optional, tmin: Optional, rhmax: Optional, rhmin: Optional, rh: Optional, pressure: Optional, elevation: Optional, lat: Optional, n: Optional, nn: Optional, rso: Optional, a: 1.35, b: -0.35

- ***Priestley and taylor:***

    tmean: **Mandatory**, wind: **Mandatory**, rs: Optional, rn: Optional, g: 0, tmax: Optional, tmin: Optional, rhmax: Optional, rhmin: Optional, rh: Optional, pressure: Optional, elevation: Optional, lat: Optional, n: Optional, nn: Optional, rso: Optional, a: 1.35, b: -0.35, alpha: 1.26

- ***Penman-Monteith:***

    tmean: **Mandatory**, wind: **Mandatory**, rs: Optional, rn: Optional, g: 0, tmax: Optional, tmin: Optional, rhmax: Optional, rhmin: Optional, rh: Optional, pressure: Optional, elevation: Optional, lat: Optional, n: Optional, nn: Optional, rso: Optional, a: 1.35, b: -0.35, lai: Optional, croph: Optional, r_l: 100, r_s: 70, ra_method: 1, a_sh: 1, a_s: 1, lai_eff: 1, srs: 0.0009, co2: 300

- ***Thom and Oliver:***

    tmean: **Mandatory**, wind: **Mandatory**, rs: Optional, rn: Optional, g: 0, tmax: Optional, tmin: Optional, rhmax: Optional, rhmin: Optional, rh: Optional, pressure: Optional, elevation: Optional, lat: Optional, n: Optional, nn: Optional, rso: Optional, aw: 2.6, bw: 0.536, a: 1.35, b: -0.35, lai: Optional, croph: Optional, r_l: 100, r_s: 70, ra_method: 1, lai_eff: 1, srs: 0.0009, co2: 300

&nbsp;

### Temperature evapotranspiration calculation methods:

&nbsp;

- ***Blaney_criddle:***

    tmean: **Mandatory**, p: **Mandatory**, k: 0.85

- ***Hamon:*** 

    tmean: **Mandatory**, lat: **Mandatory**

- ***Linacre:*** 

    tmean: **Mandatory**, elevation: **Mandatory**, lat: **Mandatory**, tdew: Optional, tmax: Optional, tmin: Optional

- ***Romanenko:*** 

    tmean: **Mandatory**, rh: **Mandatory**, k: 4.5

&nbsp;

### Radiation evapotranspiration calculation methods:

&nbsp;

- ***Abtew:*** 

    tmean: **Mandatory**, rs: **Mandatory**, k: 0.53

- ***Doorenbos–Pruitt (FAO-24):*** 

    tmean: **Mandatory**, wind: **Mandatory**, rs: **Mandatory**, rh: **Mandatory**, pressure: Optional, elevation: Optional, albedo: 0.23

- ***Hargreaves:*** 

    tmean: **Mandatory**, tmax: **Mandatory**, tmin: **Mandatory**, lat: **Mandatory**

- ***Jensen and Haise:*** 

    tmean: **Mandatory**, rs: Optional, cr: 0.025, tx: -3, lat: Optional, method: 1

- ***Makkink:*** 

    tmean: **Mandatory**, rs: **Mandatory**, pressure: Optional, elevation: Optional

- ***McGuinness and Bordne:*** 

    tmean: **Mandatory**, lat: **Mandatory**, k: 0.0147

- ***Oudin:*** 

    tmean: **Mandatory**, lat: **Mandatory**, k1: 100, k2: 5

- ***Turc:*** 

    tmean: **Mandatory**, rs: **Mandatory**, rh: **Mandatory**, k: 0.31

---

# ***Variable introduction and spatial interpolation***

&nbsp;

![](gui_help/screenshots/var_intro.png)

&nbsp;


The data can be introduced to the WaterpyBal dataset using WaterpyBal Studio in four ways: Using .CSV files, directly determining the value of a variable, from a netCDF database or from a Geotiff archive. Introducing data from a Geotiff archive will be done in a seperate step ***NOTE: The info introduced from a Geotiff arhchive overwrite the (if) already existing variables.***

To introduce various variables in WaterpyBal dataset, *Variable introduction and spatial interpolation* process have to be applied seperately. 

&nbsp;

## Variable interpolation and introduction from a .CSV file

&nbsp;


To interpolate a variable in all study area using the measured data points, a .csv file with following properties have to be introduced:

- It have to be contained at least time, lat, lon, and the variable column
- The name of the variable have to be the same as the name of the variable in the WaterpyBal dataset (Don't forget to click *refresh* button so the variables will be available to choose in drop down menu)
- The interpolation will be done in time steps that the .CSV data are available.
- Do not leave the .CSV field empty. If there is no data, delete the row.
- Determine the .CSV file time interval. **In case the .CSV time interval and the dataset time interval are different, the variable values will be devided or integrated to match the WaterpyBal dataset time interval.**
- Four methods are available to interpolate the variables. The methods parameters will appear after selecting the desired method.
- If the data for all the pixels are available (introducing data from a .CSV file), it can be done by using nearest neighbour method and a small radius. So each introduced point falls inside the final pixel.

- An example of a valid .csv file can be found [here](https://github.com/IDAEA-EVS).

&nbsp;

## Propagate the same value for a variable in all time steps

&nbsp;

This option can be used to introduce the same value for a variable in the dataset in the whole Spatial-temporal extent of the study area.

&nbsp;

## Introduce data from a netCDF dataset

&nbsp;

The dimensions and the variable name of the external netCDF dataset have to be the same as the WaterpyBal dataset.

&nbsp;

## **WaterpyBal dataset pre-defined variables:**

&nbsp;

Following variables could be introduced into the WaterpyBal dataset directly, interpolated or calculated using WaterpyBal.

&nbsp;

Precipitation: **Prec_Val**, *mm*

Run-off: **Runoff_Val**, *mm*

Irrigation: **Irig_Val**, *mm*

&nbsp;

### **Curve number-related variables**

Curve number: **CN_Val**, *No_Unit*

Five day accumulated precipitation: **five_day_acc_prec**, *mm*

Corrected curve number: **CN_mod**, *no_unit*

&nbsp;

### **Evapotranspiration-related variables**

Potential Evapotranspiration: **ETP_Val**, *mm*


&nbsp;

### **Soil properties-related variables**

Soil water reserve: **PRu_Val**, *mm*

Permanent Wilting Point: **pwp**, *no_unit*

Field Capacity: **cc**, *no_unit*

Root Radial Thickness: **rrt**, *no_unit*

&nbsp;

### **Water Balance-related variables**

Infiltration: **INF_Val**, *mm*

Actual Evapotranspiration: **ETR_Val**, *mm*

Deficit: **Def_Val**, *mm*

Recharge: **Rec_Val**, *mm*

Soil Water Storage: **Ru_Val**, *mm*

&nbsp;


### **WaterpyBal dataset pre-defined *urban* variables:**

&nbsp;

Following variables will be added to the database in case the urban WaterpyBal option is selected. More information about the following variables can be found [here]() and [here]().

&nbsp;

Water Consumption: **wat_cons**, *mm*

Water Network Loss: **wat_net_loss**, *%*

Direct Urban Evaporation (% of water precipitation+irrigation): **urb_dir_evap**, *%*

Indirect Urban Evaporation (% of water consumption): **urb_indir_evap**, *%*

Sewage Network Loss normal: **sew_net_loss_low**, *%*

Sewage Network Loss rainy season: **sew_net_loss_high**, *%*

Threshold of rainy season per time step for sewage loss: **prec_sewage_threshold**, *mm*

Run-off to Sewage: **runoff_to_sewage**, *%*

Direct Infiltration (% of water precipitation+irrigation): **dir_infil**, *%*

Water Consumption NOT from network (Wells,etc.): **wat_supp_wells**, *mm*

Water Consumption NOT from network loss: **wat_supp_wells_loss**, *%*

Water from other sources (underground infrustructures,etc.): **wat_other**, *%*

Urban to calculated Infiltration and Evapotranspiration ratio: **urban_to_ds_inf_etp_ratio**, *%*

---

# ***Import data from tiff archives***

&nbsp;

![](gui_help/screenshots/from_tiff.png)

&nbsp;




>***IMPORTANT NOTE:*** All the rasters that is used in a WaterpyBal project have to have the exact same Geographic coordinate system, pixel resolution, length and width. We recommend [QGIS](https://www.qgis.org) as a free and Open Source software for shapefile to tif conversations, creating multiband tifs, raster resampling, etc.

&nbsp;


>***NOTE: The info introduced from a Geotiff arhchive overwrite the already existing variables.***

To introduce the data from a folder to the WaterpyBal dataset, each tif file name have to be the date of the data in the YYYY-MM-DD-HH format.

Similar to the *Variable introduction and spatial interpolation* step, **in case the .tif time intervals and the dataset time interval are different, the variable values will be devided or integrated to match the WaterpyBal dataset time interval.**

---


# ***Soil Water Reserve Calculation***

&nbsp;

![](gui_help/screenshots/swr.png)

&nbsp;



CC: Field Capacity

PWP: Permanent Wilting Point

RRT: Root Radial Thickness

The data can be introduced from the WaterpyBal dataset (generally used for scenarios with time-varied soil properties that is already introduced into the dataset in step 1), a multi-band raster or as a constant value value.


&nbsp;

>***IMPORTANT NOTE:*** All the rasters that is used in a WaterpyBal project have to have the exact same Geographic coordinate system, pixel resolution, length and width. We recommend [QGIS](https://www.qgis.org) as a free and Open Source software for shapefile to tif conversations, creating multiband tifs, raster resampling, etc. 

---


# ***Infiltration Calculation***

&nbsp;

![](gui_help/screenshots/inf.png)

&nbsp;



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

---

# ***ETP Calculation***

&nbsp;

![](gui_help/screenshots/etp.png)

&nbsp;



The additional variables added to the dataset in step one can be used here to calculate **evapotranspiration**.

Note that if the variable value is the same in the whole study area or it could be introduced in form of a raster (not changes in time), there is no need to add it to the dataset and the *type* field have to be *constant* or *raster*.

&nbsp;

>***IMPORTANT NOTE:*** The variable names have to be exactly the same (Case Sensitive) as it is mentioned in this guide. The WaterpyBal evapotranspiration calculation incorporate the [**pyet python library**](https://pyet.readthedocs.io/en/latest/api/index.html). To keep the consistency between pyet and WaterpyBal, the variable names are unchanged.
The units of the variables could be found [here](https://pyet.readthedocs.io/en/latest/methods/units.html).

&nbsp;

Aformentioned variables vary based on the method that is going to be used for evapotranspiration calculation. The correct method have to be selected by the user based on the ** dataset time interval**, available data, etc.

&nbsp;

### Combination evapotranspiration calculation methods:

&nbsp;


- ***Kimberly Penman:***

    tmean: **Mandatory**, wind: **Mandatory**, rs: Optional, rn: Optional, g: 0, tmax: Optional, tmin: Optional, rhmax: Optional, rhmin: Optional, rh: Optional, pressure: Optional, elevation: Optional, lat: Optional, n: Optional, nn: Optional, rso: Optional, a: 1.35, b: -0.35

- ***Penman:***
    
    tmean: **Mandatory**, wind: **Mandatory**, rs: Optional, rn: Optional, g: 0, tmax: Optional, tmin: Optional, rhmax: Optional, rhmin: Optional, rh: Optional, pressure: Optional, elevation: Optional, lat: Optional, n: Optional, nn: Optional, rso: Optional, aw: 2.6, bw: 0.536, a: 1.35,b: -0.35

- ***FAO-56 Penman-Monteith:***

    tmean: **Mandatory**, wind: **Mandatory**, rs: Optional, rn: Optional, g: 0, tmax: Optional, tmin: Optional, rhmax: Optional, rhmin: Optional, rh: Optional, pressure: Optional, elevation: Optional, lat: Optional, n: Optional, nn: Optional, rso: Optional, a: 1.35, b: -0.35

- ***Priestley and taylor:***

    tmean: **Mandatory**, wind: **Mandatory**, rs: Optional, rn: Optional, g: 0, tmax: Optional, tmin: Optional, rhmax: Optional, rhmin: Optional, rh: Optional, pressure: Optional, elevation: Optional, lat: Optional, n: Optional, nn: Optional, rso: Optional, a: 1.35, b: -0.35, alpha: 1.26

- ***Penman-Monteith:***

    tmean: **Mandatory**, wind: **Mandatory**, rs: Optional, rn: Optional, g: 0, tmax: Optional, tmin: Optional, rhmax: Optional, rhmin: Optional, rh: Optional, pressure: Optional, elevation: Optional, lat: Optional, n: Optional, nn: Optional, rso: Optional, a: 1.35, b: -0.35, lai: Optional, croph: Optional, r_l: 100, r_s: 70, ra_method: 1, a_sh: 1, a_s: 1, lai_eff: 1, srs: 0.0009, co2: 300

- ***Thom and Oliver:***

    tmean: **Mandatory**, wind: **Mandatory**, rs: Optional, rn: Optional, g: 0, tmax: Optional, tmin: Optional, rhmax: Optional, rhmin: Optional, rh: Optional, pressure: Optional, elevation: Optional, lat: Optional, n: Optional, nn: Optional, rso: Optional, aw: 2.6, bw: 0.536, a: 1.35, b: -0.35, lai: Optional, croph: Optional, r_l: 100, r_s: 70, ra_method: 1, lai_eff: 1, srs: 0.0009, co2: 300

&nbsp;

### Temperature evapotranspiration calculation methods:

&nbsp;

- ***Blaney_criddle:***

    tmean: **Mandatory**, p: **Mandatory**, k: 0.85

- ***Hamon:*** 

    tmean: **Mandatory**, lat: **Mandatory**

- ***Linacre:*** 

    tmean: **Mandatory**, elevation: **Mandatory**, lat: **Mandatory**, tdew: Optional, tmax: Optional, tmin: Optional

- ***Romanenko:*** 

    tmean: **Mandatory**, rh: **Mandatory**, k: 4.5

&nbsp;

### Radiation evapotranspiration calculation methods:

&nbsp;

- ***Abtew:*** 

    tmean: **Mandatory**, rs: **Mandatory**, k: 0.53

- ***Doorenbos–Pruitt (FAO-24):*** 

    tmean: **Mandatory**, wind: **Mandatory**, rs: **Mandatory**, rh: **Mandatory**, pressure: Optional, elevation: Optional, albedo: 0.23

- ***Hargreaves:*** 

    tmean: **Mandatory**, tmax: **Mandatory**, tmin: **Mandatory**, lat: **Mandatory**

- ***Jensen and Haise:*** 

    tmean: **Mandatory**, rs: Optional, cr: 0.025, tx: -3, lat: Optional, method: 1

- ***Makkink:*** 

    tmean: **Mandatory**, rs: **Mandatory**, pressure: Optional, elevation: Optional

- ***McGuinness and Bordne:*** 

    tmean: **Mandatory**, lat: **Mandatory**, k: 0.0147

- ***Oudin:*** 

    tmean: **Mandatory**, lat: **Mandatory**, k1: 100, k2: 5

- ***Turc:*** 

    tmean: **Mandatory**, rs: **Mandatory**, rh: **Mandatory**, k: 0.31

---
# ***Balance Calculation***

&nbsp;

![](gui_help/screenshots/balance.png)

&nbsp;

Initial Soil Water Reserve Percentage determines the saturation of the soil in the first time step of the calculation.

---

# ***Visualization and outputs***

&nbsp;

![](gui_help/screenshots/visual.png)

&nbsp;



Generally, the dataset path loaded by WaterpyBal is the current project which could be changed if any other dataset is going to be used.

After defining the variable name and the desired time period, the excels or Figures of a specific coordination could be generated using the *Time series of a point* section.

The rasters or the maps of **each time step** could also be generated in *Maps* section. It is recommended to use short time periods to generate maps in .png format.

To clarify the water balance, the *Report* section allow to have the water balance variables integrated in an Excel report.
By introducing a raster, it is possible to have the water balance variables in each region or in the whole study area.

&nbsp;

>***IMPORTANT NOTE:*** All the rasters that is used in a WaterpyBal project have to have the exact same Geographic coordinate system, pixel resolution, length and width. We recommend [QGIS](https://www.qgis.org) as a free and Open Source software for shapefile to tif conversations, creating multiband tifs, raster resampling, etc. 