from PyQt6 import QtWidgets,QtGui

from .waterpybal_ui_py.open_dataset import Ui_Dialog_open_dataset
import os
import sys
import netCDF4 as nc


class Ui_Dialog_open_dataset_(QtWidgets.QDialog):

    def __init__(self):
        
        super().__init__()

        self.ui = Ui_Dialog_open_dataset()
        
        self.ui.setupUi(self)
        self.show()
        ##############
        self.ui.toolButton_open.clicked.connect(lambda: self.open_ds())
        self.ui.toolButton_browse_xy_raster.clicked.connect(lambda:self.selectrastFile())

        self.ui.checkBox_single_point.setStyleSheet("""
            QCheckBox {
                font-size: 13px;
            }
            QCheckBox::indicator { width: 15px; height: 15px;}
            }
        """)
        ##################
        #to work when it is okeyed
        self.ui.buttonBox.accepted.connect(lambda: self.ok_clicked())
        
        self.ui.checkBox_single_point.stateChanged.connect(lambda: self.single_p_checked())
    
    ##########################
    def single_p_checked(self):
        if self.ui.checkBox_single_point.isChecked()==True:
            self.ui.label_sample_raster.setEnabled(False)
            self.ui.lineEdit_sample_raster.setEnabled(False)
            self.ui.toolButton_browse_xy_raster.setEnabled(False)
            self.single_point=True
        if self.ui.checkBox_single_point.isChecked()==False:
            self.ui.label_sample_raster.setEnabled(True)
            self.ui.lineEdit_sample_raster.setEnabled(True)
            self.ui.toolButton_browse_xy_raster.setEnabled(True)
            self.single_point=False

    ##########################
    def open_ds(self):
        filter = "NETCDF(*.nc)"
        self.dsName = QtWidgets.QFileDialog.getOpenFileName(caption='select a NETCDF (.nc) database',filter=filter)[0]
        
        self.ui.lineEdit_open.setText(self.dsName)
    
    ##########################
    #select raster file
    def selectrastFile(self):
        filter = "Raster(*.tif)"
        self.rastfileName = QtWidgets.QFileDialog.getOpenFileName(caption='select a raster file',filter=filter)[0]
        
        self.ui.lineEdit_sample_raster.setText(self.rastfileName)
    
    ###########################
    def ok_clicked(self):
        self.sam_raster_dir=self.ui.lineEdit_sample_raster.text()
        self.ds_dir=self.ui.lineEdit_open.text()
        preferred_date_interval=self.ui.comboBox_time_interval.currentText()
        if preferred_date_interval=="Daily":self.preferred_date_interval='datetime64[D]'
        if preferred_date_interval=="Monthly":self.preferred_date_interval='datetime64[M]'
        if preferred_date_interval=="Hourly":self.preferred_date_interval='datetime64[h]'
        
