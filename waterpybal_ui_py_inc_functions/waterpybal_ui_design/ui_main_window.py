# Form implementation generated from reading ui file 'c:\Users\Ash kan\Documents\watbalpy\waterpybal\waterpybal_ui_py_inc_functions\waterpybal_ui_design\main_window.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1114, 480)
        MainWindow.setMinimumSize(QtCore.QSize(1100, 480))
        MainWindow.setMaximumSize(QtCore.QSize(1500, 700))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetMinimumSize)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.groupBox_newds = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_newds.setMinimumSize(QtCore.QSize(310, 105))
        self.groupBox_newds.setMaximumSize(QtCore.QSize(16777215, 156))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.groupBox_newds.setFont(font)
        self.groupBox_newds.setAutoFillBackground(False)
        self.groupBox_newds.setStyleSheet("QGroupBox{border:2px solid gray;border-radius:1px;margin-top: 1ex;}\n"
"QGroupBox::title{subcontrol-origin: margin;subcontrol-position:top center;padding:0 3px;}")
        self.groupBox_newds.setTitle("Create a new WaterPyBal dataset")
        self.groupBox_newds.setFlat(False)
        self.groupBox_newds.setObjectName("groupBox_newds")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_newds)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_dataset_name = QtWidgets.QLabel(self.groupBox_newds)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_dataset_name.sizePolicy().hasHeightForWidth())
        self.label_dataset_name.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_dataset_name.setFont(font)
        self.label_dataset_name.setObjectName("label_dataset_name")
        self.horizontalLayout_10.addWidget(self.label_dataset_name)
        self.lineEdit_name = QtWidgets.QLineEdit(self.groupBox_newds)
        self.lineEdit_name.setMinimumSize(QtCore.QSize(230, 22))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_name.setFont(font)
        self.lineEdit_name.setObjectName("lineEdit_name")
        self.horizontalLayout_10.addWidget(self.lineEdit_name)
        self.verticalLayout_2.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_dataset_dir = QtWidgets.QLabel(self.groupBox_newds)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_dataset_dir.sizePolicy().hasHeightForWidth())
        self.label_dataset_dir.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_dataset_dir.setFont(font)
        self.label_dataset_dir.setObjectName("label_dataset_dir")
        self.horizontalLayout_3.addWidget(self.label_dataset_dir)
        self.lineEdit_path = QtWidgets.QLineEdit(self.groupBox_newds)
        self.lineEdit_path.setMinimumSize(QtCore.QSize(230, 22))
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_path.setFont(font)
        self.lineEdit_path.setObjectName("lineEdit_path")
        self.horizontalLayout_3.addWidget(self.lineEdit_path)
        self.toolButton_path = QtWidgets.QToolButton(self.groupBox_newds)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolButton_path.sizePolicy().hasHeightForWidth())
        self.toolButton_path.setSizePolicy(sizePolicy)
        self.toolButton_path.setMaximumSize(QtCore.QSize(20, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.toolButton_path.setFont(font)
        self.toolButton_path.setObjectName("toolButton_path")
        self.horizontalLayout_3.addWidget(self.toolButton_path)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_to_lat_lon_time = QtWidgets.QPushButton(self.groupBox_newds)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_to_lat_lon_time.sizePolicy().hasHeightForWidth())
        self.pushButton_to_lat_lon_time.setSizePolicy(sizePolicy)
        self.pushButton_to_lat_lon_time.setMinimumSize(QtCore.QSize(150, 28))
        self.pushButton_to_lat_lon_time.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_to_lat_lon_time.setFont(font)
        self.pushButton_to_lat_lon_time.setObjectName("pushButton_to_lat_lon_time")
        self.horizontalLayout.addWidget(self.pushButton_to_lat_lon_time)
        self.label_to_lat_lon_time = QtWidgets.QLabel(self.groupBox_newds)
        self.label_to_lat_lon_time.setEnabled(True)
        self.label_to_lat_lon_time.setMinimumSize(QtCore.QSize(60, 0))
        self.label_to_lat_lon_time.setMaximumSize(QtCore.QSize(70, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_to_lat_lon_time.setFont(font)
        self.label_to_lat_lon_time.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.label_to_lat_lon_time.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.label_to_lat_lon_time.setLineWidth(0)
        self.label_to_lat_lon_time.setMidLineWidth(0)
        self.label_to_lat_lon_time.setText("")
        self.label_to_lat_lon_time.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_to_lat_lon_time.setObjectName("label_to_lat_lon_time")
        self.horizontalLayout.addWidget(self.label_to_lat_lon_time)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_9.addWidget(self.groupBox_newds)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.pushButton_open_dataset = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_open_dataset.sizePolicy().hasHeightForWidth())
        self.pushButton_open_dataset.setSizePolicy(sizePolicy)
        self.pushButton_open_dataset.setMinimumSize(QtCore.QSize(100, 60))
        self.pushButton_open_dataset.setMaximumSize(QtCore.QSize(150, 80))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pushButton_open_dataset.setFont(font)
        self.pushButton_open_dataset.setObjectName("pushButton_open_dataset")
        self.verticalLayout.addWidget(self.pushButton_open_dataset)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout_9.addLayout(self.verticalLayout)
        self.verticalLayout_3.addLayout(self.horizontalLayout_9)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_3.addWidget(self.line)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setMaximumSize(QtCore.QSize(15, 16777215))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout_4.addWidget(self.label)
        self.pushButton_to_var_spat_interpol = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_to_var_spat_interpol.sizePolicy().hasHeightForWidth())
        self.pushButton_to_var_spat_interpol.setSizePolicy(sizePolicy)
        self.pushButton_to_var_spat_interpol.setMinimumSize(QtCore.QSize(280, 28))
        self.pushButton_to_var_spat_interpol.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_to_var_spat_interpol.setFont(font)
        self.pushButton_to_var_spat_interpol.setFlat(False)
        self.pushButton_to_var_spat_interpol.setObjectName("pushButton_to_var_spat_interpol")
        self.horizontalLayout_4.addWidget(self.pushButton_to_var_spat_interpol)
        self.label_to_var_spat_interpol = QtWidgets.QLabel(self.centralwidget)
        self.label_to_var_spat_interpol.setMinimumSize(QtCore.QSize(60, 0))
        self.label_to_var_spat_interpol.setMaximumSize(QtCore.QSize(70, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_to_var_spat_interpol.setFont(font)
        self.label_to_var_spat_interpol.setText("")
        self.label_to_var_spat_interpol.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_to_var_spat_interpol.setObjectName("label_to_var_spat_interpol")
        self.horizontalLayout_4.addWidget(self.label_to_var_spat_interpol)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setMaximumSize(QtCore.QSize(15, 16777215))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_5.addWidget(self.label_2)
        self.pushButton_to_var_from_tiff = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_to_var_from_tiff.sizePolicy().hasHeightForWidth())
        self.pushButton_to_var_from_tiff.setSizePolicy(sizePolicy)
        self.pushButton_to_var_from_tiff.setMinimumSize(QtCore.QSize(280, 28))
        self.pushButton_to_var_from_tiff.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_to_var_from_tiff.setFont(font)
        self.pushButton_to_var_from_tiff.setObjectName("pushButton_to_var_from_tiff")
        self.horizontalLayout_5.addWidget(self.pushButton_to_var_from_tiff)
        self.label_to_var_from_tiff = QtWidgets.QLabel(self.centralwidget)
        self.label_to_var_from_tiff.setMinimumSize(QtCore.QSize(60, 0))
        self.label_to_var_from_tiff.setMaximumSize(QtCore.QSize(70, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_to_var_from_tiff.setFont(font)
        self.label_to_var_from_tiff.setText("")
        self.label_to_var_from_tiff.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_to_var_from_tiff.setObjectName("label_to_var_from_tiff")
        self.horizontalLayout_5.addWidget(self.label_to_var_from_tiff)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setMaximumSize(QtCore.QSize(15, 16777215))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_6.addWidget(self.label_3)
        self.pushButton_to_swr = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_to_swr.sizePolicy().hasHeightForWidth())
        self.pushButton_to_swr.setSizePolicy(sizePolicy)
        self.pushButton_to_swr.setMinimumSize(QtCore.QSize(280, 28))
        self.pushButton_to_swr.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_to_swr.setFont(font)
        self.pushButton_to_swr.setObjectName("pushButton_to_swr")
        self.horizontalLayout_6.addWidget(self.pushButton_to_swr)
        self.label_to_swr = QtWidgets.QLabel(self.centralwidget)
        self.label_to_swr.setMinimumSize(QtCore.QSize(60, 0))
        self.label_to_swr.setMaximumSize(QtCore.QSize(70, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_to_swr.setFont(font)
        self.label_to_swr.setText("")
        self.label_to_swr.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_to_swr.setObjectName("label_to_swr")
        self.horizontalLayout_6.addWidget(self.label_to_swr)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setMaximumSize(QtCore.QSize(15, 16777215))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_7.addWidget(self.label_4)
        self.pushButton_to_etp = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_to_etp.sizePolicy().hasHeightForWidth())
        self.pushButton_to_etp.setSizePolicy(sizePolicy)
        self.pushButton_to_etp.setMinimumSize(QtCore.QSize(280, 28))
        self.pushButton_to_etp.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_to_etp.setFont(font)
        self.pushButton_to_etp.setObjectName("pushButton_to_etp")
        self.horizontalLayout_7.addWidget(self.pushButton_to_etp)
        self.label_to_infiltration = QtWidgets.QLabel(self.centralwidget)
        self.label_to_infiltration.setMinimumSize(QtCore.QSize(60, 0))
        self.label_to_infiltration.setMaximumSize(QtCore.QSize(70, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_to_infiltration.setFont(font)
        self.label_to_infiltration.setText("")
        self.label_to_infiltration.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_to_infiltration.setObjectName("label_to_infiltration")
        self.horizontalLayout_7.addWidget(self.label_to_infiltration)
        self.verticalLayout_3.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setMaximumSize(QtCore.QSize(15, 16777215))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_8.addWidget(self.label_5)
        self.pushButton_to_infiltration = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_to_infiltration.sizePolicy().hasHeightForWidth())
        self.pushButton_to_infiltration.setSizePolicy(sizePolicy)
        self.pushButton_to_infiltration.setMinimumSize(QtCore.QSize(280, 28))
        self.pushButton_to_infiltration.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_to_infiltration.setFont(font)
        self.pushButton_to_infiltration.setObjectName("pushButton_to_infiltration")
        self.horizontalLayout_8.addWidget(self.pushButton_to_infiltration)
        self.label_to_etp = QtWidgets.QLabel(self.centralwidget)
        self.label_to_etp.setMinimumSize(QtCore.QSize(60, 0))
        self.label_to_etp.setMaximumSize(QtCore.QSize(70, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_to_etp.setFont(font)
        self.label_to_etp.setText("")
        self.label_to_etp.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_to_etp.setObjectName("label_to_etp")
        self.horizontalLayout_8.addWidget(self.label_to_etp)
        self.verticalLayout_3.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setMaximumSize(QtCore.QSize(15, 16777215))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_11.addWidget(self.label_6)
        self.pushButton_to_Balance = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_to_Balance.sizePolicy().hasHeightForWidth())
        self.pushButton_to_Balance.setSizePolicy(sizePolicy)
        self.pushButton_to_Balance.setMinimumSize(QtCore.QSize(280, 25))
        self.pushButton_to_Balance.setMaximumSize(QtCore.QSize(16777215, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_to_Balance.setFont(font)
        self.pushButton_to_Balance.setObjectName("pushButton_to_Balance")
        self.horizontalLayout_11.addWidget(self.pushButton_to_Balance)
        self.label_to_Balance = QtWidgets.QLabel(self.centralwidget)
        self.label_to_Balance.setMinimumSize(QtCore.QSize(60, 0))
        self.label_to_Balance.setMaximumSize(QtCore.QSize(70, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_to_Balance.setFont(font)
        self.label_to_Balance.setText("")
        self.label_to_Balance.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_to_Balance.setObjectName("label_to_Balance")
        self.horizontalLayout_11.addWidget(self.label_to_Balance)
        self.verticalLayout_3.addLayout(self.horizontalLayout_11)
        self.pushButton_to_visualization = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_to_visualization.sizePolicy().hasHeightForWidth())
        self.pushButton_to_visualization.setSizePolicy(sizePolicy)
        self.pushButton_to_visualization.setMinimumSize(QtCore.QSize(300, 28))
        self.pushButton_to_visualization.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_to_visualization.setFont(font)
        self.pushButton_to_visualization.setObjectName("pushButton_to_visualization")
        self.verticalLayout_3.addWidget(self.pushButton_to_visualization)
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_3.addWidget(self.line_2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem2 = QtWidgets.QSpacerItem(90, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.pushButton_save_dataset = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_save_dataset.setMinimumSize(QtCore.QSize(190, 28))
        self.pushButton_save_dataset.setMaximumSize(QtCore.QSize(250, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_save_dataset.setFont(font)
        self.pushButton_save_dataset.setObjectName("pushButton_save_dataset")
        self.horizontalLayout_2.addWidget(self.pushButton_save_dataset)
        spacerItem3 = QtWidgets.QSpacerItem(90, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_12.addLayout(self.verticalLayout_3)
        self.groupBox_help = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_help.setMinimumSize(QtCore.QSize(570, 450))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.groupBox_help.setFont(font)
        self.groupBox_help.setAutoFillBackground(False)
        self.groupBox_help.setStyleSheet("QGroupBox{border:2px solid gray;border-radius:1px;margin-top: 1ex;}\n"
"QGroupBox::title{subcontrol-origin: margin;subcontrol-position:top center;padding:0 3px;}")
        self.groupBox_help.setTitle("Help")
        self.groupBox_help.setFlat(False)
        self.groupBox_help.setObjectName("groupBox_help")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox_help)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.textBrowser_help = QtWidgets.QTextBrowser(self.groupBox_help)
        self.textBrowser_help.setMinimumSize(QtCore.QSize(550, 375))
        self.textBrowser_help.setAutoFillBackground(True)
        self.textBrowser_help.setStyleSheet("background-color: rgb(240, 240, 240)")
        self.textBrowser_help.setFrameShape(QtWidgets.QFrame.Shape.WinPanel)
        self.textBrowser_help.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.textBrowser_help.setLineWidth(0)
        self.textBrowser_help.setReadOnly(True)
        self.textBrowser_help.setObjectName("textBrowser_help")
        self.verticalLayout_4.addWidget(self.textBrowser_help)
        self.horizontalLayout_12.addWidget(self.groupBox_help)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.label_dataset_name.setBuddy(self.lineEdit_name)
        self.label_dataset_dir.setBuddy(self.lineEdit_path)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.pushButton_to_var_spat_interpol, self.pushButton_to_var_from_tiff)
        MainWindow.setTabOrder(self.pushButton_to_var_from_tiff, self.pushButton_to_swr)
        MainWindow.setTabOrder(self.pushButton_to_swr, self.pushButton_to_visualization)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "WaterPyBal Interface Main Window"))
        self.label_dataset_name.setText(_translate("MainWindow", "Dataset &name"))
        self.label_dataset_dir.setText(_translate("MainWindow", "Dataset &path"))
        self.toolButton_path.setText(_translate("MainWindow", "..."))
        self.pushButton_to_lat_lon_time.setText(_translate("MainWindow", "New dataset properties ..."))
        self.pushButton_open_dataset.setText(_translate("MainWindow", "Open an existing\n"
" WaterPyBal\n"
" dataset ..."))
        self.label.setText(_translate("MainWindow", "1."))
        self.pushButton_to_var_spat_interpol.setText(_translate("MainWindow", "Variable introduction and spatial interpolation"))
        self.label_2.setText(_translate("MainWindow", "2."))
        self.pushButton_to_var_from_tiff.setText(_translate("MainWindow", "Import data from a tiff archive"))
        self.label_3.setText(_translate("MainWindow", "3."))
        self.pushButton_to_swr.setText(_translate("MainWindow", "Soil Water Reserve Calculation"))
        self.label_4.setText(_translate("MainWindow", "4."))
        self.pushButton_to_etp.setText(_translate("MainWindow", "PET Calculation"))
        self.label_5.setText(_translate("MainWindow", "5."))
        self.pushButton_to_infiltration.setText(_translate("MainWindow", "Infiltration Calculation"))
        self.label_6.setText(_translate("MainWindow", "6."))
        self.pushButton_to_Balance.setText(_translate("MainWindow", "Balance Calculation"))
        self.pushButton_to_visualization.setText(_translate("MainWindow", "Visualization and outputs"))
        self.pushButton_save_dataset.setText(_translate("MainWindow", "&Save and close WaterPyBal dataset"))
        self.textBrowser_help.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.1pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
