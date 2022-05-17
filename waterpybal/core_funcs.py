import pandas as pd
from dataset_prep import netCDF_ds
from balance_calcs import balance
from etp_calcs import ETP
from pru_calcs import PRU
from inf_calcs import infiltration
import numpy as np
import netCDF4 as nc


dir=r"C:\Users\Ash kan\Documents\watbalpy\test5212.nc"

#lats_np=np.linspace(-3.0, 3.0, 15)
#lons_np=np.linspace(-4.0, 4.0, 30)
#times_np=data.iloc[0:16].index
lat_lon_type="raster"
lat_lon_source=r'C:\Users\Ash kan\Downloads\s2a_l2a_fishbourne.tif'
time_source=r"C:\Users\Ash kan\Documents\watbalpy\klima_daily_4_steps.csv"
time_type="csv"
time_name="time"
preferred_date_interval="day"
lat,lon,time_v,time_b1,time_b2,preferred_date_interval,tunit=netCDF_ds.ds_dimensions(lat_lon_type,lat_lon_source,time_source,time_type,lat_name=None,lon_name=None,time_name=time_name,border_res_dic=None,time_dic=None,preferred_date_interval=preferred_date_interval)
#------------------------------------------------

#creating the netcdf dataset
ds=netCDF_ds.var_generation(dir=dir,tunit=tunit,lats_np=lat,lons_np=lon,times_np=time_v,time_b1=time_b1,time_b2=time_b2,ds_values_dic={"tmean":"c"})
#------------------------------------------------

var_name="pwp"
folder_dir=r"C:\Users\Ash kan\Documents\watbalpy\tiffs"
ds=netCDF_ds.var_introduction_from_tiffs(ds,folder_dir,var_name,preferred_date_interval)
#------------------------------------------------

#calculating precipitation and other variables that need interpolation
ras_sample_dir=r'C:\Users\Ash kan\Downloads\s2a_l2a_fishbourne.tif'
csv_dir=r"C:\Users\Ash kan\Documents\watbalpy\klima_daily_t2.csv"
time_csv_col="time"
lat_csv_col="lat"
lon_csv_col="lon"
var_name="tmean"
method="invdist"
interpolation_time_int="daily"
ds=netCDF_ds.var_interpolation(ds,ras_sample_dir,csv_dir,time_csv_col,lat_csv_col,lon_csv_col,var_name,method,preferred_date_interval,interpolation_time_int)
#------------------------------------------------

#adding the optional variable for etp calculation to the ds 
oo=np.random.uniform(low=-10,high=10,size=(4,201,301))
ds['tmean'][:,:,:]=oo

#inf=np.random.uniform(low=0,high=100,size=(16,15,30))
#PRu=np.random.uniform(low=0,high=7,size=(16,15,30))
#ds['time'][:]=times_np
v1=np.random.uniform(low=0,high=7,size=(4,201,301))
v2=np.random.uniform(low=0,high=7,size=(4,201,301))
v3=np.random.uniform(low=0,high=7,size=(4,201,301))
ds['pwp'][:,:,:]=v1
ds['cc'][:,:,:]=v2
ds['rrt'][:,:,:]=v3
#ds['INF_Val'][:,:,:]=inf
#ds['PRu_Val'][:,:,:]=PRu
predef_ru=ds["PRu_Val"][0,:,:].data
#------------------------------------------------


#calculating etp
raster_etp_var_dic={"lat":[r'C:\Users\Ash kan\Downloads\s2a_l2a_fishbourne.tif',1]}
ds=ETP.ETP_calc_main(ds,preferred_date_interval=preferred_date_interval, method="oudin",var_name='ETP_Val',raster_etp_var_dic=raster_etp_var_dic,tmean="ds",lat="raster")

#------------------------------------------------
## DEBUGGING - RELOADING DS
#import netCDF4 as nc
#from pru_calcs import PRU
#from inf_calcs import infiltration
#dir=r"C:\Users\Ash kan\Documents\watbalpy\test5212.nc"
#ds=nc.Dataset(dir,'w',format='NETCDF4')
v4=np.random.uniform(low=0,high=200,size=(4,201,301))
ds['ETP_Val'][:,:,:]=v4
###########################
#calculating infiltration
CN_table_dir=r"C:\Users\Ash kan\Documents\watbalpy\cn2.csv"
raster_dir=r'C:\Users\Ash kan\Downloads\s2a_l2a_fishbourne.tif'
HSG_band=1
LU_band=1
ELEV_band=1
DEM_or_raster="raster"
DEM_path_or_raster=raster_dir
filled_dep=True
slope_range_list=None
amc1_coeffs=None
amc3_coeffs=None
dormant_thresh=None
growing_thresh=None
average_thresh=False
mon_list_dormant=None
ds=infiltration.Inf_calc(CN_table_dir,raster_dir,HSG_band,LU_band,ELEV_band,DEM_path_or_raster,DEM_or_raster,filled_dep,slope_range_list,amc1_coeffs,amc3_coeffs,dormant_thresh,growing_thresh,average_thresh,mon_list_dormant,preferred_date_interval)
#------------------------------------------------
#calculating PRU
ds=PRU.PRu_calc(ds,time_steps=None)

#------------------------------------------------
#calculating balance
v5=np.random.uniform(low=50,high=100,size=(4,201,301))
ds["INF_Val"][:,:,:]=v5
ds=balance.balance_calculation_main (ds,predef_ru)

#------------------------------------------------

    