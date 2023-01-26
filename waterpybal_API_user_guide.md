# ***waterpyBal***

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

&nbsp;

>***IMPORTANT NOTE:*** All the rasters that is used in a WaterpyBal project (waterpyBal and waterpyBal Studio) have to have the exact same Geographic coordinate system, pixel resolution, length and width. We recommend [QGIS](https://www.qgis.org) as a free and Open Source software for shapefile to tif conversations, creating multiband tifs, raster resampling, etc. 

&nbsp;

## ***Package information:***


Name: WaterpyBal

version: 1.0

Author: Ashkan Hassanzadeh   

Email: ashkan.hassanzadeh@gmail.com

python: 3.*

License: agpl-3.0

https://github.com/IDAEA-EVS/waterpybal

---

## ***Installation:***

Download the waterpybal folder and add it to lib folder in python path alongside other libraries.

---

## ***Jupyter Notebook:***

There is a Jupyter notebook that explains a synthetic example of implementing waterpybal on spatial-temporal data.

---
# class dataset_prep.dataset_gen()
The class to create the waterpybal netCDF dataset dimensions and variables

&nbsp;

>***IMPORTANT NOTE:*** All the rasters that is used in a WaterpyBal project (waterpyBal and waterpyBal Studio) have to have the exact same Geographic coordinate system, pixel resolution, length and width. We recommend [QGIS](https://www.qgis.org) as a free and Open Source software for shapefile to tif conversations, creating multiband tifs, raster resampling, etc. 

**WaterpyBal dataset pre-defined variables:**

&nbsp;

Following variables could be introduced into the WaterpyBal dataset directly, interpolated or calculated using WaterpyBal.

&nbsp;

Precipitation: **Prec_Val**, *mm*

Run-off: **Runoff_Val**, *mm*

Irrigation: **Irig_Val**, *mm*

&nbsp;

**Curve number-related variables**

Curve number: **CN_Val**, *No_Unit*

Five day accumulated precipitation: **five_day_acc_prec**, *mm*

Corrected curve number: **CN_mod**, *no_unit*

&nbsp;

**Evapotranspiration-related variables**

Potential Evapotranspiration: **ETP_Val**, *mm*


&nbsp;

**Soil properties-related variables**

Soil water reserve: **PRu_Val**, *mm*

Permanent Wilting Point: **pwp**, *no_unit*

Field Capacity: **cc**, *no_unit*

Root Radial Thickness: **rrt**, *no_unit*

&nbsp;

**Water Balance-related variables**

Infiltration: **INF_Val**, *mm*

Actual Evapotranspiration: **ETR_Val**, *mm*

Deficit: **Def_Val**, *mm*

Recharge: **Rec_Val**, *mm*

Soil Water Storage: **Ru_Val**, *mm*


---

**Methods**

> dtype = ds_dimensions(self,lat_lon_type,lat_lon_source,time_source,time_type,preferred_date_interval,lat_name="lat",lon_name="lon",time_name="time",border_res_dic=None,time_dic=None)

> ds = var_generation(self,dir,ds_values_dic=None,urban_ds=False)

---

**Attributes**

lat

lon

time

dtype

time_steps_dic

    Contains the time step information for the waterpybal netcdf dataset. Have to be introduced in var_generation function.
    Format: {"time_v": time_v, "time_b1": time_b1, "time_b2": time_b2, "tunit": tunit}

---
---
## dataset_prep.dataset_gen.ds_dimensions()

dtype = ds_dimensions(lat_lon_type,lat_lon_source,time_source,time_type,lat_name,lon_name,time_name,border_res_dic,time_dic,preferred_date_interval)

The method to create the waterpybal netCDF dataset lat long and time dimensions


**Parameters**

- lat_lon_type str

Source type that identify the lat and long of the dataset. "dataframe", "csv", "netcdf", "raster" and "border_res_dic" are valid.
if "border_res_dic" is selected, the borders of the dataset have to be defined in border_res_dic parameter.

---
- lat_lon_source str (.csv - .nc - .tif) or pandas dataframe

If the lat_lon_type is "dataframe", "csv", "netcdf" or "raster", lat_lon_source is the source of the lat and long values.

---
- time_type str

Source type that identify the time steps of the dataset. "dataframe", "csv", "netcdf" and "time_dic" are valid.
if "time_dic" is selected, the borders of the dataset have to be defined in border_res_dic parameter.

---
- time_source str (.csv - .nc) or pandas dataframe

If the time_type is "dataframe", "csv" or "netcdf", lat_lon_source is the source of the dataset time steps.

---
- lat_name str default: "lat"

Applicabale if the lat_lon_type is "dataframe", "csv", "netcdf". lat field name.

---
-lon_name str default: "lon"

Applicabale if the lat_lon_type is "dataframe", "csv", "netcdf". lon field name.

---
- time_name str default: "time"

Applicabale if the time_type is "dataframe", "csv", "netcdf". time field name.

---
- border_res_dic dic default: None

Applicabale if the lat_lon_type is "border_res_dic". Format: {"left":value,"right":value,"width":value,"top":value,"bottom":value,"height":value}

---
- time_dic dic default: None

Applicabale if the time_type is "time_dic". Format: {"start": ["yyyy","mm","dd","hh"] , "end": ["yyyy","mm"."dd","hh"]}

---
- preferred_date_interval str

Date interval of the dataset. "Hourly", "Daily" and "Monthly" are valid.

---

**Returns**


- dtype str

Dataset time interval dtype

---
---
## dataset_prep.dataset_gen.var_generation()

ds = var_generation(self,dir,ds_values_dic=None,urban_ds=False)          

The method to create the waterpybal netCDF dataset dimensions and variables


**Parameters**

- dir str

The path to save the waterpybal netcdf dataset

---
- ds_values_dic nonetype or dic default: None

To add additional variables to the waterpybal dataset. The additional variables can be used in following stages such as ETP calculation, etc.
Format: ds_values_dic={"desired_variable":"desired_variable_unit",...} 

---
- urban_ds bool default: False

To add the urban related variables to the dataset.

---

**Returns**

- ds netCDF dataset

waterpybal netcdf dataset.

---
---
# class dataset_prep.variable_management()
The class to introduce or interpolate the variables from different sources

**Methods**

> ds = var_interpolation(ds,ras_sample_dir,csv_dir,var_name,method,preferred_date_interval,interpolation_time_int,time_csv_col="time",lat_csv_col="lat",lon_csv_col="lon",multiply=False)

> ds = var_introduction_from_tiffs(ds,folder_dir,var_name,preferred_date_interval,multiply)

> ds = var_introduction_from_csv(ds,csv_dir,time_csv_col,var_name,preferred_date_interval,interpolation_time_int,multiply)

> ds = var_introduction_from_nc(new_nc_dir,ds,var_name)
---
---

## dataset_prep.variable_management.var_interpolation()

ds = var_interpolation( ds, ras_sample_dir, csv_dir, time_csv_col, lat_csv_col, lon_csv_col, var_name, method, preferred_date_interval, interpolation_time_int, multiply)

The method to interpolate variables from .csv files. The .csv have to have a lat, long, time and variable name field.
The variable name field have to be the same as the name in the waterpybal dataset.


**Parameters**

- ds netCDF dataset

waterpybal netcdf dataset.

---
- ras_sample_dir str

path to the raster (.tif) file that represents the study area.

---
- csv_dir str

Path to the .csv file that contains the measured data.

---

- time_csv_col str default: "time"

.csv time field name

---
- lat_csv_col str default "lat"

.csv lat field name

---
- lon_csv_col str default "lon"

.csv lon field name

---
- var_name str

.csv variable field name. Have to be the same as watepybal netcdf dataset.

---   
- method str
refer to gdal.grid method for more information about the available methods.

Examples:

> "nearest"

> "invdist:power=2:radius1=100:radius2=800"

> "linear"

> "average:radius1=100:radius2=800:angle=20"

> "minimum:radius1=100:radius2=800:angle=20"

---
- preferred_date_interval str

Waterpybal dataset time interval.

---
- interpolation_time_int str

.csv time interval. In case the .csv time interval differ the dataset time interval, the .csv values proportionally will be distributed between the time steps.

---
- multiply bool default: False 

In case the .csv time interval is not the same as the dataset, use the same values for valid time steps
(Ex: Temp. vs cumulative precipitation)

---

**Returns**

- ds netCDF dataset

waterpybal netcdf dataset.

---
---
## dataset_prep.variable_management.var_introduction_from_tiffs()

ds = var_introduction_from_tiffs(ds,folder_dir,var_name,preferred_date_interval,multiply)

The method to introduce variables from a folder containing the geotiff (.tif) files. the name of the files in the folder have to be the time step they're refering to.
Format: YYYY-MM-DD-HH


**Parameters**

- ds netCDF dataset

waterpybal netcdf dataset.

---
- folder_dir str

path to the folder containing the geotiff (.tif) files

---
- var_name str

.csv variable field name. Have to be the same as watepybal netcdf dataset.

---
- preferred_date_interval str

Waterpybal dataset time interval.

---
- multiply bool default: False 

In case the .csv time interval is not the same as the dataset, use the same values for valid time steps
(Ex: Temp. vs cumulative precipitation)

---

**Returns**

- ds netCDF dataset

waterpybal netcdf dataset.

---
---
## dataset_prep.variable_management.var_introduction_from_csv()

ds = var_introduction_from_csv(ds,csv_dir,var_name,preferred_date_interval,interpolation_time_int,time_csv_col="time",multiply=False)

The method to introduce **THE SAME VALUES FOR ALL THE STUDY AREA IN A TIMESTEP** from a .csv file without interpolation.


**Parameters**

- ds netCDF dataset

waterpybal netcdf dataset.

---
- csv_dir str

Path to the .csv file that contains the measured data.

---

- time_csv_col str default: "time"

.csv time field name

---
- var_name str

.csv variable field name. Have to be the same as watepybal netcdf dataset.

---
- preferred_date_interval str

Waterpybal dataset time interval.

---
- interpolation_time_int str

.csv time interval. In case the .csv time interval differ the dataset time interval, the .csv values proportionally will be distributed between the time steps.

---
- multiply bool default: False 

In case the .csv time interval is not the same as the dataset, use the same values for valid time steps
(Ex: Temp. vs cumulative precipitation)

---

**Returns**

- ds netCDF dataset

waterpybal netcdf dataset.

---
---
## dataset_prep.variable_management.var_introduction_from_nc()

ds = var_introduction_from_nc(new_nc_dir,ds,var_name)

The method to introduce variables from a netcdf database with the same dimension and variable name


**Parameters**

- ds netCDF dataset

waterpybal netcdf dataset.

---
- new_nc_dir str

path to the new netcdf file.

---
- var_name str

new netcdf variable field name. Have to be the same as watepybal netcdf dataset.

---

**Returns**

- ds netCDF dataset

waterpybal netcdf dataset.

---
---
# class etp_calcs.ETP()
The class to calculate evapotranspiration
**Methods**

> ds = ETP_calc(ds, method, preferred_date_interval, var_name='ETP_Val', raster_etp_var_dic=None, **kwargs)


---
---

## etp_calcs.ETP.ETP_calc()


ds = ETP_calc(ds, method, preferred_date_interval, var_name='ETP_Val', raster_etp_var_dic=None, **kwargs)

ETP_calc method calculate evapotranspiration in all the dataset. It uses ***pyet*** library for
ETP calculations which is opted for use in a single point.

Depending on the ETP method, necessary arguments have to be introduced to the database. If the argument is a 
fix number for all times and coordinates, it could be determined right away. If the ETP
related argument is equal to 'ds', the argument will be derived from the variable with the same name
in the dataset. Note that user have to introduce this variables to the dataset beforehead. If the
argument value changes with the coordinate but not with the time, the etp argument have to be equal
to 'raster'. the direction and the band of the targed master have to be determined in raster_etp_var_dic
argument using the following syntax:

{"var_name":["raster_dir","raster_band"]} or {"var_name":"raster_dir"} (band default to 1) or {"var_name":["raster_dir"]} (band default to 1)


Let's elaborate using this function with an example:

Suppose we are using penman method for calculating ETP. "tmean" and "wind" are mandatory arguments for this method.
Since in this example "tmean" and "wind" are changing in each coordinate, the user have to use "ds"
to determine the this data have to be retrieved from dataset variables by the same name. Then there are "aw" and "bw" which
have a fixed value by default ("aw"=2.6, "bw"=0.536), but could be changed based on the coordinates.
so by defining "aw"="raster" and "bw"="raster and raster_etp_var_dic={"aw":["ras_dir",band1],"bw":["ras_dir",band2]},
aw and bw arguments are equal to raster values of band 1 and 2 respectively. 


**Parameters**

- ds netCDF dataset

    waterpybal netcdf dataset.

---
- method str

    - Combination evapotranspiration calculation methods:


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


    - Temperature evapotranspiration calculation methods:


        - ***Blaney_criddle:***

        tmean: **Mandatory**, p: **Mandatory**, k: 0.85

        - ***Hamon:*** 

        tmean: **Mandatory**, lat: **Mandatory**

        - ***Linacre:*** 

        tmean: **Mandatory**, elevation: **Mandatory**, lat: **Mandatory**, tdew: Optional, tmax: Optional, tmin: Optional

        - ***Romanenko:*** 

        tmean: **Mandatory**, rh: **Mandatory**, k: 4.5


    - Radiation evapotranspiration calculation methods:

        - ***Abtew:*** 

        tmean: **Mandatory**, rs: **Mandatory**, k: 0.53

        - ***Doorenbos - Pruitt (FAO-24):*** 

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
- preferred_date_interval str

Waterpybal dataset time interval.

---
- raster_etp_var_dic dic default: None
If the ETP variable doesn't change in time, it is possible to use a raster to introduce it's values.

Format:

{"var_name":["raster_dir","raster_band"]} or {"var_name":"raster_dir"} (band default to 1) or {"var_name":["raster_dir"]}

---
- **kwargs dic

A dictionary that defines the inputs of the ETP method.

The constant values can be defined directly

Rasters have to be defined with "raster" keyword, and then introduced in raster_etp_var_dic argument as a dictionary

If the ETP variable exists in the waterpybal dataset, the "ds" keyword have to be used. 

Format:
{"var_name_1":constant_value, "var_name_2": "raster", "var_name_3": "ds",... }

---

**Returns**

- ds netCDF dataset

waterpybal netcdf dataset.

---
---
# class inf_calcs.infiltration()
The class to calculate the infiltration

**Methods**

> ds, Ia = Inf_calc(ds,CN_table_dir,raster_dir,HSG_band,LU_band,ELEV_or_HC_band,DEM_path_or_raster,DEM_or_raster,filled_dep,slope_range_list,amc1_coeffs,amc3_coeffs,dormant_thresh,growing_thresh,average_thresh,mon_list_dormant,preferred_date_interval,corrected_cn,single_cn_val,cn_val,advanced_cn,advanced_cn_dic,SC_or_HC)

> ds = runoff_calc(ds,Ia)

> ds = max_inf_threshold(ds,var_inp,var_out,threshold)
---
---
## inf_calcs.infiltration.Inf_calc()

ds, Ia = Inf_calc(ds,CN_table_dir,raster_dir,HSG_band,LU_band,ELEV_or_HC_band,DEM_path_or_raster,DEM_or_raster,filled_dep,slope_range_list,amc1_coeffs,amc3_coeffs,dormant_thresh,growing_thresh,average_thresh,mon_list_dormant,preferred_date_interval,corrected_cn,single_cn_val,cn_val,advanced_cn,advanced_cn_dic,SC_or_HC)

The method to calculate the infiltration


**Parameters**

- ds netCDF dataset

waterpybal netcdf dataset.

---
CN_table_dir str

Path to the curve number xls table

---
raster_dir str

The multiband raster path, containing the HSG_band,LU_band and ELEV_or_HC_band

---
HSG_band int
Hydrologic Soil Group raster band

---
LU_band int

Land Use Group raster band

---
ELEV_or_HC_band int

Elevation (Slope) Catagory or Hydrologic Condition raster band 

---
DEM_path_or_raster None or str

Path to the DEM to calculate the Slope catagories. If there is no slope catagory in the curve number table (Hydrologic condition), ir the elevations 
are introduced as a band in the multibandraster instead of a DEM, DEM_path_or_raster have to be None

---
DEM_or_raster str default "raster"

"raster" or "DEM". If *SC_or_HC* is "HC", DEM_or_raster will be ignored.

---
filled_dep default True

If to Fill Depressions in calculating elevations or not. If *SC_or_HC* is "HC", it will be ignored.

---
slope_range_list None or list default None

If None, slope_range_list=[1,5,10]. List of boundaries of the Slope Catagories.


---
amc1_coeffs None or list default None

If None, amc1_coeffs=[0.0069,0.2575,0]. Coefficient of Antecedent Moisture Condition (AMC) 1 Formula as a list.

---
amc3_coeffs None or list default None

If None, amc1_coeffs=[-0.0086,1.8338,0]. Coefficient of Antecedent Moisture Condition (AMC) 3 Formula as a list.

---
dormant_thresh None or list default None

If None, dormant_thresh=[12.7,27.9]. Dormant months AMC1 and AMC3 thresholds.

---
growing_thresh None or list default None

If None, growing_thresh=[36.6,53.3]. Growing months AMC1 and AMC3 thresholds.

---
average_thresh bool default False

To use an average of growing and dormant months to identify AMC1 and AMC3.

---
mon_list_dormant None or list default None

if None, mon_list_dormant=[10,11,12,1,2,3]. List of dormant month. Rest of the month will be growing month.

---
preferred_date_interval dtype str

Time interval of the dataset as a dtype.

---
corrected_cn None or bool default None

If the Antecedent Moisture Condition (AMC) corrections have to be applied

---
single_cn_val bool default False

To use a single CN value for the whole dataset
---
cn_val None or float default None

single CN value. Ignored if single_cn_val is False


---
advanced_cn bool default False

If the advanced curve number options are gonna be used. The variables are defined in advanced_cn_dic

---
advanced_cn_dic None or dic default None
A dictionary to change the Ia and the formula of the curve number, containing the following keys and their respective values:

advanced_cn_dic.keys(): "landa", "A","B","C","D","x","y","z"

Formulas:

S= A * CN_mod^x + B * CN_mod^y + C * z + D

S= landa * Ia



---
SC_or_HC str default "HC"

If Hydrologic Condition (default) or Slope Catagory (SC) is defined in the curve number table

---

**Returns**

- ds netCDF dataset

waterpybal netcdf dataset.

- Ia numpy array

Initial abstraction
---
---

## inf_calcs.infiltration.runoff_calc()

ds = runoff_calc(ds,Ia=None)

The method to calculate the runoff in the database. Initial abstraction is None if the
curve number is not calculated by the waterpybal.

If "runoff_Val" is imported directly to the dataset this method do not have to used.



**Parameters**

- ds netCDF dataset

waterpybal netcdf dataset.

---
- Ia    None or numpy array default None

Initial abstraction. 
If None, runoff= Prec +Irrig - Infilt
If not None, runoff= Prec +Irrig - Infilt - Ia
---

**Returns**

- ds netCDF dataset

waterpybal netcdf dataset.

---
---

## inf_calcs.infiltration.max_inf_threshold()

ds = max_inf_threshold(ds,var_inp,var_out,threshold)

The method to force a threshold to an specific variable. Normally used for "INF_Val"
to limit maximum infiltration values.

**Parameters**

- ds netCDF dataset

waterpybal netcdf dataset.

---
- var_inp str

Input variable to limit. "INF_Val" is used normally.
---
- var_out str

Out variable to save the variable. "INF_Val" or "Prec_Val" is used normally.
---
- threshold float

threshold value
---

**Returns**

- ds netCDF dataset

waterpybal netcdf dataset.

---
---
# class swr_calcs.swr.swr_calc()

The class to calculate Soil Water Reserve

**Methods**

> ds = swr_calc(ds,time_steps,raster_PRU_dir=None,raster_bands_dic_or_val=None)

---
---
## swr_calcs.swr.swr_calc.swr_calc()

ds = swr_calc(ds,time_steps,raster_PRU_dir=None,raster_bands_dic_or_val=None)

The method to calculate Soil Water Reserve

Field capacity = cc

permanent wilting point = pwp

root radial thikness = rrt

**Parameters**

- ds netCDF dataset

waterpybal netcdf dataset.

---
- time_steps None or str or list of ints default "all"

time_steps="all" variable soil properties in time-space. calculate for each step
time_steps=None same soil properties for the whole dataset. variable space.
time_steps=[] list of the dataset time steps to be used to calculate SWR for the 
following time steps.

Example:
time_steps=[ 0 , 20, 123]

SWR for steps 0 to 20 will be calculated using the data from step 0.
SWR for steps 20 to 123 will be calculated using the data from step 20.
SWR for steps 123 to the final step will be calculated using the data from step 123.

---
- raster_PRU_dir None or str default None

Path to the multiband raster that contains "cc", "pwp" & "rrt" values.
Useful when SWR is constant in time and varies in space.
If None, use the data from the waterpybal dataset (spatio-temporal variation).

---
- raster_bands_dic_or_val None or dict default None

Ignored if raster_PRU_dir is None. The dictionary containing the band number of the
multiband raster for "cc", "pwp" & "rrt".

Format: raster_bands_dic_or_val = {"cc":value, "rrt": value , "pwp": value}

---

**Returns**

- ds netCDF dataset

waterpybal netcdf dataset.

---
---
# class urban_infiltration.urban_cycle_calcs()

The class to calculate urban water cycle, inspired by the following article:
This class could be used if the waterpybal dataset is marked as the urban dataset.

**Methods**

> ds = urban_cycle_main (ds,urban_area_raster_dir,variables_dic)

---
---
## urban_infiltration.urban_cycle_calcs.urban_infiltration_main()

ds = urban_cycle_main (ds,urban_area_raster_dir,variables_dic)

The method to calculate the urban cycle.


**Parameters**

- ds netCDF dataset

waterpybal netcdf dataset.

---
- urban_area_raster_dir

Path to the raster that identifies the urban area of the study area. 
None urban area have to be nan in this raster


---
- variables_dic dict

A dictionary of the urban variables.
Each urban variable (key), has another dictionary as it's value.

The aformentioned dictionary has 2 keys:

'input_var' value could be a constant number (float), a path to a raster (str) or will be ignored if 'dataset_raster_dir_or_value' is 'Dataset'.

'dataset_raster_dir_or_value' value have to be 'Raster', 'Dataset' or 'Constant'. 
This value identifies the source of the urban cycle variables.


 Example:

                            
```
        variables_dic = {

                            'wat_cons': {

                                'input_var':,
                                'dataset_raster_dir_or_value':
                            },

                            'wat_net_loss': {

                                'input_var':,
                                'dataset_raster_dir_or_value':
                            },

                            .
                            .
                            .

                        }
```

Urban variables and their respective keys are as follows:

- Water Consumption: key wat_cons, mm

- Water Network Loss: key wat_net_loss, %

- Direct Urban Evaporation (% of water precipitation+irrigation): key urb_dir_evap, %

- Indirect Urban Evaporation (% of water consumption): key urb_indir_evap, %

- Sewage Network Loss normal: key sew_net_loss_low, %

- Sewage Network Loss rainy season: key sew_net_loss_high, %

- Threshold of rainy season per time step for sewage loss: key prec_sewage_threshold, mm

- Run-off to Sewage: key runoff_to_sewage, %

- Direct Infiltration (% of water precipitation+irrigation): key dir_infil, %

- Water Consumption NOT from network (Wells,etc.): key wat_supp_wells, mm

- Water Consumption NOT from network loss: key wat_supp_wells_loss, %

- Water from other sources (underground infrustructures,etc.): key wat_other, %

- Urban to calculated Infiltration and Evapotranspiration ratio: key urban_to_ds_inf_etp_ratio, %
---

**Returns**

- ds netCDF dataset

waterpybal netcdf dataset.

---
---
# class urban_infiltration.urban_Composite_CN_correction()

The class to calculate urban composite curve number 

**Methods**

> ds = cia_main(cia_raster,ds,corrected_cn)

> ds = ucia_main(tia_raster,ucia_raster,ds,corrected_cn)

---
---

## urban_infiltration.urban_Composite_CN_correction.cia_main()

ds = cia_main(cia_raster,ds,corrected_cn)

The method to calculate Connected Impervious Area urban composite curve number 

**Parameters**

- ds netCDF dataset

waterpybal netcdf dataset.

---
- cia_raster str

Connected Impervious Area Percentage of the urban zones of the study area

---
- corrected_cn bool default True

If use correctedCN values by AMC as the inputs of composite CN calculation. 
---

**Returns**

- ds netCDF dataset

waterpybal netcdf dataset.

---
---
## urban_infiltration.urban_Composite_CN_correction.ucia_main()

ds = ucia_main(tia_raster,ucia_raster,ds,corrected_cn=True)

The method to calculate Unconnected Impervious Area urban composite curve number 

**Parameters**

- ds netCDF dataset

waterpybal netcdf dataset.

---
- tia_raster str

Total impervious Area Percentage of the urban zones of the study area

---
- ucia_raster str

Unconnected Impervious Area Percentage of the urban zones of the study area

---
- corrected_cn bool default True

If use correctedCN values by AMC as the inputs of composite CN calculation. 

---

**Returns**

- ds netCDF dataset

waterpybal netcdf dataset.

---
---
# class swr_calcs.swr.swr_calc()

The class to calculate Soil Water Reserve

**Methods**

> ds = swr_calc(ds,time_steps,raster_PRU_dir=None,raster_bands_dic_or_val=None)

---
---
## swr_calcs.swr.swr_calc.swr_calc()

ds = swr_calc(ds,time_steps,raster_PRU_dir=None,raster_bands_dic_or_val=None)

The method to calculate Soil Water Reserve

Field capacity = cc

permanent wilting point = pwp

root radial thikness = rrt

**Parameters**

- ds netCDF dataset

waterpybal netcdf dataset.

---
- time_steps None or str or list of ints default "all"

time_steps="all" variable soil properties in time-space. calculate for each step
time_steps=None same soil properties for the whole dataset. variable space.
time_steps=[] list of the dataset time steps to be used to calculate SWR for the 
following time steps.

Example:
time_steps=[ 0 , 20, 123]

SWR for steps 0 to 20 will be calculated using the data from step 0.
SWR for steps 20 to 123 will be calculated using the data from step 20.
SWR for steps 123 to the final step will be calculated using the data from step 123.

---
- raster_PRU_dir None or str default None

Path to the multiband raster that contains "cc", "pwp" & "rrt" values.
Useful when SWR is constant in time and varies in space.
If None, use the data from the waterpybal dataset (spatio-temporal variation).

---
- raster_bands_dic_or_val None or dict default None

Ignored if raster_PRU_dir is None. The dictionary containing the band number of the
multiband raster for "cc", "pwp" & "rrt".

Format: raster_bands_dic_or_val = {"cc":value, "rrt": value , "pwp": value}

---

**Returns**

- ds netCDF dataset

waterpybal netcdf dataset.

---
---
# class balance_calcs.balance()

The class to calculate the water balance

**Methods**

> ds = balance_calculation_main (ds,predef_ru_dir_or_np,predef_ru_type='raster',init_swr=100)

---
---
## balance_calcs.balance.balance_calculation_main ()

ds = balance_calculation_main (ds,predef_ru_dir_or_np,predef_ru_type='raster',init_swr=100)

The method to calculate the water balance from the variables that are calculated using waterpybal.


**Parameters**

- ds netCDF dataset

waterpybal netcdf dataset.

---     
- predef_ru_dir_or_np None numpy array or str default None

Defines the SWR preliminary values.
None if it is iqual to the first step of the dataset.
str if it is a path to a raster.
A 2D numpy array if it is defined using an array.

---
- predef_ru_type str default 'dataset'

Defines the SWR preliminary values type. 
'raster', 'np' or 'dataset'.

---
- init_swr=100   

The percentage of the preliminary SWR values that is saturated.

---

**Returns**

- ds netCDF dataset

waterpybal netcdf dataset.

---
---
# class post_processing.post_process()

The class to create figures, rasters, datasheets and reports from the waterpybal dataset.
In most cases this class could be used to visualize any netcdf dataset.

**Methods**

> point_fig_csv(ds_dir,save_dir,time_dic,lat_val,lon_val,lat_name,lon_name,var_name_list,to_fig_or_csv)

> raster_fig_csv(ds_dir,save_dir,time_dic,var_name,fig_csv_raster)

> gen_report(ds_dir,time_dic,var_name_list,lat_name,lon_name,save_dir,sam_raster_dir,reg_pix_area=None,identifier_raster_array=None,region="Total")
---
---
## post_processing.post_process.point_fig_csv ( )

point_fig_csv(ds_dir,save_dir,time_dic,lat_val,lon_val,var_name_list,to_fig_or_csv,lat_name='lat',lon_name='lon')

To create figures or .csv datasheets in a coordination

**Parameters**

- ds_dir str

The path to the waterpybal netcdf dataset.

---
- save_dir str

The path to save the outputs.

---
- time_dic dict

A dictionary that determines the start and end of the desired period.

Format:

time_dic= {'start': [YYYY,MM,DD,HH], 'end':[YYYY,MM,DD,HH] }

---
- lat_val float

Lat. value

---
- lon_val float

Lon. value

---
- var_name_list str or list of strs

Name of the desired variable or list of the variable names.

---
- to_fig_or_csv str

'Figure', or 'CSV'. To determine the type of the output.

---
- lat_name str default 'lat'

Name of the Lat in the introduced dataset. In waterpybal datasets equal to 'lat'.


---
- lon_name str default 'lon'

Name of the Lon in the introduced dataset. In waterpybal datasets equal to 'lon'.

---
---
## post_processing.post_process.raster_fig_csv ( )

raster_fig_csv(ds_dir,save_dir,time_dic,var_name,fig_csv_raster)

To create rasters, figures or .csv datasheets in time step(s).

**Parameters**

- ds_dir str

The path to the waterpybal netcdf dataset.

---
- save_dir str

The path to save the outputs.

---
- time_dic dict

A dictionary that determines the start and end of the desired period.

Format:

time_dic= {'start': [YYYY,MM,DD,HH], 'end':[YYYY,MM,DD,HH] }

---
- var_name str

Name of the desired variable.

---
- fig_csv_raster str

'Figure', 'Raster' or 'CSV'. To determine the type of the output.

---
---
## post_processing.post_process.gen_report ( )

gen_report(ds_dir,time_dic,var_name_list,lat_name,lon_name,save_dir,sam_raster_dir,reg_pix_area=None,identifier_raster_array=None,region="Total")

To create figures or .csv datasheets in a coordination

**Parameters**

- ds_dir str

The path to the waterpybal netcdf dataset.

---
- save_dir str

The path to save the outputs.

---
- time_dic dict

A dictionary that determines the start and end of the desired period.

Format:

time_dic= {'start': [YYYY,MM,DD,HH], 'end':[YYYY,MM,DD,HH] }

---
- sam_raster_dir

Path to the sample dataset raster.

---
- identifier_raster_array None or numpy 2D array default None

A 2D numpy array that identifies the seperate regions of the study area as numbers. Ignored if 'region' is 'Total'

---
- region str or int default 'Total'

Identifies the desired region (as determined in the identifier_raster_array) to create the report. If
'Total' the report will be created for the whole study area.

---
- var_name_list str or list of strs

Name of the desired variable or list of the variable names.

---
- lat_name str default 'lat'

Name of the Lat in the introduced dataset. In waterpybal datasets equal to 'lat'.

---
- lon_name str default 'lon'

Name of the Lon in the introduced dataset. In waterpybal datasets equal to 'lon'.

---
---