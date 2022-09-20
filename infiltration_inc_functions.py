from PyQt6 import QtWidgets,QtGui,QtCore
from infiltration import Ui_Dialog_infiltration
from waterpybal.inf_calcs import infiltration
from waterpybal.urban_infiltration import urban_infiltration_calcs


class Ui_Dialog_infiltration_(QtWidgets.QDialog):

    def __init__(self):
        
        super().__init__()

        self.ui = Ui_Dialog_infiltration()
        
        self.ui.setupUi(self)

        self.table_maker()
        self.show()
        
        #################
        self.ds=None
        self.preferred_date_interval=None
        self.single_point=False
        self.urban_ds=False
        ##############
        #browse button
        self.ui.toolButton_browse_cn_csv.clicked.connect(lambda: self.selectcsvFile())
        ##############
        #browse raster button
        self.ui.toolButton_browse_cn_raster.clicked.connect(lambda: self.selectrastFilecn())
        ##################
        #browse raster button
        self.ui.toolButton_browse_urban_zone_raster.clicked.connect(lambda: self.selectrastFileurban())
        ##################
        #to work when it is okeyed
        self.ui.buttonBox.accepted.connect(lambda: self.ok_clicked())
        ##################
        #direct cn value introduction (single point and etc)
        self.ui.checkBox_cn_value.stateChanged.connect(lambda:self.cn_val_state())
        #limit the year to ints and 4 digits
        onlyInt=QtGui.QIntValidator()
        self.ui.lineEdit_elev.setValidator(onlyInt) 
        self.ui.lineEdit_lu.setValidator(onlyInt) 
        self.ui.lineEdit_hsg.setValidator(onlyInt) 
        self.ui.lineEdit_elev.setMaxLength(4)
        self.ui.lineEdit_lu.setMaxLength(4)
        self.ui.lineEdit_hsg.setMaxLength(4)
        self.ui.groupBox_curve_number.setStyleSheet("""
            
            QGroupBox::indicator { width: 15px; height: 15px;}
            }
        """)

        self.ui.checkBox_cn_value.setStyleSheet("""
            
            QCheckBox::indicator { width: 15px; height: 15px;}
            }
        """)
        self.ui.groupBox_urban.setStyleSheet("""
            
            QGroupBox::indicator { width: 15px; height: 15px;}
            }
        """)
        onlydoub=QtGui.QDoubleValidator()
        self.ui.lineEdit_CN_Val.setValidator(onlydoub) 
        self.ui.lineEdit_CN_Val.setMaxLength(4) 

        #################
        
    def table_maker(self):
        _translate = QtCore.QCoreApplication.translate
        
        var_verticalHeader=["Water Consumption (mm)",
        "Water Consumption NOT from network (Wells,etc.) (mm)",
        "Water from other sources (underground infrustructures,etc.) (mm)",
        "Water Network Loss (%)",
        "Water Consumption NOT from network loss (%)",
        "Sewage Network Loss normal (%)",
        "Sewage Network Loss rainy season (%)",
        "threshold of rainy season per time step for sewage loss (mm)",
        "Run-off to Sewage (%)",
        "Indirect Urban Evaporation (% of water consumption)",
        "Direct Urban Evaporation (% of water precipitation+irrigation)",
        "Direct Infiltration (% of water precipitation+irrigation)",
        "Urban to calculated Infiltration and Evapotranspiration ratio"]
        
        self.ui.tableWidget_urban.setColumnCount(3)
        self.ui.tableWidget_urban.setRowCount(len(var_verticalHeader))
        ####
        var_horizHeader=["Parameter","Type","Value or Path"]
        for n,horiz_head in enumerate(var_horizHeader):
            item = QtWidgets.QTableWidgetItem()
            self.ui.tableWidget_urban.setHorizontalHeaderItem(n, item)
            item = self.ui.tableWidget_urban.horizontalHeaderItem(n)
            item.setText(_translate("Dialog_infiltration", horiz_head))
        ####        
        '''for n,vert_head in enumerate(var_verticalHeader):
            item = QtWidgets.QTableWidgetItem()
            self.ui.tableWidget_urban.setVerticalHeaderItem(n, item)

            item = self.ui.tableWidget_urban.verticalHeaderItem(n)
            item.setText(_translate("Dialog_infiltration", vert_head))
        '''
        ####
        for n,vert_head in enumerate(var_verticalHeader):
            item = QtWidgets.QTableWidgetItem(vert_head)
            item.setFlags(QtCore.Qt.ItemFlag.ItemIsEnabled)
            self.ui.tableWidget_urban.setItem(n, 0, item)

        ####
        __sortingEnabled = self.ui.tableWidget_urban.isSortingEnabled()
        
        self.ui.tableWidget_urban.setSortingEnabled(False)
        ####
        for i in range(0,len(var_verticalHeader)):
            item = QtWidgets.QTableWidgetItem()
            self.ui.tableWidget_urban.setItem(i, 2, item)
            item = self.ui.tableWidget_urban.item(i, 2)
            #exception for the urban to ds ratio
            if i!=12:
                item.setText(_translate("Dialog_infiltration", "0"))
            else:
                item.setText(_translate("Dialog_infiltration", "100"))
        ####
        self.ui.tableWidget_urban.setSortingEnabled(__sortingEnabled)

    ##########################
    def cn_val_state(self):
        if self.ui.checkBox_cn_value.isChecked():
            self.ui.label_cn_val.setEnabled(True)
            self.ui.lineEdit_CN_Val.setEnabled(True)
            self.ui.groupBox_curve_number.setChecked(False)
            self.ui.groupBox_curve_number.setEnabled(False)
            self.single_cn_val=True

        
        
        if self.ui.checkBox_cn_value.isChecked()==False:
            self.ui.label_cn_val.setEnabled(False)
            self.ui.lineEdit_CN_Val.setEnabled(False)
            
            if self.single_point==False:
                self.ui.groupBox_curve_number.setEnabled(True)
                self.ui.groupBox_curve_number.setChecked(True)
            
            self.single_cn_val=False
            

    
    ##########################
    def check_single_point(self):
        if self.single_point:

            self.ui.groupBox_corrected_cn.setChecked(False)
            self.ui.groupBox_raster.setChecked(False)
            self.ui.groupBox_curve_number.setChecked(False)
            self.ui.groupBox_curve_number.setEnabled(False) 
            
            self.ui.checkBox_cn_value.setChecked(True)
            self.single_cn_val=True

            self.ui.lineEdit_urban_zone_raster.setEnabled(False) 
            self.ui.toolButton_browse_urban_zone_raster.setEnabled(False) 
            self.ui.label_urban_zone_raster.setEnabled(False) 
    ##########################
    def check_timesteps(self):
        
        self.Calc_CN=True
        # CN method not available
        if self.preferred_date_interval not in ["datetime64[D]","daily","Daily"]:
            self.Calc_CN=False
            self.ui.groupBox_curve_number.setChecked(False)
            self.ui.checkBox_cn_value.setChecked(False)  
            self.ui.groupBox_corrected_cn.setChecked(False)            
            self.ui.groupBox_raster.setChecked(False)            
          
            self.ui.groupBox_curve_number.setEnabled(False)    
            self.ui.checkBox_cn_value.setEnabled(False)
            self.ui.label_cn_val.setEnabled(False)
            self.ui.lineEdit_CN_Val.setEnabled(False)
    ##########################
    def check_urban(self):
        if self.urban_ds:
             
            self.ui.label_urban_zone_raster.setEnabled(True) 
            self.ui.tableWidget_urban.setEnabled(True) 
            
            self.ui.groupBox_urban.setEnabled(True) 
            self.ui.groupBox_urban.setChecked(False)
        
    ##########################
    def update_urban_table(self):
        
        for row in range(0,13):
            combo_c1 = QtWidgets.QComboBox()
            if self.single_point:
                combo_c1.addItems(["Constant","Dataset"])
            else:
                combo_c1.addItems(["Constant","Raster","Dataset"])
            self.ui.tableWidget_urban.setCellWidget(row, 1, combo_c1)
    ##########################
    def selectcsvFile(self):
        filter = "CSV(*.csv)"
        self.fileName = QtWidgets.QFileDialog.getOpenFileName(caption='select a .CSV file',filter=filter)[0]
        
        self.ui.lineEdit_cn_csv.setText(self.fileName)
    ##########################
    #select raster file cn
    def selectrastFilecn(self):
        filter = "Raster(*.tif)"
        self.rastfileName = QtWidgets.QFileDialog.getOpenFileName(caption='select a raster file',filter=filter)[0]
        
        self.ui.lineEdit_cn_raster.setText(self.rastfileName)
    ##########################
    #select raster file urban
    def selectrastFileurban(self):
        filter = "Raster(*.tif)"
        self.rastfileName = QtWidgets.QFileDialog.getOpenFileName(caption='select a raster file',filter=filter)[0]
        
        self.ui.lineEdit_urban_zone_raster.setText(self.rastfileName)    
    ##########################
    def ok_clicked(self):
        #calculating infiltration
        CN_table_dir=self.ui.lineEdit_cn_csv.text()
        raster_dir=self.ui.lineEdit_cn_raster.text()
        HSG_band=self.ui.lineEdit_hsg.text()
        LU_band=self.ui.lineEdit_lu.text()
        ELEV_band=self.ui.lineEdit_elev.text()
        DEM_or_raster="raster"
        DEM_path_or_raster=raster_dir
        filled_dep=True
        try: slope_range_list=[float(n) for n in self.ui.lineEdit_slope.text().split(',')]
        except: slope_range_list=list()

        if self.ui.groupBox_corrected_cn.isChecked():
    
            amc1_coeffs=[float(n) for n in self.ui.lineEdit_amc1.text().split(',')]
            amc3_coeffs=[float(n) for n in self.ui.lineEdit_amc3.text().split(',')]
            dormant_thresh=[float(n) for n in self.ui.lineEdit_dormant.text().split(',')]
            growing_thresh=[float(n) for n in self.ui.lineEdit_growing.text().split(',')]
            mon_list_dormant=[float(n) for n in self.ui.lineEdit_dormant_month.text().split(',')]
            if self.ui.comboBox_average.currentText()=='Yes': average_thresh=True
            else: average_thresh=False
            corrected_cn=True
            print ("groupBox_corrected_cn is true")

        else:
            amc1_coeffs=None
            amc3_coeffs=None
            dormant_thresh=None
            growing_thresh=None
            mon_list_dormant=None
            average_thresh=None
            corrected_cn=False

            print ("groupBox_corrected_cn is false")

        preferred_date_interval=self.preferred_date_interval
        
        threshold=self.ui.lineEdit__max_infilt.text()
        
        #check for self.Calc_CN:
        if self.ui.checkBox_cn_value.isChecked()==False and self.ui.groupBox_curve_number.isChecked()==False:
            self.Calc_CN=False
        
        if self.Calc_CN==True:  

            if self.single_cn_val:
                self.cn_val=float(self.ui.lineEdit_CN_Val.text())
            else: 
                self.cn_val=None

            self.ds,Ia=infiltration.Inf_calc(self.ds,CN_table_dir,raster_dir,HSG_band,LU_band,ELEV_band,DEM_path_or_raster,DEM_or_raster,filled_dep,slope_range_list,amc1_coeffs,amc3_coeffs,dormant_thresh,growing_thresh,average_thresh,mon_list_dormant,preferred_date_interval,corrected_cn,self.single_cn_val,self.cn_val)
            # max infiltration threshold per timestep
            var_inp="INF_Val"
            var_out="INF_Val"

        else:
            # max infiltration threshold per timestep
            var_inp="Prec_Val"
            var_out="INF_Val"
            Ia=None

        if self.ui.groupBox_urban.isChecked():
            variables_dic=self.urban_inf_dic_gen()
            urban_area_raster_dir=self.ui.lineEdit_urban_zone_raster.text()

            self.ds=urban_infiltration_calcs.urban_infiltration_main(self.ds,urban_area_raster_dir,variables_dic) 


        self.ds=infiltration.max_inf_threshold(self.ds,var_inp,var_out,threshold) 
        self.ds=infiltration.runoff_calc(self.ds,Ia)

    ##########################
    def urban_inf_dic_gen(self):
        num_of_rows=self.ui.tableWidget_urban.rowCount()
        variables_dic={}
        for i in range(0,num_of_rows):
            var_dic={}
            
            
            var_dic["dataset_raster_dir_or_value"]=self.ui.tableWidget_urban.cellWidget(i,1)
            
            
            val_or_path_t=self.ui.tableWidget_urban.item(i,2)
            if val_or_path_t!=None:
                val_or_path=val_or_path_t.text()
            else: val_or_path=None

            var_dic["input_var"]=val_or_path
            
            variable_name=self.ui.tableWidget_urban.item(i,0).text()
            
            if variable_name=="Water Consumption (mm)": variable_name="wat_cons"
            elif variable_name=="Water Network Loss (%)": variable_name="wat_net_loss"
            elif variable_name=="Sewage Network Loss normal (%)": variable_name="sew_net_loss_low" 
            elif variable_name=="Sewage Network Loss rainy season (%)": variable_name="sew_net_loss_high" 
            elif variable_name=="threshold of rainy season per time step for sewage loss (mm)": variable_name="prec_sewage_threshold" #
            elif variable_name=="Water Consumption NOT from network (Wells,etc.) (mm)": variable_name="wat_supp_wells" 
            elif variable_name=="Water Consumption NOT from network loss (%)": variable_name="wat_supp_wells_loss" 
            elif variable_name=="Water from other sources (underground infrustructures,etc.) (mm)": variable_name="wat_other" 
            elif variable_name=="Run-off to Sewage (%)": variable_name="runoff_to_sewage"
            elif variable_name=="Indirect Urban Evaporation (% of water consumption)": variable_name="urb_indir_evap"
            elif variable_name=="Direct Urban Evaporation (% of water precipitation+irrigation)": variable_name="urb_dir_evap"
            elif variable_name=="Direct Infiltration (% of water precipitation+irrigation)": variable_name="dir_infil"
            elif variable_name=="Urban to calculated Infiltration and Evapotranspiration ratio": variable_name="urban_to_ds_inf_etp_ratio"

            variables_dic[variable_name]=var_dic
        
        return variables_dic


