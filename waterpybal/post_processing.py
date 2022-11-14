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

class tools():
    '''
    Methods for the post_process class
    '''
    ##################################
    @staticmethod
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
    @staticmethod
    def reg_area_calc(region,identifier_raster_bool,reg_pix_area,df_d_t):
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
    
    ##################################
    @staticmethod
    def whole_area_calc(sam_raster_dir,df):
        #calculate the whole area
        if sam_raster_dir not in [None," ",""]:
            arr,pix_area,msk=tools.read_raster(sam_raster_dir)
            whole_trues_cnts=np.count_nonzero(msk)
            whole_area=pix_area*whole_trues_cnts
        else: whole_area=None

        #whole area
        np_wh_ar=np.full(len(df.index), whole_area)
        df_wh_ar=pd.DataFrame(np_wh_ar,index=df.index,columns=["TOTAL_AREA"])
        df=pd.concat([df, df_wh_ar],axis=1,ignore_index=False)
        return df
    
    ##################################
    @staticmethod
    def read_raster(rast_dir):
        arr=rs.open(rast_dir)
        pixelSizeX,pixelSizeY= arr.res

        return arr.read(1),pixelSizeX*pixelSizeY,arr.read_masks(1)
    
    ##################################
    @staticmethod
    def regions_list(rast_dir):
        arr=tools.read_raster(rast_dir)
        r_list=[str(int(n)) for n in list(np.unique(arr[0]))]
        r_list.remove("-9999")
        return ["All"]+r_list
    

class post_process():
    '''
    # class post_processing.post_process()

    The class to create figures, rasters, datasheets and reports from the waterpybal dataset.
    In most cases this class could be used to visualize any netcdf dataset.

    **Methods**

        > point_fig_csv(ds_dir,save_dir,time_dic,lat_val,lon_val,lat_name,lon_name,var_name_list,to_fig_or_csv)

        > raster_fig_csv(ds_dir,save_dir,time_dic,var_name,fig_csv_raster)

        > gen_report(ds_dir,time_dic,var_name_list,lat_name,lon_name,save_dir,sam_raster_dir,reg_pix_area=None,identifier_raster_array=None,region="Total")
    ---
    ---
    '''
    
    ##################################
    def point_fig_csv(ds_dir,save_dir,time_dic,lat_val,lon_val,var_name_list,to_fig_or_csv,lat_name='lat',lon_name='lon'):
        '''
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
        '''
        
        
        
        if type(var_name_list)==str: var_name_list=[var_name_list]

        var_name_list_len=len(var_name_list)
        
        selected_vars=tools.ds_date_selector(ds_dir,time_dic,var_name_list)

        
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
            if to_fig_or_csv!="Figure":
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
        '''
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

        '''

        selected_var=tools.ds_date_selector(ds_dir,time_dic,var_name)
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
    
    ##################################
    def gen_report(ds_dir,time_dic,var_name_list,save_dir,sam_raster_dir,lat_name='lat',lon_name='lon',identifier_raster_array=None,region="Total"): #region: "Total", "1"
        
        '''
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
        '''

        selected_vars=tools.ds_date_selector(ds_dir,time_dic,var_name_list)
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
        reg_pix_area=None
        try: d,reg_pix_area,mks= tools.read_raster(sam_raster_dir)
        except: pass

        for selected_var in selected_vars:
            
            
            
            s_t=selected_var.sum(dim=[lat_name,lon_name])
            
            #total values of each time step
            csv_total="TOTAL_"+selected_var.name
            df_d_t=pd.DataFrame(s_t,index=s_t.time,columns=[csv_total])
            
            if region!="Total":
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
                    
                    df_d_t=tools.reg_area_calc(reg,identifier_raster_bool,reg_pix_area,df_d_t)
            
            if df is None:
                df=df_d_t
            else:
                df=pd.concat([df, df_d_t],axis=1,ignore_index=False)
        
        
        #csv save
        df=tools.whole_area_calc(sam_raster_dir,df)
        df.to_csv(excel_dir)



