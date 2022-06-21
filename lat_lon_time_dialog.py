from PyQt6 import QtCore, QtGui, QtWidgets
import os

class Ui_Dialog_lat_lon_time(object):


    def setupUi(self, Dialog_lat_lon_time):

        Dialog_lat_lon_time.setObjectName("Dialog_lat_lon_time")
        Dialog_lat_lon_time.resize(600, 490)
        Dialog_lat_lon_time.setMinimumSize(QtCore.QSize(500, 490))
        Dialog_lat_lon_time.setMaximumSize(QtCore.QSize(900, 730))
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(Dialog_lat_lon_time)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.groupBox_spatialtemporal = QtWidgets.QGroupBox(Dialog_lat_lon_time)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox_spatialtemporal.setFont(font)
        self.groupBox_spatialtemporal.setObjectName("groupBox_spatialtemporal")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.groupBox_spatialtemporal)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_xy_raster = QtWidgets.QLabel(self.groupBox_spatialtemporal)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_xy_raster.setFont(font)
        self.label_xy_raster.setObjectName("label_xy_raster")
        self.horizontalLayout_5.addWidget(self.label_xy_raster)
        self.lineEdit_xyraster = QtWidgets.QLineEdit(self.groupBox_spatialtemporal)
        self.lineEdit_xyraster.setMinimumSize(QtCore.QSize(160, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.lineEdit_xyraster.setFont(font)
        self.lineEdit_xyraster.setObjectName("lineEdit_xyraster")
        self.horizontalLayout_5.addWidget(self.lineEdit_xyraster)

        #browse button raster
        self.toolButton_browse_xy_raster = QtWidgets.QToolButton(self.groupBox_spatialtemporal)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolButton_browse_xy_raster.sizePolicy().hasHeightForWidth())
        self.toolButton_browse_xy_raster.setSizePolicy(sizePolicy)
        self.toolButton_browse_xy_raster.setMaximumSize(QtCore.QSize(20, 20))
        self.toolButton_browse_xy_raster.setObjectName("toolButton_browse_xy_raster")
        self.horizontalLayout_5.addWidget(self.toolButton_browse_xy_raster)
        self.verticalLayout_7.addLayout(self.horizontalLayout_5)
        spacerItem = QtWidgets.QSpacerItem(471, 0, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Maximum)
        self.verticalLayout_7.addItem(spacerItem)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.label_time_interval = QtWidgets.QLabel(self.groupBox_spatialtemporal)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_time_interval.setFont(font)
        self.label_time_interval.setObjectName("label_time_interval")
        self.horizontalLayout_3.addWidget(self.label_time_interval)
        self.comboBox_time_interval = QtWidgets.QComboBox(self.groupBox_spatialtemporal)
        self.comboBox_time_interval.setMinimumSize(QtCore.QSize(60, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comboBox_time_interval.setFont(font)
        self.comboBox_time_interval.setObjectName("comboBox_time_interval")
        self.comboBox_time_interval.addItem("")
        self.comboBox_time_interval.addItem("")
        self.comboBox_time_interval.addItem("")
        self.horizontalLayout_3.addWidget(self.comboBox_time_interval)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.verticalLayout_6.addLayout(self.horizontalLayout_3)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Maximum)
        self.verticalLayout_6.addItem(spacerItem4)
        self.splitter = QtWidgets.QSplitter(self.groupBox_spatialtemporal)
        self.splitter.setOrientation(QtCore.Qt.Orientation.Vertical)
        self.splitter.setObjectName("splitter")
        self.layoutWidget_4 = QtWidgets.QWidget(self.splitter)
        self.layoutWidget_4.setObjectName("layoutWidget_4")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.layoutWidget_4)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum)
        self.verticalLayout_5.addItem(spacerItem5)
        self.label_start_time = QtWidgets.QLabel(self.layoutWidget_4)
        self.label_start_time.setMinimumSize(QtCore.QSize(35, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_start_time.setFont(font)
        self.label_start_time.setObjectName("label_start_time")
        self.verticalLayout_5.addWidget(self.label_start_time)
        self.label_end_time = QtWidgets.QLabel(self.layoutWidget_4)
        self.label_end_time.setMinimumSize(QtCore.QSize(35, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_end_time.setFont(font)
        self.label_end_time.setObjectName("label_end_time")
        self.verticalLayout_5.addWidget(self.label_end_time)
        self.horizontalLayout_7.addLayout(self.verticalLayout_5)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_hour = QtWidgets.QLabel(self.layoutWidget_4)
        self.label_hour.setMinimumSize(QtCore.QSize(50, 20))
        self.label_hour.setMaximumSize(QtCore.QSize(40, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_hour.setFont(font)
        self.label_hour.setObjectName("label_hour")
        self.verticalLayout.addWidget(self.label_hour)
        self.comboBox_start_hour = QtWidgets.QComboBox(self.layoutWidget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_start_hour.sizePolicy().hasHeightForWidth())
        self.comboBox_start_hour.setSizePolicy(sizePolicy)
        self.comboBox_start_hour.setMinimumSize(QtCore.QSize(50, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.comboBox_start_hour.setFont(font)
        self.comboBox_start_hour.setObjectName("comboBox_start_hour")
        for i in range (0,24):
            self.comboBox_start_hour.addItem("")


        self.verticalLayout.addWidget(self.comboBox_start_hour)
        self.comboBox_end_hour = QtWidgets.QComboBox(self.layoutWidget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_end_hour.sizePolicy().hasHeightForWidth())
        self.comboBox_end_hour.setSizePolicy(sizePolicy)
        self.comboBox_end_hour.setMinimumSize(QtCore.QSize(50, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.comboBox_end_hour.setFont(font)
        self.comboBox_end_hour.setObjectName("comboBox_end_hour")
        for i in range (0,24):
            self.comboBox_end_hour.addItem("")

        self.verticalLayout.addWidget(self.comboBox_end_hour)
        self.horizontalLayout_7.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_day = QtWidgets.QLabel(self.layoutWidget_4)
        self.label_day.setMinimumSize(QtCore.QSize(50, 20))
        self.label_day.setMaximumSize(QtCore.QSize(40, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_day.setFont(font)
        self.label_day.setObjectName("label_day")
        self.verticalLayout_2.addWidget(self.label_day)
        self.comboBox_start_day = QtWidgets.QComboBox(self.layoutWidget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_start_day.sizePolicy().hasHeightForWidth())
        self.comboBox_start_day.setSizePolicy(sizePolicy)
        self.comboBox_start_day.setMinimumSize(QtCore.QSize(50, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.comboBox_start_day.setFont(font)
        self.comboBox_start_day.setObjectName("comboBox_start_day")
        for i in range (0,30):
            self.comboBox_start_day.addItem("")
        
        self.verticalLayout_2.addWidget(self.comboBox_start_day)
        self.comboBox_end_day = QtWidgets.QComboBox(self.layoutWidget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_end_day.sizePolicy().hasHeightForWidth())
        self.comboBox_end_day.setSizePolicy(sizePolicy)
        self.comboBox_end_day.setMinimumSize(QtCore.QSize(50, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.comboBox_end_day.setFont(font)
        self.comboBox_end_day.setObjectName("comboBox_end_day")
        for i in range (0,30):
            self.comboBox_end_day.addItem("")

        self.verticalLayout_2.addWidget(self.comboBox_end_day)
        self.horizontalLayout_7.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_month = QtWidgets.QLabel(self.layoutWidget_4)
        self.label_month.setMinimumSize(QtCore.QSize(50, 20))
        self.label_month.setMaximumSize(QtCore.QSize(50, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_month.setFont(font)
        self.label_month.setObjectName("label_month")
        self.verticalLayout_3.addWidget(self.label_month)
        self.comboBox_start_month = QtWidgets.QComboBox(self.layoutWidget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_start_month.sizePolicy().hasHeightForWidth())
        self.comboBox_start_month.setSizePolicy(sizePolicy)
        self.comboBox_start_month.setMinimumSize(QtCore.QSize(50, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.comboBox_start_month.setFont(font)
        self.comboBox_start_month.setObjectName("comboBox_start_month")
        for i in range (0,12):
            self.comboBox_start_month.addItem("")

        self.verticalLayout_3.addWidget(self.comboBox_start_month)
        self.comboBox_end_month = QtWidgets.QComboBox(self.layoutWidget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_end_month.sizePolicy().hasHeightForWidth())
        self.comboBox_end_month.setSizePolicy(sizePolicy)
        self.comboBox_end_month.setMinimumSize(QtCore.QSize(50, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.comboBox_end_month.setFont(font)
        self.comboBox_end_month.setObjectName("comboBox_end_month")
        for i in range (0,12):
            self.comboBox_end_month.addItem("")

        self.verticalLayout_3.addWidget(self.comboBox_end_month)
        self.horizontalLayout_7.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_year = QtWidgets.QLabel(self.layoutWidget_4)
        self.label_year.setMinimumSize(QtCore.QSize(50, 20))
        self.label_year.setMaximumSize(QtCore.QSize(40, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_year.setFont(font)
        self.label_year.setObjectName("label_year")
        self.verticalLayout_4.addWidget(self.label_year)
        self.lineEdit_start_year = QtWidgets.QLineEdit(self.layoutWidget_4)
        self.lineEdit_start_year.setMinimumSize(QtCore.QSize(50, 20))
        self.lineEdit_start_year.setMaximumSize(QtCore.QSize(40, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.lineEdit_start_year.setFont(font)
        self.lineEdit_start_year.setObjectName("lineEdit_start_year")
        self.verticalLayout_4.addWidget(self.lineEdit_start_year)
        self.lineEdit_end_year = QtWidgets.QLineEdit(self.layoutWidget_4)
        self.lineEdit_end_year.setMinimumSize(QtCore.QSize(50, 20))
        self.lineEdit_end_year.setMaximumSize(QtCore.QSize(40, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.lineEdit_end_year.setFont(font)
        self.lineEdit_end_year.setObjectName("lineEdit_end_year")
        self.verticalLayout_4.addWidget(self.lineEdit_end_year)
        self.horizontalLayout_7.addLayout(self.verticalLayout_4)
        self.verticalLayout_6.addWidget(self.splitter)
        self.horizontalLayout_4.addLayout(self.verticalLayout_6)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem6)
        self.verticalLayout_7.addLayout(self.horizontalLayout_4)
        self.verticalLayout_8.addWidget(self.groupBox_spatialtemporal)
        self.groupBox_additional_vars = QtWidgets.QGroupBox(Dialog_lat_lon_time)
        self.groupBox_additional_vars.setMinimumSize(QtCore.QSize(275, 235))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.groupBox_additional_vars.setFont(font)
        self.groupBox_additional_vars.setObjectName("groupBox_additional_vars")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox_additional_vars)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem7 = QtWidgets.QSpacerItem(60, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem7)
        self.tableWidget_additional_vars_3 = QtWidgets.QTableWidget(self.groupBox_additional_vars)
        self.tableWidget_additional_vars_3.setObjectName("tableWidget_additional_vars_3")
        self.tableWidget_additional_vars_3.setColumnCount(2)
        self.tableWidget_additional_vars_3.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_additional_vars_3.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_additional_vars_3.setHorizontalHeaderItem(1, item)
        self.horizontalLayout.addWidget(self.tableWidget_additional_vars_3)
        self.verticalLayout_14 = QtWidgets.QVBoxLayout()
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout()
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_15.addItem(spacerItem8)
        self.toolButton_new_3 = QtWidgets.QToolButton(self.groupBox_additional_vars)
        self.toolButton_new_3.setMinimumSize(QtCore.QSize(70, 25))
        self.toolButton_new_3.setArrowType(QtCore.Qt.ArrowType.NoArrow)
        self.toolButton_new_3.setObjectName("toolButton_new_3")
        self.verticalLayout_15.addWidget(self.toolButton_new_3)
        self.toolButton_remove_3 = QtWidgets.QToolButton(self.groupBox_additional_vars)
        self.toolButton_remove_3.setMinimumSize(QtCore.QSize(70, 25))
        self.toolButton_remove_3.setObjectName("toolButton_remove_3")
        self.verticalLayout_15.addWidget(self.toolButton_remove_3)
        self.verticalLayout_14.addLayout(self.verticalLayout_15)
        spacerItem9 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_14.addItem(spacerItem9)
        self.horizontalLayout.addLayout(self.verticalLayout_14)
        spacerItem10 = QtWidgets.QSpacerItem(60, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem10)
        self.verticalLayout_8.addWidget(self.groupBox_additional_vars)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog_lat_lon_time)
        self.buttonBox.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.StandardButton.Cancel|QtWidgets.QDialogButtonBox.StandardButton.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout_8.addWidget(self.buttonBox)
        self.verticalLayout_9.addLayout(self.verticalLayout_8)

        self.retranslateUi(Dialog_lat_lon_time)

        self.buttonBox.accepted.connect(Dialog_lat_lon_time.accept)
        self.buttonBox.rejected.connect(Dialog_lat_lon_time.reject)
        

        QtCore.QMetaObject.connectSlotsByName(Dialog_lat_lon_time)




    def retranslateUi(self, Dialog_lat_lon_time):
        _translate = QtCore.QCoreApplication.translate
        Dialog_lat_lon_time.setWindowTitle(_translate("Dialog_lat_lon_time", "Spatial -Temporal properties"))
        self.groupBox_spatialtemporal.setTitle(_translate("Dialog_lat_lon_time", "Spatial -Temporal properties"))
        self.label_xy_raster.setText(_translate("Dialog_lat_lon_time", "Raster to determine Spatial properties (X and Y) :"))
        self.toolButton_browse_xy_raster.setText(_translate("Dialog_lat_lon_time", "..."))
        self.label_time_interval.setText(_translate("Dialog_lat_lon_time", "Time interval: "))
        self.comboBox_time_interval.setItemText(0, _translate("Dialog_lat_lon_time", "Monthly"))
        self.comboBox_time_interval.setItemText(1, _translate("Dialog_lat_lon_time", "Daily"))
        self.comboBox_time_interval.setItemText(2, _translate("Dialog_lat_lon_time", "Hourly"))
        self.label_start_time.setText(_translate("Dialog_lat_lon_time", "Start"))
        self.label_end_time.setText(_translate("Dialog_lat_lon_time", "End"))
        self.label_hour.setText(_translate("Dialog_lat_lon_time", "Hour"))
        for i in range(0,24):
            if i in [0,1,2,3,4,5,6,7,8,9]:  tmp="0"+str(i) 
            else: tmp=str(i)
            self.comboBox_start_hour.setItemText(i, _translate("MainWindow", tmp))
            self.comboBox_end_hour.setItemText(i, _translate("MainWindow", tmp))

        self.label_day.setText(_translate("Dialog_lat_lon_time", "Day"))
        for i in range(0,30):
            if i in [0,1,2,3,4,5,6,7,8]:  tmp="0"+str(i+1) 
            else: tmp=str(i+1)
            self.comboBox_start_day.setItemText(i, _translate("MainWindow", tmp))
            self.comboBox_end_day.setItemText(i, _translate("MainWindow", tmp))
        
        self.label_month.setText(_translate("Dialog_lat_lon_time", "Month"))
        for i in range(0,12):
            if i in [0,1,2,3,4,5,6,7,8]:  tmp="0"+str(i+1) 
            else: tmp=str(i+1)
            self.comboBox_start_month.setItemText(i, _translate("MainWindow", tmp))
            self.comboBox_end_month.setItemText(i, _translate("MainWindow", tmp))
        
        self.label_year.setText(_translate("Dialog_lat_lon_time", "Year"))
        self.groupBox_additional_vars.setTitle(_translate("Dialog_lat_lon_time", "Additional Variables"))
        item = self.tableWidget_additional_vars_3.horizontalHeaderItem(0)
        item.setText(_translate("Dialog_lat_lon_time", "Var. Name"))
        item = self.tableWidget_additional_vars_3.horizontalHeaderItem(1)
        item.setText(_translate("Dialog_lat_lon_time", "Var. Unit"))
        self.toolButton_new_3.setText(_translate("Dialog_lat_lon_time", "New"))
        self.toolButton_remove_3.setText(_translate("Dialog_lat_lon_time", "Remove"))


'''if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog_lat_lon_time = QtWidgets.QDialog()
    ui = Ui_Dialog_lat_lon_time()
    ui.setupUi(Dialog_lat_lon_time)
    #Dialog_lat_lon_time.show()
    sys.exit(app.exec())'''