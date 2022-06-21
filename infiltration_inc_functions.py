from PyQt6 import QtWidgets,QtGui
from infiltration import Ui_Dialog_infiltration
from waterpybal.inf_calcs import infiltration


class Ui_Dialog_infiltration_(QtWidgets.QDialog):

    def __init__(self):
        
        super().__init__()

        self.ui = Ui_Dialog_infiltration()
        
        self.ui.setupUi(self)
        self.show()
        ##############
        #browse button
        self.ui.toolButton_browse_cn_csv.clicked.connect(lambda: self.selectcsvFile())
        ##############
        #browse raster button
        self.ui.toolButton_browse_cn_raster.clicked.connect(lambda: self.selectrastFile())
        ##################
        #to work when it is okeyed
        self.ui.buttonBox.accepted.connect(lambda: self.ok_clicked())
        ##################
        #limit the year to ints and 4 digits
        onlyInt=QtGui.QIntValidator()
        self.ui.lineEdit_elev.setValidator(onlyInt) 
        self.ui.lineEdit_lu.setValidator(onlyInt) 
        self.ui.lineEdit_hsg.setValidator(onlyInt) 
        self.ui.lineEdit_elev.setMaxLength(4)
        self.ui.lineEdit_lu.setMaxLength(4)
        self.ui.lineEdit_hsg.setMaxLength(4)
        #################
        self.ds=None
        self.preferred_date_interval=None
    ##########################
    def selectcsvFile(self):
        filter = "CSV(*.csv)"
        self.fileName = QtWidgets.QFileDialog.getOpenFileName(caption='select a .CSV file',filter=filter)[0]
        
        self.ui.lineEdit_cn_csv.setText(self.fileName)
    ##########################
    #select raster file
    def selectrastFile(self):
        filter = "Raster(*.tif)"
        self.rastfileName = QtWidgets.QFileDialog.getOpenFileName(caption='select a raster file',filter=filter)[0]
        
        self.ui.lineEdit_cn_raster.setText(self.rastfileName)
    ##########################
    def ok_clicked(self):
        #calculating infiltration
        CN_table_dir=self.ui.lineEdit_cn_csv.text()
        raster_dir=self.ui.lineEdit_cn_raster.text()
        HSG_band=int(self.ui.lineEdit_hsg.text())
        LU_band=int(self.ui.lineEdit_lu.text())
        ELEV_band=int(self.ui.lineEdit_elev.text())
        DEM_or_raster="raster"
        DEM_path_or_raster=raster_dir
        filled_dep=True
        slope_range_list=[float(n) for n in self.ui.lineEdit_slope.text().split(',')]
        amc1_coeffs=[float(n) for n in self.ui.lineEdit_amc1.text().split(',')]
        amc3_coeffs=[float(n) for n in self.ui.lineEdit_amc3.text().split(',')]
        dormant_thresh=[float(n) for n in self.ui.lineEdit_dormant.text().split(',')]
        growing_thresh=[float(n) for n in self.ui.lineEdit_growing.text().split(',')]
        mon_list_dormant=[float(n) for n in self.ui.lineEdit_dormant_month.text().split(',')]
        print (self.ui.comboBox_average.currentText())
        if self.ui.comboBox_average.currentText()=='Yes': average_thresh=True
        else: average_thresh=False
        preferred_date_interval=self.preferred_date_interval
        self.ds=infiltration.Inf_calc(self.ds,CN_table_dir,raster_dir,HSG_band,LU_band,ELEV_band,DEM_path_or_raster,DEM_or_raster,filled_dep,slope_range_list,amc1_coeffs,amc3_coeffs,dormant_thresh,growing_thresh,average_thresh,mon_list_dormant,preferred_date_interval)
