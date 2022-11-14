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