from PyQt6 import QtWidgets,QtGui
from gui_help.gui_help_load import loadhelp
from .waterpybal_ui_py.swr_window import Ui_Dialog_swr
from waterpybal.swr_calcs import SWR


class Ui_Dialog_swr_(QtWidgets.QDialog):

    def __init__(self):
        
        super().__init__()

        self.ui = Ui_Dialog_swr()
        
        self.ui.setupUi(self)
        self.show()
        ##############
        self.ds=None
        #browse raster button
        self.ui.toolButton_browse_csv.clicked.connect(lambda: self.selectrastFile())
        ##################

        self.ui.checkBox_raster.setStyleSheet("""

            QCheckBox::indicator { width: 15px; height: 15px;}
            }
        """)
        self.ui.checkbox_ds_vals.setStyleSheet("""

            QCheckBox::indicator { width: 15px; height: 15px;}
            }
        """)
        ##################
        #to work when it is okeyed
        self.ui.buttonBox.accepted.connect(lambda: self.ok_clicked())
        #################
        #limit the year to ints and 5 digits
        onlyInt=QtGui.QIntValidator()
        self.ui.lineEdit_cc.setValidator(onlyInt) 
        self.ui.lineEdit_pwp.setValidator(onlyInt) 
        self.ui.lineEdit_rrt.setValidator(onlyInt) 
        self.ui.lineEdit_cc.setMaxLength(3)
        self.ui.lineEdit_pwp.setMaxLength(3)
        self.ui.lineEdit_rrt.setMaxLength(3)
        onlydoub=QtGui.QDoubleValidator()
        self.ui.lineEdit_cc_val.setValidator(onlydoub) 
        self.ui.lineEdit_pwp_val.setValidator(onlydoub) 
        self.ui.lineEdit_rrt_val.setValidator(onlydoub) 
        self.ui.lineEdit_cc_val.setMaxLength(5)
        self.ui.lineEdit_pwp_val.setMaxLength(5)
        self.ui.lineEdit_rrt_val.setMaxLength(5)
        #################
        self.ui.checkBox_raster.stateChanged.connect(lambda: self.statechange_checkBox_raster())
        self.ui.checkbox_ds_vals.stateChanged.connect(lambda: self.statechange_checkBox_ds_vals())


        loadhelp(self,"swr_help.md")

    #################
    def statechange_checkBox_raster(self):
        if self.ui.checkBox_raster.isChecked():
            self.ui.groupBox_raster.setEnabled(True)
            self.ui.checkbox_ds_vals.setChecked(False)
            self.ui.groupBox_single_values.setEnabled(False)

        else:
            self.ui.groupBox_raster.setEnabled(False)
            self.ui.groupBox_single_values.setEnabled(True)

    def statechange_checkBox_ds_vals(self):
        if self.ui.checkbox_ds_vals.isChecked():
            self.ui.groupBox_raster.setEnabled(False)
            
            self.ui.checkBox_raster.setChecked(False)
            self.ui.groupBox_single_values.setEnabled(False)

        else:
            self.ui.groupBox_single_values.setEnabled(True)
    #################
    def single_point_mod(self):
        if self.ds.single_point=="TRUE":
            self.ui.checkBox_raster.setChecked(False)
            self.ui.checkBox_raster.setEnabled(False)
            self.ui.groupBox_raster.setEnabled(False)
            self.ui.groupBox_single_values.setEnabled(True)
        else:
            self.ui.checkBox_raster.setChecked(True)
            self.ui.checkBox_raster.setEnabled(True)
            self.ui.groupBox_raster.setEnabled(True)
    ###############
    #select raster file
    def selectrastFile(self):
        filter = "Raster(*.tif)"
        self.rastfileName = QtWidgets.QFileDialog.getOpenFileName(caption='select raster file',filter=filter)[0]
        self.ui.lineEdit_csv.setText(self.rastfileName)
    ################
    def ok_clicked(self):
        
        
        #######
        raster_bands_dic_or_val={}

        if self.ui.checkBox_raster.isChecked(): #raster

            raster_SWR_dir=self.ui.lineEdit_csv.text()
            time_steps=None

            raster_bands_dic_or_val['pwp']=int(self.ui.lineEdit_pwp.text())
            raster_bands_dic_or_val['cc']=int(self.ui.lineEdit_cc.text())
            raster_bands_dic_or_val['rrt']=int(self.ui.lineEdit_rrt.text())
        
        elif self.ui.checkbox_ds_vals.isChecked(): #use the dataset values 
            raster_SWR_dir=None
            time_steps="all"


        else: #same value
            raster_SWR_dir=None
            time_steps=None

            raster_bands_dic_or_val['pwp']=float(self.ui.lineEdit_pwp_val.text())
            raster_bands_dic_or_val['cc']=float(self.ui.lineEdit_cc_val.text())
            raster_bands_dic_or_val['rrt']=float(self.ui.lineEdit_rrt_val.text())
            #to add single point values to db
            self.ds=self.single_val_to_netcdf(self.ds,raster_bands_dic_or_val)
            
            
        self.ds=SWR.swr(self.ds,time_steps,raster_SWR_dir,raster_bands_dic_or_val)
    
    ################
    #to add single point values to db
    def single_val_to_netcdf(self,ds,raster_bands_dic_or_val):
        ds["pwp"][:,:,:]=raster_bands_dic_or_val['pwp']
        ds["cc"][:,:,:]=raster_bands_dic_or_val["cc"]
        ds["rrt"][:,:,:]=raster_bands_dic_or_val["rrt"]

        return ds