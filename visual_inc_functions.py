from PyQt6 import QtWidgets,QtGui
from waterpybal_ui_py.visual import Ui_Dialog_visual
from waterpybal.post_processing import post_process
import netCDF4 as nc
from gui_help.gui_help_load import loadhelp


class Ui_Dialog_visual_(QtWidgets.QDialog):

    def __init__(self):
        
        super().__init__()

        self.ui = Ui_Dialog_visual()
        



        self.ui.setupUi(self)

        self.ui.checkBox_all_vars.setStyleSheet("""
            QCheckBox {
                font-size: 13px;
            }
            QCheckBox::indicator { width: 15px; height: 15px;}
            }
        """)

        self.ui.checkBox_regions_raster.setStyleSheet("""
            QCheckBox {
                font-size: 13px;
            }
            QCheckBox::indicator { width: 15px; height: 15px;}
            }
        """)

        self.show()
        ##############
        #limit the year to ints and 4 digits
        onlyInt=QtGui.QIntValidator()
        self.ui.lineEdit_start_year.setValidator(onlyInt) 
        self.ui.lineEdit_end_year.setValidator(onlyInt) 
        self.ui.lineEdit_start_year.setMaxLength(4)
        self.ui.lineEdit_end_year.setMaxLength(4)
        #################
        #limit the latlon
        onlyInt=QtGui.QDoubleValidator()
        self.ui.lineEdit_lat.setValidator(onlyInt) 
        self.ui.lineEdit_lon.setValidator(onlyInt) 
        self.ui.lineEdit_lat.setMaxLength(15)
        self.ui.lineEdit_lon.setMaxLength(15)
        #################
        self.ds=None
        self.org_ds_dir=None
        self.sam_raster_dir=None
        self.single_point=False
        #################
        self.ui.toolButton_refresh.clicked.connect(lambda: self.updatelist_vars())
        self.ui.toolButton_path.clicked.connect(lambda: self.open_ds())
        self.ui.toolButton_path_2.clicked.connect(lambda: self.selectFolder())
        self.ui.pushButton_point_time_excel.clicked.connect(lambda: self.time_funcs("CSV"))
        self.ui.pushButton_point_time_plot.clicked.connect(lambda: self.time_funcs("Figure"))
        #self.ui.pushButton_maps_excel.clicked.connect(lambda: self.maps_funcs("CSV"))
        self.ui.pushButton_maps_raster.clicked.connect(lambda: self.maps_funcs("Raster"))
        self.ui.pushButton_map_figure.clicked.connect(lambda: self.maps_funcs("Figure"))
        self.ui.checkBox_all_vars.stateChanged.connect(lambda:self.all_vars_checkboxclicked())
        self.ui.pushButton_report_excel.clicked.connect(lambda:self.gen_csv_report())
        self.ui.checkBox_regions_raster.stateChanged.connect(lambda:self.regions_checkboxclicked())
        self.ui.toolButton_refresh_regions_raster.clicked.connect(lambda:self.update_regions())
        self.ui.toolButton_regions_raster.clicked.connect(lambda:self.selectrastFile())

        loadhelp(self,"visual_output_help.md")
        
        
    

    def sing_point_mods(self):
        if self.single_point:
            self.ui.lineEdit_lat.setText("0")
            self.ui.lineEdit_lat.setEnabled(False)

            self.ui.lineEdit_lon.setText("0")
            self.ui.lineEdit_lon.setEnabled(False)
            self.ui.groupBox_2.setEnabled(False)
            self.ui.groupBox_report_raster.setEnabled(False)



    def update_regions(self):
        self.ui.comboBox_region.clear()

        #try:
        self.r_list=post_process.regions_list(self.ui.lineEdit_regions_raster.text())
        #update list of variables:
        self.ui.comboBox_region.addItems(self.r_list)
        #except: pass
        
        
    def regions_checkboxclicked(self):
        if self.ui.checkBox_regions_raster.isChecked()==True:
            self.ui.label_regions_raster.setEnabled(True)
            self.ui.lineEdit_regions_raster.setEnabled(True)
            self.ui.toolButton_regions_raster.setEnabled(True)
            self.ui.toolButton_refresh_regions_raster.setEnabled(True)
            self.ui.label_region.setEnabled(True)
            self.ui.comboBox_region.setEnabled(True)
        if self.ui.checkBox_regions_raster.isChecked()==False:
            self.ui.label_regions_raster.setEnabled(False)
            self.ui.lineEdit_regions_raster.setEnabled(False)
            self.ui.toolButton_regions_raster.setEnabled(False)
            self.ui.toolButton_refresh_regions_raster.setEnabled(False)
            self.ui.label_region.setEnabled(False)
            self.ui.comboBox_region.setEnabled(False)


    
    def gen_csv_report(self):
        
        ds_dir=self.ui.lineEdit_dataset_path.text()
        
        time_dic={
                    "start":[self.ui.lineEdit_start_year.text(),self.ui.comboBox_start_month.currentText(),self.ui.comboBox_start_day.currentText(),self.ui.comboBox_start_hour.currentText()],
                    "end":[self.ui.lineEdit_end_year.text(),self.ui.comboBox_end_month.currentText(),self.ui.comboBox_end_day.currentText(),self.ui.comboBox_end_hour.currentText()]
                    }
        
        if self.ui.checkBox_all_vars.isChecked()==False:
            var_name_list=[self.ui.comboBox_var_name.currentText()]
        else: 
            var_name_list=["Prec_Val","Irig_Val","INF_Val","ETP_Val","PRu_Val","ETR_Val","Def_Val","Rec_Val","Ru_Val"]

        
        lat_name=self.ui.lineEdit_lat_name.text()

        lon_name=self.ui.lineEdit_lon_name.text()

        save_dir=self.ui.lineEdit_save_path.text()

        if self.ui.checkBox_regions_raster.isChecked()==False:
            identifier_raster_array=None
            region="Total"
            reg_pix_area=None
        elif self.ui.checkBox_regions_raster.isChecked()==True:
            region=self.ui.comboBox_region.currentText()
            #if all regions
            if region=="All":
                
                if "All" in self.r_list: self.r_list.remove("All")

                region=self.r_list

            identifier_raster_array,reg_pix_area,msk=post_process.read_raster(self.ui.lineEdit_regions_raster.text())
            self.sam_raster_dir=self.ui.lineEdit_regions_raster.text()
        post_process.gen_report(ds_dir,time_dic,var_name_list,lat_name,lon_name,save_dir,self.sam_raster_dir,reg_pix_area,identifier_raster_array,region)    
        
        msgBox=QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Icon.Information)
        msgBox.setText("The report (.CSV) created successfully in"+ save_dir)
        msgBox.setWindowTitle("Saved successfully")
        msgBox.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
        msgBox.exec()
    
    def all_vars_checkboxclicked(self):
        if self.ui.checkBox_all_vars.isChecked()==True:
            self.updatelist_vars()
            self.ui.pushButton_map_figure.setEnabled(False)
            #self.ui.pushButton_maps_excel.setEnabled(False)
            self.ui.pushButton_maps_raster.setEnabled(False)
            self.ui.pushButton_point_time_plot.setEnabled(False)
            self.ui.comboBox_var_name.setEnabled(False)
        if self.ui.checkBox_all_vars.isChecked()==False:
            self.ui.pushButton_map_figure.setEnabled(True)
            #self.ui.pushButton_maps_excel.setEnabled(True)
            self.ui.pushButton_maps_raster.setEnabled(True)
            self.ui.pushButton_point_time_plot.setEnabled(True)
            self.ui.comboBox_var_name.setEnabled(True)

    #################
    def set_ds_path(self):
        self.ui.lineEdit_dataset_path.setText(self.org_ds_dir)
        try:
            #close the dataset
            self.ds.close()
        except: pass    

    ###############       
    def updatelist_vars(self):
        self.ui.comboBox_var_name.clear()
        #read ds from lineedit
        ds_dir=self.ui.lineEdit_dataset_path.text()
        try:
            self.ds_n=nc.Dataset(ds_dir,'r',format='NETCDF4')
            #update list of variables:
            list_vars=list(self.ds_n.variables.keys())
            dims_list=["time_bnds","time","lat","lon","x","y"]
            self.list_vars=[n for n in list_vars if n not in dims_list]
            self.ui.comboBox_var_name.addItems(self.list_vars)
            self.ds_n.close()
        except: pass
    
    ###############    
    def time_funcs(self,to_fig_or_csv):
        ds_dir=self.ui.lineEdit_dataset_path.text()
        save_dir=self.ui.lineEdit_save_path.text()
        time_dic={
                    "start":[self.ui.lineEdit_start_year.text(),self.ui.comboBox_start_month.currentText(),self.ui.comboBox_start_day.currentText(),self.ui.comboBox_start_hour.currentText()],
                    "end":[self.ui.lineEdit_end_year.text(),self.ui.comboBox_end_month.currentText(),self.ui.comboBox_end_day.currentText(),self.ui.comboBox_end_hour.currentText()]
                    }
        lat_val=self.ui.lineEdit_lat.text()
        lon_val=self.ui.lineEdit_lon.text()
        lat_name=self.ui.lineEdit_lat_name.text()
        lon_name=self.ui.lineEdit_lon_name.text()
        if self.ui.checkBox_all_vars.isChecked()==False:
            var_name_list=[self.ui.comboBox_var_name.currentText()]
        else: 
            var_name_list=self.list_vars
        print (var_name_list)    
        post_process.point_fig_csv(ds_dir,save_dir,time_dic,lat_val,lon_val,lat_name,lon_name,var_name_list,to_fig_or_csv)
        print ("vis after func")
        msgBox=QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Icon.Information)
        msgBox.setText(to_fig_or_csv+"s created successfully in"+ save_dir)
        msgBox.setWindowTitle("Saved successfully")
        msgBox.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
        msgBox.exec()
    ###############
    def maps_funcs(self,fig_csv_raster):
        ds_dir=self.ui.lineEdit_dataset_path.text()
        save_dir=self.ui.lineEdit_save_path.text()
        time_dic={
                    "start":[self.ui.lineEdit_start_year.text(),self.ui.comboBox_start_month.currentText(),self.ui.comboBox_start_day.currentText(),self.ui.comboBox_start_hour.currentText()],
                    "end":[self.ui.lineEdit_end_year.text(),self.ui.comboBox_end_month.currentText(),self.ui.comboBox_end_day.currentText(),self.ui.comboBox_end_hour.currentText()]
                    }
        var_name=self.ui.comboBox_var_name.currentText()
        post_process.raster_fig_csv(ds_dir,save_dir,time_dic,var_name,fig_csv_raster)
        msgBox=QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Icon.Information)
        msgBox.setText(fig_csv_raster + "s created successfully in"+ save_dir)
        msgBox.setWindowTitle("Saved successfully")
        msgBox.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
        msgBox.exec()
    ###############
        
    
    ###############
    def selectFolder(self):
        self.Folder_dir = QtWidgets.QFileDialog.getExistingDirectory(caption='select a directory')
        
        self.ui.lineEdit_save_path.setText(self.Folder_dir)
    
    ###############
    def open_ds(self):
        filter = "NETCDF(*.nc)"
        self.dsName = QtWidgets.QFileDialog.getOpenFileName(caption='select a NETCDF (.nc) database',filter=filter)[0]
        
        self.ui.lineEdit_dataset_path.setText(self.dsName)
    ###############

    #select raster file
    def selectrastFile(self):
        filter = "Raster(*.tif)"
        self.rastfileName = QtWidgets.QFileDialog.getOpenFileName(caption='select a raster file',filter=filter)[0]
        
        self.ui.lineEdit_regions_raster.setText(self.rastfileName)
    ###############

#ds_dir=r'C:\Users\Ash kan\Documents\watbalpy\daymet_v4_daily_hi_prcp_2021.nc'
#sds=nc.Dataset(ds_dir,'r+',format='NETCDF4')
#sds.close()