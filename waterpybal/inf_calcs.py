from turtle import shape
import numpy as np
import pandas as pd
import netCDF4 as nc
#Infiltration function:
#precipitation-runoff (curvenumber)
class infiltration(object):

    def five_day_acc_prec(ds):
        #to be used for AMC1 or 2 or 3
        time_steps=[ n for n in range(0,ds["time"].shape[0])]
        #lats=[ n for n in range(0,ds["lat"].shape[0])]
        #lons=[ n for n in range(0,ds["lon"].shape[0])]
        #for lat in lats:
        #    for lon in lons:
        prec_plane=ds["Prec_Val"].data
        for t in time_steps:
            fdap=0
            #for less than  5 timestep
            if t<5: lim=t
            #other timesteps
            else: lim=5

            for tt in range(1,lim+1):
                fdap=fdap+prec_plane[t-tt,:,:]
                #append somewhere
            #to the ds
            fdap[fdap<-9999]=-9999
            ds["five_day_acc_prec"][t,:,:]=fdap
        ds

    #-----------------------------------------
    def CNN(cnt,HSG,SC,LU):
        #HSG: Hydrological soil group A B C D
        #SC: Slope category
        #LU: Land Use
        #dir=r"C:\Users\Ash kan\Documents\watbalpy\cn2.csv"
        #cnt=pd.read_csv(dir) database

        #LU="Woods in poor hydrological condition"
        #SC=3
        #HSG="B"

        return float(cnt[(cnt["Land use code"]==LU) & (cnt["Slope category"]==SC)][HSG])
    #-----------------------------------------
    def CN_AMC_modded(CN,ds,preferred_date_interval,amc1_coeffs=None,amc3_coeffs=None,dormant_thresh=None,growing_thresh=None,average_thresh=True,mon_list_dormant=None):
        #CN,ds,amc1_coeffs=None,amc3_coeffs=None,dormant_thresh=None,growing_thresh=None,average_thresh=True,mon_list_dormant=None
        if amc1_coeffs==None: amc1_coeffs=[0.0069,0.2575,0]
        if amc3_coeffs==None: amc3_coeffs=[-0.0086,1.8338,0]
        if dormant_thresh==None: dormant_thresh=[12.7,27.9]
        if growing_thresh==None: growing_thresh=[36.6,53.3]
        if mon_list_dormant==None:mon_list_dormant=[10,11,12,1,2,3]
        
        time_steps=[ n for n in range(0,ds["time"].shape[0])]
        
        if preferred_date_interval=='datetime64[h]': time_str= 'minutes'
        elif preferred_date_interval=='datetime64[D]': time_str= 'hours'
        elif preferred_date_interval=='datetime64[M]': time_str= 'days'

        time_str=time_str+" since 1970-01-01 00:00:00"
        
        time=ds["time"][:].data

        time=nc.num2date(time,time_str,only_use_cftime_datetimes=False,only_use_python_datetimes=True)
        
        if average_thresh==True:
            thresh=[(dormant_thresh[0]+growing_thresh[0])/2,(dormant_thresh[1]+growing_thresh[1])/2]
        

        xyshape=ds["five_day_acc_prec"][0,:,:].data.shape
        for t in time_steps:
            five_day_acc_prec=ds["five_day_acc_prec"][t,:,:]
            five_day_acc_prec[five_day_acc_prec==-9999]=np.nan
            if average_thresh==True:
                pass

            else: #average_thresh==False
                mon=time[t].month #extract a month array of the time ds
                
                if mon in mon_list_dormant:
                    thresh=dormant_thresh
                else:
                    thresh=growing_thresh
            CN_mod_list=list()
            for prec,CN_ in zip(five_day_acc_prec.flat,CN.flat):
                if np.isnan(prec)!=False:
                    #AMC1
                    if prec<thresh[0]: CN_mod=amc1_coeffs[0]*CN_^2 + amc1_coeffs[1]*CN_+amc1_coeffs[2]
                    #AMC3
                    elif prec>thresh[1]: CN_mod=amc3_coeffs[0]*CN_^2 + amc3_coeffs[1]*CN_+amc3_coeffs[2]
                    #AMC2
                    else: CN_mod=CN_
                else:
                    CN_mod=-9999

                CN_mod_list.append(CN_mod)

            ds["CN_mod"][t,:,:]=np.array(CN_mod_list).reshape(xyshape)
        
        return ds

    #-----------------------------------------
    def runoff_infilt_calc(ds):
        #Ia=0.2*S (Initial abstraction)
        #S (potential max retention) calculation from the curve number
        #Q runoff
        #F infiltration
        CN_mod=ds["CN_mod"].data
        P=ds["Prec_Val"].data
        S=(25400/CN_mod)-254
        
        Q=np.zeros(CN_mod.shape)

        P_bool=P>0.2*S

        Q[P_bool]=(P[P_bool]-0.2*S[P_bool])^2/(P[P_bool]+0.8*S[P_bool])

        #inf=P-Ia-Q
        inf=P-0.2*S-Q
        #inf[inf<0]=0
        inf[P==-9999]=-9999
        ds["INF_Val"]=inf
        
        return  ds      
    
    #-----------------------------------------
    @staticmethod
    def slope_catagory(DEM_path_or_raster,slope_range_list,DEM_or_raster,filled_dep): #DEM_or_raster="DEM" or "raster"
        
        import richdem as rd
        if DEM_or_raster=="DEM":
            #DEM_path=r"C:\Users\Ash kan\Documents\watbalpy\test.dem"
            #DEM_path=r'Downloads\s2a_l2a_fishbourne.tif'
            dem = rd.LoadGDAL(DEM_path_or_raster, no_data=-9999)
        if DEM_or_raster=="raster":
            dem=rd.rdarray(DEM_path_or_raster,no_data=-9999)

        if filled_dep==True:
            rd.FillDepressions(dem, in_place=True)
        slope = rd.TerrainAttribute(dem, attrib='slope_percentage')
        slope=np.array(slope)


        len_slope_list=len(slope_range_list)

        for count in range(0,len_slope_list):
            #first slope catagory
            if count==0:
                slope[slope<slope_range_list[count]]=-1
            else:
                slope[ (slope>slope_range_list[count-1]) & (slope<slope_range_list[count])  ]=-1*(count+1)
        #last slope catagory
        slope[slope>slope_range_list[-1]]=-1*(len_slope_list+1)
        slope=-1*slope

        return slope
    
    #-----------------------------------------
    def read_raster_DEM_HSG_LU(raster_dir,HSG_band,LU_band,ELEV_band,DEM_path,DEM_or_raster,filled_dep,slope_range_list):
        import rasterio as rs
        if slope_range_list==None: slope_range_list=[1,5,10,20]
        data=rs.open(raster_dir)
        HSG=data.read(HSG_band)
        LU=data.read(LU_band)
        data_elev=None
        if ELEV_band!=None and DEM_or_raster=="raster":
            #elevation as a raster
            data_elev=data.read(ELEV_band)
            SC=infiltration.slope_catagory(DEM_path_or_raster=data_elev,DEM_or_raster="raster",slope_range_list=slope_range_list,filled_dep=filled_dep)
        else:
            #elevation as a dem
            SC=infiltration.slope_catagory(DEM_path_or_raster=DEM_path,DEM_or_raster="DEM",slope_range_list=slope_range_list,filled_dep=filled_dep)

        return HSG,SC,LU
    
    #-----------------------------------------

    def Inf_calc(ds,CN_table_dir,raster_dir,HSG_band,LU_band,ELEV_band,DEM_path_or_raster,DEM_or_raster,filled_dep,slope_range_list,amc1_coeffs,amc3_coeffs,dormant_thresh,growing_thresh,average_thresh,mon_list_dormant,preferred_date_interval):  
        
        #1-from raster, read HSG, LU,read Slope and calculate slope catagory
        HSG,SC,LU,msk=infiltration.read_raster_DEM_HSG_LU(raster_dir,HSG_band,LU_band,ELEV_band,DEM_path_or_raster,DEM_or_raster,filled_dep,slope_range_list)
        #---------------
        # 2-read cn table db   for each point of the raster (array)
        #CN_table_dir=r"C:\Users\Ash kan\Documents\watbalpy\cn2.csv"
        cnt=pd.read_csv(CN_table_dir)
        #LU=np.array(cnt[["Land use"]])[:9].reshape(3,3,1)
        #Ru0=np.random.uniform(low=0,high=10,size=(3,3,1))
        #SC=np.random.randint(low=1,high=5,size=(3,3,1))
        #HSG=np.array([["A","D","B"],["C","B","C"],["A","C","A"]])
        cn_l=list()
        for HSG_,SC_,LU_,msk_ in zip(HSG.flat,SC.flat,LU.flat,msk.flat):
            if msk_==0: cn_l.append(-9999)
            else: cn_l.append(infiltration.CNN(cnt,HSG_,SC_,LU_))
        CN=np.array(cn_l).reshape(SC.shape)
        
        ds["CN_Val"]= np.repeat(CN[np.newaxis,:, : ], ds["time"].shape[0], axis=0)
        #---------------
        #calculate five day percs
        ds=infiltration.five_day_acc_prec(ds)
        #---------------
        #calculate cn_amc_modded
        infiltration.CN_AMC_modded(CN,ds,preferred_date_interval,amc1_coeffs,amc3_coeffs,dormant_thresh,growing_thresh,average_thresh,mon_list_dormant)
        #calculate infiltr
        ds=infiltration.runoff_infilt_calc(ds)


        return ds
    
