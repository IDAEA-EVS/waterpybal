from PyQt6 import QtWidgets
from var_from_tiff import Ui_Dialog_var_from_tiff
from waterpybal.dataset_prep import netCDF_ds


class Ui_Dialog_var_from_tiff_(QtWidgets.QDialog):

    def __init__(self):
        
        super().__init__()

        self.ui = Ui_Dialog_var_from_tiff()
        
        self.ui.setupUi(self)
        
        self.show()
        ##############
        self.ui.toolButton.clicked.connect(self.selectFolder)
        ##############
        self.ds=None
        self.preferred_date_interval=None
        ##############
        #to work when it is okeyed
        self.ui.buttonBox_from_tiff.accepted.connect(lambda: self.ok_clicked())
    #function to list the variables
    def updatelist_vars(self):
        try:
            list_vars=list(self.ds.variables.keys())
            dims_list=["time_bnds","time","lat","lon"]
            list_vars=[n for n in list_vars if n not in dims_list]
            self.ui.comboBox.addItems(list_vars)
        except: pass    
    #######################################
    def selectFolder(self):
        self.Folder_dir = QtWidgets.QFileDialog.getExistingDirectory(caption='select a directory')
        
        self.ui.lineEdit_var_path.setText(self.Folder_dir)
    #######################################
    def ok_clicked(self):
        folder_dir=self.ui.lineEdit_var_path.text()
        var_name=self.ui.comboBox.currentText()
        preferred_date_interval=self.preferred_date_interval
        
        self.ds=netCDF_ds.var_introduction_from_tiffs(self.ds,folder_dir,var_name,preferred_date_interval)