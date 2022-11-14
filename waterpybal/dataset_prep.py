import csv
import os
import netCDF4 as nc
import numpy as np
import pandas as pd
import rasterio as rs
from osgeo import gdal
import datetime as dt

###################################################################
class dataset_gen(object):
    '''
    # class dataset_prep.dataset_gen()
    The class to create the waterpybal netCDF dataset dimensions and variables

    **Methods**

        > dtype = ds_dimensions(self,lat_lon_type,lat_lon_source,time_source,time_type,preferred_date_interval,lat_name="lat",lon_name="lon",time_name="time",border_res_dic=None,time_dic=None)
        
        > ds = var_generation(self,dir,ds_values_dic=None,urban_ds=False)
        
        ---
    
    **Attributes**

        lat

        lon

        time

        dtype

        time_steps_dic

            Contains the time step information for the waterpybal netcdf dataset. Have to be introduced in var_generation function.
            Format: {"time_v": time_v, "time_b1": time_b1, "time_b2": time_b2, "tunit": tunit}

    ---
    ---

    '''
    def __init__(self) -> None:
        self.lat=None
        self.lon=None
        self.dtype=None
        self.time_steps_dic=None
    
    ######################
    def ds_dimensions(self,lat_lon_type,lat_lon_source,time_source,time_type,preferred_date_interval,lat_name="lat",lon_name="lon",time_name="time",border_res_dic=None,time_dic=None): #lat_lon_type="raster", "dataframe", "csv","border_res_list","netcdf"
        '''
            ## dataset_prep.dataset_gen.ds_dimensions()
            
            dtype = ds_dimensions(lat_lon_type,lat_lon_source,time_source,time_type,lat_name,lon_name,time_name,border_res_dic,time_dic,preferred_date_interval)
            
            The method to create the waterpybal netCDF dataset lat long and time dimensions


            **Parameters**

                - lat_lon_type str

                    Source type that identify the lat and long of the dataset. "dataframe", "csv", "netcdf", "raster" and "border_res_dic" are valid.
                    if "border_res_dic" is selected, the borders of the dataset have to be defined in border_res_dic parameter.
                
                ---
                - lat_lon_source str (.csv - .nc - .tif) or pandas dataframe

                    If the lat_lon_type is "dataframe", "csv", "netcdf" or "raster", lat_lon_source is the source of the lat and long values.
                
                ---
                - time_type str

                    Source type that identify the time steps of the dataset. "dataframe", "csv", "netcdf" and "time_dic" are valid.
                    if "time_dic" is selected, the borders of the dataset have to be defined in border_res_dic parameter.

                ---
                - time_source str (.csv - .nc) or pandas dataframe

                    If the time_type is "dataframe", "csv" or "netcdf", time_source is the source of the dataset time steps.

                ---
                - lat_name str default: "lat"

                    Applicabale if the lat_lon_type is "dataframe", "csv", "netcdf". lat field name.
                
                ---
                -lon_name str default: "lon"

                    Applicabale if the lat_lon_type is "dataframe", "csv", "netcdf". lon field name.

                ---
                - time_name str default: "time"

                    Applicabale if the time_type is "dataframe", "csv", "netcdf". time field name.

                ---
                - border_res_dic dic default: None

                    Applicabale if the lat_lon_type is "border_res_dic". Format: {"left":value,"right":value,"width":value,"top":value,"bottom":value,"height":value}
                ---
                - time_dic dic default: None

                    Applicabale if the time_type is "time_dic". Format: {"start":["yyyy","mm","dd","hh"], "end":["yyyy","mm"."dd","hh"]}
                
                ---
                - preferred_date_interval str

                    Date interval of the dataset. "Hourly", "Daily" and "Monthly" are valid.

                ---

            **Returns**

                - dtype str
                
                    Dataset time interval dtype
                ---
                ---
        '''
        #For lat lon
        if lat_lon_type=="dataframe":
            lat=np.unique(np.array(lat_lon_source[lat_name])).sort()
            lon=np.unique(np.array(lat_lon_source[lon_name])).sort()
        #########
        elif lat_lon_type=="csv": 
            data = pd.read_csv(lat_lon_source)
            lat=np.unique(np.array(data[lat_name])).sort()
            lon=np.unique(np.array(data[lon_name])).sort()
        #########
        elif lat_lon_type=="netcdf":
            ds=nc.Dataset(lat_lon_source,'r',format='NETCDF4')
            lat=np.unique(ds[lat_name][:])
            lon=np.unique(ds[lon_name][:])
        #########
        elif lat_lon_type=="raster":
            src = rs.open(lat_lon_source)
            lon = np.linspace(src.bounds.left, src.bounds.right, src.width)
            lat = np.linspace(src.bounds.top, src.bounds.bottom, src.height)
        #########
        elif lat_lon_type=="border_res_dic":
            lon = np.linspace(border_res_dic["left"],border_res_dic["right"],border_res_dic["width"])
            lat = np.linspace(border_res_dic["top"],border_res_dic["bottom"],border_res_dic["height"])
        else: print ("lat long dimensions failed!")
        ####################################
        if preferred_date_interval=="Hourly": 
            dtype='datetime64[h]'
            tunit="minutes since 1970-01-01 00:00:00 UTC"
        elif preferred_date_interval=="Daily": 
            dtype='datetime64[D]'
            tunit="hours since 1970-01-01 00:00:00 UTC"
        elif preferred_date_interval=="Monthly": 
            dtype='datetime64[M]'
            tunit="days since 1970-01-01 00:00:00 UTC"
        
        #For time     
        if time_type=="dataframe":
            #time=np.sort(np.unique(np.array(pd.to_datetime(time_source[time_name]),dtype=dtype)))
            time_source[time_name]
        #########
        elif time_type=="csv": 
            
            data = pd.read_csv(time_source)
            time=np.sort(np.unique(np.array(pd.to_datetime(data[time_name]),dtype=dtype)))
        #########
        elif time_type=="netcdf":
            ds=nc.Dataset(time_source,'r',format='NETCDF4')
            time=np.unique(np.array(ds[time_name][:],dtype=dtype))
        
        elif time_type== "time_dic": #{"start":["yyyy","mm","dd","hh"], "end":["yyyy","mm"."dd","hh"]}
            start=np.datetime64( time_dic["start"][0] +'-'+ time_dic["start"][1] +'-'+ time_dic["start"][2] + 'T'+ time_dic["start"][3])
            end=np.datetime64( time_dic["end"][0] +'-'+ time_dic["end"][1] +'-'+ time_dic["end"][2] + 'T'+ time_dic["end"][3])
            time=np.arange(start,end,dtype=dtype)
        else: print ("time dimension failed!")
        
        ####################################
        
        origin_2 = np.array("1970-01-01",dtype=dtype)  
      
        if preferred_date_interval=="Hourly":
            time_v_delta=np.timedelta64(30,'m')
            time_b2_delta=np.timedelta64(1, "h")
            origin = np.array("1970-01-01",dtype='datetime64[m]')   
        elif preferred_date_interval=="Daily": 
            time_v_delta= np.timedelta64(12,'h')
            time_b2_delta=np.timedelta64(1, "D")
            origin = np.array("1970-01-01",dtype='datetime64[h]')   
        elif preferred_date_interval=="Monthly": 
            time_v_delta = np.timedelta64(15,'D')
            time_b2_delta=np.timedelta64(1, "M")
            origin = np.array("1970-01-01",dtype='datetime64[D]')   

        since_origin = time - origin
        time_b1=time - origin_2

        time_b2=time_b1[1:]        

        time_v = since_origin +time_v_delta
        time_b2=np.append(time_b2,time_b2[-1]+time_b2_delta)


        time_steps_dic={"time_v":time_v,"time_b1":time_b1,"time_b2":time_b2,"tunit":tunit}

        self.lon=lon
        self.lat=lat
        self.time=time
        self.dtype=dtype
        self.time_steps_dic=time_steps_dic

        return self.dtype

    
    ######################
    def var_generation(self,dir,ds_values_dic=None,urban_ds=False):
        '''
            ## dataset_prep.dataset_gen.var_generation()
            
            ds = var_generation(self,dir,ds_values_dic=None,urban_ds=False)            
            
            The method to create the waterpybal netCDF dataset dimensions and variables


            **Parameters**

                - dir str

                    The path to save the waterpybal netcdf dataset
                
                ---
                - ds_values_dic nonetype or dic default: None

                    To add additional variables to the waterpybal dataset. The additional variables can be used in following stages such as ETP calculation, etc.
                    Format: ds_values_dic={"desired_variable":"desired_variable_unit",...} 
                
                ---
                - urban_ds bool default: False

                    To add the urban related variables to the dataset.
                ---

            **Returns**

                -ds netCDF dataset

                    waterpybal netcdf dataset.
            
            ---
            ---

        '''
        lons_np=self.lon
        lats_np=self.lat
        times_np=self.time
        time_steps_dic=self.time_steps_dic

        time_b1=time_steps_dic["time_b1"]
        time_b2=time_steps_dic["time_b2"]
        tunit=time_steps_dic["tunit"]

        inputs_dic={"Prec_Val":"mm","Runoff_Val":"mm","Irig_Val":"mm","CN_Val":"No_Unit","INF_Val":"mm","ETP_Val":"mm","PRu_Val":"mm","pwp":"no_unit","cc":"no_unit","rrt":"no_unit"}
        outputs_dic={"ETR_Val":"mm","Def_Val":"mm","Rec_Val":"mm","Ru_Val":"mm","five_day_acc_prec":"mm","CN_mod":"no_unit"}
        urban_dic={"wat_cons":"mm","wat_net_loss":"%","urb_dir_evap":"%","urb_indir_evap":"%","sew_net_loss_low":"%","sew_net_loss_high":"%","prec_sewage_threshold":"mm","runoff_to_sewage":"%","dir_infil":"%","wat_supp_wells":"mm","wat_supp_wells_loss":"%","wat_other":"%","urban_to_ds_inf_etp_ratio":"%"}
        
        if type(ds_values_dic)==dict: inputs_dic= {**inputs_dic,**ds_values_dic}
        if urban_ds: inputs_dic={**inputs_dic,**urban_dic}
        
        ds=nc.Dataset(dir,'w',format='NETCDF4')
        #create dimensions
        ds.createDimension("time",None) #None: unlimited dimension
        ds.createDimension("lon",None)
        ds.createDimension("lat",None)
        ds.createDimension("nv", 2)

        #create variables
        time=ds.createVariable( "time","f8", ("time",) )
        time.standard_name = "time"
        time.long_name = "time"
        time.calendar = "standard"
        time.units = tunit
        time.bounds = "time_bnds"

        time_bnds = ds.createVariable("time_bnds", "f4", ("time","nv",))
        lons=ds.createVariable( "lon","f4", ("lon",) )
        lats=ds.createVariable( "lat","f4", ("lat",) )
        time[:]=times_np
        time_bnds[:,0]=time_b1
        time_bnds[:,1]=time_b2
        #define lats and longs
        lats[:]=lats_np
        lons[:]=lons_np
        
        #times_np=np.datetime_as_string(times_np,unit='h')
        time[:]=times_np
        
        #create values

        #INPUTS &OUTPUTS
        for di in [inputs_dic,outputs_dic]:
            for val,unit in di.items():
                ds.createVariable( val,"f4", ("time", "lat", "lon", ), fill_value=-9999 )
                ds[val].units=unit

        return ds

###################################################################
class variable_management(object):
    '''
    # class dataset_prep.variable_management()
    
    The class to introduce or interpolate the variables from different sources

    **Methods**

        > ds = var_interpolation(ds,ras_sample_dir,csv_dir,var_name,method,preferred_date_interval,interpolation_time_int,time_csv_col="time",lat_csv_col="lat",lon_csv_col="lon",multiply=False)
        
        > ds = var_introduction_from_tiffs(ds,folder_dir,var_name,preferred_date_interval,multiply)

        > ds = var_introduction_from_csv(ds,csv_dir,time_csv_col,var_name,preferred_date_interval,interpolation_time_int,multiply)
    
        > ds = var_introduction_from_nc(new_nc_dir,ds,var_name)
    ---
    ---
    '''

    ######################
    @staticmethod
    def var_interpolation(ds,ras_sample_dir,csv_dir,var_name,method,preferred_date_interval,interpolation_time_int,time_csv_col="time",lat_csv_col="lat",lon_csv_col="lon",multiply=False):
        
        '''
        ## dataset_prep.variable_management.var_interpolation()
            
            ds = var_interpolation(ds,ras_sample_dir,csv_dir,time_csv_col,lat_csv_col,lon_csv_col,var_name,method,preferred_date_interval,interpolation_time_int,multiply)
            
            The method to interpolate variables from .csv files. The .csv have to have a lat, long, time and variable name field.
            The variable name field have to be the same as the name in the waterpybal dataset.


            **Parameters**

                - ds netCDF dataset

                    waterpybal netcdf dataset.

                ---
                - ras_sample_dir str

                    path to the raster (.tif) file that represents the study area.

                ---
                - csv_dir str
                
                    Path to the .csv file that contains the measured data.
                ---
                
                - time_csv_col str default: "time"
                    
                    .csv time field name

                ---
                - lat_csv_col str default "lat"
                
                    .csv lat field name

                ---
                - lon_csv_col str default "lon"
                
                    .csv lon field name

                ---
                - var_name str
            
                    .csv variable field name. Have to be the same as watepybal netcdf dataset.

                ---   
                - method str
                    refer to gdal.grid method for more information about the available methods.
                    
                    Examples:

                        > "nearest"
                        
                        > "invdist:power=2:radius1=100:radius2=800"
                        
                        > "linear"
                        
                        > "average:radius1=100:radius2=800:angle=20"
                        
                        > "minimum:radius1=100:radius2=800:angle=20"
                
                ---
                - preferred_date_interval str

                    Waterpybal dataset time interval.

                ---
                - interpolation_time_int str
                
                    .csv time interval. In case the .csv time interval differ the dataset time interval, the .csv values proportionally will be distributed between the time steps.
                
                ---
                - multiply bool default: False 

                    In case the .csv time interval is not the same as the dataset, use the same values for valid time steps
                    (Ex: Temp. vs cumulative precipitation)
                ---

            **Returns**

                -ds netCDF dataset

                    waterpybal netcdf dataset.
            
            ---
            ---
        '''

        # get raster info for bounds
        src = rs.open(ras_sample_dir)
        outputBounds=[src.bounds.left,src.bounds.top,src.bounds.right,src.bounds.bottom]
        width=src.width
        height=src.height
        msk = src.read_masks(1)
        src.close()

        if interpolation_time_int in ["Daily",'datetime64[D]']: interpolation_time_int='datetime64[D]'
        elif interpolation_time_int in ["Monthly",'datetime64[M]']: interpolation_time_int='datetime64[M]'
        elif interpolation_time_int in ["Hourly",'datetime64[h]']: interpolation_time_int='datetime64[h]'        
        '''if time_interpolation==False:'''
        #group the csv in timesteps
        df=pd.read_csv(csv_dir)
        df[time_csv_col]=np.array(pd.to_datetime(df[time_csv_col]))
        df=df.set_index(time_csv_col)
        '''else:
            df=df_fin
        '''


        np_interpolated_dic=dict()
        np_interpolated_dic_cntr=dict()
        
        #datetime64
        time_tt=np.array(df.index.unique())
        nute=0

        #delete existing files
        if os.path.exists("temp_tiff.tiff"): os.remove("temp_tiff.tiff")
        if os.path.exists("temp_csv.csv"): os.remove("temp_csv.csv")
        if os.path.exists("temp_csv.vrt"): os.remove("temp_csv.vrt")

        for i in time_tt:
            nute=nute+1
            print ("timestep count: ", nute)
            

            ########

            #create a temporal csv pf just one timestep
            df_t=df[df.index==i]
            df_t=df_t.sort_values(by=[lat_csv_col,lon_csv_col],ascending=[False,True])
            df_t.to_csv("temp_csv.csv")

            #for each timestep, a gdal dataset
            
            OGRVRT="<OGRVRTDataSource>\n \
                <OGRVRTLayer name=\"temp_csv\">\n \
                    <SrcDataSource>temp_csv.csv</SrcDataSource>\n \
                    <GeometryType>wkbPoint</GeometryType>\n \
                    <GeometryField encoding=\"PointFromColumns\" x=\""+ lon_csv_col +"\" y=\""+ lat_csv_col +"\" z=\""+ var_name +"\"/>\n \
                </OGRVRTLayer>\n \
                </OGRVRTDataSource>"

            f=open("temp_csv.vrt","w")
            f.write(OGRVRT)
            f.close()

            #interpolate the dataset
            nn=gdal.Grid("temp_tiff.tiff", "temp_csv.vrt",zfield=var_name,algorithm=method,
            outputBounds=outputBounds,width=width,height=height,noData=-9999)
            nn=None

            #open temp_tiff
            src_temp = rs.open("temp_tiff.tiff")
            rast=src_temp.read(1)
            rast[msk==0]=np.nan #no data
            #here we have to change the index (i) to number:



            ###########
            # #to make average if not fits
            if i in np_interpolated_dic: 

                np_interpolated_dic[i]=(np_interpolated_dic[i]+rast)
                np_interpolated_dic_cntr[i]=np_interpolated_dic_cntr[i]+1
            else:
                np_interpolated_dic[i]=rast
                np_interpolated_dic_cntr[i]=1
            
            for date,val in np_interpolated_dic_cntr.items():
                np_interpolated_dic[date]=np_interpolated_dic[date]/val

            src_temp.close()      
        
            if os.path.exists("temp_tiff.tiff"): os.remove("temp_tiff.tiff")
            if os.path.exists("temp_csv.csv"): os.remove("temp_csv.csv")
            if os.path.exists("temp_csv.vrt"): os.remove("temp_csv.vrt")      

        #store in netcdf

        
        ds=tools.match_date(new_dic=np_interpolated_dic,preferred_date_interval=preferred_date_interval,new_time_int=interpolation_time_int,ds=ds,var_name=var_name,multiply=multiply)

        '''elif time_interpolation==True: #add the data to ds in case time interpolation is True and space interpolation is false
            #create a temporal csv pf just one timestep
            time=ds["time"][:].data
            lat_ds=ds["lat"][:].data
            lon_ds=ds["lon"][:].data
            for index, row in df_fin.iterrows():
                t_idx=np.where(time==row[time_csv_col])
                lat_idx=np.where(lat_ds==row[lat_csv_col])
                lon_idx=np.where(lon_ds==row[lon_csv_col])
            ds[var_name][t_idx,lat_idx,lon_idx]=row[var_name]'''

        #else:
        #    pass


        return ds
    
    ######################
    @staticmethod
    def var_introduction_from_tiffs(ds,folder_dir,var_name,preferred_date_interval,multiply=False):
        '''
        ## dataset_prep.variable_management.var_introduction_from_tiffs()
            
            ds = var_introduction_from_tiffs(ds,folder_dir,var_name,preferred_date_interval,multiply)
            
            The method to introduce variables from a folder containing the geotiff (.tif) files. the name of the files in the folder have to be the time step they're refering to.
            Format: YYYY-MM-DD-HH


            **Parameters**

                - ds netCDF dataset

                    waterpybal netcdf dataset.

                ---
                - folder_dir str

                    path to the folder containing the geotiff (.tif) files

                ---
                - var_name str
            
                    .csv variable field name. Have to be the same as watepybal netcdf dataset.

                ---
                - preferred_date_interval str

                    Waterpybal dataset time interval.

                ---
                - multiply bool default: False 

                    In case the .csv time interval is not the same as the dataset, use the same values for valid time steps
                    (Ex: Temp. vs cumulative precipitation)
                    ---

            **Returns**

                -ds netCDF dataset

                    waterpybal netcdf dataset.
            
            ---
            ---
        '''
        import glob
        tifs = glob.glob(os.path.join(folder_dir,"*"))
        rast_dic={}

        for t in tifs:
            date=os.path.splitext(t)[0].split("\\")[-1].split("-")
            d=os.path.splitext(t)[0].split("\\")[-1]

            if len(date)==2: date_interval='datetime64[M]'
                
            elif len(date)==3: date_interval='datetime64[D]'

            elif len(date)==4: date_interval='datetime64[h]'
            
            d=np.array(d,dtype=date_interval)
            d=str(d.astype(preferred_date_interval))

            src_temp = rs.open(t)
            arr=src_temp.read(1)
            if d in rast_dic: rast_dic[d]=(rast_dic[d]+arr)/2
            else: rast_dic[d]=arr
            src_temp.close()

        ds=tools.match_date(new_dic=rast_dic,preferred_date_interval=preferred_date_interval,new_time_int=date_interval,ds=ds,var_name=var_name,multiply=multiply)
        return ds
    
    ######################
    @staticmethod
    def var_introduction_from_csv(ds,csv_dir,var_name,preferred_date_interval,interpolation_time_int,time_csv_col="time",multiply=False):
        '''
        ## dataset_prep.variable_management.var_introduction_from_csv()
            
            ds = var_introduction_from_csv(ds,csv_dir,var_name,preferred_date_interval,interpolation_time_int,time_csv_col="time",multiply=False)
            
            The method to introduce **THE SAME VALUES FOR ALL THE STUDY AREA IN A TIMESTEP** from a .csv file without interpolation.


            **Parameters**

                - ds netCDF dataset

                    waterpybal netcdf dataset.

                ---
                - csv_dir str
                
                    Path to the .csv file that contains the measured data.
                ---
                
                - time_csv_col str default: "time"
                    
                    .csv time field name

                ---
                - var_name str
            
                    .csv variable field name. Have to be the same as watepybal netcdf dataset.

                ---
                - preferred_date_interval str

                    Waterpybal dataset time interval.

                ---
                - interpolation_time_int str
                
                    .csv time interval. In case the .csv time interval differ the dataset time interval, the .csv values proportionally will be distributed between the time steps.
                
                ---
                - multiply bool default: False 

                    In case the .csv time interval is not the same as the dataset, use the same values for valid time steps
                    (Ex: Temp. vs cumulative precipitation)
                ---

            **Returns**

                -ds netCDF dataset

                    waterpybal netcdf dataset.
            
            ---
            ---
        '''
        
        
        if interpolation_time_int in ["Daily",'datetime64[D]']: interpolation_time_int='datetime64[D]'
        elif interpolation_time_int in ["Monthly",'datetime64[M]']: interpolation_time_int='datetime64[M]'
        elif interpolation_time_int in ["Hourly",'datetime64[h]']: interpolation_time_int='datetime64[h]'  
        #group the csv in timesteps
        df=pd.read_csv(csv_dir)
        df[time_csv_col]=np.array(pd.to_datetime(df[time_csv_col]))
        df=df.drop_duplicates(subset=time_csv_col)
        df=df.set_index(time_csv_col) 
        df=df[[var_name] ]
        ##################
        np_interpolated_dic=dict()
        np_interpolated_dic_cntr=dict()
        
        #datetime64
        time_tt=np.array(df.index.unique())   

        if interpolation_time_int!=preferred_date_interval:
            for i in time_tt:
            
            
        
                ###########
                df_t=df[df.index==i]
                # #to make average if not fits
                if i in np_interpolated_dic: 

                    np_interpolated_dic[i]=(np_interpolated_dic[i]+df_t)
                    np_interpolated_dic_cntr[i]=np_interpolated_dic_cntr[i]+1
                else:
                    np_interpolated_dic[i]=df_t
                    np_interpolated_dic_cntr[i]=1
                
                for date,val in np_interpolated_dic_cntr.items():
                    np_interpolated_dic[date]=np_interpolated_dic[date]/val

            ds=tools.match_date(new_dic=np_interpolated_dic,preferred_date_interval=preferred_date_interval,new_time_int=interpolation_time_int,ds=ds,var_name=var_name,multiply=multiply)
            
        else:
            #select df times that exist in the dataframe
            ds_date_interval=tools.dtimechanger(preferred_date_interval)
            
            
            time=ds["time"][:].data #numbers
            
            time=time.astype(ds_date_interval)
            time=time.astype(interpolation_time_int)
            
            ds_time_pd=pd.DataFrame(time,dtype=interpolation_time_int,columns=[time_csv_col])
            
            ds_time_pd[time_csv_col]=np.array(pd.to_datetime(ds_time_pd[time_csv_col]))
            
            arr=ds_time_pd.merge(df ,how='left', on=time_csv_col)

            arr=np.nan_to_num(arr[var_name],nan=-9999) 
            arr=arr.reshape(ds[var_name].shape)


            ds[var_name][: ,:,:]=arr

            
        return ds
    
    ######################
    @staticmethod
    def var_introduction_from_nc(new_nc_dir,ds,var_name):
        '''
        ## dataset_prep.variable_management.var_introduction_from_nc()
            
            ds = var_introduction_from_nc(new_nc_dir,ds,var_name)
            
            The method to introduce variables from a netcdf database with the same dimension and variable name


            **Parameters**

                - ds netCDF dataset

                    waterpybal netcdf dataset.

                ---
                - new_nc_dir str

                    path to the new netcdf file.

                ---
                - var_name str
            
                    new netcdf variable field name. Have to be the same as watepybal netcdf dataset.

                ---

            **Returns**

                -ds netCDF dataset

                    waterpybal netcdf dataset.
            
            ---
            ---
        '''
        ds_temp=nc.Dataset(new_nc_dir,'r+',format='NETCDF')
        ds[var_name][: ,:,:]=ds_temp["var_name"][:,:,:]
        return ds

###################################################################
class tools(object):
    '''
    The class containing the tools used in variable_management class.
    '''

    @staticmethod
    def match_date(new_dic,preferred_date_interval,new_time_int,ds,var_name,multiply):
        '''
           To match the date of the inputs and the dataset 
        '''



        ds_date_interval=tools.dtimechanger(preferred_date_interval)

        
        time=ds["time"][:].data #numbers
        time=time.astype(ds_date_interval)

        for date,arr in new_dic.items():
            date_dt=np.array(date,dtype=preferred_date_interval)
               
            
            #date_dt = date_dt - origin
            #interpolated data is more frequent than the dataset preferred_date_interval
            if preferred_date_interval==new_time_int or (preferred_date_interval in ['datetime64[D]', 'datetime64[M]'] and new_time_int=='datetime64[h]') or (preferred_date_interval=='datetime64[M]' and new_time_int=='datetime64[D]'):
                #origin = np.array("1970-01-01",dtype=preferred_date_interval)
                time_temp=time.astype(preferred_date_interval)
         
            else:

                if multiply==True:  
                    if preferred_date_interval=='datetime64[h]' and new_time_int=='datetime64[D]': #hour to daily
                        arr=arr/24
                    elif preferred_date_interval=='datetime64[h]' and new_time_int=='datetime64[M]': #hour to month
                        arr=arr/720
                    elif preferred_date_interval=='datetime64[D]' and new_time_int=='datetime64[M]': #day to month
                        arr=arr/30
                else: print ("match_date function error - 2!")    
                
                #origin = np.array("1970-01-01",dtype=new_time_int)

                time_temp=time.astype(new_time_int)

            u=np.where(time_temp == date_dt)
            if len(u)>0:
                u_list=list(u[0])
                if len(u_list)>0:
                    for uu in u_list:
                        arr=np.nan_to_num(arr,nan=-9999)
                        ds[var_name][uu ,:,:]=arr

        return ds
    
    ######################
    @staticmethod
    def dtimechanger(preferred_date_interval):
        '''
            To change the user introduced time interval to dataset time interval
        '''
        if preferred_date_interval=='datetime64[h]': ds_date_interval='datetime64[m]'
        elif preferred_date_interval=='datetime64[D]': ds_date_interval='datetime64[h]'
        elif preferred_date_interval=='datetime64[M]': ds_date_interval='datetime64[D]'
        return ds_date_interval 