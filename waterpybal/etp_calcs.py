import numpy as np
import pandas as pd
import pyet
import rasterio as rs

#ETP calculation from soil parameters
#Example ETP_calcs.ETP_calc_main(ds,method="oudin",tmean='ds', lat=0.91) 

class ETP_tools(object):
    """
    Methods to be used in ETP class, ETP_calc_main
    """
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
        #print ("inside add_ETP_method_point")
        if method in self.methods_dic:

            kwargs_=dict()

            #add the args introduced by the user
            for k,v in kwargs.items():
                if k in self.methods_dic[method]: 
                    
                    if k=="lat": 
                        #print ("v before",v)
                        v=v * np.pi / 180
                        #print ("k",k)
                        #print ("lats changed")
                        #print ("v after",v)

                    kwargs_[k]=v
                else: print ( f"argument {k} not found in the list of the ETP method argument and ignored." )
            #add default values:
            for key_arg,val_arg in self.methods_dic[method].items(): 
                if key_arg not in kwargs_: kwargs_[key_arg]=val_arg

        self.exec_etp_inps[method]=kwargs_

    def exec_ETPs_point(self):
        #print ("inside exec_ETPs_point")

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
class ETP(ETP_tools):
    '''
    # class etp_calcs.ETP()
    The class to calculate evapotranspiration
    **Methods**
        
        > ds = ETP_calc(ds, method, preferred_date_interval, var_name='ETP_Val', raster_etp_var_dic=None, **kwargs)
    ---
    ---
    '''
    def __init__(self):
        super().__init__()


    @staticmethod
    def ETP_calc_temp_out(ds,method,preferred_date_interval,raster_etp_var_dic=None,var_name='ETP_Val',**kwargs):
        '''
            ## etp_calcs.ETP.ETP_calc()
            
            ds = ETP_calc(ds, method, preferred_date_interval, var_name='ETP_Val', raster_etp_var_dic=None, **kwargs)
            
            ETP_calc method calculate evapotranspiration in all the dataset. It uses ***pyet*** library for
            ETP calculations which is opted for use in a single point.

            Depending on the ETP method, necessary arguments have to be introduced to the database. If the argument is a 
            fix number for all times and coordinates, it could be determined right away. If the ETP
            related argument is equal to 'ds', the argument will be derived from the variable with the same name
            in the dataset. Note that user have to introduce this variables to the dataset beforehead. If the
            argument value changes with the coordinate but not with the time, the etp argument have to be equal
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


            **Parameters**

                - ds netCDF dataset

                    waterpybal netcdf dataset.

                ---
                - method
                    
                    - Combination evapotranspiration calculation methods:


                        - ***Kimberly Penman:***

                            tmean: **Mandatory**, wind: **Mandatory**, rs: Optional, rn: Optional, g: 0, tmax: Optional, tmin: Optional, rhmax: Optional, rhmin: Optional, rh: Optional, pressure: Optional, elevation: Optional, lat: Optional, n: Optional, nn: Optional, rso: Optional, a: 1.35, b: -0.35

                        - ***Penman:***
                            
                            tmean: **Mandatory**, wind: **Mandatory**, rs: Optional, rn: Optional, g: 0, tmax: Optional, tmin: Optional, rhmax: Optional, rhmin: Optional, rh: Optional, pressure: Optional, elevation: Optional, lat: Optional, n: Optional, nn: Optional, rso: Optional, aw: 2.6, bw: 0.536, a: 1.35,b: -0.35

                        - ***FAO-56 Penman-Monteith:***

                            tmean: **Mandatory**, wind: **Mandatory**, rs: Optional, rn: Optional, g: 0, tmax: Optional, tmin: Optional, rhmax: Optional, rhmin: Optional, rh: Optional, pressure: Optional, elevation: Optional, lat: Optional, n: Optional, nn: Optional, rso: Optional, a: 1.35, b: -0.35

                        - ***Priestley and taylor:***

                            tmean: **Mandatory**, wind: **Mandatory**, rs: Optional, rn: Optional, g: 0, tmax: Optional, tmin: Optional, rhmax: Optional, rhmin: Optional, rh: Optional, pressure: Optional, elevation: Optional, lat: Optional, n: Optional, nn: Optional, rso: Optional, a: 1.35, b: -0.35, alpha: 1.26

                        - ***Penman-Monteith:***

                            tmean: **Mandatory**, wind: **Mandatory**, rs: Optional, rn: Optional, g: 0, tmax: Optional, tmin: Optional, rhmax: Optional, rhmin: Optional, rh: Optional, pressure: Optional, elevation: Optional, lat: Optional, n: Optional, nn: Optional, rso: Optional, a: 1.35, b: -0.35, lai: Optional, croph: Optional, r_l: 100, r_s: 70, ra_method: 1, a_sh: 1, a_s: 1, lai_eff: 1, srs: 0.0009, co2: 300

                        - ***Thom and Oliver:***

                            tmean: **Mandatory**, wind: **Mandatory**, rs: Optional, rn: Optional, g: 0, tmax: Optional, tmin: Optional, rhmax: Optional, rhmin: Optional, rh: Optional, pressure: Optional, elevation: Optional, lat: Optional, n: Optional, nn: Optional, rso: Optional, aw: 2.6, bw: 0.536, a: 1.35, b: -0.35, lai: Optional, croph: Optional, r_l: 100, r_s: 70, ra_method: 1, lai_eff: 1, srs: 0.0009, co2: 300


                    - Temperature evapotranspiration calculation methods:


                        - ***Blaney_criddle:***

                            tmean: **Mandatory**, p: **Mandatory**, k: 0.85

                        - ***Hamon:*** 

                            tmean: **Mandatory**, lat: **Mandatory**

                        - ***Linacre:*** 

                            tmean: **Mandatory**, elevation: **Mandatory**, lat: **Mandatory**, tdew: Optional, tmax: Optional, tmin: Optional

                        - ***Romanenko:*** 

                            tmean: **Mandatory**, rh: **Mandatory**, k: 4.5


                    - Radiation evapotranspiration calculation methods:

                        - ***Abtew:*** 

                            tmean: **Mandatory**, rs: **Mandatory**, k: 0.53

                        - ***Doorenbos - Pruitt (FAO-24):*** 

                            tmean: **Mandatory**, wind: **Mandatory**, rs: **Mandatory**, rh: **Mandatory**, pressure: Optional, elevation: Optional, albedo: 0.23

                        - ***Hargreaves:*** 

                            tmean: **Mandatory**, tmax: **Mandatory**, tmin: **Mandatory**, lat: **Mandatory**

                        - ***Jensen and Haise:*** 

                            tmean: **Mandatory**, rs: Optional, cr: 0.025, tx: -3, lat: Optional, method: 1

                        - ***Makkink:*** 

                            tmean: **Mandatory**, rs: **Mandatory**, pressure: Optional, elevation: Optional

                        - ***McGuinness and Bordne:*** 

                            tmean: **Mandatory**, lat: **Mandatory**, k: 0.0147

                        - ***Oudin:*** 

                            tmean: **Mandatory**, lat: **Mandatory**, k1: 100, k2: 5

                        - ***Turc:*** 

                            tmean: **Mandatory**, rs: **Mandatory**, rh: **Mandatory**, k: 0.31
                
                ---
                - preferred_date_interval str

                    Waterpybal dataset time interval.
                
                ---
                - raster_etp_var_dic dic default: None
                    If the ETP variable doesn't change in time, it is possible to use a raster to introduce it's values.
                    
                    Format:

                    {"var_name":["raster_dir","raster_band"]} or {"var_name":"raster_dir"} (band default to 1) or {"var_name":["raster_dir"]}
                
                ---
                - **kwargs dic
                
                    A dictionary that defines the inputs of the ETP method.
                    
                    The constant values can be defined directly
                    
                    Rasters have to be defined with "raster" keyword, and then introduced in raster_etp_var_dic argument as a dictionary

                    If the ETP variable exists in the waterpybal dataset, the "ds" keyword have to be used. 

                    Format:
                        {"var_name_1":constant_value, "var_name_2": "raster", "var_name_3": "ds",... }
                ---

            **Returns**

                -ds netCDF dataset

                    waterpybal netcdf dataset.
            
            ---
            ---
            
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
        
        for lat_t in lats:
            
            for lon_t in lons: 
                
                kwargs_={}
                nodata_etp=False
                for k in kwargs:
                    
                    if type(kwargs[k])==str and kwargs[k]=='ds':
                        
                        #print (ds)
                        #print ("k",k)
                        #print ("ds[k]",ds[k])
                        #print ("time_step_st,time_step_fin,lat_t,lon_t",time_step_st,time_step_fin,lat_t,lon_t)
                        #print (ds[k][time_step_st:time_step_fin,lat_t,lon_t].data)
                        v=ds[k][time_step_st:time_step_fin,lat_t,lon_t].data
                        #if k=="lat": v=v * np.pi / 180
                        if np.all(v==-9999):
                            #print ("nodata_etp_311")
                            nodata_etp=True
                        
                        else:
                            print ("k",k)        
                            print ("time_ind",time_ind)
                            print ("lon_t",lon_t) 
                            print("lat_t",lat_t)
                            print ("k extracted 318")
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
                        if msk[lat_t,lon_t]==0: 
                            nodata_etp=True
                            print ("nodata_etp_334")
                        else:kwargs_[k]=band[lat_t,lon_t]

                    else: 
                        va=kwargs[k] 
                        kwargs_[k]=va

                if nodata_etp==False:
                    #print ("nodata_etp==False")
                    etp_t=ETP_tools()
                    etp_t.add_ETP_method_point(method,**kwargs_)
                    etp_t=etp_t.exec_ETPs_point()
                    #print ("after exec_ETPs_point")
                    #define ETPs (calculated for each point for all time steps)
                    ds[var_name][time_step_st:time_step_fin,lat_t,lon_t]=etp_t #output from etp function
                else: 
                    #print ("in the last else")
                    ds[var_name][time_step_st:time_step_fin,lat_t,lon_t]=np.full(ds[var_name][time_step_st:time_step_fin,lat_t,lon_t].shape,-9999)
        
        return ds


    @staticmethod
    #ETP_calc_better_performance
    def ETP_calc(ds,method,preferred_date_interval,raster_etp_var_dic=None,var_name='ETP_Val',**kwargs):
        '''
            ## etp_calcs.ETP.ETP_calc()
            
            ds = ETP_calc(ds, method, preferred_date_interval, var_name='ETP_Val', raster_etp_var_dic=None, **kwargs)
            
            ETP_calc method calculate evapotranspiration in all the dataset. It uses ***pyet*** library for
            ETP calculations which is opted for use in a single point.

            Depending on the ETP method, necessary arguments have to be introduced to the database. If the argument is a 
            fix number for all times and coordinates, it could be determined right away. If the ETP
            related argument is equal to 'ds', the argument will be derived from the variable with the same name
            in the dataset. Note that user have to introduce this variables to the dataset beforehead. If the
            argument value changes with the coordinate but not with the time, the etp argument have to be equal
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


            **Parameters**

                - ds netCDF dataset

                    waterpybal netcdf dataset.

                ---
                - method
                    
                    - Combination evapotranspiration calculation methods:


                        - ***Kimberly Penman:***

                            tmean: **Mandatory**, wind: **Mandatory**, rs: Optional, rn: Optional, g: 0, tmax: Optional, tmin: Optional, rhmax: Optional, rhmin: Optional, rh: Optional, pressure: Optional, elevation: Optional, lat: Optional, n: Optional, nn: Optional, rso: Optional, a: 1.35, b: -0.35

                        - ***Penman:***
                            
                            tmean: **Mandatory**, wind: **Mandatory**, rs: Optional, rn: Optional, g: 0, tmax: Optional, tmin: Optional, rhmax: Optional, rhmin: Optional, rh: Optional, pressure: Optional, elevation: Optional, lat: Optional, n: Optional, nn: Optional, rso: Optional, aw: 2.6, bw: 0.536, a: 1.35,b: -0.35

                        - ***FAO-56 Penman-Monteith:***

                            tmean: **Mandatory**, wind: **Mandatory**, rs: Optional, rn: Optional, g: 0, tmax: Optional, tmin: Optional, rhmax: Optional, rhmin: Optional, rh: Optional, pressure: Optional, elevation: Optional, lat: Optional, n: Optional, nn: Optional, rso: Optional, a: 1.35, b: -0.35

                        - ***Priestley and taylor:***

                            tmean: **Mandatory**, wind: **Mandatory**, rs: Optional, rn: Optional, g: 0, tmax: Optional, tmin: Optional, rhmax: Optional, rhmin: Optional, rh: Optional, pressure: Optional, elevation: Optional, lat: Optional, n: Optional, nn: Optional, rso: Optional, a: 1.35, b: -0.35, alpha: 1.26

                        - ***Penman-Monteith:***

                            tmean: **Mandatory**, wind: **Mandatory**, rs: Optional, rn: Optional, g: 0, tmax: Optional, tmin: Optional, rhmax: Optional, rhmin: Optional, rh: Optional, pressure: Optional, elevation: Optional, lat: Optional, n: Optional, nn: Optional, rso: Optional, a: 1.35, b: -0.35, lai: Optional, croph: Optional, r_l: 100, r_s: 70, ra_method: 1, a_sh: 1, a_s: 1, lai_eff: 1, srs: 0.0009, co2: 300

                        - ***Thom and Oliver:***

                            tmean: **Mandatory**, wind: **Mandatory**, rs: Optional, rn: Optional, g: 0, tmax: Optional, tmin: Optional, rhmax: Optional, rhmin: Optional, rh: Optional, pressure: Optional, elevation: Optional, lat: Optional, n: Optional, nn: Optional, rso: Optional, aw: 2.6, bw: 0.536, a: 1.35, b: -0.35, lai: Optional, croph: Optional, r_l: 100, r_s: 70, ra_method: 1, lai_eff: 1, srs: 0.0009, co2: 300


                    - Temperature evapotranspiration calculation methods:


                        - ***Blaney_criddle:***

                            tmean: **Mandatory**, p: **Mandatory**, k: 0.85

                        - ***Hamon:*** 

                            tmean: **Mandatory**, lat: **Mandatory**

                        - ***Linacre:*** 

                            tmean: **Mandatory**, elevation: **Mandatory**, lat: **Mandatory**, tdew: Optional, tmax: Optional, tmin: Optional

                        - ***Romanenko:*** 

                            tmean: **Mandatory**, rh: **Mandatory**, k: 4.5


                    - Radiation evapotranspiration calculation methods:

                        - ***Abtew:*** 

                            tmean: **Mandatory**, rs: **Mandatory**, k: 0.53

                        - ***Doorenbos - Pruitt (FAO-24):*** 

                            tmean: **Mandatory**, wind: **Mandatory**, rs: **Mandatory**, rh: **Mandatory**, pressure: Optional, elevation: Optional, albedo: 0.23

                        - ***Hargreaves:*** 

                            tmean: **Mandatory**, tmax: **Mandatory**, tmin: **Mandatory**, lat: **Mandatory**

                        - ***Jensen and Haise:*** 

                            tmean: **Mandatory**, rs: Optional, cr: 0.025, tx: -3, lat: Optional, method: 1

                        - ***Makkink:*** 

                            tmean: **Mandatory**, rs: **Mandatory**, pressure: Optional, elevation: Optional

                        - ***McGuinness and Bordne:*** 

                            tmean: **Mandatory**, lat: **Mandatory**, k: 0.0147

                        - ***Oudin:*** 

                            tmean: **Mandatory**, lat: **Mandatory**, k1: 100, k2: 5

                        - ***Turc:*** 

                            tmean: **Mandatory**, rs: **Mandatory**, rh: **Mandatory**, k: 0.31
                
                ---
                - preferred_date_interval str

                    Waterpybal dataset time interval.
                
                ---
                - raster_etp_var_dic dic default: None
                    If the ETP variable doesn't change in time, it is possible to use a raster to introduce it's values.
                    
                    Format:

                    {"var_name":["raster_dir","raster_band"]} or {"var_name":"raster_dir"} (band default to 1) or {"var_name":["raster_dir"]}
                
                ---
                - **kwargs dic
                
                    A dictionary that defines the inputs of the ETP method.
                    
                    The constant values can be defined directly
                    
                    Rasters have to be defined with "raster" keyword, and then introduced in raster_etp_var_dic argument as a dictionary

                    If the ETP variable exists in the waterpybal dataset, the "ds" keyword have to be used. 

                    Format:
                        {"var_name_1":constant_value, "var_name_2": "raster", "var_name_3": "ds",... }
                ---

            **Returns**

                -ds netCDF dataset

                    waterpybal netcdf dataset.
            
            ---
            ---
            
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
        
        #extracting the arguments for etp calculation
        all_kwargs_dic={}

        for k in kwargs:

            if type(kwargs[k])==str and kwargs[k]=='ds':
                v_k=ds[k][time_step_st:time_step_fin,:,:].data
            
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

            kwargs_dic={}
            for lat_t in lats:
            
                for lon_t in lons: 
                    
                    #kwargs_dic_key=str(lat_t)+str(lon_t)
                    #kwargs_={}
                    #nodata_etp=False
                
                    
                    if type(kwargs[k])==str and kwargs[k]=='ds':
                        
                        #print (ds)
                        #print ("k",k)
                        #print ("ds[k]",ds[k])
                        #print ("time_step_st,time_step_fin,lat_t,lon_t",time_step_st,time_step_fin,lat_t,lon_t)
                        #print (ds[k][time_step_st:time_step_fin,lat_t,lon_t].data)
                        v=v_k[:,lat_t,lon_t]
                        #if k=="lat": v=v * np.pi / 180
                        if np.all(v==-9999):
                            #print ("nodata_etp_311")
                            nodata_etp=True
                            temp_v=False
                        else:
                            '''print ("k",k)        
                            print ("time_ind",time_ind)
                            print ("lon_t",lon_t) 
                            print("lat_t",lat_t)
                            print ("k extracted 318")'''
                            temp_v=pd.DataFrame(v,columns=[k],index=time_ind).squeeze()
                            #kwargs_[k]=temp_v[k]

                    elif type(kwargs[k])==str and kwargs[k]=='raster':

                        if msk[lat_t,lon_t]==0: 
                            nodata_etp=True
                            #print ("nodata_etp_raster")
                            temp_v=False

                        else:
                            #kwargs_[k]=band[lat_t,lon_t]
                            temp_v=band[lat_t,lon_t]
                    else: 
                        #kwargs_[k]=kwargs[k]
                        try:
                            f=kwargs[k].squeeze()
                        except:
                            f=kwargs[k]

                        temp_v=f

                    kwargs_dic[str(lat_t)+str(lon_t)]=temp_v
            all_kwargs_dic[k]=kwargs_dic    
        ######################        
        
        #calculating the etp in each point
        array_for_ds=np.full(ds[var_name].shape,-9999)
        for lat_t in lats:
            
                for lon_t in lons: 
                    
                    kwargs_={}
                    nodata_etp=False
                    for k in kwargs:
                        aa=all_kwargs_dic[k][str(lat_t)+str(lon_t)]
                        if type(aa)==bool and aa==False:
                            nodata_etp=True
                        else:
                            kwargs_[k]=aa

                    if nodata_etp==False:
                        #print ("nodata_etp==False")
                        etp_t=ETP_tools()
                        etp_t.add_ETP_method_point(method,**kwargs_)
                        etp_t=etp_t.exec_ETPs_point()
                        #print (etp_t)
                        #print (etp_t[method].shape)
                        #print ("after exec_ETPs_point")
                        #define ETPs (calculated for each point for all time steps)
                        etp_t[method][etp_t[method]<0]=0
                        array_for_ds[time_step_st:time_step_fin,lat_t,lon_t]=etp_t[method] #output from etp function
                    else: 
                        #print ("in the last else")
                        #ds[var_name][time_step_st:time_step_fin,lat_t,lon_t]=np.full(ds[var_name][time_step_st:time_step_fin,lat_t,lon_t].shape,-9999)
                        pass
        
        ds[var_name][:,:,:]=array_for_ds
        
        
        return ds

        