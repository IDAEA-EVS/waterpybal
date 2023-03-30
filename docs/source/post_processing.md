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