from PyQt6 import QtWidgets,QtGui
from waterpybal_ui_py_inc_functions.waterpybal_ui_py.balance import Ui_balance_Dialog
from waterpybal.balance_calcs import balance
#from waterpybal.balance_calcs import balance #meth balance_calculation_main
import sys
import inspect



class Ui_balance_Dialog_(QtWidgets.QDialog):

    def __init__(self):
        
        super().__init__()

        self.ui = Ui_balance_Dialog()
        
        self.ui.setupUi(self)
        self.show()
        ##############
        self.ds=None
        ##############
        #limit the year to ints and 4 digits
        onlyflt=QtGui.QDoubleValidator(bottom=0,top=100,decimals=2)
        self.ui.lineEdit_init_swr.setValidator(onlyflt) 
        self.ui.lineEdit_init_swr.setMaxLength(5)
        #self.ui.toolButton_raster.clicked.connect(lambda: self.selectrastFile())
        #to work when it is okeyed
        self.ui.buttonBox.accepted.connect(lambda: self.ok_clicked())
    #select raster file
    '''def selectrastFile(self):
        filter = "Raster(*.tif)"
        self.rastfileName = QtWidgets.QFileDialog.getOpenFileName(caption='select a raster file',filter=filter)[0]
        
        self.ui.lineEdit_raster.setText(self.rastfileName)
        '''
    ##########################
    def ok_clicked(self):
        init_swr=self.ui.lineEdit_init_swr.text()
        self.ds=balance.balance_calculation_main(self.ds,predef_ru_dir_or_np=None,predef_ru_type="dataset",init_swr=init_swr)