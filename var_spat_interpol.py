# Form implementation generated from reading ui file 'var_spat_interpol.ui'
#
# Created by: PyQt6 UI code generator 6.1.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog_var_spat_interpol(object):
    def setupUi(self, Dialog_var_spat_interpol):
        Dialog_var_spat_interpol.setObjectName("Dialog_var_spat_interpol")
        Dialog_var_spat_interpol.resize(456, 322)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog_var_spat_interpol)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_csv = QtWidgets.QLabel(Dialog_var_spat_interpol)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_csv.setFont(font)
        self.label_csv.setObjectName("label_csv")
        self.horizontalLayout.addWidget(self.label_csv)
        self.lineEdit_csv = QtWidgets.QLineEdit(Dialog_var_spat_interpol)
        self.lineEdit_csv.setMinimumSize(QtCore.QSize(160, 20))
        self.lineEdit_csv.setObjectName("lineEdit_csv")
        self.horizontalLayout.addWidget(self.lineEdit_csv)
        self.toolButton_browse_csv = QtWidgets.QToolButton(Dialog_var_spat_interpol)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolButton_browse_csv.sizePolicy().hasHeightForWidth())
        self.toolButton_browse_csv.setSizePolicy(sizePolicy)
        self.toolButton_browse_csv.setMaximumSize(QtCore.QSize(20, 20))
        self.toolButton_browse_csv.setObjectName("toolButton_browse_csv")
        self.horizontalLayout.addWidget(self.toolButton_browse_csv)
        self.toolButton_refresh = QtWidgets.QToolButton(Dialog_var_spat_interpol)
        self.toolButton_refresh.setMinimumSize(QtCore.QSize(40, 20))
        self.toolButton_refresh.setObjectName("toolButton_refresh")
        self.horizontalLayout.addWidget(self.toolButton_refresh)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_xy_raster = QtWidgets.QLabel(Dialog_var_spat_interpol)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_xy_raster.setFont(font)
        self.label_xy_raster.setObjectName("label_xy_raster")
        self.horizontalLayout_5.addWidget(self.label_xy_raster)
        self.lineEdit_xyraster = QtWidgets.QLineEdit(Dialog_var_spat_interpol)
        self.lineEdit_xyraster.setMinimumSize(QtCore.QSize(160, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.lineEdit_xyraster.setFont(font)
        self.lineEdit_xyraster.setObjectName("lineEdit_xyraster")
        self.horizontalLayout_5.addWidget(self.lineEdit_xyraster)
        self.toolButton_browse_xy_raster = QtWidgets.QToolButton(Dialog_var_spat_interpol)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolButton_browse_xy_raster.sizePolicy().hasHeightForWidth())
        self.toolButton_browse_xy_raster.setSizePolicy(sizePolicy)
        self.toolButton_browse_xy_raster.setMaximumSize(QtCore.QSize(20, 20))
        self.toolButton_browse_xy_raster.setObjectName("toolButton_browse_xy_raster")
        self.horizontalLayout_5.addWidget(self.toolButton_browse_xy_raster)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_var_name = QtWidgets.QLabel(Dialog_var_spat_interpol)
        self.label_var_name.setMinimumSize(QtCore.QSize(85, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_var_name.setFont(font)
        self.label_var_name.setObjectName("label_var_name")
        self.horizontalLayout_3.addWidget(self.label_var_name)
        self.comboBox_var_name = QtWidgets.QComboBox(Dialog_var_spat_interpol)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_var_name.sizePolicy().hasHeightForWidth())
        self.comboBox_var_name.setSizePolicy(sizePolicy)
        self.comboBox_var_name.setMinimumSize(QtCore.QSize(70, 20))
        self.comboBox_var_name.setObjectName("comboBox_var_name")
        self.horizontalLayout_3.addWidget(self.comboBox_var_name)
        self.horizontalLayout_7.addLayout(self.horizontalLayout_3)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem1)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_time_interval = QtWidgets.QLabel(Dialog_var_spat_interpol)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_time_interval.setFont(font)
        self.label_time_interval.setObjectName("label_time_interval")
        self.horizontalLayout_6.addWidget(self.label_time_interval)
        self.comboBox_time_interval = QtWidgets.QComboBox(Dialog_var_spat_interpol)
        self.comboBox_time_interval.setMinimumSize(QtCore.QSize(60, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.comboBox_time_interval.setFont(font)
        self.comboBox_time_interval.setObjectName("comboBox_time_interval")
        self.comboBox_time_interval.addItem("")
        self.comboBox_time_interval.addItem("")
        self.comboBox_time_interval.addItem("")
        self.horizontalLayout_6.addWidget(self.comboBox_time_interval)
        self.horizontalLayout_7.addLayout(self.horizontalLayout_6)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.label_method = QtWidgets.QLabel(Dialog_var_spat_interpol)
        self.label_method.setMinimumSize(QtCore.QSize(45, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_method.setFont(font)
        self.label_method.setObjectName("label_method")
        self.horizontalLayout_2.addWidget(self.label_method)
        self.comboBox_method = QtWidgets.QComboBox(Dialog_var_spat_interpol)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_method.sizePolicy().hasHeightForWidth())
        self.comboBox_method.setSizePolicy(sizePolicy)
        self.comboBox_method.setMinimumSize(QtCore.QSize(100, 20))
        self.comboBox_method.setObjectName("comboBox_method")
        self.comboBox_method.addItem("")
        self.comboBox_method.addItem("")
        self.comboBox_method.addItem("")
        self.comboBox_method.addItem("")
        self.horizontalLayout_2.addWidget(self.comboBox_method)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.tableWidget_intp_method_params = QtWidgets.QTableWidget(Dialog_var_spat_interpol)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget_intp_method_params.sizePolicy().hasHeightForWidth())
        self.tableWidget_intp_method_params.setSizePolicy(sizePolicy)
        self.tableWidget_intp_method_params.setObjectName("tableWidget_intp_method_params")
        self.tableWidget_intp_method_params.setColumnCount(2)
        self.tableWidget_intp_method_params.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.tableWidget_intp_method_params.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setStrikeOut(False)
        item.setFont(font)
        self.tableWidget_intp_method_params.setHorizontalHeaderItem(1, item)
        self.tableWidget_intp_method_params.horizontalHeader().setDefaultSectionSize(160)
        self.tableWidget_intp_method_params.verticalHeader().setDefaultSectionSize(25)
        self.tableWidget_intp_method_params.verticalHeader().setMinimumSectionSize(20)
        self.verticalLayout.addWidget(self.tableWidget_intp_method_params)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem5)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label_time_col = QtWidgets.QLabel(Dialog_var_spat_interpol)
        self.label_time_col.setMinimumSize(QtCore.QSize(138, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_time_col.setFont(font)
        self.label_time_col.setObjectName("label_time_col")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_time_col)
        self.lineEdit_time_col = QtWidgets.QLineEdit(Dialog_var_spat_interpol)
        self.lineEdit_time_col.setMinimumSize(QtCore.QSize(100, 20))
        self.lineEdit_time_col.setMaximumSize(QtCore.QSize(100, 16777215))
        self.lineEdit_time_col.setObjectName("lineEdit_time_col")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.lineEdit_time_col)
        self.label_lat_col = QtWidgets.QLabel(Dialog_var_spat_interpol)
        self.label_lat_col.setMinimumSize(QtCore.QSize(138, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_lat_col.setFont(font)
        self.label_lat_col.setObjectName("label_lat_col")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_lat_col)
        self.lineEdit_lat_col = QtWidgets.QLineEdit(Dialog_var_spat_interpol)
        self.lineEdit_lat_col.setMinimumSize(QtCore.QSize(100, 20))
        self.lineEdit_lat_col.setMaximumSize(QtCore.QSize(100, 16777215))
        self.lineEdit_lat_col.setObjectName("lineEdit_lat_col")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.lineEdit_lat_col)
        self.label_lon_col = QtWidgets.QLabel(Dialog_var_spat_interpol)
        self.label_lon_col.setMinimumSize(QtCore.QSize(40, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_lon_col.setFont(font)
        self.label_lon_col.setObjectName("label_lon_col")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_lon_col)
        self.lineEdit_lon_col = QtWidgets.QLineEdit(Dialog_var_spat_interpol)
        self.lineEdit_lon_col.setMinimumSize(QtCore.QSize(100, 20))
        self.lineEdit_lon_col.setMaximumSize(QtCore.QSize(100, 16777215))
        self.lineEdit_lon_col.setObjectName("lineEdit_lon_col")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.lineEdit_lon_col)
        self.horizontalLayout_4.addLayout(self.formLayout)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem6)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.buttonBox_spat_interpol = QtWidgets.QDialogButtonBox(Dialog_var_spat_interpol)
        self.buttonBox_spat_interpol.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.buttonBox_spat_interpol.setStandardButtons(QtWidgets.QDialogButtonBox.StandardButton.Cancel|QtWidgets.QDialogButtonBox.StandardButton.Ok)
        self.buttonBox_spat_interpol.setObjectName("buttonBox_spat_interpol")
        self.verticalLayout.addWidget(self.buttonBox_spat_interpol)

        self.retranslateUi(Dialog_var_spat_interpol)
        self.buttonBox_spat_interpol.accepted.connect(Dialog_var_spat_interpol.accept)
        self.buttonBox_spat_interpol.rejected.connect(Dialog_var_spat_interpol.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog_var_spat_interpol)

    def retranslateUi(self, Dialog_var_spat_interpol):
        _translate = QtCore.QCoreApplication.translate
        Dialog_var_spat_interpol.setWindowTitle(_translate("Dialog_var_spat_interpol", "Spatial Interpolation of a variable"))
        self.label_csv.setText(_translate("Dialog_var_spat_interpol", "File path (.CSV)"))
        self.toolButton_browse_csv.setText(_translate("Dialog_var_spat_interpol", "..."))
        self.toolButton_refresh.setText(_translate("Dialog_var_spat_interpol", "refresh"))
        self.label_xy_raster.setText(_translate("Dialog_var_spat_interpol", "Sample Raster"))
        self.toolButton_browse_xy_raster.setText(_translate("Dialog_var_spat_interpol", "..."))
        self.label_var_name.setText(_translate("Dialog_var_spat_interpol", "Variable name"))
        self.label_time_interval.setText(_translate("Dialog_var_spat_interpol", "Time interval: "))
        self.comboBox_time_interval.setItemText(0, _translate("Dialog_var_spat_interpol", "Daily"))
        self.comboBox_time_interval.setItemText(1, _translate("Dialog_var_spat_interpol", "Monthly"))
        self.comboBox_time_interval.setItemText(2, _translate("Dialog_var_spat_interpol", "Hourly"))
        self.label_method.setText(_translate("Dialog_var_spat_interpol", "Method"))
        self.comboBox_method.setItemText(0, _translate("Dialog_var_spat_interpol", "Inverse Distance"))
        self.comboBox_method.setItemText(1, _translate("Dialog_var_spat_interpol", "Nearest Neighbor"))
        self.comboBox_method.setItemText(2, _translate("Dialog_var_spat_interpol", "ID-NN"))
        self.comboBox_method.setItemText(3, _translate("Dialog_var_spat_interpol", "Linear"))
        item = self.tableWidget_intp_method_params.horizontalHeaderItem(0)
        item.setText(_translate("Dialog_var_spat_interpol", "Meth. Parameter"))
        item = self.tableWidget_intp_method_params.horizontalHeaderItem(1)
        item.setText(_translate("Dialog_var_spat_interpol", "Value"))
        self.label_time_col.setText(_translate("Dialog_var_spat_interpol", "Time column name"))
        self.lineEdit_time_col.setText(_translate("Dialog_var_spat_interpol", "time"))
        self.label_lat_col.setText(_translate("Dialog_var_spat_interpol", "Latitude column name"))
        self.lineEdit_lat_col.setText(_translate("Dialog_var_spat_interpol", "lat"))
        self.label_lon_col.setText(_translate("Dialog_var_spat_interpol", "Longitude column name"))
        self.lineEdit_lon_col.setText(_translate("Dialog_var_spat_interpol", "lon"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog_var_spat_interpol = QtWidgets.QDialog()
    ui = Ui_Dialog_var_spat_interpol()
    ui.setupUi(Dialog_var_spat_interpol)
    Dialog_var_spat_interpol.show()
    sys.exit(app.exec())
