import numpy as np
import rasterio as rs

#-----------------------------------------
class tools():
    '''
        Contains methods to be used individually or on balance class
    '''
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
    #Ru0=np.array([48]) #prev time step
    #I1=np.array([2.87])
    #ETP1=np.array([0.41])
    #PRu1=np.array([48])
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

        x1_nan=np.zeros(Ru0.shape)
        x1_nan[:] = np.nan
        if np.isnan(x1_nan).all()!=True: print ("NOT ALL ZEROS!!")

        x1_nan[X1_bool]=X1[X1_bool]
        R=x1_nan-PRu1 #R is a matrix with nan when 
        #if R>0 &x1>0:
        R_bool=R>0 #R_bool=~R_bool is not correct since it interferes with x1_nan s.
        Ru1[R_bool]=PRu1[R_bool]

        Rec1[R_bool]=R[R_bool]
        #else:
        R_bool=R<=0
        Ru1[R_bool]=X1[R_bool]
        
        #else #True means x1<0:
        X1_bool=~X1_bool
        
        ETR1[X1_bool]=Ru0[X1_bool]+I1[X1_bool]
        Def1[X1_bool]=-1*X1[X1_bool]

        

        return [ETR1,Def1,Ru1,Rec1]


#-----------------------------------------
class balance(object):
    '''
    # class balance_calcs.balance()

    The class to calculate the water balance

    **Methods**

        > ds = balance_calculation_main (ds,predef_ru_dir_or_np,predef_ru_type='raster',init_swr=100)

    ---
    ---
    
    '''

    @staticmethod
    def balance_calculation_main (ds,predef_ru_dir_or_np=None,predef_ru_type='dataset',init_swr=100):
        '''
        ## balance_calcs.balance.balance_calculation_main ()
        
            ds = balance_calculation_main (ds,predef_ru_dir_or_np,predef_ru_type='raster',init_swr=100)
        
            The method to calculate the water balance from the variables that are calculated using waterpybal.


            **Parameters**

                - ds netCDF dataset

                    waterpybal netcdf dataset.

                ---     
                - predef_ru_dir_or_np None numpy array or str default None

                    Defines the SWR preliminary values.
                    None if it is iqual to the first step of the dataset.
                    str if it is a path to a raster.
                    A 2D numpy array if it is defined using an array.
                
                ---
                - predef_ru_type str default 'dataset'

                    Defines the SWR preliminary values type. 
                    'raster', 'np' or 'dataset'.
                
                ---
                - init_swr=100   

                    The percentage of the preliminary SWR values that is saturated.
                ---

            **Returns**

                -ds netCDF dataset

                    waterpybal netcdf dataset.
            
            ---
            ---
        '''
        
        
        
        #Append data to the variables
        time_steps=[ n for n in range(0,len(ds["time"][:].data))]
        

        if predef_ru_type=="raster":
            rast=rs.open(predef_ru_dir_or_np)
            predef_ru_dir_or_np=rast.read(1)
            msk = rast.read_masks(1)
            rast=rast.astype(np.float32)
            rast[msk==0]=np.nan
            rast.close()

        if predef_ru_type=="dataset":
            pru0= ds["PRu_Val"][0,:,:].data
            predef_ru_dir_or_np=pru0*float(init_swr)/100
            predef_ru_dir_or_np[pru0==-9999]=np.nan

        for time_t in time_steps:
            

            if time_t!= 0: Ru_Val=ds["Ru_Val"][time_t-1,:,:].data
            else: Ru_Val=predef_ru_dir_or_np
            PRu_Val=ds["PRu_Val"][time_t,:,:].data
            INF_Val=ds["INF_Val"][time_t,:,:].data
            ETP_Val=ds["ETP_Val"][time_t,:,:].data
            
            for j in [Ru_Val,PRu_Val,INF_Val,ETP_Val]:
                j[j==-9999]=np.nan

                                            #Ru0,I1,ETP1,PRu1
            bal_res=tools.balance_calc_arr(Ru_Val,INF_Val,ETP_Val,PRu_Val)

            #append to NETCDF
            #for time_t in time_steps:  #ETR1,Def1,Ru1,Rec1
            for c,i in enumerate(["ETR_Val","Def_Val","Ru_Val","Rec_Val"]):                

                x=bal_res[c]
                x[np.isnan(PRu_Val)]=np.nan
                x[np.isnan(Ru_Val)]=np.nan
                x[np.isnan(INF_Val)]=np.nan
                x[np.isnan(ETP_Val)]=np.nan

                x[np.isnan(x)]=-9999
                ds[i][time_t,:,:]=x
        
        return ds     
