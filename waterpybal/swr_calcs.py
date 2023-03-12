

import numpy as np
import rasterio as rs

class SWR():
    '''
    # class swr_calcs.swr.swr_calc()

    The class to calculate Soil Water Reserve

    **Methods**

        > ds = swr_calc(ds,time_steps,raster_SWR_dir=None,raster_bands_dic_or_val=None)
                
        ---
        ---

    '''

    @staticmethod
    def swr(ds,time_steps="all",raster_SWR_dir=None,raster_bands_dic_or_val=None):
        '''
            ## swr_calcs.swr.swr_calc.swr_calc()
            
            ds = swr_calc(ds,time_steps,raster_SWR_dir=None,raster_bands_dic_or_val=None)
            
                The method to calculate Soil Water Reserve
                
                camp capacity = cc
                
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
                - raster_SWR_dir None or str default None

                        Path to the multiband raster that contains "cc", "pwp" & "rrt" values.
                        Useful when SWR is constant in time and varies in space.
                        If None, use the data from the waterpybal dataset (spatio-temporal variation).
                
                ---
                - raster_bands_dic_or_val None or dict default None

                    Ignored if raster_SWR_dir is None. The dictionary containing the band number of the
                    multiband raster for "cc", "pwp" & "rrt".

                    Format: raster_bands_dic_or_val = {"cc":value, "rrt": value , "pwp": value}
                
                ---

            **Returns**

                -ds netCDF dataset

                    waterpybal netcdf dataset.
            
            ---
            ---

        '''
        #camp capacity = cc
        #permanent wilting point = pwp
        #root radial thikness = rrt
        #retrieve data for each timestep from ds
        #ASWR: soil water reserve


        if time_steps=="all": time_steps=[ n for n in range(0,ds["time"].shape[0])]

        elif time_steps==None or type(time_steps)!=list: time_steps= [ 0,ds["time"].shape[0] ]
        
        for t in range(0,len(time_steps)-1):

            if raster_SWR_dir==None:

                pwp=ds["pwp"][time_steps[t],:,:].data
                #pwp[pwp==-9999]=np.nan
                cc=ds["cc"][time_steps[t],:,:].data
                #cc[cc==-9999]=np.nan
                rrt=ds["rrt"][time_steps[t],:,:].data
                #rrt[rrt==-9999]=np.nan

            elif raster_SWR_dir!=None:
                
                src=rs.open(raster_SWR_dir)
                pwp=src.read(raster_bands_dic_or_val["pwp"])
                cc=src.read(raster_bands_dic_or_val["cc"])
                rrt=src.read(raster_bands_dic_or_val["rrt"])
                msk = src.read_masks(raster_bands_dic_or_val["pwp"])
                src.close()

            SWR_sh=(cc-pwp)*rrt*1000 #1000 to convert it to mm
            
            SWR_sh=np.nan_to_num(SWR_sh,nan=-9999)
            
            if raster_SWR_dir!=None: SWR_sh[msk==0]=np.nan  
            else: 
                SWR_sh[pwp==-9999]=np.nan  
                SWR_sh[cc==-9999]=np.nan  
                SWR_sh[rrt==-9999]=np.nan  


            #the same xy plane of values have to be added to the ds from t to t+1 step
            if time_steps==None: 
                ds["SWR"]=np.transpose(np.repeat(np.transpose(SWR_sh)[:,:,np.newaxis], ds["time"].shape[0],axis=2))
            
            else:
                ts=[n for n in range(time_steps[t],time_steps[t+1])]
            
                for tt in ts:
                    ds["SWR"][tt,:,:]=SWR_sh

        return ds
#-----------------------------------------
