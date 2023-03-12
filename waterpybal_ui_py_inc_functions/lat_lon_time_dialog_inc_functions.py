from PyQt6 import QtWidgets,QtGui

from .waterpybal_ui_py.lat_lon_time_dialog import Ui_Dialog_lat_lon_time
import os
import sys
from waterpybal.dataset_prep import dataset_gen
from gui_help.gui_help_load import loadhelp


class lat_lon_time_dialog_(QtWidgets.QDialog):

    def __init__(self):
        
        super().__init__()

        self.ui = Ui_Dialog_lat_lon_time()
        
        self.ui.setupUi(self)
        self.single_p_checked()
        self.show()
        ##############

        loadhelp(self,"new_dataset_properties_help.md")
        
        ##############
        #to work when it is okeyed
        self.ui.buttonBox.accepted.connect(lambda: self.ok_clicked())
        
        #single point
        self.ui.checkBox_single_point.stateChanged.connect(lambda: self.single_p_checked())

        #to select file
        self.ui.toolButton_browse_xy_raster.clicked.connect(lambda: self.selectFile())
        #add row button
        self.ui.toolButton_new_3.clicked.connect(lambda: self._addRow())
        #remove row button
        self.ui.toolButton_remove_3.clicked.connect(lambda:self._removeRow())
        #################
        #limit the year to ints and 4 digits
        onlyInt=QtGui.QIntValidator()
        self.ui.lineEdit_start_year.setValidator(onlyInt) 
        self.ui.lineEdit_end_year.setValidator(onlyInt) 
        self.ui.lineEdit_start_year.setMaxLength(4)
        self.ui.lineEdit_end_year.setMaxLength(4)
        #################
        self.ui.checkBox_single_point.setStyleSheet("""
            QCheckBox {
                font-size: 13px;
            }
            QCheckBox::indicator { width: 15px; height: 15px;}
            }
        """)
        self.ui.checkBox_urban.setStyleSheet("""
            QCheckBox {
                font-size: 13px;
            }
            QCheckBox::indicator { width: 15px; height: 15px;}
            }
        """)
        #define dir for var_generation function
        self.dir=""

        


    ##########################
    def single_p_checked(self):
        if self.ui.checkBox_single_point.isChecked()==True:
            self.ui.label_xy_raster.setEnabled(False)
            self.ui.lineEdit_xyraster.setEnabled(False)
            self.ui.toolButton_browse_xy_raster.setEnabled(False)
            self.single_point=True
        if self.ui.checkBox_single_point.isChecked()==False:
            self.ui.label_xy_raster.setEnabled(True)
            self.ui.lineEdit_xyraster.setEnabled(True)
            self.ui.toolButton_browse_xy_raster.setEnabled(True)
            self.single_point=False
    
    ##########################
    
    
    
    #select raster file
    def selectFile(self):
        filter = "Raster(*.tif)"
        self.fileName = QtWidgets.QFileDialog.getOpenFileName(caption='select a raster file',filter=filter)[0]
        
        self.ui.lineEdit_xyraster.setText(self.fileName)

    def ok_clicked(self):

        time_dic={
                    "start":[str(self.ui.lineEdit_start_year.text()),str(self.ui.comboBox_start_month.currentText()),str(self.ui.comboBox_start_day.currentText()),str(self.ui.comboBox_start_hour.currentText())],
                    "end":[str(self.ui.lineEdit_end_year.text()),str(self.ui.comboBox_end_month.currentText()),str(self.ui.comboBox_end_day.currentText()),str(self.ui.comboBox_end_hour.currentText())]
                }
        for se in time_dic.values():
            for i in range(1,4):
                if len(se[i])==1: se[i]="0"+se[i]
                elif len(se[i])==3: se[i]=se[i][1:]

        print ("time_dic",time_dic)
        time_type="time_dic"  
        preferred_date_interval=self.ui.comboBox_time_interval.currentText()
        
        if self.ui.checkBox_urban.isChecked()==True:
            self.urban_ds=True
        else:
            self.urban_ds=False


        dataset_cl=dataset_gen()

        if self.single_point==False:
            self.sam_raster_dir=self.ui.lineEdit_xyraster.text()

            
            lat_lon_type="raster"

            
                        
            
            dtype=dataset_cl.ds_dimensions(

                lat_lon_type=lat_lon_type,
                lat_lon_source=self.sam_raster_dir,
                time_source=None,
                time_type=time_type,
                preferred_date_interval=preferred_date_interval,
                lat_name=None,
                lon_name=None,
                time_name=None,
                border_res_dic=None,
                time_dic=time_dic,
                single_point=self.single_point   
            )

        else:
            
            lat_lon_type=None
            border_res_dic=None


            dtype=dataset_cl.ds_dimensions(
                lat_lon_type=lat_lon_type,
                lat_lon_source=None,
                time_source=None,
                time_type=time_type,
                preferred_date_interval=preferred_date_interval,
                lat_name="lat",
                lon_name="lon",
                time_name=None,
                border_res_dic=border_res_dic,
                time_dic=time_dic,
                single_point=self.single_point
            )

        #self.preferred_date_interval=dtype

        ds_values_dic=self.new_var_to_ds()
        
        print ("dataset_cl.time", dataset_cl.time)

        self.ds=dataset_cl.var_generation(dir=self.dir,ds_values_dic=ds_values_dic,urban_ds=self.urban_ds)

        print ("self.ds['time'][:]",self.ds["time"][:])

    #######
    def new_var_to_ds(self):
        rowCount=self.ui.tableWidget_additional_vars_3.rowCount()
        ds_values_dic={}
        for row in range(rowCount):
           k=self.ui.tableWidget_additional_vars_3.item(row,0)
           v= self.ui.tableWidget_additional_vars_3.item(row,1)
           numstr_list=[str (n) for n in range(0,10)]
           if k!=None:
                if k.text()[0] not in numstr_list:
                    k_text=k.text()
                    if v==None or v.text()[0] in numstr_list: v_text="unknown"
                    else: v_text=v.text()

                    ds_values_dic[k_text]=v_text 
        return ds_values_dic
        
    #######
    def _addRow(self):
        rowCount=self.ui.tableWidget_additional_vars_3.rowCount()
        self.ui.tableWidget_additional_vars_3.insertRow(rowCount)
    
    #######
    def _removeRow(self):
        rowCount=self.ui.tableWidget_additional_vars_3.rowCount()
        if rowCount > 0:
            self.ui.tableWidget_additional_vars_3.removeRow(rowCount-1)

############################
#app = QtWidgets.QApplication(sys.argv)

#application = lat_lon_time_dialog_()

#application.show()

#sys.exit(app.exec())