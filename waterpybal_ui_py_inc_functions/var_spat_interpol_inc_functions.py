from PyQt6 import QtWidgets,QtCore,QtGui
from .waterpybal_ui_py.var_spat_interpol import Ui_Dialog_var_spat_interpol
from waterpybal.dataset_prep import variable_management
import pandas as pd
import netCDF4 as nc
from gui_help.gui_help_load import loadhelp

class Ui_Dialog_var_spat_interpol_(QtWidgets.QDialog):

    def __init__(self):
        
        super().__init__()

        self.ui = Ui_Dialog_var_spat_interpol()
        
        self.ui.setupUi(self)
        self.show()
        ##############
        #browse button
        self.ui.toolButton_browse_csv.clicked.connect(lambda: self.selectcsvFile())
        ##############
        #browse raster button
        self.ui.toolButton_browse_xy_raster.clicked.connect(lambda: self.selectrastFile())
        ##################
        self.ds=None
        self.preferred_date_interval=None
        self.sam_raster_dir=None
        self.single_point=False
        self.sam_val=False
        self.nc_ds=False
        ##################
        #Linear as default
        self.ui.comboBox_method.setCurrentIndex(3)
        self.met='linear'
        ###################
        self.ui.checkBox.setStyleSheet("""
            QCheckBox {
                font-size: 13px;
            }
            QCheckBox::indicator { width: 15px; height: 15px;}
            }
        """)
        self.ui.checkBox_variable_input.setStyleSheet("""
            QCheckBox {
                font-size: 13px;
            }
            QCheckBox::indicator { width: 15px; height: 15px;}
            }
        """)
        self.ui.checkBox_nc.setStyleSheet("""
            QCheckBox {
                font-size: 13px;
            }
            QCheckBox::indicator { width: 15px; height: 15px;}
            }
        """)        
        ###################
        #limit the sameval line edit
        doub=QtGui.QDoubleValidator()
        self.ui.lineEdit_same_val.setValidator(doub) 
        self.ui.lineEdit_same_val.setMaxLength(15)
        ###################
        #first vars of the table
        self.init_table()
        #################
        #same value checkbox
        self.ui.checkBox_variable_input.stateChanged.connect(lambda: self.variable_input())
        #################
        # nc checkbox statechange
        self.ui.checkBox_nc.stateChanged.connect(lambda: self.nc_checkbox_state())
        #################
        #nc refresh
        self.ui.toolButton_refresh_nc.clicked.connect(lambda: self.updatelist_vars("nc"))
        #nc open
        self.ui.toolButton_browse_nc.clicked.connect(lambda:self.selectncFile())

        #################
        #refresh
        self.ui.toolButton_refresh.clicked.connect(lambda: self.updatelist_vars("csv"))
        #Method combo box and table
        self.ui.comboBox_method.currentTextChanged.connect(lambda: self.update_table())
        ##################
        
        ##################
        #to work when it is okeyed
        self.ui.buttonBox_spat_interpol.accepted.connect(lambda: self.ok_clicked())
    

        loadhelp(self,"var_intro_interpol_help.md")

    #################
    def ds_size_calc(self):
        self.ui.label_3.setText(list(self.ds.dimensions.values())[0].name)
        self.ui.label_4.setText(list(self.ds.dimensions.values())[1].name)
        self.ui.label_5.setText(list(self.ds.dimensions.values())[2].name)
        self.ui.label_longx.setText(str(list(self.ds.dimensions.values())[0].size))
        self.ui.label_laty.setText(str(list(self.ds.dimensions.values())[1].size))
        self.ui.label_time.setText(str(list(self.ds.dimensions.values())[2].size))
    #################
    def nc_checkbox_state(self):
        if self.ui.checkBox_nc.isChecked():
            self.nc_ds=True
            self.ui.groupBox_2.setEnabled(True)

            
            #same value
            self.sam_val=False
            self.ui.groupBox.setEnabled(False)
            self.ui.checkBox_variable_input.setChecked(False)
            
            #raster
            self.ui.groupBox_variable_input.setEnabled(False)        
        
        else:
            self.nc_ds=False
            self.ui.groupBox_2.setEnabled(False)
            self.ui.groupBox_variable_input.setEnabled(True)

    #################
    def variable_input(self):
        if self.ui.checkBox_variable_input.isChecked():
            self.sam_val=True
            self.ui.groupBox.setEnabled(True)
            #.nc
            self.ui.checkBox_nc.setChecked(False)
            self.ui.groupBox_2.setEnabled(False)
            self.nc_ds=False

            self.updatelist_vars_same_val()

            #raster
            self.ui.groupBox_variable_input.setEnabled(False)

        else:
            self.sam_val=False
            self.ui.groupBox.setEnabled(False)
            self.ui.groupBox_variable_input.setEnabled(True)

    #################        
    def init_table(self):
        #set the tableWidget_intp_method_params table
        self.ui.tableWidget_intp_method_params.setRowCount(1)
        cellinfo=QtWidgets.QTableWidgetItem('radius')
        cellinfo.setFlags(QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.ui.tableWidget_intp_method_params.setItem(0, 0, cellinfo)
        cellinfo=QtWidgets.QTableWidgetItem('0.0')
        self.ui.tableWidget_intp_method_params.setItem(0, 1, cellinfo)
    #################
    def single_point_mod(self):
        
        if self.single_point:
            self.ui.lineEdit_xyraster.setEnabled(False)
            self.ui.label_xy_raster.setEnabled(False)
            self.ui.toolButton_browse_xy_raster.setEnabled(False)
            self.ui.label_method.setEnabled(False)
            self.ui.comboBox_method.setEnabled(False)
            self.ui.tableWidget_intp_method_params.setEnabled(False)
            self.ui.lineEdit_lat_col.setEnabled(False)
            self.ui.lineEdit_lon_col.setEnabled(False)
    
    #################
    def update_table(self):
        
        self.ui.tableWidget_intp_method_params.setRowCount(0)
        src=0
        new_method=self.ui.comboBox_method.currentText()
        data = []
        if new_method== "Inverse Distance":
            self.met="invdist"
            src=7
            data=[
                ('power','2.0'),
                ('smoothing','0.0'),
                ('radius1','0.0'),
                ('radius2','0.0'),
                ('angle','0.0'),
                ('max_points','0'),
                ('min_points','0'),
                ]  

        elif new_method== "Nearest Neighbor":
            self.met="nearest"
            src=3
            data=[
                ('radius1','0.0'),
                ('radius2','0.0'),
                ('angle','0.0'),
                ] 

        elif new_method== "ID-NN":
            self.met="invdistnn"
            src=5
            data=[
                ('power','2.0'),
                ('smoothing','0.0'),
                ('radius','0.0'),
                ('max_points','0'),
                ('min_points','0'),
                ] 
        elif  new_method=="Linear":
            self.met="linear"
            src=1
            data=[
                ('radius','0.0'),
                ] 
            
        elif new_method== "Mov. Average":
            self.met="average"
            src=4
            data=[
                ('radius1','0.0'),
                ('radius2','0.0'),
                ('angle','0.0'),
                ('min_points','0'),
                ] 
        ####################
        self.ui.tableWidget_intp_method_params.setRowCount(src)
        row=0

        for tup in data:

            col=0

            for item in tup:

                

                cellinfo=QtWidgets.QTableWidgetItem(item)
                if col==0: cellinfo.setFlags(QtCore.Qt.ItemFlag.ItemIsEnabled)

                #print (cellinfo)
                self.ui.tableWidget_intp_method_params.setItem(row, col, cellinfo)

                col+=1

            row += 1

    #################
    def set_samp_rast(self):
        #same sample raster as before as a default path
        self.ui.lineEdit_xyraster.setText(self.sam_raster_dir)
    
    #################
    #function to list the variables
    def updatelist_vars(self,csv_or_nc):
        self.ui.comboBox_var_name.clear()
        self.ui.comboBox_var_name_nc.clear()
        #try:
            #list of variables:

            
            #self.ds=None
            #dir=r"C:\Users\Ash kan\Documents\watbalpy\daymet_v4_daily_hi_prcp_2021.nc"
            #ds=nc.Dataset(dir,'r',format='NETCDF4')
            
            #ds heads
        list_vars_ds=list(self.ds.variables.keys())
        dims_list=["time_bnds","time","lat","lon","x","y"]
        list_vars_ds=[n for n in list_vars_ds if n not in dims_list]
        #------
        if csv_or_nc=="csv":
            #read csv heads
            csv_dir=self.ui.lineEdit_csv.text()
            df=pd.read_csv(csv_dir)
            list_vars_filtered=list(df.head())
            list_vars=[n for n in list_vars_ds if n in list_vars_filtered]
            self.ui.comboBox_var_name.addItems(list_vars)
        #-----
        elif csv_or_nc=="nc":
            print ("in nc!!!")
            self.ui.label_longx_new.clear()
            self.ui.label_laty_new.clear()
            self.ui.label_time_new.clear()
            self.ui.label_6.clear()
            self.ui.label_7.clear()
            self.ui.label_8.clear()

            nc_ds_tmp_dir=self.ui.lineEdit_nc.text()
            nc_ds_tmp=nc.Dataset(nc_ds_tmp_dir,'r+',format='NETCDF4')
            list_vars_filtered=list(nc_ds_tmp.variables.keys())
            list_vars=[n for n in list_vars_ds if n in list_vars_filtered]
            self.ui.comboBox_var_name_nc.addItems(list_vars)

            self.ui.label_longx_new.setText(str(list(nc_ds_tmp.dimensions.values())[0].size))
            self.ui.label_laty_new.setText(str(list(nc_ds_tmp.dimensions.values())[1].size))
            self.ui.label_time_new.setText(str(list(nc_ds_tmp.dimensions.values())[2].size))
            self.ui.label_6.setText(list(nc_ds_tmp.dimensions.values())[0].name)
            self.ui.label_7.setText(list(nc_ds_tmp.dimensions.values())[1].name)
            self.ui.label_8.setText(list(nc_ds_tmp.dimensions.values())[2].name)

            nc_ds_tmp.close()
     
        #except: pass
    
    
    ###############
    def updatelist_vars_same_val(self):
        self.ui.comboBox_var_same_val.clear()
        try:
            #list of variables:

            list_vars_ds=list(self.ds.variables.keys())
            dims_list=["time_bnds","time","lat","lon","x","y"]
            list_vars_ds=[n for n in list_vars_ds if n not in dims_list]
            self.ui.comboBox_var_same_val.addItems(list_vars_ds)
        
        except: pass
    ###############
    #select csv
    def selectcsvFile(self):
        filter = "CSV(*.csv)"
        self.fileName = QtWidgets.QFileDialog.getOpenFileName(caption='select a .CSV file',filter=filter)[0]
        
        self.ui.lineEdit_csv.setText(self.fileName)
    
    ###############
    #select raster file
    def selectrastFile(self):
        filter = "Raster(*.tif)"
        self.rastfileName = QtWidgets.QFileDialog.getOpenFileName(caption='select a raster file',filter=filter)[0]
        
        self.ui.lineEdit_xyraster.setText(self.rastfileName)
    
    ###############
    def selectncFile(self):
        filter = "NETCDF(*.nc)"
        self.ncfileName = QtWidgets.QFileDialog.getOpenFileName(caption='select a .nc file',filter=filter)[0]
        
        self.ui.lineEdit_nc.setText(self.ncfileName)
    ###############
    def ok_clicked(self):
        
        
        if self.sam_val==False and self.nc_ds==False:

            ######
            multiply=True
            if self.ui.checkBox.isChecked(): multiply=False

            ######
            preferred_date_interval=self.preferred_date_interval
            interpolation_time_int=self.ui.comboBox_time_interval.currentText()
            csv_dir=self.ui.lineEdit_csv.text()
            time_csv_col=self.ui.lineEdit_time_col.text()
            lat_csv_col=self.ui.lineEdit_lat_col.text()
            lon_csv_col=self.ui.lineEdit_lon_col.text()    
            var_name=self.ui.comboBox_var_name.currentText()
            ras_sample_dir=self.ui.lineEdit_xyraster.text()

            ######
            if self.single_point==False:
                method=self.method_str_construct()
                self.ds=variable_management.var_interpolation(self.ds,ras_sample_dir,csv_dir,var_name,method,preferred_date_interval,interpolation_time_int,time_csv_col,lat_csv_col,lon_csv_col,multiply)

            else:
                self.ds=variable_management.var_introduction_from_csv(self.ds,csv_dir,var_name,preferred_date_interval,interpolation_time_int,time_csv_col,multiply)

        elif self.sam_val==True and self.nc_ds==False:
            #same value for all timesteps and in all space
            var_name=self.ui.comboBox_var_name.currentText()
            self.ds[var_name][:,:,:]=float(self.ui.lineEdit_same_val.text())
        
        elif self.sam_val==False and self.nc_ds==True:
            #nc
            var_name=self.ui.comboBox_var_name_nc.currentText
            new_nc_dir=self.ui.lineEdit_nc.text()

            self.ds=variable_management.var_introduction_from_nc(new_nc_dir,self.ds,var_name)


    '''def single_point_csv_config(self,csv_dir):
        df=pd.read_csv(csv_dir)
        df["lat"]=0
        df["lon"]=0
        csv_dir=r"single_point_internal_csv.csv"
        df.to_csv(csv_dir)
        return csv_dir'''

    ###############
    def method_str_construct(self):
            #read method and construc the str
        num_of_rows=self.ui.tableWidget_intp_method_params.rowCount()
        parstr=''
        for i in range(0,num_of_rows):
            par_name=self.ui.tableWidget_intp_method_params.item(i,0).text()
            par_val=self.ui.tableWidget_intp_method_params.item(i,1).text()
            parstr=parstr+':'+par_name+'='+par_val
        
        method=self.met+parstr+":nodata=-9999"
        return method



'''app = QtWidgets.QApplication(sys.argv)

application = Ui_Dialog_var_spat_interpol_()

application.show()

sys.exit(app.exec())'''