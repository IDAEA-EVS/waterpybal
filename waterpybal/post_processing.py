import numpy as np
import xarray as xr
import netCDF4 as nc
import pandas as pd
import matplotlib.pyplot as plt
import os
from pathlib import Path
import rioxarray as rio
#ds_dir=r'C:\Users\Ash kan\Documents\watbalpy\waterpybal\qgis_test3.nc'
#var_name='prcp'
#time_dic={
#    'start':['2021','01','01','00'],
#    'end':['2021','03','01','00']
#}
#save_dir=r'C:\Users\Ash kan\Documents\watbalpy\waterpybal'
#lat_val=5.623e+06
#lon_val=6.246e+05
class post_process():

    def ds_date_selector(ds_dir,time_dic,var_name):

        ds_disk=xr.open_dataset(ds_dir)
        '''
            #ds_disk.dims
            #ds_disk.coords
            #ds_disk.coords['time'].data
            #start="2001-01-15"
            #end="2001-03-16"
            #var_name="tmean"
            #ds_dir=
            #ds=nc.Dataset(dir,'r',format='NETCDF4')

            #time=np.array(ds_disk['time'])
            #time=time.astype(ds_date_interval)

            #ind_strt=np.where(time == start)
            #ind_end=np.where(time == end)
        '''        
        
        start=np.datetime64( time_dic["start"][0] +'-'+ time_dic["start"][1] +'-'+ time_dic["start"][2] + 'T'+ time_dic["start"][3])
        end=np.datetime64( time_dic["end"][0] +'-'+ time_dic["end"][1] +'-'+ time_dic["end"][2] + 'T'+ time_dic["end"][3])

        selected_var=ds_disk[var_name].sel(time=slice(start,end))

        ds_disk.close()
        
        return selected_var
    
    ##################################    
    def point_fig_csv(ds_dir,save_dir,time_dic,lat_val,lon_val,lat_name,lon_name,var_name,to_fig_or_csv):
        
        selected_var=post_process.ds_date_selector(ds_dir,time_dic,var_name)

        try:
            coords={lat_name:np.array(lat_val),lon_name:np.array(lon_val)}
            s_t=selected_var.sel(coords,method="nearest")
            
            if to_fig_or_csv=="Figure":
                #dir
                fig_dir=os.path.join(save_dir,'lat_'+str(lat_val)+'_lon_'+str(lon_val)+'.png')
                ##############
                fig, ax = plt.subplots()
                s_t.plot(ax=ax)
                fig.savefig(fig_dir)
            else:
                #dir
                excel_dir=os.path.join(save_dir,'lat_'+str(lat_val)+'_lon_'+str(lon_val)+'.csv')
                ##############
                df_d_t=pd.DataFrame(s_t,index=s_t.time,columns=[var_name])
                df_d_t.to_csv(excel_dir)

        except: print ("lat lon not found in point_plot method!!")

    ##################################
    def raster_fig_csv(ds_dir,save_dir,time_dic,var_name,fig_csv_raster):
        

        selected_var=post_process.ds_date_selector(ds_dir,time_dic,var_name)
        #dirs
        if  fig_csv_raster=='Figure':
            fig_path=os.path.join(save_dir,"map_figures_"+var_name)
            Path(fig_path).mkdir(parents=True, exist_ok=True)
        elif  fig_csv_raster=='Raster':
            ras_path=os.path.join(save_dir,"rasters_"+var_name)
            Path(ras_path).mkdir(parents=True, exist_ok=True)
        elif  fig_csv_raster=='CSV':
            csv_path=os.path.join(save_dir,"csv_excels_"+var_name)
            Path(csv_path).mkdir(parents=True, exist_ok=True)

        print ("selected_var",selected_var)
        for i in selected_var:

            date_str=i["time"].dt.strftime('%Y-%m-%d-%H-%M')
            date_str=str(date_str.data)

            if  fig_csv_raster=='Figure':

                fig, ax = plt.subplots()
                i.plot(ax=ax)
                fig.savefig( os.path.join(fig_path,date_str+'.png') )

            elif  fig_csv_raster=='Raster':
                if len(i["lon"].shape)==1 and len(i["lat"].shape)==1:
                    
                    i=i.rename({"lon":"x","lat":'y'})
                else:
                    pass
                    
                i.rio.to_raster(os.path.join(ras_path,date_str+'.tif'))

            elif  fig_csv_raster=='CSV':    

                i.to_dataframe(name=None, dim_order=None)
                i=i.to_pandas()
                i.to_csv(os.path.join(csv_path,date_str+'.csv'))



