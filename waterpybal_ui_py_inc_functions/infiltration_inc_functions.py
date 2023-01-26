from PyQt6 import QtWidgets,QtGui,QtCore
from .waterpybal_ui_py.infiltration import Ui_Dialog_infiltration
from waterpybal.inf_calcs import infiltration
from waterpybal.urban_cycle import urban_cycle_calcs,urban_Composite_CN_correction
from gui_help.gui_help_load import loadhelp
import numpy as np


class Ui_Dialog_infiltration_(QtWidgets.QDialog):

    def __init__(self):
        
        super().__init__()

        self.ui = Ui_Dialog_infiltration()
        
        self.ui.setupUi(self)

        self.show()

        #################
        #set variables
        self.ds=None
        self.preferred_date_interval=None
        self.single_point=False
        self.urban_ds=False
        self.single_cn_val=False
        ##############
        #connect the clicks to functions
        self.clickconnect()

        ##################
        #limit the line edits with validators:
        self.lineeditvalidator()
        ##################
        #set style sheet
        self.stylesheetset()
        ##################
        #set cn table
        self.ui.lineEdit_cn_csv.setText("curve_number_standard_table.xls")

        loadhelp(self,"infiltration_help.md")


    ########################################################################################################
    ########################################################################################################
    ########################################################################################################

    #connect the clicks to functions
    def clickconnect(self):
        #slope cat checkbox statchange
        self.ui.checkBox_slope_cat.stateChanged.connect(lambda: self.slopecat_statchange())
        #browse button
        self.ui.toolButton_browse_cn_csv.clicked.connect(lambda: self.selectcsvFile())
        ##############
        #browse raster button curve number
        self.ui.toolButton_browse_cn_raster.clicked.connect(lambda: self.selectrast(self.ui.lineEdit_cn_raster))
        ##################
        #browse raster button urban raster
        self.ui.toolButton_browse_urban_zone_raster.clicked.connect(lambda: self.selectrast(self.ui.lineEdit_urban_zone_raster))
        ##################
        #browse composite cn con.imp. area
        self.ui.toolButton_browse_cn_urban_cia_raster.clicked.connect(lambda: self.selectrast(self.ui.lineEdit_cn_urban_cia_raster))
        ##################
        #browse composite cn con.imp. area
        self.ui.toolButton_browse_cn_urban_uncia_total_raster.clicked.connect(lambda: self.selectrast(self.ui.lineEdit_cn_urban_uncia_total_raster))
        ##################
        #browse composite cn con.imp. area
        self.ui.toolButton_browse_cn_urban_uncia_raster.clicked.connect(lambda: self.selectrast(self.ui.lineEdit_cn_urban_uncia_raster))
        ##################
        #direct cn value introduction (single point and etc)
        self.ui.checkBox_cn_value.stateChanged.connect(lambda:self.single_cn_val_state())
        ##############
        self.ui.checkBox_adv_cn.stateChanged.connect(lambda:self.adv_cn_state())
        ##############
        self.ui.checkBox_urban_cn_correction.stateChanged.connect(lambda:self.urban_cn_composit_state())
        ##############
        self.ui.checkBox_cia_cn_composite.stateChanged.connect(lambda:self.cia_cn_composite_state())
        self.ui.checkBox_uncia_cn_composite.stateChanged.connect(lambda:self.uncia_cn_composite_state())
        ##############
        self.ui.checkBox_urban_cycle.stateChanged.connect(lambda:self.urbancycle_state())



        #to work when it is okeyed
        self.ui.buttonBox.accepted.connect(lambda: self.ok_clicked())    
    ##############################################################################
    ##############################################################################
    def slopecat_statchange(self):
        if self.ui.checkBox_slope_cat.isChecked():
            self.ui.label_slope.setEnabled(True)
            self.ui.lineEdit_slope.setEnabled(True)
        else:
            self.ui.label_slope.setEnabled(False)
            self.ui.lineEdit_slope.setEnabled(False)
    #############################
    def urbancycle_state(self):
        if self.ui.checkBox_urban_cycle.isChecked():
            self.ui.tableWidget_urban.setEnabled(True)
        else: self.ui.tableWidget_urban.setEnabled(False)

    #############################
    def cia_cn_composite_state(self):
        if self.ui.checkBox_cia_cn_composite.isChecked():
            
            #checkbox ucia
            self.ui.checkBox_uncia_cn_composite.setChecked(False)
            self.uncia_cn_composite_state() #to the uncia_cn_composite_state else


            self.ui.label_cn_urban_cia_raster.setEnabled(True)
            self.ui.lineEdit_cn_urban_cia_raster.setEnabled(True)
            self.ui.toolButton_browse_cn_urban_cia_raster.setEnabled(True)
        else:
            self.ui.label_cn_urban_cia_raster.setEnabled(False)
            self.ui.lineEdit_cn_urban_cia_raster.setEnabled(False)
            self.ui.toolButton_browse_cn_urban_cia_raster.setEnabled(False)

            self.ui.checkBox_uncia_cn_composite.setEnabled(True)

    #############################
    def uncia_cn_composite_state(self):
        if self.ui.checkBox_uncia_cn_composite.isChecked():
            #line total ucia
            self.ui.label_cn_urban_uncia_total_raster.setEnabled(True)
            self.ui.lineEdit_cn_urban_uncia_total_raster.setEnabled(True)
            self.ui.toolButton_browse_cn_urban_uncia_total_raster.setEnabled(True)
            #line _cn_urban_uncia_raster
            self.ui.label_cn_urban_uncia_raster.setEnabled(True)
            self.ui.lineEdit_cn_urban_uncia_raster.setEnabled(True)
            self.ui.toolButton_browse_cn_urban_uncia_raster.setEnabled(True)
            
            #disable connected
            self.ui.checkBox_cia_cn_composite.setChecked(False)
            self.ui.label_cn_urban_cia_raster.setEnabled(False)
            self.ui.lineEdit_cn_urban_cia_raster.setEnabled(False)
            self.ui.toolButton_browse_cn_urban_cia_raster.setEnabled(False)

        else:
            #line total ucia
            self.ui.label_cn_urban_uncia_total_raster.setEnabled(False)
            self.ui.lineEdit_cn_urban_uncia_total_raster.setEnabled(False)
            self.ui.toolButton_browse_cn_urban_uncia_total_raster.setEnabled(False)
            #line _cn_urban_uncia_raster
            self.ui.label_cn_urban_uncia_raster.setEnabled(False)
            self.ui.lineEdit_cn_urban_uncia_raster.setEnabled(False)
            self.ui.toolButton_browse_cn_urban_uncia_raster.setEnabled(False)
            
            #enable connected
            if self.ui.checkBox_cia_cn_composite.isEnabled()==False:
                self.ui.checkBox_cia_cn_composite.setEnabled(True)

    #############################
    def urban_cn_composit_state(self):
        if self.ui.checkBox_urban_cn_correction.isChecked():
            self.ui.groupBox_urban_cn_correction.setEnabled(True)
        
        else: self.ui.groupBox_urban_cn_correction.setEnabled(False)
    #############################
    def adv_cn_state(self):
        if self.ui.checkBox_adv_cn.isChecked():
            self.ui.groupBox_adv_cn.setEnabled(True)

        else: self.ui.groupBox_adv_cn.setEnabled(False)
    #############################    
    #the direct cn value introduction state change
    def single_cn_val_state(self):
        if self.ui.checkBox_cn_value.isChecked():
            
            self.single_cn_val=True

            #enable single cn val groupbox
            self.ui.label_cn_val.setEnabled(True)
            self.ui.lineEdit_CN_Val.setEnabled(True)
            #disable curve number groupbox
            self.ui.groupBox_curve_number.setChecked(False)
            self.ui.groupBox_curve_number.setEnabled(False)
            #disable composite urban cn
            self.ui.checkBox_urban_cn_correction.setChecked(False)
            self.ui.checkBox_urban_cn_correction.setEnabled(False)
            self.ui.groupBox_urban_cn_correction.setEnabled(False)
            

        
        
        if self.ui.checkBox_cn_value.isChecked()==False:
            
            #disable single cn val groupbox
            self.ui.label_cn_val.setEnabled(False)
            self.ui.lineEdit_CN_Val.setEnabled(False)
            
            self.single_cn_val=False

            if self.single_point==False:
                #enable curve number groupbox
                self.ui.groupBox_curve_number.setEnabled(True)

                #enable composite urban cn
                self.ui.checkBox_urban_cn_correction.setChecked(False)
                self.ui.checkBox_urban_cn_correction.setEnabled(True)
                self.ui.groupBox_urban_cn_correction.setEnabled(True)
            
            
    ##############################################################################
    ##############################################################################
    #check for daily timesteps - used in the main window - 1
    def check_timesteps(self):
        
        self.Calc_CN=True
        # CN method not available
        print ("self.preferred_date_interval",self.preferred_date_interval)
        if self.preferred_date_interval not in ["datetime64[D]","daily","Daily"]:
            self.Calc_CN=False
            
            #curve number groupbox
            self.ui.groupBox_curve_number.setChecked(False)
            self.ui.groupBox_curve_number.setEnabled(False) 

            #single cn value
            self.ui.checkBox_cn_value.setChecked(False)  
            self.ui.checkBox_cn_value.setEnabled(False)
            self.ui.label_cn_val.setEnabled(False)
            self.ui.lineEdit_CN_Val.setEnabled(False)
               
            
            #urban composite cn correction
            self.ui.checkBox_urban_cn_correction.setEnabled(False)
            self.ui.groupBox_urban_cn_correction.setEnabled(False)
                                    
    ##########################
    #check if urban is enabled in the netcdf dataset - used in the main window - 2
    def check_urban(self):
        if self.urban_ds:
            
            self.ui.lineEdit_urban_zone_raster.setEnabled(True) 
            self.ui.toolButton_browse_urban_zone_raster.setEnabled(True) 
            self.ui.label_urban_zone_raster.setEnabled(True) 
            self.ui.checkBox_urban_cycle.setEnabled(True)
            self.ui.tableWidget_urban.setEnabled(True) 

            self.ui.checkBox_urban_cn_correction.setEnabled(True)
            self.ui.groupBox_urban_cn_correction.setEnabled(True)
            
            self.ui.groupBox_urban.setEnabled(True) 
            self.ui.groupBox_urban.setChecked(False)    
    ##########################
    #if single point is true enable and disable options - used in the main window - 3
    def check_single_point(self):
        if self.single_point:
            #disable  cn groupbox
            self.ui.groupBox_curve_number.setChecked(False)
            self.ui.groupBox_curve_number.setEnabled(False) 
            
            #enable and check single cn value
            self.ui.checkBox_cn_value.setChecked(True)
            self.ui.checkBox_cn_value.setEnabled(True)
            self.single_cn_val=True

            #disable raster introduction for urban area
            self.ui.lineEdit_urban_zone_raster.setEnabled(False) 
            self.ui.toolButton_browse_urban_zone_raster.setEnabled(False) 
            self.ui.label_urban_zone_raster.setEnabled(False) 

            #urban composite cn correction
            self.ui.checkBox_urban_cn_correction.setEnabled(False)
            self.ui.groupBox_urban_cn_correction.setEnabled(False)  
    
    ##########################
    #urban table maker    
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
    #update the urban table - used in the main window - 4
    def update_urban_table(self):
        
        self.table_maker()

        
        for row in range(0,13):
            combo_c1 = QtWidgets.QComboBox()
            if self.single_point:
                combo_c1.addItems(["Constant","Dataset"])
            else:
                combo_c1.addItems(["Constant","Raster","Dataset"])
            self.ui.tableWidget_urban.setCellWidget(row, 1, combo_c1)
    
    ##############################################################################
    ##############################################################################
    #main
    def ok_clicked(self):
        
        #calculating infiltration

        
        

        if self.ui.groupBox_corrected_cn.isChecked():
    
            amc1_coeffs=[float(n) for n in [self.ui.lineEdit_amc1_a.text(),self.ui.lineEdit_amc1_b.text(),self.ui.lineEdit_amc1_c.text()]]
            amc3_coeffs=[float(n) for n in [self.ui.lineEdit_amc3_a.text(),self.ui.lineEdit_amc3_b.text(),self.ui.lineEdit_amc3_c.text()]]
            dormant_thresh=[float(n) for n in [self.ui.lineEdit_dormant_1.text(),self.ui.lineEdit_dormant_3.text()]]
            growing_thresh=[float(n) for n in [self.ui.lineEdit_grow_1.text(),self.ui.lineEdit_grow_3.text()]]
            mon_list_dormant=[float(n) for n in self.ui.lineEdit_dormant_month.text().split(',')]
            if self.ui.comboBox_average.currentText()=='Yes': average_thresh=True
            else: average_thresh=False
            corrected_cn=True

        else:
            amc1_coeffs,amc3_coeffs,dormant_thresh,growing_thresh,mon_list_dormant,average_thresh=None,None,None,None,None,None
            corrected_cn=False
    
        threshold=self.ui.lineEdit__max_infilt.text()
        
        #check for self.Calc_CN:
        if self.ui.checkBox_cn_value.isChecked()==False and self.ui.groupBox_curve_number.isChecked()==False:
            self.Calc_CN=False
        
        if self.Calc_CN==True:  

            if self.single_cn_val:
                self.cn_val=float(self.ui.lineEdit_CN_Val.text())
            else: 
                self.cn_val=None

            #check for advanced cn calculation
            advanced_cn=False
            advanced_cn_dic=dict()
            if self.ui.checkBox_adv_cn.isChecked() and self.ui.groupBox_adv_cn.isEnabled():
                advanced_cn_dic=self.advanced_cn_dic_gen()
                advanced_cn=True

            ########################
            ########################
            # inf calc arguments
            

            CN_table_dir=self.ui.lineEdit_cn_csv.text()
            HSG_band=self.ui.lineEdit_hsg.text()
            LU_band=self.ui.lineEdit_lu.text()
            ELEV_or_HC_band=self.ui.lineEdit_elev.text()
            DEM_or_raster="raster"
            raster_dir=self.ui.lineEdit_cn_raster.text()
            DEM_path_or_raster=raster_dir
            filled_dep=True
            preferred_date_interval=self.preferred_date_interval
            #Hydrologic condition (HC) or slope catagory (SC) & slope range list
            if self.ui.checkBox_slope_cat.isChecked(): 
                SC_or_HC="SC"
                slope_range_list=[float(n) for n in self.ui.lineEdit_slope.text().split(',')]
            else:
                SC_or_HC="HC"
                slope_range_list=list()
            print (self.cn_val)
            self.ds,Ia=infiltration.Inf_calc(self.ds,CN_table_dir,raster_dir,HSG_band,LU_band,ELEV_or_HC_band,
                preferred_date_interval,corrected_cn,self.single_cn_val,self.cn_val,advanced_cn_dic,advanced_cn,
                filled_dep,slope_range_list,amc1_coeffs,amc3_coeffs,dormant_thresh,growing_thresh,average_thresh,
                mon_list_dormant,SC_or_HC,DEM_path_or_raster,DEM_or_raster)
            # max infiltration threshold per timestep
            var_inp="INF_Val"
            var_out="INF_Val"
            ########################
            print ("INF_Val line 418 before urban",np.count_nonzero(self.ds["INF_Val"][:,:,:].data==-9999))
        else:

            # max infiltration threshold per timestep
            #var_inp="Prec_Val"
            var_inp="INF_Val"
            var_out="INF_Val"
            Ia=None

        if self.ui.groupBox_urban.isChecked():
            ##########################
            #composite curve number
            if self.ui.checkBox_urban_cn_correction.isChecked() and self.ui.groupBox_urban_cn_correction.isEnabled() and self.ui.checkBox_adv_cn.isChecked()==False and self.ui.groupBox_adv_cn.isEnabled()==False:
                
                #connected imp. area cn correction
                if self.ui.checkBox_cia_cn_composite.isChecked() and self.ui.lineEdit_cn_urban_cia_raster.isEnabled():
                    cia_raster=self.ui.lineEdit_cn_urban_cia_raster.text()
                    
                    self.ds=urban_Composite_CN_correction.cia_main(self.ds,cia_raster,corrected_cn)
                #unconnected imp.area cn correction
                if self.ui.checkBox_uncia_cn_composite.isChecked() and self.ui.lineEdit_cn_urban_uncia_total_raster.isEnabled() and self.ui.lineEdit_cn_urban_uncia_raster.isEnabled():
                    tia_raster=self.ui.lineEdit_cn_urban_uncia_total_raster.text()
                    ucia_raster=self.ui.lineEdit_cn_urban_uncia_raster.text()

                    self.ds=urban_Composite_CN_correction.ucia_main(self.ds,tia_raster,ucia_raster,corrected_cn)

            
            #urban cycle
            if self.ui.checkBox_urban_cycle.isChecked() and self.ui.tableWidget_urban.isEnabled():
                variables_dic=self.urban_inf_dic_gen()
                urban_area_raster_dir=self.ui.lineEdit_urban_zone_raster.text()
                self.ds=urban_cycle_calcs.urban_cycle_main(self.ds,urban_area_raster_dir,variables_dic) 

        ##############################################################################
        print ("INF_Val line 453 after urban",np.count_nonzero(self.ds["INF_Val"][:,:,:].data==-9999))
        #apply the max infiltration threshold and calculate runoff
        self.ds=infiltration.max_inf_threshold(self.ds,var_inp,var_out,threshold) 
        self.ds=infiltration.runoff_calc(self.ds,Ia)
        print ("INF_Val line 458 after all",np.count_nonzero(self.ds["INF_Val"][:,:,:].data==-9999))

    ##############################################################################
    ##############################################################################
    #select thew csv file
    def selectcsvFile(self):
        filter = "XLS(*.xls)"
        self.fileName = QtWidgets.QFileDialog.getOpenFileName(caption='select a .xls file',filter=filter)[0]
        
        self.ui.lineEdit_cn_csv.setText(self.fileName)
    
    ##########################
    #select raster file cn
    def selectrast(self,lineeditobject):
        filter = "Raster(*.tif)"
        self.rastfileName = QtWidgets.QFileDialog.getOpenFileName(caption='select a raster file',filter=filter)[0]
        
        lineeditobject.setText(self.rastfileName)
    
    ##########################
    #to generate the dictionary of the urban cycle
    def urban_inf_dic_gen(self):
        num_of_rows=self.ui.tableWidget_urban.rowCount()
        variables_dic={}
        for i in range(0,num_of_rows):
            var_dic={}
            
            
            var_dic["dataset_raster_dir_or_value"]=self.ui.tableWidget_urban.cellWidget(i,1).currentText()
            
            
            val_or_path_t=self.ui.tableWidget_urban.item(i,2)
            if val_or_path_t!=None:
                val_or_path=val_or_path_t.text().strip()
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
        print ("variables_dic",variables_dic)
        return variables_dic

    ##########################
    #to generate the dictionary of the advanced CN
    def advanced_cn_dic_gen(self):
        advanced_cn_dic=dict()
        advanced_cn_dic["landa"]=float(self.ui.lineEdit_landa.text())
        advanced_cn_dic["A"]=float(self.ui.lineEdit_a.text())
        advanced_cn_dic["B"]=float(self.ui.lineEdit_b.text())
        advanced_cn_dic["C"]=float(self.ui.lineEdit_c.text())
        advanced_cn_dic["D"]=float(self.ui.lineEdit_d.text())
        advanced_cn_dic["x"]=float(self.ui.lineEdit_x.text())
        advanced_cn_dic["y"]=float(self.ui.lineEdit_y.text())
        advanced_cn_dic["z"]=float(self.ui.lineEdit_z.text())
        return advanced_cn_dic

    ##########################
    #to limit the lineedits
    def lineeditvalidator(self):
        # elev lu hsg
        onlyInt=QtGui.QIntValidator()
        self.ui.lineEdit_elev.setValidator(onlyInt) 
        self.ui.lineEdit_lu.setValidator(onlyInt) 
        self.ui.lineEdit_hsg.setValidator(onlyInt) 
        self.ui.lineEdit_elev.setMaxLength(4)
        self.ui.lineEdit_lu.setMaxLength(4)
        self.ui.lineEdit_hsg.setMaxLength(4)
        
        onlydoub=QtGui.QDoubleValidator()

        #cn value
        self.ui.lineEdit_CN_Val.setValidator(onlydoub) 
        self.ui.lineEdit_CN_Val.setMaxLength(4) 

        #a,b,c,d,x,y,z,landa
        self.ui.lineEdit_a.setValidator(onlydoub)
        self.ui.lineEdit_b.setValidator(onlydoub)
        self.ui.lineEdit_c.setValidator(onlydoub)
        self.ui.lineEdit_d.setValidator(onlydoub)
        self.ui.lineEdit_x.setValidator(onlydoub)
        self.ui.lineEdit_y.setValidator(onlydoub)
        self.ui.lineEdit_z.setValidator(onlydoub)
        self.ui.lineEdit_landa.setValidator(onlydoub)

    ##########################
    #to define the style of the group boxes and check boxes
    def stylesheetset(self):

        #for groupbox:
        for i in [self.ui.groupBox_curve_number,self.ui.groupBox_urban]:

            i.setStyleSheet("""
                QGroupBox::indicator { width: 15px; height: 15px;}
                }
            """)

        #for checkbox:
        for i in [self.ui.checkBox_cn_value,self.ui.checkBox_adv_cn,self.ui.checkBox_cia_cn_composite,self.ui.checkBox_uncia_cn_composite,self.ui.checkBox_urban_cn_correction,self.ui.checkBox_urban_cycle,self.ui.checkBox_slope_cat]:
            i.setStyleSheet("""
                QCheckBox::indicator { width: 15px; height: 15px;}
                }
            """)


