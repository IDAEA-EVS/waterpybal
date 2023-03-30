# class pet_calcs.PET()
The class to calculate evapotranspiration
**Methods**

> ds = pet(ds,method,raster_PET_var_dic=None,var_name='PET',**kwargs)


---
---

## pet_calcs.PET.pet()


ds = pet(ds,method,raster_PET_var_dic=None,var_name='PET',**kwargs)

pet method calculate evapotranspiration in all the dataset. It uses ***pyet*** library for
PET calculations which is opted for use in a single point.

Depending on the PET method, necessary arguments have to be introduced to the database. If the argument is a 
fix number for all times and coordinates, it could be determined right away. If the PET
related argument is equal to 'ds', the argument will be derived from the variable with the same name
in the dataset. Note that user have to introduce this variables to the dataset beforehead. If the
argument value changes with the coordinate but not with the time, the pet argument have to be equal
to 'raster'. the direction and the band of the targed master have to be determined in raster_pet_var_dic
argument using the following syntax:

{"var_name":["raster_dir","raster_band"]} or {"var_name":"raster_dir"} (band default to 1) or {"var_name":["raster_dir"]} (band default to 1)


Let's elaborate using this function with an example:

Suppose we are using penman method for calculating PET. "tmean" and "wind" are mandatory arguments for this method.
Since in this example "tmean" and "wind" are changing in each coordinate, the user have to use "ds"
to determine the this data have to be retrieved from dataset variables by the same name. Then there are "aw" and "bw" which
have a fixed value by default ("aw"=2.6, "bw"=0.536), but could be changed based on the coordinates.
so by defining "aw"="raster" and "bw"="raster and raster_pet_var_dic={"aw":["ras_dir",band1],"bw":["ras_dir",band2]},
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
- raster_pet_var_dic dic default: None
If the PET variable doesn't change in time, it is possible to use a raster to introduce it's values.

Format:

{"var_name":["raster_dir","raster_band"]} or {"var_name":"raster_dir"} (band default to 1) or {"var_name":["raster_dir"]}

---
- **kwargs dic

A dictionary that defines the inputs of the PET method.

The constant values can be defined directly

Rasters have to be defined with "raster" keyword, and then introduced in raster_pet_var_dic argument as a dictionary

If the PET variable exists in the waterpybal dataset, the "ds" keyword have to be used. 

Format:
{"var_name_1":constant_value, "var_name_2": "raster", "var_name_3": "ds",... }

---

**Returns**

- ds netCDF dataset

waterpybal netcdf dataset.

---
---