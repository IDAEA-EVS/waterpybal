# Form implementation generated from reading ui file 'var_from_tiff.ui'
#
# Created by: PyQt6 UI code generator 6.1.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog_var_from_tiff(object):
    def setupUi(self, Dialog_var_from_tiff):
        Dialog_var_from_tiff.setObjectName("Dialog_var_from_tiff")
        Dialog_var_from_tiff.resize(838, 200)
        Dialog_var_from_tiff.setMaximumSize(QtCore.QSize(16777215, 200))
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog_var_from_tiff)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_from_tiffs = QtWidgets.QLabel(Dialog_var_from_tiff)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_from_tiffs.setFont(font)
        self.label_from_tiffs.setObjectName("label_from_tiffs")
        self.verticalLayout.addWidget(self.label_from_tiffs)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_var_path = QtWidgets.QLabel(Dialog_var_from_tiff)
        self.label_var_path.setMinimumSize(QtCore.QSize(70, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_var_path.setFont(font)
        self.label_var_path.setObjectName("label_var_path")
        self.horizontalLayout_2.addWidget(self.label_var_path)
        self.lineEdit_var_path = QtWidgets.QLineEdit(Dialog_var_from_tiff)
        self.lineEdit_var_path.setMinimumSize(QtCore.QSize(150, 20))
        self.lineEdit_var_path.setObjectName("lineEdit_var_path")
        self.horizontalLayout_2.addWidget(self.lineEdit_var_path)
        self.toolButton = QtWidgets.QToolButton(Dialog_var_from_tiff)
        self.toolButton.setMinimumSize(QtCore.QSize(0, 20))
        self.toolButton.setMaximumSize(QtCore.QSize(30, 20))
        self.toolButton.setObjectName("toolButton")
        self.horizontalLayout_2.addWidget(self.toolButton)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.checkBox = QtWidgets.QCheckBox(Dialog_var_from_tiff)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBox.setFont(font)
        self.checkBox.setChecked(False)
        self.checkBox.setObjectName("checkBox")
        self.verticalLayout.addWidget(self.checkBox)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.label_var_name = QtWidgets.QLabel(Dialog_var_from_tiff)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_var_name.sizePolicy().hasHeightForWidth())
        self.label_var_name.setSizePolicy(sizePolicy)
        self.label_var_name.setMinimumSize(QtCore.QSize(70, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_var_name.setFont(font)
        self.label_var_name.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_var_name.setObjectName("label_var_name")
        self.horizontalLayout.addWidget(self.label_var_name)
        self.comboBox = QtWidgets.QComboBox(Dialog_var_from_tiff)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy)
        self.comboBox.setMinimumSize(QtCore.QSize(70, 20))
        self.comboBox.setObjectName("comboBox")
        self.horizontalLayout.addWidget(self.comboBox)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem5)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem6)
        self.buttonBox_from_tiff = QtWidgets.QDialogButtonBox(Dialog_var_from_tiff)
        self.buttonBox_from_tiff.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.buttonBox_from_tiff.setStandardButtons(QtWidgets.QDialogButtonBox.StandardButton.Cancel|QtWidgets.QDialogButtonBox.StandardButton.Ok)
        self.buttonBox_from_tiff.setObjectName("buttonBox_from_tiff")
        self.verticalLayout.addWidget(self.buttonBox_from_tiff)

        self.retranslateUi(Dialog_var_from_tiff)
        self.buttonBox_from_tiff.accepted.connect(Dialog_var_from_tiff.accept)
        self.buttonBox_from_tiff.rejected.connect(Dialog_var_from_tiff.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog_var_from_tiff)

    def retranslateUi(self, Dialog_var_from_tiff):
        _translate = QtCore.QCoreApplication.translate
        Dialog_var_from_tiff.setWindowTitle(_translate("Dialog_var_from_tiff", "Import data from TIFF archives"))
        self.label_from_tiffs.setText(_translate("Dialog_var_from_tiff", "Introduce variables from single band tiffs:"))
        self.label_var_path.setText(_translate("Dialog_var_from_tiff", "Folder path"))
        self.toolButton.setText(_translate("Dialog_var_from_tiff", "..."))
        self.checkBox.setText(_translate("Dialog_var_from_tiff", "In case time interval of .tiff is not the same as the Database, Use the same values for valid time steps(EX: Temp. vs comulative precipitation)"))
        self.label_var_name.setText(_translate("Dialog_var_from_tiff", "Variable name"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog_var_from_tiff = QtWidgets.QDialog()
    ui = Ui_Dialog_var_from_tiff()
    ui.setupUi(Dialog_var_from_tiff)
    Dialog_var_from_tiff.show()
    sys.exit(app.exec())
