import numpy as np
import rasterio as rs

#-----------------------------------------
class tools():
    '''
        Contains methods to be used individually or on balance class
    '''
    @staticmethod
    def balance_calc_point(Ru0,I1,PET1,SWR1):
        X1=Ru0+I1-PET1
        #print ("X1: ",X1)
        if X1>0:
            
            ETR1=PET1
            Def1=0

            R=X1-SWR1
            #print ("R: ",R)
            if R>0:
                Ru1=SWR1
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
    #PET1=np.random.uniform(low=0,high=20,size=(3,3,1))
    #SWR1=np.random.uniform(low=0,high=10,size=(3,3,1))
    #-----------------------------------------
    #Ru0=np.array([48]) #prev time step
    #I1=np.array([2.87])
    #PET1=np.array([0.41])
    #SWR1=np.array([48])
    #-----------------------------------------

    @staticmethod
    #ASWR,INF,PET,SWR
    def balance_calc_arr(Ru0,I1,PET1,SWR1):

        #build the output vars:
        ETR1=np.zeros(Ru0.shape)
        Def1=np.zeros(Ru0.shape)
        Ru1=np.zeros(Ru0.shape)
        Rec1=np.zeros(Ru0.shape)
        ####
        X1=Ru0+I1-PET1

        X1_bool=X1>0 #True means x1>0

        ETR1[X1_bool]=PET1[X1_bool]

        x1_nan=np.zeros(Ru0.shape)
        x1_nan[:] = np.nan
        if np.isnan(x1_nan).all()!=True: print ("NOT ALL ZEROS!!")

        x1_nan[X1_bool]=X1[X1_bool]
        R=x1_nan-SWR1 #R is a matrix with nan when 
        #if R>0 &x1>0:
        R_bool=R>0 #R_bool=~R_bool is not correct since it interferes with x1_nan s.
        Ru1[R_bool]=SWR1[R_bool]

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

    @staticmethod
    def urb_inf_no_urb_PET_correction_before_balance(ds):

        urb_inf=ds["URB_INF"][:,:,:].data    
        urb_perc=ds["urban_to_ds_inf_PET_ratio"][:,:,:].data
        urb_inf[urb_inf==-9999]=np.nan
        urb_inf[urb_perc==-9999]=np.nan
        urb_perc[urb_perc==-9999]=np.nan
        inf=ds["INF"][:,:,:].data    
        #to just overwrite the values that are marked as urban area
        pr_true=~np.isnan(urb_perc)
        inf[pr_true]=inf[pr_true] * (1-urb_perc[pr_true]/100) + urb_inf[pr_true] * (urb_perc[pr_true]/100)
        inf=np.nan_to_num(inf,nan=-9999)
        ds["INF"][:,:,:]=inf

        #PET: just the non urban chunk
        pet=ds["PET"][:,:,:].data    
        pet[pr_true]=pet[pr_true] * (1-urb_perc[pr_true]/100)
        pet=np.nan_to_num(pet,nan=-9999)
        ds["PET"][:,:,:]=pet
            
        return ds
    #-----------------------------------------    
    @staticmethod
    def urb_etr_correction_after_balance(ds):

        urb_ep=ds["URB_EP"][:,:,:].data    
        urb_perc=ds["urban_to_ds_inf_PET_ratio"][:,:,:].data
        urb_ep[urb_ep==-9999]=np.nan
        urb_ep[urb_perc==-9999]=np.nan
        urb_perc[urb_perc==-9999]=np.nan
        etr=ds["ETR"][:,:,:].data    
        #to just overwrite the values that are marked as urban area
        pr_true=~np.isnan(urb_perc)
        etr[pr_true]=etr[pr_true] + urb_ep[pr_true] * (urb_perc[pr_true]/100)

        etr=np.nan_to_num(etr,nan=-9999)

        ds["ETR"][:,:,:]=etr
            
        return ds
    #-----------------------------------------    
    def  runoff_calc(ds):
        '''
            ## inf_calcs.infiltration.runoff_calc()

            ds = runoff_calc(ds,Ia=None)

            The method to calculate the runoff in the database. Initial abstraction is None if the
            curve number is not calculated by the waterpybal.
            
            If "runoff" is imported directly to the dataset this method shouldn't to used.



            **Parameters**

                - ds netCDF dataset

                    waterpybal netcdf dataset.
                
                ---
                - Ia    None or numpy array default None

                    Initial abstraction. 
                    If None, runoff= Prec +Irrig - Infilt
                    If not None, runoff= Prec +Irrig - Infilt - Ia
                ---

            **Returns**

                -ds netCDF dataset

                    waterpybal netcdf dataset.
            
            ---
            ---
        '''
        prec=ds["Prec"][:,:,:].data    
        prec[prec==-9999]=np.nan
        
        inf=ds["INF"][:,:,:].data    
        inf[inf==-9999]=np.nan
        
        etr=ds["ETR"][:,:,:].data    
        etr[etr==-9999]=np.nan

        runoff=ds["Irrig"][:,:,:].data+prec-inf-etr

        try:
            ia=ds["Ia"][:,:,:].data
            ia[ia==-9999]=np.nan
            if np.isnan(ia).all():
                pass
                
            else:
                runoff[~np.isnan(ia)]=runoff[~np.isnan(ia)]-ia[~np.isnan(ia)]
            
            '''if ds.urban=="TRUE":
                urb_perc=ds["urban_to_ds_inf_PET_ratio"][:,:,:].data
                urb_runoff=ds["URB_Runoff"][:,:,:].data
                urbtrue=urb_perc!=-9999
                runoff[urbtrue]=runoff[urbtrue] * (1- urb_perc/100 )+ urb_runoff[urbtrue] * (urb_perc/100 )
            '''
        except: #maybe it is not daily so ia not exists
            pass
        runoff[np.isnan(prec)]=-9999
        runoff[np.isnan(inf)]=-9999
        runoff[np.isnan(etr)]=-9999

        runoff=np.nan_to_num(runoff,nan=-9999)
        
        ds["Runoff"][:,:,:]=runoff

        return ds 
#-----------------------------------------
class Balance(object):
    '''
    # class balance_calcs.balance()

    The class to calculate the water balance

    **Methods**

        > ds = balance_calculation_main (ds,predef_ru_dir_or_np,predef_ru_type='raster',init_swr=100)

    ---
    ---
    
    '''

    @staticmethod
    def balance (ds,predef_ru_dir_or_np=None,predef_ru_type='dataset',init_swr=100):
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
        
        if ds.urban=="TRUE":
            ds=tools.urb_inf_no_urb_PET_correction_before_balance(ds)
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
            SWR0= ds["SWR"][0,:,:].data
            predef_ru_dir_or_np=SWR0*float(init_swr)/100
            predef_ru_dir_or_np[SWR0==-9999]=np.nan

        for time_t in time_steps:
            

            if time_t!= 0: Ru_Val=ds["ASWR"][time_t-1,:,:].data
            else: Ru_Val=predef_ru_dir_or_np
            SWR_Val=ds["SWR"][time_t,:,:].data
            INF_Val=ds["INF"][time_t,:,:].data
            PET_Val=ds["PET"][time_t,:,:].data
            
            for j in [Ru_Val,SWR_Val,INF_Val,PET_Val]:
                j[j==-9999]=np.nan

                                            #Ru0,I1,PET1,SWR1
            bal_res=tools.balance_calc_arr(Ru_Val,INF_Val,PET_Val,SWR_Val)

            #append to NETCDF
            #for time_t in time_steps:  #ETR1,Def1,Ru1,Rec1
            for c,i in enumerate(["ETR","Def","ASWR","Rec"]):                

                x=bal_res[c]
                x[np.isnan(SWR_Val)]=np.nan
                x[np.isnan(Ru_Val)]=np.nan
                x[np.isnan(INF_Val)]=np.nan
                x[np.isnan(PET_Val)]=np.nan

                x[np.isnan(x)]=-9999
                ds[i][time_t,:,:]=x
        
        if ds.urban=="TRUE":
            ds=tools.urb_etr_correction_after_balance(ds)
        ds=tools.runoff_calc(ds)
        
        return ds     
