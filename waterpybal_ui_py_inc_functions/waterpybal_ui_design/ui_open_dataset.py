# Form implementation generated from reading ui file 'c:\Users\Ash kan\Documents\watbalpy\waterpybal\waterpybal_ui_py_inc_functions\waterpybal_ui_design\open_dataset.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog_open_dataset(object):
    def setupUi(self, Dialog_open_dataset):
        Dialog_open_dataset.setObjectName("Dialog_open_dataset")
        Dialog_open_dataset.resize(560, 145)
        Dialog_open_dataset.setMinimumSize(QtCore.QSize(560, 0))
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog_open_dataset)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_open_dataset = QtWidgets.QLabel(Dialog_open_dataset)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_open_dataset.sizePolicy().hasHeightForWidth())
        self.label_open_dataset.setSizePolicy(sizePolicy)
        self.label_open_dataset.setMinimumSize(QtCore.QSize(130, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_open_dataset.setFont(font)
        self.label_open_dataset.setObjectName("label_open_dataset")
        self.horizontalLayout.addWidget(self.label_open_dataset)
        self.lineEdit_open = QtWidgets.QLineEdit(Dialog_open_dataset)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.MinimumExpanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_open.sizePolicy().hasHeightForWidth())
        self.lineEdit_open.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.lineEdit_open.setFont(font)
        self.lineEdit_open.setObjectName("lineEdit_open")
        self.horizontalLayout.addWidget(self.lineEdit_open)
        self.toolButton_open = QtWidgets.QToolButton(Dialog_open_dataset)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolButton_open.sizePolicy().hasHeightForWidth())
        self.toolButton_open.setSizePolicy(sizePolicy)
        self.toolButton_open.setMaximumSize(QtCore.QSize(20, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.toolButton_open.setFont(font)
        self.toolButton_open.setObjectName("toolButton_open")
        self.horizontalLayout.addWidget(self.toolButton_open)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_sample_raster = QtWidgets.QLabel(Dialog_open_dataset)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_sample_raster.setFont(font)
        self.label_sample_raster.setObjectName("label_sample_raster")
        self.horizontalLayout_2.addWidget(self.label_sample_raster)
        self.lineEdit_sample_raster = QtWidgets.QLineEdit(Dialog_open_dataset)
        self.lineEdit_sample_raster.setMinimumSize(QtCore.QSize(160, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.lineEdit_sample_raster.setFont(font)
        self.lineEdit_sample_raster.setObjectName("lineEdit_sample_raster")
        self.horizontalLayout_2.addWidget(self.lineEdit_sample_raster)
        self.toolButton_browse_xy_raster = QtWidgets.QToolButton(Dialog_open_dataset)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolButton_browse_xy_raster.sizePolicy().hasHeightForWidth())
        self.toolButton_browse_xy_raster.setSizePolicy(sizePolicy)
        self.toolButton_browse_xy_raster.setMaximumSize(QtCore.QSize(20, 20))
        self.toolButton_browse_xy_raster.setObjectName("toolButton_browse_xy_raster")
        self.horizontalLayout_2.addWidget(self.toolButton_browse_xy_raster)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog_open_dataset)
        self.buttonBox.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.StandardButton.Cancel|QtWidgets.QDialogButtonBox.StandardButton.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)
        self.label_open_dataset.setBuddy(self.lineEdit_open)

        self.retranslateUi(Dialog_open_dataset)
        self.buttonBox.accepted.connect(Dialog_open_dataset.accept) # type: ignore
        self.buttonBox.rejected.connect(Dialog_open_dataset.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Dialog_open_dataset)

    def retranslateUi(self, Dialog_open_dataset):
        _translate = QtCore.QCoreApplication.translate
        Dialog_open_dataset.setWindowTitle(_translate("Dialog_open_dataset", "Open Dataset"))
        self.label_open_dataset.setText(_translate("Dialog_open_dataset", "WaterpyBal dataset Path"))
        self.toolButton_open.setText(_translate("Dialog_open_dataset", "..."))
        self.label_sample_raster.setText(_translate("Dialog_open_dataset", "Sample Raster of the area"))
        self.toolButton_browse_xy_raster.setText(_translate("Dialog_open_dataset", "..."))
