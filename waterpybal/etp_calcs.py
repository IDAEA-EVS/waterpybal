import numpy as np
import pandas as pd
import pyet
import rasterio as rs

#ETP calculation from soil parameters
#Example ETP_calcs.ETP_calc_main(ds,method="oudin",tmean='ds', lat=0.91) 

class ETP(object):

    def __init__(self):
        #"obl" defines the obligatory input arguments of each function
        self.methods_dic={
            "kimberly_penman":{"tmean":"obl", "wind":"obl", "rs":None, "rn":None, "g":0, "tmax":None, "tmin":None, "rhmax":None, "rhmin":None, "rh":None, "pressure":None, "elevation":None, "lat":None, "n":None, "nn":None, "rso":None, "a":1.35, "b":-0.35},
            "penman":{"tmean":"obl", "wind":"obl", "rs":None, "rn":None, "g":0, "tmax":None, "tmin":None, "rhmax":None, "rhmin":None, "rh":None, "pressure":None, "elevation":None, "lat":None, "n":None, "nn":None, "rso":None, "aw":2.6, "bw":0.536, "a":1.35,"b":-0.35},
            "pm_fao56":{"tmean":"obl", "wind":"obl", "rs":None, "rn":None, "g":0, "tmax":None, "tmin":None, "rhmax":None, "rhmin":None, "rh":None, "pressure":None, "elevation":None, "lat":None, "n":None, "nn":None, "rso":None, "a":1.35, "b":-0.35},
            "priestley_taylor":{"tmean":"obl", "wind":"obl", "rs":None, "rn":None, "g":0, "tmax":None, "tmin":None, "rhmax":None, "rhmin":None, "rh":None, "pressure":None, "elevation":None, "lat":None, "n":None, "nn":None, "rso":None, "a":1.35, "b":-0.35, "alpha":1.26},
            "pm":{"tmean":"obl", "wind":"obl", "rs":None, "rn":None, "g":0, "tmax":None, "tmin":None, "rhmax":None, "rhmin":None, "rh":None, "pressure":None, "elevation":None, "lat":None, "n":None, "nn":None, "rso":None, "a":1.35, "b":-0.35, "lai":None, "croph":None, "r_l":100, "r_s":70, "ra_method":1, "a_sh":1, "a_s":1, "lai_eff":1, "srs":0.0009, "co2":300},
            "thom_oliver":{"tmean":"obl", "wind":"obl", "rs":None, "rn":None, "g":0, "tmax":None, "tmin":None, "rhmax":None, "rhmin":None, "rh":None, "pressure":None, "elevation":None, "lat":None, "n":None, "nn":None, "rso":None, "aw":2.6, "bw":0.536, "a":1.35, "b":-0.35, "lai":None, "croph":None, "r_l":100, "r_s":70, "ra_method":1, "lai_eff":1, "srs":0.0009, "co2":300},
            "blaney_criddle":{"tmean":"obl", "p":"obl", "k":0.85},
            "hamon":{"tmean":"obl", "lat":"obl"},
            "linacre":{"tmean":"obl", "elevation":"obl", "lat":"obl", "tdew":None, "tmax":None, "tmin":None},
            "romanenko":{"tmean":"obl", "rh":"obl", "k":4.5},
            "abtew":{"tmean":"obl", "rs":"obl", "k":0.53},
            "fao_24":{"tmean":"obl", "wind":"obl", "rs":"obl", "rh":"obl", "pressure":None, "elevation":None, "albedo":0.23},
            "hargreaves":{"tmean":"obl", "tmax":"obl", "tmin":"obl", "lat":"obl"},
            "jensen_haise":{"tmean":"obl", "rs":None, "cr":0.025, "tx":-3, "lat":None, "method":1},
            "makkink":{"tmean":"obl", "rs":"obl", "pressure":None, "elevation":None},
            "mcguinness_bordne":{"tmean":"obl", "lat":"obl", "k":0.0147},
            "oudin":{"tmean":"obl", "lat":"obl", "k1":100, "k2":5},
            "turc":{"tmean":"obl", "rs":"obl", "rh":"obl", "k":0.31}
        }

        self.pyet_func_dic={
            "kimberly_penman":pyet.kimberly_penman,
            "penman":pyet.penman,
            "pm_fao56":pyet.pm_fao56,
            "priestley_taylor":pyet.priestley_taylor,
            "pm":pyet.pm,
            "thom_oliver":pyet.thom_oliver,
            "blaney_criddle":pyet.blaney_criddle,
            "hamon":pyet.hamon,
            "linacre":pyet.linacre,
            "romanenko":pyet.romanenko,
            "abtew":pyet.abtew,
            "fao_24":pyet.fao_24,
            "hargreaves":pyet.hargreaves,
            "jensen_haise":pyet.jensen_haise,
            "makkink":pyet.makkink,
            "mcguinness_bordne":pyet.mcguinness_bordne,
            "oudin":pyet.oudin,
            "turc":pyet.turc,
        }
        

        self.exec_etp_inps=dict()
        self.results_df=pd.DataFrame()

    def add_ETP_method_point(self,method,**kwargs):

        if method in self.methods_dic:

            kwargs_=dict()

            #add the args introduced by the user
            for k,v in kwargs.items():
                if k in self.methods_dic[method]: 
                    kwargs_[k]=v
                else: print ( f"argument {k} not found in the list of the ETP method argument and ignored." )
            #add default values:
            for key_arg,val_arg in self.methods_dic[method].items(): 
                if key_arg not in kwargs_: kwargs_[key_arg]=val_arg

        self.exec_etp_inps[method]=kwargs_

    def exec_ETPs_point(self):
        #print ("self.exec_etp_inps",self.exec_etp_inps)
        for meth_name,meth_kwargs in self.exec_etp_inps.items():

            temp_meth_kwargs_list=[]
            for n in meth_kwargs.values():
                if type(n)==str: temp_meth_kwargs_list.append(n)

            if "obl" not in temp_meth_kwargs_list:
                #print ("meth_kwargs",meth_kwargs)
                #print ("meth_name",meth_name)
                etp_res=self.pyet_func_dic[meth_name](**meth_kwargs)
                self.results_df[meth_name]=etp_res
            else: raise Exception ("The non-optional input arguments of {meth_name} ETP method is not defined!" )
        return self.results_df
    #########
    @staticmethod
    def ETP_calc_main(ds,method,preferred_date_interval,var_name='ETP_Val',raster_etp_var_dic=None,**kwargs):
        '''
            ETP_calc_main function calculate evapotranspiration in all the dataset. It used "pyet" library for
            ETP calculations which is opted for use in a single point. So we iterate along the coordinates. In
            each iteration, ETP for all time steps will be calculated, then we move along to the next point.
            Depending on the ETP method, necessary arguments have to be introduced to the database. If the argument is a 
            fix number for all times and coordinates, it could be determined right away. If the ETP
            related argument is equal to 'ds', the argument will be derived from the variable with the same name
            in the dataset. Note that user have to introduce this variables to the dataset beforehead. If the
            argument value changes with the coordinate but not with the time, it, the etp argument have to be equal
            to 'raster'. the direction and the band of the targed master have to be determined in raster_etp_var_dic
            argument using the following syntax:
            {"var_name":["raster_dir","raster_band"]} or {"var_name":"raster_dir"} (band default to 1) or {"var_name":["raster_dir"]} (band default to 1)
            
        
            Let's elaborate using this function with an example:
            Suppose we are using penman method for calculating ETP. "tmean" and "wind" are mandatory arguments for this method.
            Since in this example "tmean" and "wind" are changing in each coordinate, the user have to use "ds"
            to determine the this data have to be retrieved from dataset variables by the same name. Then there are "aw" and "bw" which
            have a fixed value by default ("aw"=2.6, "bw"=0.536), but could be changed based on the coordinates.
            so by defining "aw"="raster" and "bw"="raster and raster_etp_var_dic={"aw":["ras_dir",band1],"bw":["ras_dir",band2]},
            aw and bw arguments are equal to raster values of band 1 and 2 respectively. 
        '''
        #retrieve data for each timestep from ds
        #data change in time t
        time_step_st= 0
        time_step_fin=ds["time"].shape[0]

        lats=[ n for n in range(0,ds["lat"].shape[0])]
        lons=[ n for n in range(0,ds["lon"].shape[0])]
        times=ds["time"][:].data

        if raster_etp_var_dic==None: raster_etp_var_dic={} #{"var_name":["raster_dir",raster_band]} or {"var_name":"raster_dir"} (band default to 1) or {"var_name":["raster_dir"]} (band default to 1)

        if preferred_date_interval=='datetime64[h]': d_i_t='datetime64[m]'
        elif preferred_date_interval=='datetime64[D]':d_i_t='datetime64[h]'
        elif preferred_date_interval=='datetime64[M]':d_i_t='datetime64[D]'

        time_ind=times[time_step_st:time_step_fin].astype(d_i_t)
        #print ("time_ind",time_ind)
        
        for lat_t in lats:
            for lon_t in lons:  
                kwargs_={}
                nodata_etp=False
                for k in kwargs:
                    if type(kwargs[k])==str and kwargs[k]=='ds':
                        
                        
                        v=ds[k][time_step_st:time_step_fin,lat_t,lon_t].data
                        if np.all(v==-9999):
                            nodata_etp=True
                        
                        else:
                            t_v=pd.DataFrame(v,columns=[k],index=time_ind)
                            kwargs_[k]=t_v[k]

                    elif type(kwargs[k])==str and kwargs[k]=='raster':
                        if type(raster_etp_var_dic[k])==str:
                            rast_dir=raster_etp_var_dic[k]
                            rast_band=1 
                        else:
                            rast_dir=raster_etp_var_dic[k][0]
                            try:
                                rast_band=raster_etp_var_dic[k][1]
                            except:  
                                rast_band=1  
                        dataset = rs.open(rast_dir)
                        band = dataset.read(rast_band)
                        msk = dataset.read_masks(rast_band)
                        if msk[lat_t,lon_t]==0: nodata_etp=True
                        else:kwargs_[k]=band[lat_t,lon_t]

                    else: kwargs_[k]=kwargs[k]    

                if nodata_etp==False:
                    etp_t=ETP()
                    etp_t.add_ETP_method_point(method,**kwargs_)
                    etp_t=etp_t.exec_ETPs_point()
                    #define ETPs (calculated for each point for all time steps)
                    ds[var_name][time_step_st:time_step_fin,lat_t,lon_t]=etp_t #output from etp function
                else: ds[var_name][time_step_st:time_step_fin,lat_t,lon_t]=np.full(ds[var_name][time_step_st:time_step_fin,lat_t,lon_t].shape,-9999)
        
        return ds