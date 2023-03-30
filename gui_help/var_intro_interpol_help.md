# ***Variable introduction and spatial interpolation***

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

Potential Evapotranspiration: **PET_Val**, *mm*


&nbsp;

### **Soil properties-related variables**

Soil water reserve: **PRu_Val**, *mm*

Permanent Wilting Point: **pwp**, *no_unit*

Field Capacity: **fc**, *no_unit* (Volumetric Content)

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

Water from other sources (underground infrustructures,etc.): **wat_other**, *mm*

Urban to calculated Infiltration and Evapotranspiration ratio: **urban_to_ds_inf_pet_ratio**, *%*

