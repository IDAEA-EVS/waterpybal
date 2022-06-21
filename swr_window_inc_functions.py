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
        #browse raster button
        self.ui.toolButton_browse_csv.clicked.connect(lambda: self.selectrastFile())
        ##################
        #to work when it is okeyed
        self.ui.buttonBox.accepted.connect(lambda: self.ok_clicked())
        #################
        #limit the year to ints and 4 digits
        onlyInt=QtGui.QIntValidator()
        self.ui.lineEdit_cc.setValidator(onlyInt) 
        self.ui.lineEdit_pwp.setValidator(onlyInt) 
        self.ui.lineEdit_rrt.setValidator(onlyInt) 
        self.ui.lineEdit_cc.setMaxLength(4)
        self.ui.lineEdit_pwp.setMaxLength(4)
        self.ui.lineEdit_rrt.setMaxLength(4)
        #################


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
        raster_bands_dic={}
        raster_bands_dic['pwp']=int(self.ui.lineEdit_pwp.text())
        raster_bands_dic['cc']=int(self.ui.lineEdit_cc.text())
        raster_bands_dic['rrt']=int(self.ui.lineEdit_rrt.text())
        
        self.ds=PRU.PRu_calc(self.ds,time_steps,raster_PRU_dir,raster_bands_dic)