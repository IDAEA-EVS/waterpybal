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