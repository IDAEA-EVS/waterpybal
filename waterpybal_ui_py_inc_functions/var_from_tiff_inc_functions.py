from PyQt6 import QtWidgets
from .waterpybal_ui_py.var_from_tiff import Ui_Dialog_var_from_tiff
from waterpybal.dataset_prep import variable_management
from gui_help.gui_help_load import loadhelp


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

        #########################
        self.ui.checkBox.setStyleSheet("""
            QCheckBox {
                font-size: 13px;
            }
            QCheckBox::indicator { width: 15px; height: 15px;}
            }
        """)
        loadhelp(self,"import_from_tiff_help.md")
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
        if self.ui.checkBox.isChecked()==False:
            multiply=True
        if self.ui.checkBox.isChecked()==True:
            multiply=False

        self.ds=variable_management.var_introduction_from_tiffs(self.ds,folder_dir,var_name,preferred_date_interval,multiply)