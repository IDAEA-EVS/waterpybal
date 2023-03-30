import numpy as np
import pandas as pd
import netCDF4 as nc
import math
#Infiltration function:
#precipitation-runoff (curvenumber)
class infiltration_functions(object):
    '''
        The class containing the methods to use in infiltration class 
    '''
    def five_day_acc_prec_f(ds,msk):
        #to be used for AMC1 or 2 or 3
        time_steps=[ n for n in range(0,ds["time"].shape[0])]
        #lats=[ n for n in range(0,ds["lat"].shape[0])]
        #lons=[ n for n in range(0,ds["lon"].shape[0])]
        #for lat in lats:
        #    for lon in lons:
        prec_plane=ds["Prec"][:,:,:].data
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
        #print ('str(int(HSG_)),int(SC_),int(LU_)')

        #print (str(int(HSG_)),int(SC_),int(LU_))

        return float(cnt[(cnt["Land use code"]==int(LU_)) & (cnt["Slope category-Hydrologic condition"]==int(SC_))][int(HSG_)])
    #-----------------------------------------
    def CN_AMC_modded(CN,ds,msk,amc1_coeffs=None,amc3_coeffs=None,dormant_thresh=None,growing_thresh=None,average_thresh=True,mon_list_dormant=None):
        #CN,ds,amc1_coeffs=None,amc3_coeffs=None,dormant_thresh=None,growing_thresh=None,average_thresh=True,mon_list_dormant=None
        if amc1_coeffs==None: amc1_coeffs=[0.0069,0.2575,0]
        if amc3_coeffs==None: amc3_coeffs=[-0.0086,1.8338,0]
        if dormant_thresh==None: dormant_thresh=[12.7,27.9]
        if growing_thresh==None: growing_thresh=[36.6,53.3]
        if mon_list_dormant==None:mon_list_dormant=[10,11,12,1,2,3]
        
        time_steps=[ n for n in range(0,ds["time"].shape[0])]
        
        preferred_date_interval=ds.date_interval

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
    def infilt_runoff__calc(ds,cn_var,advanced_cn,advanced_cn_dic):
        #Ia=0.2*S (Initial abstraction)
        #S (potential max retention) calculation from the curve number
        #Q runoff
        #F infiltration
        ##########
        CN_mod=ds[cn_var][:,:,:].data
        CN_mod[CN_mod==-9999]=np.nan
        ##########
        P=ds["Prec"][:,:,:].data
        P[P==-9999]=np.nan
        ##########
        Irrig=ds["Irrig"][:,:,:].data       
        Irrig[Irrig==-9999]=np.nan 
        ##########
        P_Irrig=P+Irrig
        ##########
        #calculate runoff
        if advanced_cn==False:
            S=(25400/CN_mod)-254
            landa=0.2
 
        else:
            S,landa=infiltration_functions.adv_runoff_calc(
                advanced_cn_dic["landa"],
                CN_mod,
                advanced_cn_dic["A"],
                advanced_cn_dic["B"],
                advanced_cn_dic["C"],
                advanced_cn_dic["D"],
                advanced_cn_dic["x"],
                advanced_cn_dic["y"],
                advanced_cn_dic["z"])
        ##########
        Ia=landa*S
        Ia[Ia<0]=0
        Q=np.zeros(CN_mod.shape)
        ##########
        P_bool=P_Irrig>Ia #to calculate if P>Ia if not, zero
        P_bool[np.isnan(P_Irrig)]==False
        P_bool[np.isnan(CN_mod)]==False
        Q[P_bool]=(P_Irrig[P_bool]-Ia[P_bool])*(P_Irrig[P_bool]-Ia[P_bool])/(P_Irrig[P_bool]-Ia[P_bool]+S[P_bool])
        #Q[~P_bool]=np.nan
        Q[Q<0]=0
        
        #inf=P-Ia-Q
        inf=P_Irrig-Ia-Q
        print ("inf in runoff inf cal 0",np.count_nonzero(inf==0))
        inf[inf<0]=0
        print ("inf in runoff inf cal 0 after",np.count_nonzero(inf==0))

        inf[np.isnan(P)]=np.nan
        inf[np.isnan(CN_mod)]=np.nan
        inf=np.nan_to_num(inf,nan=-9999)
        print ("inf in runoff inf cal 9999 2",np.count_nonzero(inf==-9999))
        print ("inf in runoff inf cal 0 2",np.count_nonzero(inf==0))
        ds["INF"][:,:,:]=inf
        Ia[np.isnan(P)]=np.nan
        Ia[np.isnan(CN_mod)]=np.nan
        Ia=np.nan_to_num(inf,nan=-9999)
        ds["Ia"][:,:,:]=Ia

        
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
        slope[dem==-9999]=-9999

        return slope
    
    #-----------------------------------------
    def read_raster_DEM_HSG_LU(raster_dir,HSG_band,LU_band,ELEV_or_HC_band,DEM_path_or_raster,DEM_or_raster,filled_dep,slope_range_list,SC_or_HC):
        import rasterio as rs
        if slope_range_list==None: slope_range_list=[1,5,10]
        data=rs.open(raster_dir)
        HSG=data.read(HSG_band)
        LU=data.read(LU_band)
        data_elev=None
        msk = data.read_masks(1)
        if SC_or_HC=="SC":
            if ELEV_or_HC_band!=None and DEM_or_raster=="raster":
                #elevation as a raster
                data_elev=data.read(ELEV_or_HC_band)
                SC=infiltration_functions.slope_catagory(DEM_path_or_raster=data_elev,DEM_or_raster="raster",slope_range_list=slope_range_list,filled_dep=filled_dep)
            else:
                #elevation as a dem
                SC=infiltration_functions.slope_catagory(DEM_path_or_raster=DEM_path_or_raster,DEM_or_raster="DEM",slope_range_list=slope_range_list,filled_dep=filled_dep)
        else:
            SC=data.read(ELEV_or_HC_band)


        return HSG,SC,LU,msk
    

    #-----------------------------------------
    #zero values of Irrigation if it is not defined
    def Irrig_calc(ds):

        Irrig=ds["Irrig"][:,:,:].data
        P=ds["Prec"][:,:,:].data
        # if Irrigation var is empty
        if np.all(Irrig==-9999):
            Irrig=np.zeros(Irrig.shape)
        

            Irrig[P==-9999]=-9999

        ds["Irrig"][:,:,:]=Irrig

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
        S= A * np.power(CN_mod,x) + B * np.power(CN_mod,y) + C * np.power(CN_mod,z)  + D

        return S,landa
        
    #-----------------------------------------

class Infiltration(object):
    '''
    # class inf_calcs.infiltration()
    The class to calculate the infiltration

    **Methods**

        > ds= inf(ds,CN_table_dir,raster_dir,HSG_band,LU_band,ELEV_or_HC_band,corrected_cn=False, single_cn_val=False,cn_val=None,advanced_cn_dic=None,advanced_cn=False, filled_dep=True, slope_range_list=None, amc1_coeffs=None, amc3_coeffs=None, dormant_thresh=None, growing_thresh=None, average_thresh=False, mon_list_dormant=None, SC_or_HC="HC", DEM_or_raster="raster" ,DEM_path_or_raster=None)
                
        > ds = max_inf_threshold(ds,var_inp,var_out,threshold)
        
    ---
    ---

    '''
    def inf(ds,CN_table_dir,raster_dir,HSG_band,LU_band,ELEV_or_HC_band,corrected_cn=False, single_cn_val=False,cn_val=None,advanced_cn_dic=None,advanced_cn=False, filled_dep=True, slope_range_list=None, amc1_coeffs=None, amc3_coeffs=None, dormant_thresh=None, growing_thresh=None, average_thresh=False, mon_list_dormant=None, SC_or_HC="HC", DEM_or_raster="raster" ,DEM_path_or_raster=None):  
        '''
            ## inf_calcs.infiltration.Inf_calc()

            ds = inf(ds,CN_table_dir,raster_dir,HSG_band,LU_band,ELEV_or_HC_band,corrected_cn=False, single_cn_val=False,cn_val=None,advanced_cn_dic=None,advanced_cn=False, filled_dep=True, slope_range_list=None, amc1_coeffs=None, amc3_coeffs=None, dormant_thresh=None, growing_thresh=None, average_thresh=False, mon_list_dormant=None, SC_or_HC="HC", DEM_or_raster="raster" ,DEM_path_or_raster=None)

            The method to calculate the infiltration


            **Parameters**

                -ds netCDF dataset

                    waterpybal netcdf dataset.

                ---
                CN_table_dir str

                    Path to the curve number xls table
                ---
                raster_dir str

                    The multiband raster path, containing the HSG_band,LU_band and ELEV_or_HC_band

                ---
                HSG_band int
                    Hydrologic Soil Group raster band

                ---
                LU_band int

                    Land Use Group raster band

                ---
                ELEV_or_HC_band int

                    Elevation (Slope) Catagory or Hydrologic Condition raster band 

                ---
                DEM_path_or_raster None or str

                    Path to the DEM to calculate the Slope catagories. If there is no slope catagory in the curve number table (Hydrologic condition), ir the elevations 
                    are introduced as a band in the multibandraster instead of a DEM, DEM_path_or_raster have to be None

                ---
                DEM_or_raster str default "raster"

                    "raster" or "DEM". If *SC_or_HC* is "HC", DEM_or_raster will be ignored.

                ---
                filled_dep default True

                    If to Fill Depressions in calculating elevations or not. If *SC_or_HC* is "HC", it will be ignored.

                ---
                slope_range_list None or list default None

                    If None, slope_range_list=[1,5,10]. List of boundaries of the Slope Catagories.


                ---
                amc1_coeffs None or list default None

                    If None, amc1_coeffs=[0.0069,0.2575,0]. Coefficient of Antecedent Moisture Condition (AMC) 1 Formula as a list.

                ---
                amc3_coeffs None or list default None

                    If None, amc1_coeffs=[-0.0086,1.8338,0]. Coefficient of Antecedent Moisture Condition (AMC) 3 Formula as a list.

                ---
                dormant_thresh None or list default None

                    If None, dormant_thresh=[12.7,27.9]. Dormant months AMC1 and AMC3 thresholds.

                ---
                growing_thresh None or list default None

                    If None, growing_thresh=[36.6,53.3]. Growing months AMC1 and AMC3 thresholds.

                ---
                average_thresh bool default False

                    To use an average of growing and dormant months to identify AMC1 and AMC3.

                ---
                mon_list_dormant None or list default None
                
                    if None, mon_list_dormant=[10,11,12,1,2,3]. List of dormant month. Rest of the month will be growing month.

                ---
                corrected_cn bool default False

                    If the Antecedent Moisture Condition (AMC) corrections have to be applied

                ---
                single_cn_val bool default False

                    To use a single CN value for the whole dataset
                ---
                cn_val None or float default None

                    single CN value. Ignored if single_cn_val is False


                ---
                advanced_cn bool default False

                    If the advanced curve number options are gonna be used. The variables are defined in advanced_cn_dic

                ---
                advanced_cn_dic None or dic default None
                    A dictionary to change the Ia and the formula of the curve number, containing the following keys and their respective values:
                    
                    advanced_cn_dic.keys(): "landa", "A","B","C","D","x","y","z"

                    Formulas:
                        
                        S= A * CN_mod^x + B * CN_mod^y + C * CN_mod^z + D

                        S= landa * Ia



                ---
                SC_or_HC str default "HC"

                    If Hydrologic Condition (default) or Slope Catagory (SC) is defined in the curve number table

                ---

            **Returns**

                -ds netCDF dataset

                    waterpybal netcdf dataset.

                ---
                ---
        
        '''

        if single_cn_val==False:
            
            ds=infiltration_functions.Irrig_calc(ds)

            #1-from raster, read HSG, LU,read Slope and calculate slope catagory
            HSG,SC,LU,msk=infiltration_functions.read_raster_DEM_HSG_LU(raster_dir,int(HSG_band),int(LU_band),int(ELEV_or_HC_band),DEM_path_or_raster,DEM_or_raster,filled_dep,slope_range_list,SC_or_HC=SC_or_HC)
            #---------------
            # 2-read cn table db   for each point of the raster (array)
            #CN_table_dir=r"C:\Users\Ash kan\Documents\watbalpy\cn2.csv"
            cnt=pd.read_excel(CN_table_dir)
            #LU=np.array(cnt[["Land use"]])[:9].reshape(3,3,1)
            #Ru0=np.random.uniform(low=0,high=10,size=(3,3,1))
            #SC=np.random.randint(low=1,high=5,size=(3,3,1))
            #HSG=np.array([["A","D","B"],["C","B","C"],["A","C","A"]])
            cn_l=list()
            for HSG_,SC_,LU_,msk_ in zip(HSG.flat,SC.flat,LU.flat,msk.flat):
                if msk_==0 or SC_==-9999: cn_l.append(-9999)
                else: cn_l.append(infiltration_functions.CNN(cnt,HSG_,SC_,LU_))
            CN=np.array(cn_l,dtype='float32').reshape(SC.shape)
            CN_all=np.repeat(CN[np.newaxis,:, : ], ds["time"].shape[0], axis=0)
            ds["CN"][:,:,:]= CN_all
            #---------------
            #calculate five day percs
            if corrected_cn==True:
                ds=infiltration_functions.five_day_acc_prec_f(ds,msk)


        #single cn value defined by user
        else:
            ds=infiltration_functions.Irrig_calc(ds)
            corrected_cn=False
            temp_arr=np.full(ds["Prec"].shape,cn_val)
            P=ds["Prec"][:,:,:].data
            temp_arr[P==-9999]=-9999
            ds["CN"][:,:,:]=temp_arr
        #---------------
        #calculate cn_amc_modded
        if corrected_cn==True:
            ds=infiltration_functions.CN_AMC_modded(CN,ds,msk,amc1_coeffs,amc3_coeffs,dormant_thresh,growing_thresh,average_thresh,mon_list_dormant)
            cn_var="CN_mod"
        else:
            cn_var="CN"


        #calculate infiltr
        ds=infiltration_functions.infilt_runoff__calc(ds,cn_var,advanced_cn,advanced_cn_dic)
    
         
            
        return ds

   

    #-----------------------------------------
    def max_inf_threshold(ds,var_inp,var_out,threshold):
        '''
            ## inf_calcs.infiltration.max_inf_threshold()

            ds = max_inf_threshold(ds,var_inp,var_out,threshold)

            The method to force a threshold to an specific variable. Normally used for "INF"
            to limit maximum infiltration values.

            **Parameters**

                - ds netCDF dataset

                    waterpybal netcdf dataset.
                
                ---
                - var_inp str

                    Input variable to limit. "INF" is used normally.
                ---
                - var_out str

                    Out variable to save the variable. "INF" or "Prec" is used normally.
                ---
                - threshold float

                    threshold value
                ---

            **Returns**

                -ds netCDF dataset

                    waterpybal netcdf dataset.
            
            ---
            ---
        '''

        if threshold is not None and threshold not in [" ","  ",""]:
            threshold=float(threshold)
            cn=ds[var_inp][:,:,:].data
            cn[cn>threshold]=threshold
            ds[var_out][:,:,:]= cn
        return ds
    
    #-----------------------------------------
