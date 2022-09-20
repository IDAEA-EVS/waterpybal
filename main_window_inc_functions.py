from PyQt6 import QtWidgets
from balance_inc_functions import Ui_balance_Dialog_
from main_window import Ui_MainWindow  # importing our generated file
from lat_lon_time_dialog_inc_functions import lat_lon_time_dialog_
from var_spat_interpol_inc_functions import Ui_Dialog_var_spat_interpol_
from var_from_tiff_inc_functions import Ui_Dialog_var_from_tiff_
from swr_window_inc_functions import Ui_Dialog_swr_
from infiltration_inc_functions import Ui_Dialog_infiltration_
from etp_window_inc_functions import Ui_Dialog_etp_
from open_dataset_inc_functions import Ui_Dialog_open_dataset_
from visual_inc_functions import Ui_Dialog_visual_
from qErrorHandler import UncaughtHook
import os
import sys
import netCDF4 as nc

class waterpybalMainwindow(QtWidgets.QMainWindow):

    def __init__(self):

        super().__init__()

        self.ui = Ui_MainWindow()
        
        self.ui.setupUi(self)
        ##############        
        ##############
        self.ds=None
        self.preferred_date_interval=None
        self.sam_raster_dir=None
        self.ds_dir=None
        self.win_open=False
        self.single_point=False
        self.urban_ds=False
        ###############
        self.ui.toolButton_path.clicked.connect(self.selectFolder)
        self.ui.pushButton_open_dataset.clicked.connect(self.open_dataset)
        self.ui.pushButton_to_lat_lon_time.clicked.connect(self.open_lat_lon)  
        self.ui.pushButton_to_var_spat_interpol.clicked.connect(self.open_interpol)
        self.ui.pushButton_to_var_from_tiff.clicked.connect(self.open_var_tif)
        self.ui.pushButton_to_swr.clicked.connect(self.open_swr)
        self.ui.pushButton_to_infiltration.clicked.connect(self.open_infilt)
        self.ui.pushButton_to_etp.clicked.connect(self.open_etp)
        self.ui.pushButton_to_Balance.clicked.connect(self.open_bal)
        self.ui.pushButton_to_visualization.clicked.connect(self.open_visual)
        self.ui.pushButton_save_dataset.clicked.connect(self.save_close)


    #######################################
    def open_visual(self):
        if self.win_open==False: #to just have one window open!
            self.win_open=True

            # create a global instance of our class to register the hook
            qt_exception_hook = UncaughtHook()
            #########

            self.ui_visual=Ui_Dialog_visual_()
            self.ui_visual.sam_raster_dir=self.sam_raster_dir
            self.ui_visual.ds=self.ds
            self.ui_visual.org_ds_dir=self.ds_dir
            self.ui_visual.single_point=self.single_point
            self.ui_visual.set_ds_path()
            self.ui_visual.updatelist_vars()
            self.ui_visual.sing_point_mods()
            if self.ui_visual.exec()==0:
                print ("out_of_ui_visual!!!!")
                self.win_open=False
                self.ds=self.ui_visual.ds
                try: self.ds=nc.Dataset(self.ds_dir,'r+',format='NETCDF4')
                except: pass
            else:
                self.win_open=False
    
    #######################################
    def open_bal(self):
        if self.win_open==False: #to just have one window open!
            self.win_open=True

            # create a global instance of our class to register the hook
            qt_exception_hook = UncaughtHook()
            #########

            self.ui.label_to_Balance.setText("In process")
            self.ui_bal=Ui_balance_Dialog_()
            self.ui_bal.ds=self.ds
            if self.ui_bal.exec()==1 and qt_exception_hook.exception_hook_bool==False:
                self.ds=self.ui_bal.ds
                self.ui.label_to_Balance.setText("Done")
                self.win_open=False
            else:
                self.win_open=False
                self.ui.label_to_Balance.setText("")
    
    #######################################
    def open_etp(self):
        if self.win_open==False: #to just have one window open!
            self.win_open=True

            # create a global instance of our class to register the hook
            qt_exception_hook = UncaughtHook()
            #########
            
            self.ui.label_to_etp.setText("In process")
            self.ui_etp=Ui_Dialog_etp_()
            self.ui_etp.ds=self.ds
            self.ui_etp.preferred_date_interval=self.preferred_date_interval
            self.ui_etp.single_point=self.single_point
            if self.ui_etp.exec()==1 and qt_exception_hook.exception_hook_bool==False:
                self.ds=self.ui_etp.ds
                self.ui.label_to_etp.setText("Done")
                self.win_open=False
            else:
                self.ui.label_to_etp.setText("")
                self.win_open=False

    #######################################
    def open_infilt(self):
        if self.win_open==False: #to just have one window open!
            self.win_open=True 

            # create a global instance of our class to register the hook
            qt_exception_hook = UncaughtHook()
            #########
            
            self.ui.label_to_infiltration.setText("In process")
            self.ui_infilt=Ui_Dialog_infiltration_()
            self.ui_infilt.ds=self.ds
            self.ui_infilt.preferred_date_interval=self.preferred_date_interval
            self.ui_infilt.single_point=self.single_point
            self.ui_infilt.urban_ds=self.urban_ds
            #################
            self.ui_infilt.check_timesteps()
            self.ui_infilt.check_urban()
            self.ui_infilt.check_single_point()
            self.ui_infilt.update_urban_table()
            #################
            if self.ui_infilt.exec()==1 and qt_exception_hook.exception_hook_bool==False:
                self.ds=self.ui_infilt.ds
                self.ui.label_to_infiltration.setText("Done")
                self.win_open=False
            else:
                self.ui.label_to_infiltration.setText("")
                self.win_open=False

    #######################################
    def open_swr(self):
        if self.win_open==False: #to just have one window open!
            self.win_open=True

            # create a global instance of our class to register the hook
            qt_exception_hook = UncaughtHook()
            #########
            
            self.ui.label_to_swr.setText("In process")
            self.ui_swr=Ui_Dialog_swr_()
            self.ui_swr.ds=self.ds
            self.ui_swr.single_point=self.single_point
            self.ui_swr.single_point_mod()
            if self.ui_swr.exec()==1 and qt_exception_hook.exception_hook_bool==False:
                self.ds=self.ui_swr.ds
                self.ui.label_to_swr.setText("Done")
                self.win_open=False

            else:
                self.ui.label_to_swr.setText("")
                self.win_open=False


    #######################################
    def open_var_tif(self):
        if self.win_open==False: #to just have one window open!
            self.win_open=True

            # create a global instance of our class to register the hook
            qt_exception_hook = UncaughtHook()
            #########
            
            self.ui.label_to_var_from_tiff.setText("In process")
            self.ui_tif=Ui_Dialog_var_from_tiff_()
            self.ui_tif.ds=self.ds
            self.ui_tif.preferred_date_interval=self.preferred_date_interval
            self.ui_tif.updatelist_vars()
            if self.ui_tif.exec()==1 and qt_exception_hook.exception_hook_bool==False:
                self.ds=self.ui_tif.ds
                self.ui.label_to_var_from_tiff.setText("Done")
                self.win_open=False

            else:
                self.ui.label_to_var_from_tiff.setText("")
                self.win_open=False


    #######################################
    def open_interpol(self):
        if self.win_open==False: #to just have one window open!
            self.win_open=True

            # create a global instance of our class to register the hook
            qt_exception_hook = UncaughtHook()
            #########
               
            self.ui.label_to_var_spat_interpol.setText("In process")
            self.ui_interpol=Ui_Dialog_var_spat_interpol_()
            self.ui_interpol.ds=self.ds
            print ("self.single_point",self.single_point)
            self.ui_interpol.single_point=self.single_point
            self.ui_interpol.single_point_mod()
            self.ui_interpol.preferred_date_interval=self.preferred_date_interval
            try: self.ui_interpol.sam_raster_dir=self.sam_raster_dir
            except: pass
            self.ui_interpol.set_samp_rast()
            if self.ui_interpol.exec()==1 and qt_exception_hook.exception_hook_bool==False:
                self.ds=self.ui_interpol.ds
                self.ui.label_to_var_spat_interpol.setText("Done")
                self.win_open=False

            else:
                self.ui.label_to_var_spat_interpol.setText("")
                self.win_open=False
    
    #######################################
    def open_lat_lon(self):
        if self.win_open==False: #to just have one window open!
            self.win_open=True

            # create a global instance of our class to register the hook
            qt_exception_hook = UncaughtHook()
            #########
               
            self.ui.label_to_lat_lon_time.setText("In process")
            self.ui_lat_lon= lat_lon_time_dialog_()
            self.ui_lat_lon.ds=self.ds
            self.ui_lat_lon.preferred_date_interval=self.preferred_date_interval
            self.ui_lat_lon.dir=os.path.join(self.ui.lineEdit_path.text(),self.ui.lineEdit_name.text()+'.nc')
            
            if self.ui_lat_lon.exec()==1 and qt_exception_hook.exception_hook_bool==False:
                self.ds=self.ui_lat_lon.ds
                self.preferred_date_interval=self.ui_lat_lon.preferred_date_interval
                self.single_point=self.ui_lat_lon.single_point
                self.urban_ds=self.ui_lat_lon.urban_ds
                if self.single_point:
                    self.sam_raster_dir=self.single_raster()
                    
                    #disable tiff import option
                    self.ui.pushButton_to_var_from_tiff.setEnabled(False)
                else:
                    self.sam_raster_dir=self.ui_lat_lon.sam_raster_dir

                self.ui.label_to_lat_lon_time.setText("Done")
                self.win_open=False
            else:
                self.ui.label_to_lat_lon_time.setText("")
                self.win_open=False

    #######################################
    def open_dataset(self):
        if self.win_open==False: #to just have one window open!
            self.win_open=True

            # create a global instance of our class to register the hook
            qt_exception_hook = UncaughtHook()
            #########
               
            import netCDF4 as nc
            self.open_ds=Ui_Dialog_open_dataset_()
            
            if self.open_ds.exec()==1 and qt_exception_hook.exception_hook_bool==False:
                self.win_open=False

                self.ds_dir=self.open_ds.ds_dir
                self.preferred_date_interval=self.open_ds.preferred_date_interval
                self.single_point=self.open_ds.single_point
                
                if self.single_point:
                    self.sam_raster_dir=self.single_raster()
                    #disable tiff import option
                    self.ui.pushButton_to_var_from_tiff.setEnabled(False)
                else:
                    self.sam_raster_dir=self.open_ds.sam_raster_dir

                #add code to split the name and it to the file name and path
                dir_list=os.path.splitext(self.ds_dir)[0].split("/")
                #print (dir_list)
                name=dir_list[-1]
                self.ui.lineEdit_name.setText(name)
                self.ui.lineEdit_path.setText(os.path.join(*dir_list[0:-1]))
                self.ds=nc.Dataset(self.ds_dir,'r+',format='NETCDF4')
                
                #to identify if the opened database id urban compatible
                try:
                    self.ds["wat_cons"]
                    self.urban_ds=True
                except:
                    self.urban_ds=False
                #########

                if self.sam_raster_dir in ["", " ", "  "] and self.single_point==False:
                    msgBox=QtWidgets.QMessageBox()
                    msgBox.setIcon(QtWidgets.QMessageBox.Icon.Information)
                    msgBox.setText("Sample raster directory is not idefined!")
                    msgBox.setWindowTitle("Sample raster directory is missing!")
                    msgBox.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
                    msgBox.exec()
                
            
            else: self.win_open=False
    
    #######################################
    def selectFolder(self):
        self.Folder_dir = QtWidgets.QFileDialog.getExistingDirectory(caption='select a directory')
        
        self.ui.lineEdit_path.setText(self.Folder_dir)
    
    #######################################
    def save_close(self):
        qt_exception_hook = UncaughtHook()
        print (qt_exception_hook.exception_hook_bool)
        #if qt_exception_hook.exception_hook_bool==True:

        if self.ds!=None:
            try:

                self.ds.close()
                msgBox=QtWidgets.QMessageBox()
                msgBox.setIcon(QtWidgets.QMessageBox.Icon.Information)
                msgBox.setText(self.ui.lineEdit_name.text()+ " NETCDF dataset is saved and closed successfully!")
                msgBox.setWindowTitle("Save and close the dataset")
                msgBox.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
                msgBox.exec()
            except:
                msgBox=QtWidgets.QMessageBox()
                msgBox.setIcon(QtWidgets.QMessageBox.Icon.Information)
                msgBox.setText(self.ui.lineEdit_name.text()+ " NETCDF dataset is already closed! This window normally appears if you already saved and closed the dataset!")
                msgBox.setWindowTitle("Save and close the dataset")
                msgBox.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
                msgBox.exec()
    
    #######################################
    def single_raster(self):
        import numpy as np
        import rasterio as rs
        arr=np.array([[0]])
        rs.open('single_point_internal_raster.tiff', 'w', driver='GTiff',
                            height = arr.shape[0], width = arr.shape[1],
                            count=1, dtype=str(arr.dtype))
        sr_dir=r'single_point_internal_raster.tiff'
        return sr_dir
        



app = QtWidgets.QApplication(sys.argv)

application = waterpybalMainwindow()

application.show()

sys.exit(app.exec())