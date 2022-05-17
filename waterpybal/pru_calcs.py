

import numpy as np
import rasterio as rs
class PRU(object):

    @staticmethod
    def PRu_calc(ds,time_steps,raster_PRU_dir=None,raster_bands_dic=None):
        #camp capacity = cc
        #permanent wilting point = pwp
        #root radial thikness = rrt
        #retrieve data for each timestep from ds
        #ru: soil water reserve


        if time_steps=="all": time_steps=[ n for n in range(0,ds["time"].shape[0])]
        #data change in time t
        elif time_steps==None or type(time_steps)!=list: time_steps= [ 0,ds["time"].shape[0] ]
        
        for t in range(0,len(time_steps)-1):

            if raster_PRU_dir==None:
                pwp=ds["pwp"][time_steps[t],:,:].data
                cc=ds["cc"][time_steps[t],:,:].data
                rrt=ds["rrt"][time_steps[t],:,:]
            elif time_steps != "all":
                src=rs.open(raster_PRU_dir)
                pwp=src.read(raster_bands_dic["pwp"])
                cc=src.read(raster_bands_dic["cc"])
                rrt=src.read(raster_bands_dic["rrt"])
                src.close()

            pru_sh=(pwp-cc)*rrt

            #the same xy plane of values have to be added to the ds from t to t+1 step
            if time_steps==None: 
                ds["PRu_Val"]=np.transpose(np.repeat(np.transpose(pru_sh)[:,:,np.newaxis], ds["time"].shape[0],axis=2))
            ts=[n for n in range(time_steps[t],time_steps[t+1])]
            
            for tt in ts:
                ds["PRu_Val"][tt,:,:]=pru_sh

        return ds
#-----------------------------------------