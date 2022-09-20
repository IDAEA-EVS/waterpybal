from PyQt6 import QtWidgets,QtGui
from swr_window import Ui_Dialog_swr
from waterpybal.pru_calcs import PRU


class Ui_Dialog_swr_(QtWidgets.QDialog):

    def __init__(self):
        
        super().__init__()

        self.ui = Ui_Dialog_swr()
        
        self.ui.setupUi(self)
        self.show()
        ##############
        self.ds=None
        self.single_point=False
        #browse raster button
        self.ui.toolButton_browse_csv.clicked.connect(lambda: self.selectrastFile())
        ##################
        self.ui.groupBox_raster.setStyleSheet("""
            
            QGroupBox::indicator { width: 15px; height: 15px;}
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
        

    #################
    def single_point_mod(self):
        if self.single_point:
            self.ui.groupBox_raster.setChecked(False)
            self.ui.groupBox_raster.setEnabled(False)
    ###############
    #select raster file
    def selectrastFile(self):
        filter = "Raster(*.tif)"
        self.rastfileName = QtWidgets.QFileDialog.getOpenFileName(caption='select raster file',filter=filter)[0]
        self.ui.lineEdit_csv.setText(self.rastfileName)
    ################
    def ok_clicked(self):
        time_steps=None
        raster_PRU_dir=self.ui.lineEdit_csv.text()
        #######
        raster_bands_dic_or_val={}
        print ("self.ui.groupBox_raster.isChecked",self.ui.groupBox_raster.isChecked())
        if self.ui.groupBox_raster.isChecked():
            raster_bands_dic_or_val['pwp']=int(self.ui.lineEdit_pwp.text())
            raster_bands_dic_or_val['cc']=int(self.ui.lineEdit_cc.text())
            raster_bands_dic_or_val['rrt']=int(self.ui.lineEdit_rrt.text())
        else:
            raster_bands_dic_or_val['pwp']=float(self.ui.lineEdit_pwp_val.text())
            raster_bands_dic_or_val['cc']=float(self.ui.lineEdit_cc_val.text())
            raster_bands_dic_or_val['rrt']=float(self.ui.lineEdit_rrt_val.text())
            #to add single point values to db
            self.ds=self.single_val_to_netcdf(self.ds,raster_bands_dic_or_val)
            raster_PRU_dir=None
        
        self.ds=PRU.PRu_calc(self.ds,time_steps,raster_PRU_dir,raster_bands_dic_or_val)
    
    ################
    #to add single point values to db
    def single_val_to_netcdf(self,ds,raster_bands_dic_or_val):
        ds["pwp"][:,:,:]=raster_bands_dic_or_val['pwp']
        ds["cc"][:,:,:]=raster_bands_dic_or_val["cc"]
        ds["rrt"][:,:,:]=raster_bands_dic_or_val["rrt"]

        return ds