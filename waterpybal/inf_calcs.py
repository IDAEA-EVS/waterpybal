from cmath import sqrt
from turtle import shape
import numpy as np
import pandas as pd
import netCDF4 as nc
import math
#Infiltration function:
#precipitation-runoff (curvenumber)
class infiltration(object):

    def five_day_acc_prec_f(ds,msk):
        #to be used for AMC1 or 2 or 3
        time_steps=[ n for n in range(0,ds["time"].shape[0])]
        #lats=[ n for n in range(0,ds["lat"].shape[0])]
        #lons=[ n for n in range(0,ds["lon"].shape[0])]
        #for lat in lats:
        #    for lon in lons:
        prec_plane=ds["Prec_Val"][:,:,:].data
        prec_plane[prec_plane==-9999]=np.nan
        for time_step in time_steps:
            fdap=0
            #for less than  5 timestep
            
            if time_step<5: lim=time_step
            #other timesteps
            else: lim=5

            for tt in range(1,lim+1):
                fdap=fdap+prec_plane[time_step-tt,:,:]
                #append somewhere
            #to the ds            
            if time_step==0: fdap=prec_plane[0,:,:]
            
            fdap[fdap<-9999]=-9999
            fdap[msk==0]=-9999
            fdap=np.nan_to_num(fdap, nan=-9999)
            ds["five_day_acc_prec"][time_step,:,:]=fdap
        return ds

    #-----------------------------------------
    def CNN(cnt,HSG_,SC_,LU_):
        #HSG: Hydrological soil group A B C D
        #SC: Slope category
        #LU: Land Use
        #dir=r"C:\Users\Ash kan\Documents\watbalpy\cn2.csv"
        #cnt=pd.read_csv(dir) database

        #LU="Woods in poor hydrological condition"
        #SC=3
        #HSG="B"
        print ('str(int(HSG_)),int(SC_),int(LU_)')

        print (str(int(HSG_)),int(SC_),int(LU_))

        return float(cnt[(cnt["Land use code"]==int(LU_)) & (cnt["Slope category"]==int(SC_))][str(int(HSG_))])
    #-----------------------------------------
    def CN_AMC_modded(CN,ds,preferred_date_interval,msk,amc1_coeffs=None,amc3_coeffs=None,dormant_thresh=None,growing_thresh=None,average_thresh=True,mon_list_dormant=None):
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
        five_day_acc_prec_tot=ds["five_day_acc_prec"][:,:,:].data
        five_day_acc_prec_tot[five_day_acc_prec_tot==-9999]=np.nan
        for t in time_steps:
            five_day_acc_prec=five_day_acc_prec_tot[t,:,:]
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
                if np.isnan(prec)==False:
                    #AMC1
                    if prec<thresh[0]: CN_mod=amc1_coeffs[0]*CN_*CN_ + amc1_coeffs[1]*CN_+amc1_coeffs[2]
                    #AMC3
                    elif prec>thresh[1]: CN_mod=amc3_coeffs[0]*CN_*CN_ + amc3_coeffs[1]*CN_+amc3_coeffs[2]
                    #AMC2
                    else: CN_mod=CN_
                else:
                    CN_mod=-9999

                CN_mod_list.append(CN_mod)
            
            CN_mod_t=np.array(CN_mod_list).reshape(xyshape)
            CN_mod_t[msk==0]=-9999
            ds["CN_mod"][t,:,:]=CN_mod_t
        
        return ds

    #-----------------------------------------
    def runoff_infilt_calc(ds,cn_var,advanced_cn,advanced_cn_dic):
        #Ia=0.2*S (Initial abstraction)
        #S (potential max retention) calculation from the curve number
        #Q runoff
        #F infiltration
        ##########
        CN_mod=ds[cn_var][:,:,:].data
        CN_mod[CN_mod==-9999]=np.nan
        ##########
        P=ds["Prec_Val"][:,:,:].data
        P[P==-9999]=np.nan
        ##########
        Irig=ds["Irig_Val"][:,:,:].data       
        Irig[Irig==-9999]=np.nan 
        ##########
        P_Irig=P+Irig
        ##########
        #calculate runoff
        if advanced_cn==False:
            S=(25400/CN_mod)-254
            Ia=0.2*S
            ##########
            Q=np.zeros(CN_mod.shape)
            ##########
            P_bool=P_Irig>Ia
            P_bool[P_Irig==np.nan]==False
            P_bool[CN_mod==np.nan]==False
            Q[P_bool]=(P_Irig[P_bool]-Ia[P_bool])*(P_Irig[P_bool]-Ia[P_bool])/(P_Irig[P_bool]+0.8*S[P_bool])
        else:

            S,Q=infiltration.adv_runoff_calc(
                advanced_cn_dic["landa"],
                CN_mod,
                advanced_cn_dic["A"],
                advanced_cn_dic["B"],
                advanced_cn_dic["C"],
                advanced_cn_dic["D"],
                advanced_cn_dic["x"],
                advanced_cn_dic["y"],
                advanced_cn_dic["z"])


        #inf=P-Ia-Q
        inf=P_Irig-Ia-Q
        inf[P_Irig==np.nan]==np.nan
        inf[CN_mod==np.nan]==np.nan
        
        inf=np.nan_to_num(inf,nan=-9999)
        inf[inf<0]=0
        ds["INF_Val"][:,:,:]=inf
        
        return  ds,Ia      
    
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
        slope[dem==-9999]=-9999

        return slope
    
    #-----------------------------------------
    def read_raster_DEM_HSG_LU(raster_dir,HSG_band,LU_band,ELEV_band,DEM_path_or_raster,DEM_or_raster,filled_dep,slope_range_list):
        import rasterio as rs
        if slope_range_list==None: slope_range_list=[1,5,10,20]
        data=rs.open(raster_dir)
        HSG=data.read(HSG_band)
        LU=data.read(LU_band)
        data_elev=None
        msk = data.read_masks(1)
        if ELEV_band!=None and DEM_or_raster=="raster":
            #elevation as a raster
            data_elev=data.read(ELEV_band)
            SC=infiltration.slope_catagory(DEM_path_or_raster=data_elev,DEM_or_raster="raster",slope_range_list=slope_range_list,filled_dep=filled_dep)
        else:
            #elevation as a dem
            SC=infiltration.slope_catagory(DEM_path_or_raster=DEM_path_or_raster,DEM_or_raster="DEM",slope_range_list=slope_range_list,filled_dep=filled_dep)

        return HSG,SC,LU,msk
    
    #-----------------------------------------

    def Inf_calc(ds,CN_table_dir,raster_dir,HSG_band,LU_band,ELEV_band,DEM_path_or_raster,DEM_or_raster,filled_dep,slope_range_list,amc1_coeffs,amc3_coeffs,dormant_thresh,growing_thresh,average_thresh,mon_list_dormant,preferred_date_interval,corrected_cn,single_cn_val,cn_val,advanced_cn,advanced_cn_dic):  
        

        if single_cn_val==False:
            ds=infiltration.Irig_calc(ds)

            #1-from raster, read HSG, LU,read Slope and calculate slope catagory
            HSG,SC,LU,msk=infiltration.read_raster_DEM_HSG_LU(raster_dir,int(HSG_band),int(LU_band),int(ELEV_band),DEM_path_or_raster,DEM_or_raster,filled_dep,slope_range_list)
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
                if msk_==0 or SC_==-9999: cn_l.append(-9999)
                else: cn_l.append(infiltration.CNN(cnt,HSG_,SC_,LU_))
            CN=np.array(cn_l,dtype='float32').reshape(SC.shape)
            CN_all=np.repeat(CN[np.newaxis,:, : ], ds["time"].shape[0], axis=0)
            ds["CN_Val"][:,:,:]= CN_all
            #---------------
            #calculate five day percs
            if corrected_cn==True:
                ds=infiltration.five_day_acc_prec_f(ds,msk)


        #single cn value defined by user
        else:
            corrected_cn==False
            ds["CN_Val"][:,:,:]=cn_val
        #---------------
        #calculate cn_amc_modded
        if corrected_cn==True:
            infiltration.CN_AMC_modded(CN,ds,preferred_date_interval,msk,amc1_coeffs,amc3_coeffs,dormant_thresh,growing_thresh,average_thresh,mon_list_dormant)
            cn_var="CN_mod"
        else:
            cn_var="CN_Val"


        #calculate infiltr
        ds,Ia=infiltration.runoff_infilt_calc(ds,cn_var,advanced_cn,advanced_cn_dic)
    
         
            
        return ds,Ia

    #-----------------------------------------    
    def max_inf_threshold(ds,var_inp,var_out,threshold):
        if threshold is not None and threshold not in [" ","  ",""]:
            threshold=float(threshold)
            cn=ds[var_inp][:,:,:].data
            cn[cn>threshold]=threshold
            ds[var_out][:,:,:]= cn
        return ds
    
    #-----------------------------------------
    def  runoff_calc(ds,Ia):
        if Ia is not None:
            runoff=ds["Irig_Val"][:,:,:].data+ds["Prec_Val"][:,:,:].data-ds["INF_Val"][:,:,:].data-Ia
        else:
            runoff=ds["Irig_Val"][:,:,:].data+ds["Prec_Val"][:,:,:].data-ds["INF_Val"][:,:,:].data

        runoff[runoff<0]=0
        ds["Runoff_Val"][:,:,:]=runoff

        return ds
    
    #-----------------------------------------
    #zero values of irigation if it is not defined
    def Irig_calc(ds):

        irig=ds["Irig_Val"][:,:,:].data
        P=ds["Prec_Val"][:,:,:].data
        # if irigation var is empty
        if np.all(irig==-9999):
            irig=np.zeros(irig.shape)
        

            irig[P==-9999]=-9999

        ds["Irig_Val"][:,:,:]=irig

        return ds

    #-----------------------------------------
    #advanced runoff calculation
    def adv_runoff_calc(landa,CN_mod,A,B,C,D,x,y,z):
        #SCS-CN METHOD REVISITED S.K. Mishra1, P. Suresh Babu2, V.P. Singh3
        #formulas calculated by ashkan for this function
        #Equation (2.12) is valid for P ≥ Ia, Q = 0 otherwise.
        #proposed solution between Q and S: user defined polynomial-like function

        #--------------------
        
        #calculate S from CN
        S= A * np.power(CN_mod,x) + B * np.power(CN_mod,y) + C * z + D

        #calculate Q

        numerator= 2*landa * ( S * landa -1)
        
        denominator= 1- landa - 2 *  math.sqrt( landa )

        Q= numerator/denominator

        if Q<0: Q=0

        return S,Q
        

