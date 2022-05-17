from PyQt6 import QtWidgets,QtCore
from var_spat_interpol import Ui_Dialog_var_spat_interpol
from waterpybal.dataset_prep import netCDF_ds


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
        ##################
        #Linear as default
        self.ui.comboBox_method.setCurrentIndex(3)
        self.met='linear'
        ###################

        #set the tableWidget_intp_method_params table
        self.ui.tableWidget_intp_method_params.setRowCount(1)
        cellinfo=QtWidgets.QTableWidgetItem('radius')
        cellinfo.setFlags(QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.ui.tableWidget_intp_method_params.setItem(0, 0, cellinfo)
        cellinfo=QtWidgets.QTableWidgetItem('0.0')
        self.ui.tableWidget_intp_method_params.setItem(0, 1, cellinfo)

        #Method combo box and table
        self.ui.comboBox_method.currentTextChanged.connect(lambda: self.update_table())
        ##################
        #to work when it is okeyed
        self.ui.buttonBox_spat_interpol.accepted.connect(lambda: self.ok_clicked())


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
    #function to list the variables
    def updatelist_vars(self):
        try:
            #list of variables:

            
            #self.ds=None
            #dir=r"C:\Users\Ash kan\Documents\watbalpy\daymet_v4_daily_hi_prcp_2021.nc"
            #ds=nc.Dataset(dir,'r',format='NETCDF4')

            list_vars=list(self.ds.variables.keys())
            dims_list=["time_bnds","time","lat","lon","x","y"]
            list_vars=[n for n in list_vars if n not in dims_list]
            self.ui.comboBox_var_name.addItems(list_vars)
            
            #same sample raster as before as a default path
            self.ui.lineEdit_xyraster.setText(self.sam_raster_dir)
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
############################
    def ok_clicked(self):
        #############
        #read method and construc the str
        num_of_rows=self.ui.tableWidget_intp_method_params.rowCount()
        parstr=''
        for i in range(0,num_of_rows):
            par_name=self.ui.tableWidget_intp_method_params.item(i,0).text()
            par_val=self.ui.tableWidget_intp_method_params.item(i,1).text()
            parstr=parstr+':'+par_name+'='+par_val
        
        method=self.met+parstr+":nodata=-9999"
        print (method)

        ras_sample_dir=self.ui.lineEdit_xyraster.text()
        csv_dir=self.ui.lineEdit_csv.text()
        time_csv_col=self.ui.lineEdit_time_col.text()
        lat_csv_col=self.ui.lineEdit_lat_col.text()
        lon_csv_col=self.ui.lineEdit_lon_col.text()
        var_name=self.ui.comboBox_var_name.currentText()
        
        preferred_date_interval=self.preferred_date_interval
        print ('preferred_date_interval',preferred_date_interval)
        print ()
        interpolation_time_int=self.ui.comboBox_time_interval.currentText()
        self.ds=netCDF_ds.var_interpolation(self.ds,ras_sample_dir,csv_dir,time_csv_col,lat_csv_col,lon_csv_col,var_name,method,preferred_date_interval,interpolation_time_int)




'''app = QtWidgets.QApplication(sys.argv)

application = Ui_Dialog_var_spat_interpol_()

application.show()

sys.exit(app.exec())'''