from PyQt6 import QtWidgets,QtCore
from balance import Ui_balance_Dialog
from waterpybal.balance_calcs import balance #meth balance_calculation_main
import sys

class Ui_balance_Dialog_(QtWidgets.QDialog):

    def __init__(self):
        
        super().__init__()

        self.ui = Ui_balance_Dialog()
        
        self.ui.setupUi(self)
        self.show()
        ##############
        self.ds=None
        ##############
        self.ui.toolButton_raster.clicked.connect(lambda: self.selectrastFile())
        #to work when it is okeyed
        self.ui.buttonBox.accepted.connect(lambda: self.ok_clicked())
    #select raster file
    def selectrastFile(self):
        filter = "Raster(*.tif)"
        self.rastfileName = QtWidgets.QFileDialog.getOpenFileName(caption='select a raster file',filter=filter)[0]
        
        self.ui.lineEdit_raster.setText(self.rastfileName)
    ##########################
    def ok_clicked(self):
        ras_dir=self.ui.lineEdit_raster.text()
        self.ds=balance.balance_calculation_main(self.ds,predef_ru_dir_or_np=ras_dir,predef_ru_type="raster")