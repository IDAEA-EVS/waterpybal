import re
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
from pathlib import Path
import rioxarray as rio
import xarray as xr
import netCDF4 as nc
import rasterio as rs
#ds_dir=r'C:\Users\Ash kan\Documents\watbalpy\waterpybal\qgis_test3.nc'
#var_name='prcp'
#time_dic={
#    'start':['2021','01','01','00'],
#    'end':['2021','03','01','00']
#}
#save_dir=r'C:\Users\Ash kan\Documents\watbalpy\waterpybal'
#lat_val=5.623e+06
#lon_val=6.246e+05
#var_name_list=["Prec_Val","Rec_Val","Def_Val"]
class post_process():

    def ds_date_selector(ds_dir,time_dic,var_name_list):

        if type(var_name_list)==str: var_name_list=[var_name_list] #for map and rasters

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

        selected_vars=list()
        for selected_var in var_name_list:
            selected_vars.append(ds_disk[selected_var].sel(time=slice(start,end)))

        ds_disk.close()
        
        return selected_vars
    
    ##################################    
    def point_fig_csv(ds_dir,save_dir,time_dic,lat_val,lon_val,lat_name,lon_name,var_name_list,to_fig_or_csv):
        if type(var_name_list)==str: var_name_list=[var_name_list]

        var_name_list_len=len(var_name_list)
        
        selected_vars=post_process.ds_date_selector(ds_dir,time_dic,var_name_list)

        
        for cnt,selected_var in enumerate(selected_vars):

            #try:
            coords={lat_name:np.array(float(lat_val)),lon_name:np.array(float(lon_val))}
            print (coords)
            s_t=selected_var.sel(coords,method="nearest")
            #except:
                #print("lat lon not found in point_plot method!!")
            
            
            if to_fig_or_csv=="Figure":
                #dir
                fig_dir=os.path.join(save_dir,str(s_t.name)+'_lat_'+str(lat_val)+'_lon_'+str(lon_val)+'.png')
                ##############
                fig, ax = plt.subplots()
                s_t.plot(ax=ax)
                fig.savefig(fig_dir)
            else:
                
                #dir
                excel_dir=os.path.join(save_dir,str(s_t.name)+'_lat_'+str(lat_val)+'_lon_'+str(lon_val)+'.csv')
                print (s_t.name)
                print (s_t)
                df_d_t=pd.DataFrame(s_t,index=s_t.time,columns=[s_t.name])


                ##############

            if cnt==0: 
                df_d_t_f=df_d_t   
            else: 
                df_d_t_f=pd.concat([df_d_t_f, df_d_t],axis=1,ignore_index=False)
        
        if to_fig_or_csv!="Figure":
                            
            if var_name_list_len==1: df_d_t_f.to_csv(excel_dir)
            else: 
                excel_dir=os.path.join(save_dir,'All_variables_lat_'+str(lat_val)+'_lon_'+str(lon_val)+'.csv')
                df_d_t_f.to_csv(excel_dir)
    ##################################
    def raster_fig_csv(ds_dir,save_dir,time_dic,var_name,fig_csv_raster):
        

        selected_var=post_process.ds_date_selector(ds_dir,time_dic,var_name)
        selected_var=selected_var[0]
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
        for i in selected_var: #i is each time step

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

    def gen_report(ds_dir,time_dic,var_name_list,lat_name,lon_name,save_dir,sam_raster_dir,reg_pix_area=None,identifier_raster_array=None,region="Total"): #region: "Total", "1"

        selected_vars=post_process.ds_date_selector(ds_dir,time_dic,var_name_list)
        identifier_raster_bool=None

        ##########

        if region!="Total":
            if type(region)!=list: #just one region
                
                excel_dir=os.path.join(save_dir,'region_'+str(region)+'_and_Total_report.csv')
            else: excel_dir=os.path.join(save_dir,'all_regions_and_Total_report.csv')

        else:
            excel_dir=os.path.join(save_dir,'Whole_area_report.csv')

        ################
        df=None
        for selected_var in selected_vars:
            
            
            
            s_t=selected_var.sum(dim=[lat_name,lon_name])
            
            #total values of each time step
            csv_total="TOTAL_"+selected_var.name
            df_d_t=pd.DataFrame(s_t,index=s_t.time,columns=[csv_total])
            
            if region!="Total":
                print (region)
                if type(region)!=list: region=list(region) #if just one region
                
                for reg in region:

                    ##Create 2D mask of the region
                    identifier_raster_bool=np.ones(identifier_raster_array.shape, dtype=bool) #all true
                    identifier_raster_bool[identifier_raster_array!=int(reg)]=False
                    identifier_raster_bool=np.repeat(identifier_raster_bool[np.newaxis,:, : ], selected_vars[0].shape[0], axis=0)


                    csv_reg="REG_"+str(reg)+"_"+selected_var.name
                    mskd_selected_var=xr.where(identifier_raster_bool,selected_var,np.nan)
                    mskd_selected_var=mskd_selected_var.sum(dim=[lat_name,lon_name])
                
                    df_d_t_f=pd.DataFrame(mskd_selected_var,index=s_t.time,columns=[csv_reg])
                    df_d_t=pd.concat([df_d_t, df_d_t_f],axis=1,ignore_index=False)
                    
                    df_d_t=post_process.reg_area_calc(sam_raster_dir,reg,identifier_raster_bool,reg_pix_area,df_d_t)
            
            if df is None:
                df=df_d_t
            else:
                df=pd.concat([df, df_d_t],axis=1,ignore_index=False)
        
        
        #csv save
        df=post_process.whole_area_calc(sam_raster_dir,df)
        df.to_csv(excel_dir)

    #########################################################
    def read_raster(rast_dir):
        arr=rs.open(rast_dir)
        pixelSizeX,pixelSizeY= arr.res

        return arr.read(1),pixelSizeX*pixelSizeY,arr.read_masks(1)

    def regions_list(rast_dir):
        arr=post_process.read_raster(rast_dir)
        r_list=[str(int(n)) for n in list(np.unique(arr[0]))]
        r_list.remove("-9999")
        return ["All"]+r_list
    
    
    def reg_area_calc(sam_raster_dir,region,identifier_raster_bool,reg_pix_area,df_d_t):
        region_area=None

        #for each region

        #calculate the region area
        trues_cnts=np.count_nonzero(identifier_raster_bool[0,:, : ])
        region_area=reg_pix_area*trues_cnts

        #############
        #Add areas to df
        np_rg_ar=np.full(len(df_d_t.index), region_area)
        df_rg_ar=pd.DataFrame(np_rg_ar,index=df_d_t.index,columns=["REG_"+str(region)+"_AREA"])
        df_d_t=pd.concat([df_d_t, df_rg_ar],axis=1,ignore_index=False)
        ########
        return df_d_t
    
    def whole_area_calc(sam_raster_dir,df):
        #calculate the whole area
        if sam_raster_dir not in [None," ",""]:
            arr,pix_area,msk=post_process.read_raster(sam_raster_dir)
            whole_trues_cnts=np.count_nonzero(msk)
            whole_area=pix_area*whole_trues_cnts
        else: whole_area=None

        #whole area
        np_wh_ar=np.full(len(df.index), whole_area)
        df_wh_ar=pd.DataFrame(np_wh_ar,index=df.index,columns=["TOTAL_AREA"])
        df=pd.concat([df, df_wh_ar],axis=1,ignore_index=False)
        return df


