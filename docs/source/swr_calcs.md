# class swr_calcs.SWR.swr()

The class to calculate Soil Water Reserve

**Methods**

> ds = swr(ds,time_steps,raster_PRU_dir=None,raster_bands_dic_or_val=None)

---
---
## swr_calcs.swr.SWR.swr()

ds = swr(ds,time_steps,raster_PRU_dir=None,raster_bands_dic_or_val=None)

The method to calculate Soil Water Reserve

field capacity = fc

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

Path to the multiband raster that contains "fc", "pwp" & "rrt" values.
Useful when SWR is constant in time and varies in space.
If None, use the data from the waterpybal dataset (spatio-temporal variation).

---
- raster_bands_dic_or_val None or dict default None

Ignored if raster_PRU_dir is None. The dictionary containing the band number of the
multiband raster for "fc", "pwp" & "rrt".

Format: raster_bands_dic_or_val = {"fc":value, "rrt": value , "pwp": value}

---

**Returns**

- ds netCDF dataset

waterpybal netcdf dataset.

---
---