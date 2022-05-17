from PyQt6 import QtWidgets,QtGui

from lat_lon_time_dialog import Ui_Dialog_lat_lon_time
import os
import sys
from waterpybal.dataset_prep import netCDF_ds


class lat_lon_time_dialog_(QtWidgets.QDialog):

    def __init__(self):
        
        super().__init__()

        self.ui = Ui_Dialog_lat_lon_time()
        
        self.ui.setupUi(self)
        self.show()
        ##############

        #to work when it is okeyed
        self.ui.buttonBox.accepted.connect(lambda: self.ok_clicked())
        #to select file
        self.ui.toolButton_browse_xy_raster.clicked.connect(lambda: self.selectFile())
        #add row button
        self.ui.toolButton_new_3.clicked.connect(lambda: self._addRow())
        #remove row button
        self.ui.toolButton_remove_3.clicked.connect(lambda:self._removeRow())
        #################
        #limit the year to ints and 4 digits
        onlyInt=QtGui.QIntValidator()
        self.ui.lineEdit_start_year.setValidator(onlyInt) 
        self.ui.lineEdit_end_year.setValidator(onlyInt) 
        self.ui.lineEdit_start_year.setMaxLength(4)
        self.ui.lineEdit_end_year.setMaxLength(4)
        #################

        #define dir for var_generation function
        self.dir=""

        #select raster file
    def selectFile(self):
        filter = "Raster(*.tif)"
        self.fileName = QtWidgets.QFileDialog.getOpenFileName(caption='select a raster file',filter=filter)[0]
        
        self.ui.lineEdit_xyraster.setText(self.fileName)

    def ok_clicked(self):
        self.sam_raster_dir=self.ui.lineEdit_xyraster.text()
        lat,lon,time_v,time_b1,time_b2,dtype,tunit=netCDF_ds.ds_dimensions(
                lat_lon_type="raster",
                lat_lon_source=self.sam_raster_dir,
                time_source=None,
                time_type="time_dic",
                lat_name=None,
                lon_name=None,
                time_name=None,
                border_res_dic=None,
                time_dic={
                    "start":[self.ui.lineEdit_start_year.text(),self.ui.comboBox_start_month.currentText(),self.ui.comboBox_start_day.currentText(),self.ui.comboBox_start_hour.currentText()],
                    "end":[self.ui.lineEdit_end_year.text(),self.ui.comboBox_end_month.currentText(),self.ui.comboBox_end_day.currentText(),self.ui.comboBox_end_hour.currentText()]
                },
                preferred_date_interval=self.ui.comboBox_time_interval.currentText()
            )


        rowCount=self.ui.tableWidget_additional_vars_3.rowCount()
        ds_values_dic={}
        for row in range(rowCount):
           k=self.ui.tableWidget_additional_vars_3.item(row,0)
           v= self.ui.tableWidget_additional_vars_3.item(row,1)
           numstr_list=[str (n) for n in range(0,10)]
           if k!=None:
                if k.text()[0] not in numstr_list:
                    k_text=k.text()
                    if v==None or v.text()[0] in numstr_list: v_text="unknown"
                    else: v_text=v.text()

                    ds_values_dic[k_text]=v_text 

        self.ds=netCDF_ds.var_generation(dir=self.dir,tunit=tunit,lats_np=lat,lons_np=lon,times_np=time_v,time_b1=time_b1,time_b2=time_b2,ds_values_dic=ds_values_dic)
        self.preferred_date_interval=dtype

    def _addRow(self):
        rowCount=self.ui.tableWidget_additional_vars_3.rowCount()
        self.ui.tableWidget_additional_vars_3.insertRow(rowCount)
    
    def _removeRow(self):
        rowCount=self.ui.tableWidget_additional_vars_3.rowCount()
        if rowCount > 0:
            self.ui.tableWidget_additional_vars_3.removeRow(rowCount-1)

############################
#app = QtWidgets.QApplication(sys.argv)

#application = lat_lon_time_dialog_()

#application.show()

#sys.exit(app.exec())