from PyQt6 import QtWidgets,QtGui
from visual import Ui_Dialog_visual
from waterpybal.post_processing import post_process
import netCDF4 as nc


class Ui_Dialog_visual_(QtWidgets.QDialog):

    def __init__(self):
        
        super().__init__()

        self.ui = Ui_Dialog_visual()
        
        self.ui.setupUi(self)
        
        self.show()
        ##############
        #limit the year to ints and 4 digits
        onlyInt=QtGui.QIntValidator()
        self.ui.lineEdit_start_year.setValidator(onlyInt) 
        self.ui.lineEdit_end_year.setValidator(onlyInt) 
        self.ui.lineEdit_start_year.setMaxLength(4)
        self.ui.lineEdit_end_year.setMaxLength(4)
        #################
        #limit the year to ints and 4 digits
        onlyInt=QtGui.QDoubleValidator()
        self.ui.lineEdit_lat.setValidator(onlyInt) 
        self.ui.lineEdit_lon.setValidator(onlyInt) 
        self.ui.lineEdit_lat.setMaxLength(15)
        self.ui.lineEdit_lon.setMaxLength(15)
        #################
        self.ds=None
        self.org_ds_dir=None
        #################
        self.ui.toolButton_refresh.clicked.connect(lambda: self.updatelist_vars())
        self.ui.toolButton_path.clicked.connect(lambda: self.open_ds())
        self.ui.toolButton_path_2.clicked.connect(lambda: self.selectFolder())
        self.ui.pushButton_point_time_excel.clicked.connect(lambda: self.time_funcs("CSV"))
        self.ui.pushButton_point_time_plot.clicked.connect(lambda: self.time_funcs("Figure"))
        self.ui.pushButton_maps_excel.clicked.connect(lambda: self.maps_funcs("CSV"))
        self.ui.pushButton_maps_raster.clicked.connect(lambda: self.maps_funcs("Raster"))
        self.ui.pushButton_map_figure.clicked.connect(lambda: self.maps_funcs("Figure"))

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
            list_vars=[n for n in list_vars if n not in dims_list]
            self.ui.comboBox_var_name.addItems(list_vars)
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
        var_name=self.ui.comboBox_var_name.currentText()
        post_process.point_fig_csv(ds_dir,save_dir,time_dic,lat_val,lon_val,lat_name,lon_name,var_name,to_fig_or_csv)
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

ds_dir=r'C:\Users\Ash kan\Documents\watbalpy\daymet_v4_daily_hi_prcp_2021.nc'
sds=nc.Dataset(ds_dir,'r+',format='NETCDF4')
sds.close()