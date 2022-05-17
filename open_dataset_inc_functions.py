from PyQt6 import QtWidgets,QtGui

from open_dataset import Ui_Dialog_open_dataset
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

        ##################
        #to work when it is okeyed
        self.ui.buttonBox.accepted.connect(lambda: self.ok_clicked())

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
        self.preferred_date_interval=self.ui.comboBox_time_interval.currentText()
        
