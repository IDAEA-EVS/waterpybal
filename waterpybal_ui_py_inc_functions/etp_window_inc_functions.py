from PyQt6 import QtWidgets,QtCore
from .waterpybal_ui_py.etp_window import Ui_Dialog_etp
from waterpybal.pet_calcs import PET
import sys
from gui_help.gui_help_load import loadhelp

class Ui_Dialog_etp_(QtWidgets.QDialog):

    def __init__(self):
        
        super().__init__()

        self.ui = Ui_Dialog_etp()
        
        self.ui.setupUi(self)
        self.show()
        ##############
        self.ds=None
        ##############
        self.etp_wpb_etp=PET()
        self.methods_dic=self.etp_wpb_etp.methods_dic
        methods_list=[" "]+list(self.methods_dic.keys())
        self.ui.comboBox_etp_method.addItems(methods_list)
        ####################
        #Method combo box and table
        self.ui.comboBox_etp_method.currentTextChanged.connect(lambda: self.update_table())
        ##################
        #to work when it is okeyed
        self.ui.buttonBox.accepted.connect(lambda: self.ok_clicked())

        loadhelp(self,"pet_help.md")

    
    def ok_clicked(self):
        num_of_rows=self.ui.tableWidget_etp_method_params.rowCount()
        raster_etp_var_dic=dict()
        etp_meth_input_dic=dict()
        for i in range(0,num_of_rows):
            par_name=self.ui.tableWidget_etp_method_params.item(i,0).text()
            
            par_type_=self.ui.tableWidget_etp_method_params.cellWidget(i,1)
            if isinstance(par_type_,QtWidgets.QComboBox):
                par_type=par_type_.currentText()

            val_or_path_t=self.ui.tableWidget_etp_method_params.item(i,2)
            if val_or_path_t!=None:
                val_or_path=val_or_path_t.text().strip()
            else: val_or_path=None

            #create raster_etp_var_dic
            if val_or_path=="None":
                etp_meth_input_dic[par_name]=None
            else:    
                if par_type=="Raster":
                    raster_etp_var_dic[par_name]=val_or_path
                    etp_meth_input_dic[par_name]="raster"
                elif par_type=="Dataset":
                    etp_meth_input_dic[par_name]="ds"
                elif par_type=="Constant":
                    etp_meth_input_dic[par_name]=float(val_or_path)
        #execute the method
        
        #print ("raster_etp_var_dic####\n",raster_etp_var_dic)
        #print ("etp_meth_input_dic####\n",etp_meth_input_dic)

        self.ds=PET.pet(self.ds,method=self.new_method,
            raster_etp_var_dic=raster_etp_var_dic,var_name='PET',**etp_meth_input_dic)
      
    ######################
    def update_table(self):
        self.ui.tableWidget_etp_method_params.setRowCount(0)
        
        self.new_method=self.ui.comboBox_etp_method.currentText()
        if self.new_method!=" ":

            new_method_dic=self.methods_dic[self.new_method]

            new_method_list = [[k, str(v)] for k, v in new_method_dic.items()]
            
            #set num of rows
            self.ui.tableWidget_etp_method_params.setRowCount(len(new_method_list))
            
            
            row=0
            for item in new_method_list:
                
                cellinfo_c0=QtWidgets.QTableWidgetItem(item[0])
                cellinfo_c0.setFlags(QtCore.Qt.ItemFlag.ItemIsEnabled)
                self.ui.tableWidget_etp_method_params.setItem(row, 0, cellinfo_c0)
                
                #lat parameter is an exception because lat & lon is defined 1D in dataset
                if item[0] in ["lat", "lon"]:
                    combo_c1 = QtWidgets.QComboBox()
                    if self.ds.single_point=="TRUE":
                        combo_c1.addItems(["Constant"])
                    else:
                        combo_c1.addItems(["Constant","Raster"])
                    self.ui.tableWidget_etp_method_params.setCellWidget(row, 1, combo_c1)

                else:
                #combobox
                    combo_c1 = QtWidgets.QComboBox()
                    if self.ds.single_point=="TRUE":
                        combo_c1.addItems(["Constant","Dataset"])
                    else:
                        combo_c1.addItems(["Constant","Raster","Dataset"])
                    
                    self.ui.tableWidget_etp_method_params.setCellWidget(row, 1, combo_c1)
                
                if item[1]!='obl':
                    cellinfo_c2=QtWidgets.QTableWidgetItem(item[1])
                    self.ui.tableWidget_etp_method_params.setItem(row, 2, cellinfo_c2)
                row += 1


'''app = QtWidgets.QApplication(sys.argv)

application = Ui_Dialog_etp_()

application.show()

sys.exit(app.exec())'''