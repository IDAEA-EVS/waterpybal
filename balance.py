# Form implementation generated from reading ui file 'balance.ui'
#
# Created by: PyQt6 UI code generator 6.1.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_balance_Dialog(object):
    def setupUi(self, balance_Dialog):
        balance_Dialog.setObjectName("balance_Dialog")
        balance_Dialog.resize(400, 69)
        self.verticalLayout = QtWidgets.QVBoxLayout(balance_Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_raster = QtWidgets.QLabel(balance_Dialog)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_raster.setFont(font)
        self.label_raster.setObjectName("label_raster")
        self.horizontalLayout.addWidget(self.label_raster)
        self.lineEdit_raster = QtWidgets.QLineEdit(balance_Dialog)
        self.lineEdit_raster.setMinimumSize(QtCore.QSize(160, 20))
        self.lineEdit_raster.setObjectName("lineEdit_raster")
        self.horizontalLayout.addWidget(self.lineEdit_raster)
        self.toolButton_raster = QtWidgets.QToolButton(balance_Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolButton_raster.sizePolicy().hasHeightForWidth())
        self.toolButton_raster.setSizePolicy(sizePolicy)
        self.toolButton_raster.setMaximumSize(QtCore.QSize(20, 20))
        self.toolButton_raster.setObjectName("toolButton_raster")
        self.horizontalLayout.addWidget(self.toolButton_raster)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(balance_Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.StandardButton.Cancel|QtWidgets.QDialogButtonBox.StandardButton.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(balance_Dialog)
        self.buttonBox.accepted.connect(balance_Dialog.accept)
        self.buttonBox.rejected.connect(balance_Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(balance_Dialog)

    def retranslateUi(self, balance_Dialog):
        _translate = QtCore.QCoreApplication.translate
        balance_Dialog.setWindowTitle(_translate("balance_Dialog", "Balance calculation"))
        self.label_raster.setText(_translate("balance_Dialog", "Soil Water Reserve a priori values (raster)"))
        self.toolButton_raster.setText(_translate("balance_Dialog", "..."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    balance_Dialog = QtWidgets.QDialog()
    ui = Ui_balance_Dialog()
    ui.setupUi(balance_Dialog)
    balance_Dialog.show()
    sys.exit(app.exec())
