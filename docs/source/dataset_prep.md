# class dataset_prep.dataset_gen()
The class to create the waterpybal netCDF dataset dimensions and variables

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

Potential Evapotranspiration: **PET_Val**, *mm*


&nbsp;

**Soil properties-related variables**

Soil water reserve: **PRu_Val**, *mm*

Permanent Wilting Point: **pwp**, *no_unit*

Field Capacity: **fc**, *no_unit*

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

> ds_dimensions(self,lat_lon_type,lat_lon_source,time_source,time_type,preferred_date_interval,lat_name="lat",lon_name="lon",time_name="time",border_res_dic=None,time_dic=None,single_point=False)

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

ds_dimensions(self,lat_lon_type,lat_lon_source,time_source,time_type,preferred_date_interval,lat_name="lat",lon_name="lon",time_name="time",border_res_dic=None,time_dic=None,single_point=False)

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
- single_point boolean default: False

    If the balance has to be calculated in a single point instead of a raster area


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

To add additional variables to the waterpybal dataset. The additional variables can be used in following stages such as PET calculation, etc.
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

> ds = var_interpolation(ds,ras_sample_dir,csv_dir,var_name,method,interpolation_time_int,time_csv_col="time",lat_csv_col="lat",lon_csv_col="lon",multiply=False)

> ds = var_introduction_from_tiffs(ds,folder_dir,var_name,multiply=False)

> ds = var_introduction_from_csv(ds,csv_dir,var_name,interpolation_time_int,time_csv_col="time",multiply=False)

> ds = var_introduction_from_nc(new_nc_dir,ds,var_name)

---
---

## dataset_prep.variable_management.var_interpolation()

ds = var_interpolation( ds, ras_sample_dir, csv_dir, time_csv_col, lat_csv_col, lon_csv_col, var_name, method, interpolation_time_int, multiply)

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

ds = var_introduction_from_tiffs(ds,folder_dir,var_name,multiply)

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

ds = var_introduction_from_csv(ds,csv_dir,var_name,interpolation_time_int,time_csv_col="time",multiply=False)

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