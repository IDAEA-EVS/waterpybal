import rasterio as rs
import numpy as np




class urban_infiltration_calcs():
    

    # inputs:
    
    #precipitation mm  prec
    #irrigation mm irrig
    #water consumption mm wat_cons
    #water supply that are not flowing through network mm wat_supp_wells
    #wat_supp_wells loss  % wat_supp_wells_loss
    #water from other sources that finish in the sewer mm wat_other (groundwater drains, basements,etc...) (we assume this par doesn't have a loss)
    #water network loss (%)    wat_net_loss
    #urban direct evaporation (%) urb_dir_evap (percentage of water precipitation+irrigation)
    #urban indirect evaporation (%) urb_indir_evap (percentage of water consumption)
    #sewage network loss (%) sew_net_loss_low
    #sewage network loss (%) sew_net_loss_high
    #run-off urban catchments to sewage (%)  runoff_to_sewage
    #direct infiltration (%) dir_infil (percentage of water precipitation+irrigation)


    

    ###############
    def urban_infiltration_np(prec,irrig,wat_cons,wat_net_loss,urb_dir_evap,urb_indir_evap,sew_net_loss_low,sew_net_loss_high,prec_sewage_threshold,runoff_to_sewage,dir_infil,wat_supp_wells,wat_supp_wells_loss,wat_other):

        irrig[irrig==-9999]=0
        prec[prec==-9999]=0
        #####
        val_wat_net_loss_infiltration=wat_cons*(wat_net_loss/100)
        
        val_wat_cons=wat_cons*(1-wat_net_loss/100)
        
        #####

        val_wat_supp_wells_loss=wat_supp_wells*(wat_supp_wells_loss/100)
        
        val_wat_supp_wells=wat_supp_wells*(1-wat_supp_wells_loss/100)

        #####

        #val_sewage_input_before_runoff from water network and wells after indirect evaporation
        val_sewage_input_before_runoff=(val_wat_cons+val_wat_supp_wells)*(1-urb_indir_evap/100)

        #val_runoff_to_sewage from prec and irrig
        val_runoff_to_sewage=(prec+irrig)*(1-urb_dir_evap/100)*(runoff_to_sewage/100)
        
        
        
        sew_input=val_sewage_input_before_runoff+val_runoff_to_sewage + wat_other

        val_sew_net_out,val_sew_net_loss_infiltration=urban_infiltration_calcs.sewage_loss(sew_net_loss_low,sew_net_loss_high,sew_input,prec,prec_sewage_threshold)

        
        val_dir_infil=(prec+irrig)*(dir_infil/100)

        in_out_water_delta=wat_cons+prec+irrig+ wat_supp_wells+ wat_other -val_sew_net_out
        
        #total_infiltration= water supply network loss + wells loss+ sewer los + direct infiltration from perc and irrig +
        total_infiltration=val_wat_net_loss_infiltration + val_wat_supp_wells_loss + val_sew_net_loss_infiltration + val_dir_infil

        #total_evapotranspiration= indirect urban evap (from water network and wells) + direc evap of prec and irrig
        total_evapotranspiration= (val_wat_cons+val_wat_supp_wells) * (urb_indir_evap/100) + (prec+irrig)*(urb_dir_evap/100) 
        

        total_runoff= in_out_water_delta - total_infiltration - total_evapotranspiration
        
        total_runoff[total_runoff<0]=0

        return total_infiltration,total_evapotranspiration,total_runoff
    
    ###############
    def sewage_loss(sew_net_loss_low,sew_net_loss_high,sew_input,prec,prec_sewage_threshold):
        
        val_sew_net_loss_infiltration=np.zeros_like(prec)
        val_sew_net_out=np.zeros_like(prec)

        low_bool=prec<prec_sewage_threshold
        high_bool=~low_bool

        for bool_lh,sw_net_los in zip([low_bool,high_bool],[sew_net_loss_low,sew_net_loss_high]):
            val_sew_net_loss_infiltration[bool_lh]=sew_input[bool_lh]*(sw_net_los[bool_lh]/100)
            val_sew_net_out[bool_lh]=sew_input[bool_lh]*(1-sw_net_los[bool_lh]/100)


        return  val_sew_net_out,val_sew_net_loss_infiltration
    
    ###############
    def urban_input_raster_or_value(ds,urban_area_raster_dir,variable_name, input_var ,dataset_raster_dir_or_value):


        if ds["lat"].shape[0]==1 and ds["lon"].shape[0]==1:
            urban_raster_np=np.array([[0]])
        else:
            urban_raster_np=urban_infiltration_calcs.read_rast(urban_area_raster_dir)
        
        
        if dataset_raster_dir_or_value=="Raster":
            input_raster_np=urban_infiltration_calcs.read_rast(input_var)
            input_raster_np[np.isnan(urban_raster_np)]=np.nan
        
        
        elif dataset_raster_dir_or_value=="Dataset":
            pass

        else:

            input_raster_np= np.full(urban_raster_np.shape, np.nan) 
            input_raster_np[~np.isnan(urban_raster_np)]=float(input_var)

        ds=urban_infiltration_calcs.inp_to_ds(input_raster_np,ds,variable_name)
        
        return ds
    
    ###############
    def read_rast(raster_dir):
        src=rs.open(raster_dir)
        rast=src.read(1)
        msk = src.read_masks(1)
        rast[msk==0]=np.nan
        src.close()
        return rast
    
    ###############
    def inp_to_ds(input_raster_np,ds,variable_name):


        ds[variable_name][:,:,:]=np.repeat(input_raster_np[np.newaxis,:, : ], ds["time"].shape[0], axis=0)
        
        return ds

    ###############
    def urban_infiltration_main (ds,urban_area_raster_dir,variables_dic):
        
        for k,v in variables_dic.items():
            
            variable_name=k
            input_var=v["input_var"]
            dataset_raster_dir_or_value=v["dataset_raster_dir_or_value"]

            ds=urban_infiltration_calcs.urban_input_raster_or_value(ds,urban_area_raster_dir,variable_name, input_var ,dataset_raster_dir_or_value)
        
        #Append data to the variables
        time_steps=[ n for n in range(0,len(ds["time"][:].data))]

        


        INF_Val_list=[]
        ETP_Val_list=[]
        Runoff_Val_list=[]
        
        urban_to_ds_inf_etp_ratio=ds["urban_to_ds_inf_etp_ratio"][:,:,:].data

        for time_t in time_steps:
            prec=ds["Prec_Val"][time_t,:,:].data
            irrig=ds["Irig_Val"][time_t,:,:].data
            wat_cons=ds["wat_cons"][time_t,:,:].data
            dir_infil=ds["dir_infil"][time_t,:,:].data            
            wat_net_loss=ds["wat_net_loss"][time_t,:,:].data
            urb_dir_evap=ds["urb_dir_evap"][time_t,:,:].data
            urb_indir_evap=ds["urb_indir_evap"][time_t,:,:].data
            runoff_to_sewage=ds["runoff_to_sewage"][time_t,:,:].data
            sew_net_loss_low=ds["sew_net_loss_low"][time_t,:,:].data
            sew_net_loss_high=ds["sew_net_loss_high"][time_t,:,:].data
            prec_sewage_threshold=ds["prec_sewage_threshold"][time_t,:,:].data
            wat_supp_wells=ds["wat_supp_wells"][time_t,:,:].data
            wat_supp_wells_loss=ds["wat_supp_wells_loss"][time_t,:,:].data
            wat_other=ds["wat_other"][time_t,:,:].data
            

            INF_Val,ETP_Val,Runoff_Val=urban_infiltration_calcs.urban_infiltration_np(prec,irrig,wat_cons,wat_net_loss,urb_dir_evap,urb_indir_evap,sew_net_loss_low,sew_net_loss_high,prec_sewage_threshold,runoff_to_sewage,dir_infil,wat_supp_wells,wat_supp_wells_loss,wat_other)            
            
            INF_Val_list.append(INF_Val)
            ETP_Val_list.append(ETP_Val)
            Runoff_Val_list.append(Runoff_Val)

        #append to NETCDF
        urban_results_list=[INF_Val_list,ETP_Val_list,Runoff_Val_list]
        
        ds=urban_infiltration_calcs.infilt_to_ds(ds,urban_area_raster_dir,urban_results_list,urban_to_ds_inf_etp_ratio)
        
        return ds 
    
    
    ###############
    def infilt_to_ds(ds,urban_area_raster_dir,urban_results_list,urban_to_ds_inf_etp_ratio):
        #for time_t in time_steps:  #ETR1,Def1,Ru1,Rec1
        
        if ds["lat"].shape[0]==1 and ds["lon"].shape[0]==1:
            urban_raster_np=np.array([[0]])
        else:
            urban_raster_np=urban_infiltration_calcs.read_rast(urban_area_raster_dir)

        urban_raster_3d=np.repeat(urban_raster_np[np.newaxis,:, : ], ds["time"].shape[0], axis=0)

        
        for name,lst in zip(["INF_Val","ETP_Val","Runoff_Val"],urban_results_list):                
            
            urb_val=np.array(lst)  #3D

            ds_vals=ds[name][:,:,:].data
            
            #to just overwrite the values that are marked as urban area
            ds_vals[~np.isnan(urban_raster_3d)]=ds_vals[~np.isnan(urban_raster_3d)]*(1-urban_to_ds_inf_etp_ratio[~np.isnan(urban_raster_3d)]/100)  + urb_val[~np.isnan(urban_raster_3d)]*(urban_to_ds_inf_etp_ratio[~np.isnan(urban_raster_3d)]/100)
            
            ds_vals[np.isnan(ds_vals)]=-9999

            ds[name][:,:,:]=ds_vals
            
        return ds

class urban_CN_correction():


    def connected_imperv_area_correction(CN_Prev,Con_Imp_area_perc):

        composite_CN=CN_Prev+(98-CN_Prev)*Con_Imp_area_perc/100
        
        return composite_CN

        
    def unconnected_imperv_area_correction(CN_Prev,Uncon_Imp_area_perc,Imp_area_perc):

        if Imp_area_perc >30:
            composite_CN=urban_CN_correction.connected_imperv_area_correction(CN_Prev,Uncon_Imp_area_perc)
        
        else:

            input_to_t2=(1-Uncon_Imp_area_perc/Imp_area_perc)*1.7*Imp_area_perc


            composite_CN=CN_Prev + (120-CN_Prev) * input_to_t2/460

        return composite_CN