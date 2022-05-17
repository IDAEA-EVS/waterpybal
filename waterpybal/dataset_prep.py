import os
import netCDF4 as nc
import numpy as np
import pandas as pd
import rasterio as rs
from osgeo import gdal
import datetime as dt
#-------------------------------------
#Integrate inputs into netCDF
#NETCDF database generation and assigning the time,lat and long

class netCDF_ds(object):
    
    @staticmethod
    def var_generation(dir,tunit,lats_np,lons_np,times_np,time_b1,time_b2,ds_values_dic=None):
        
        inputs_dic={"Prec_Val":"mm","CN_Val":"No_Unit","INF_Val":"mm","ETP_Val":"mm","PRu_Val":"mm","pwp":"no_unit","cc":"no_unit","rrt":"no_unit"}
        outputs_dic={"ETR_Val":"mm","Def_Val":"mm","Rec_Val":"mm","Ru_Val":"mm","five_day_acc_prec":"mm","CN_mod":"no_unit"}
        if type(ds_values_dic)==dict: inputs_dic= {**inputs_dic,**ds_values_dic}

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

    @staticmethod
    def ds_dimensions(lat_lon_type,lat_lon_source,time_source,time_type,lat_name,lon_name,time_name,border_res_dic,time_dic,preferred_date_interval): #lat_lon_type="raster", "dataframe", "csv","border_res_list","netcdf"
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


        return lat,lon,time_v,time_b1,time_b2,dtype,tunit
    
    @staticmethod
    def match_date(new_dic,preferred_date_interval,new_time_int,ds,var_name):
        
        print ("new_dic:\n",new_dic)

        if preferred_date_interval=='datetime64[h]': ds_date_interval='datetime64[m]'
        elif preferred_date_interval=='datetime64[D]': ds_date_interval='datetime64[h]'
        elif preferred_date_interval=='datetime64[M]': ds_date_interval='datetime64[D]'
        
        time=ds["time"][:].data #numbers
        time=time.astype(ds_date_interval)

        for date,arr in new_dic.items():
            date_dt=np.array(date,dtype=preferred_date_interval)
               
            
            #date_dt = date_dt - origin
            #interpolated data is more frequent than the dataset preferred_date_interval
            if preferred_date_interval==new_time_int or (preferred_date_interval in ['datetime64[D]', 'datetime64[M]'] and new_time_int=='datetime64[h]') or (preferred_date_interval=='datetime64[M]' and new_time_int=='datetime64[D]'):
                #origin = np.array("1970-01-01",dtype=preferred_date_interval)
                time_temp=time.astype(preferred_date_interval)
                
                '''if preferred_date_interval=='datetime64[h]': 
                    #dt_delt= np.timedelta64(30,'m')  
                    time_temp=origin+time.astype('datetime64[m]')
                elif preferred_date_interval=='datetime64[D]':
                    #dt_delt= np.timedelta64(12,'h')
                    time_temp=origin+time.astype('datetime64[h]')
                elif preferred_date_interval=='datetime64[M]':
                    #dt_delt= np.timedelta64(15,'D')
                    time_temp=origin+time.astype('datetime64[D]')
                else: print ("match_date function error - 1!")'''
                            
            else:

                if preferred_date_interval=='datetime64[h]' and new_time_int=='datetime64[D]': #hour to daily
                    arr=arr/24
                elif preferred_date_interval=='datetime64[h]' and new_time_int=='datetime64[M]': #hour to month
                    arr=arr/720
                elif preferred_date_interval=='datetime64[D]' and new_time_int=='datetime64[M]': #day to month
                    arr=arr/30
                else: print ("match_date function error - 2!")    
                
                #origin = np.array("1970-01-01",dtype=new_time_int)
                #print (time.astype(new_time_int))
                #print (origin)
                time_temp=time.astype(new_time_int)

            u=np.where(time_temp == date_dt)
            if len(u)>0:
                u_list=list(u[0])
                if len(u_list)>0:
                    for uu in u_list:
                        ds[var_name][uu ,:,:]=arr

        return ds
    
    @staticmethod
    def var_interpolation(ds,ras_sample_dir,csv_dir,time_csv_col,lat_csv_col,lon_csv_col,var_name,method,preferred_date_interval,interpolation_time_int):
        '''
        method: "nearest" - "invdist:power=2:radius1=100:radius2=800" - "linear" - "average:radius1=100:radius2=800:angle=20"-"minimum:radius1=100:radius2=800:angle=20"
        '''
        '''if time_interpolation==True:
            df=pd.read_csv(csv_dir)
            df.sort_values(by=[time_csv_col])
            lon_t=pd.unique(df[lon_csv_col])
            lat_t=pd.unique(df[lat_csv_col])
            n=0
            for lo,la in zip(list(lon_t),list(lat_t)):
                df_t=df[ (df[lon_csv_col]==lo) & (df[lat_csv_col]==la) ]
                if df_t.empty==False:
                    df_t[var_name]=df_t[var_name].interpolate(method='linear', limit_direction='forward', axis=0,inplace=True)
                    n=n+1
                    if n==1:
                        df_fin=df_t
                    else:
                        df_fin=pd.concat([df_fin, df_t], ignore_index=True) 
            df_fin=df_fin.sort_values(by=[lat_csv_col,lon_csv_col],ascending=[False,True])
        '''
        #if space_interpolation==True:

        # get raster info for bounds
        src = rs.open(ras_sample_dir)
        outputBounds=[src.bounds.left,src.bounds.top,src.bounds.right,src.bounds.bottom]
        width=src.width
        height=src.height
        src.close()

        if interpolation_time_int in ["Daily",'datetime64[D]']: interpolation_time_int='datetime64[D]'
        elif interpolation_time_int in ["Monthly",'datetime64[M]']: interpolation_time_int='datetime64[M]'
        elif interpolation_time_int in ["Hourly",'datetime64[h]']: interpolation_time_int='datetime64[h]'        
        '''if time_interpolation==False:'''
        #group the csv in timesteps
        df=pd.read_csv(csv_dir)
        df[time_csv_col]=np.array(pd.to_datetime(df[time_csv_col]))
        df=df.set_index(time_csv_col)
        #print (df)
        '''else:
            df=df_fin
        '''


        np_interpolated_dic=dict()
        
        #datetime64
        time_tt=np.array(df.index.unique())
        print ("time_tt",time_tt)
        for i in time_tt:
            print ("i,type i",i, type(i))
            #delete existing files
            if os.path.exists("temp_tiff.tiff"): os.remove("temp_tiff.tiff")
            if os.path.exists("temp_csv.csv"): os.remove("temp_csv.csv")
            if os.path.exists("temp_csv.vrt"): os.remove("temp_csv.vrt")

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
            outputBounds=outputBounds,width=width,height=height)
            nn=None

            #open temp_tiff
            src_temp = rs.open("temp_tiff.tiff")
            rast=src_temp.read(1)
            #here we have to change the index (i) to number:



            ###########
            if i in np_interpolated_dic: #to make average if not fits

                np_interpolated_dic[i]=(np_interpolated_dic[i]+rast)/2
            else:
                np_interpolated_dic[i]=rast

            src_temp.close()            

        #store in netcdf
        #time=ds["time"][:].data


        
        ds=netCDF_ds.match_date(new_dic=np_interpolated_dic,preferred_date_interval=preferred_date_interval,new_time_int=interpolation_time_int,ds=ds,var_name=var_name)

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
    
    @staticmethod
    def var_introduction_from_tiffs(ds,folder_dir,var_name,preferred_date_interval):

        import glob
        tifs = glob.glob(os.path.join(folder_dir,"*"))
        rast_dic={}
        #print (tifs)
        for t in tifs:
            date=os.path.splitext(t)[0].split("\\")[-1].split("-")
            d=os.path.splitext(t)[0].split("\\")[-1]
            #print (date,d)
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

        ds=netCDF_ds.match_date(new_dic=rast_dic,preferred_date_interval=preferred_date_interval,new_time_int=date_interval,ds=ds,var_name=var_name)
        return ds

