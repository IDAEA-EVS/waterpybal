import numpy as np
import rasterio as rs
#Input Parameters:

#Ru0 Reserva Util in t0 (this is the main calculation)
#Ru0=35.7
#I1=infilteration in t1
#I1=38.1
#Potential Evapotranspiration in t1
#ETP1=110
#Potential Reserva Util in t1 (comes from soil properties)
#PRu1=65
#---------------

#Output Parameters:

#Real Evapotranspiration in t1
#ETR1
#Deficit in t1
#Def1
#Recharge in t1
#Rec1
#Ru1 Reserva Util in t1
#Ru1
#-----------------------------------------
class balance(object):

    @staticmethod
    def balance_calc_point(Ru0,I1,ETP1,PRu1):
        X1=Ru0+I1-ETP1
        #print ("X1: ",X1)
        if X1>0:
            
            ETR1=ETP1
            Def1=0

            R=X1-PRu1
            #print ("R: ",R)
            if R>0:
                Ru1=PRu1
                Rec1=R
            else:
                Ru1=X1
                Rec1=0
        else:
            ETR1=Ru0+I1
            Def1=-X1
            Ru1=0
            Rec1=0

        return ETR1,Def1,Ru1,Rec1
#-----------------------------------------
#Ru0=np.random.uniform(low=0,high=10,size=(3,3,1))
#I1=np.random.uniform(low=0,high=10,size=(3,3,1))
#ETP1=np.random.uniform(low=0,high=20,size=(3,3,1))
#PRu1=np.random.uniform(low=0,high=10,size=(3,3,1))
#-----------------------------------------

    @staticmethod
    def balance_calc_arr(Ru0,I1,ETP1,PRu1):

        #build the output vars:
        ETR1=np.zeros(Ru0.shape)
        Def1=np.zeros(Ru0.shape)
        Ru1=np.zeros(Ru0.shape)
        Rec1=np.zeros(Ru0.shape)
        ####
        X1=Ru0+I1-ETP1

        X1_bool=X1>0 #True means x1>0

        ETR1[X1_bool]=ETP1[X1_bool]
        #Def1=0

        x1_nan=np.empty(Ru0.shape)
        x1_nan[~X1_bool]=np.nan
        x1_nan[X1_bool]=X1[X1_bool]
        R=x1_nan-PRu1 #R is a matrix with nan when 
        
        #if R>0 &x1>0:
        R_bool=R>0 #R_bool=~R_bool is not correct since it interferes with x1_nan s.
        Ru1[R_bool]=PRu1[R_bool]

        Rec1[R_bool]=R[R_bool]
        #else:
        R_bool=R<=0
        Ru1[R_bool]=X1[R_bool]
        #Rec1=0
        
        #else #True means x1<0:
        X1_bool=~X1_bool
        
        ETR1[X1_bool]=Ru0[X1_bool]+I1[X1_bool]
        Def1[X1_bool]=-1*X1[X1_bool]
        #Ru1=0
        #Rec1=0

        return ETR1,Def1,Ru1,Rec1

#-----------------------------------------
    #ETR1,Def1,Ru1,Rec1=balance_calc_arr(Ru0,I1,ETP1,PRu1)
    @staticmethod
    def balance_calculation_main (ds,predef_ru_dir_or_np,predef_ru_type='raster'):
        #Append data to the variables
        time_steps=[ n for n in range(0,len(ds["time"][:].data))]
        
        bal_res=[]

        if predef_ru_type=="raster":
            rast=rs.open(predef_ru_dir_or_np)
            predef_ru_dir_or_np=rast.read(1)


        for time_t in time_steps:
            if time_t!= 0: Ru_Val=ds["Ru_Val"][time_t-1,:,:].data
            else: Ru_Val=predef_ru_dir_or_np
            PRu_Val=ds["PRu_Val"][time_t,:,:].data
            INF_Val=ds["INF_Val"][time_t,:,:].data
            ETP_Val=ds["ETP_Val"][time_t,:,:].data

            bal_res.append(balance.balance_calc_arr(Ru_Val,INF_Val,ETP_Val,PRu_Val)) #calculate balance in each point
                
        #append to NETCDF
        for time_t in time_steps:
            for c,i in enumerate(["ETR_Val","Def_Val","Ru_Val","Rec_Val"]):
                
                ds[i][time_t,:,:]=bal_res[time_t][c]
        
        return ds     
