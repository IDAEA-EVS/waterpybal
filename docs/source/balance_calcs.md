# class balance_calcs.Balance()

The class to calculate the water balance

**Methods**

> ds = balance (ds,predef_ru_dir_or_np=None,predef_ru_type='dataset',init_swr=100)

---


## balance_calcs.Balance.balance()

> ds = balance (ds,predef_ru_dir_or_np=None,predef_ru_type='dataset',init_swr=100)

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
