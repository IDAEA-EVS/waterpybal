# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'var_spat_interpol.ui'
##
## Created by: Qt User Interface Compiler version 6.2.4
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractButton, QApplication, QCheckBox, QComboBox,
    QDialog, QDialogButtonBox, QFrame, QGridLayout,
    QGroupBox, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QSizePolicy, QSpacerItem, QTableWidget,
    QTableWidgetItem, QTextBrowser, QToolButton, QVBoxLayout,
    QWidget)

class Ui_Dialog_var_spat_interpol(object):
    def setupUi(self, Dialog_var_spat_interpol):
        if not Dialog_var_spat_interpol.objectName():
            Dialog_var_spat_interpol.setObjectName(u"Dialog_var_spat_interpol")
        Dialog_var_spat_interpol.resize(803, 749)
        Dialog_var_spat_interpol.setMinimumSize(QSize(800, 620))
        self.horizontalLayout_21 = QHBoxLayout(Dialog_var_spat_interpol)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.groupBox_variable_input = QGroupBox(Dialog_var_spat_interpol)
        self.groupBox_variable_input.setObjectName(u"groupBox_variable_input")
        self.groupBox_variable_input.setMinimumSize(QSize(570, 385))
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_variable_input)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_xy_raster = QLabel(self.groupBox_variable_input)
        self.label_xy_raster.setObjectName(u"label_xy_raster")
        font = QFont()
        font.setPointSize(10)
        self.label_xy_raster.setFont(font)

        self.horizontalLayout_5.addWidget(self.label_xy_raster)

        self.lineEdit_xyraster = QLineEdit(self.groupBox_variable_input)
        self.lineEdit_xyraster.setObjectName(u"lineEdit_xyraster")
        self.lineEdit_xyraster.setMinimumSize(QSize(160, 20))
        font1 = QFont()
        font1.setPointSize(8)
        self.lineEdit_xyraster.setFont(font1)

        self.horizontalLayout_5.addWidget(self.lineEdit_xyraster)

        self.toolButton_browse_xy_raster = QToolButton(self.groupBox_variable_input)
        self.toolButton_browse_xy_raster.setObjectName(u"toolButton_browse_xy_raster")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolButton_browse_xy_raster.sizePolicy().hasHeightForWidth())
        self.toolButton_browse_xy_raster.setSizePolicy(sizePolicy)
        self.toolButton_browse_xy_raster.setMaximumSize(QSize(20, 20))

        self.horizontalLayout_5.addWidget(self.toolButton_browse_xy_raster)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_csv = QLabel(self.groupBox_variable_input)
        self.label_csv.setObjectName(u"label_csv")
        self.label_csv.setFont(font)

        self.horizontalLayout.addWidget(self.label_csv)

        self.lineEdit_csv = QLineEdit(self.groupBox_variable_input)
        self.lineEdit_csv.setObjectName(u"lineEdit_csv")
        self.lineEdit_csv.setMinimumSize(QSize(160, 20))

        self.horizontalLayout.addWidget(self.lineEdit_csv)

        self.toolButton_browse_csv = QToolButton(self.groupBox_variable_input)
        self.toolButton_browse_csv.setObjectName(u"toolButton_browse_csv")
        sizePolicy.setHeightForWidth(self.toolButton_browse_csv.sizePolicy().hasHeightForWidth())
        self.toolButton_browse_csv.setSizePolicy(sizePolicy)
        self.toolButton_browse_csv.setMaximumSize(QSize(20, 20))

        self.horizontalLayout.addWidget(self.toolButton_browse_csv)

        self.toolButton_refresh = QToolButton(self.groupBox_variable_input)
        self.toolButton_refresh.setObjectName(u"toolButton_refresh")
        self.toolButton_refresh.setMinimumSize(QSize(40, 20))

        self.horizontalLayout.addWidget(self.toolButton_refresh)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.tableWidget_intp_method_params = QTableWidget(self.groupBox_variable_input)
        if (self.tableWidget_intp_method_params.columnCount() < 2):
            self.tableWidget_intp_method_params.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_intp_method_params.setHorizontalHeaderItem(0, __qtablewidgetitem)
        font2 = QFont()
        font2.setStrikeOut(False)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem1.setFont(font2);
        self.tableWidget_intp_method_params.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.tableWidget_intp_method_params.setObjectName(u"tableWidget_intp_method_params")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.tableWidget_intp_method_params.sizePolicy().hasHeightForWidth())
        self.tableWidget_intp_method_params.setSizePolicy(sizePolicy1)
        self.tableWidget_intp_method_params.setMinimumSize(QSize(330, 0))
        self.tableWidget_intp_method_params.horizontalHeader().setDefaultSectionSize(160)
        self.tableWidget_intp_method_params.verticalHeader().setMinimumSectionSize(20)
        self.tableWidget_intp_method_params.verticalHeader().setDefaultSectionSize(25)

        self.horizontalLayout_7.addWidget(self.tableWidget_intp_method_params)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_method = QLabel(self.groupBox_variable_input)
        self.label_method.setObjectName(u"label_method")
        self.label_method.setMinimumSize(QSize(45, 20))
        self.label_method.setFont(font)

        self.horizontalLayout_2.addWidget(self.label_method)

        self.comboBox_method = QComboBox(self.groupBox_variable_input)
        self.comboBox_method.addItem("")
        self.comboBox_method.addItem("")
        self.comboBox_method.addItem("")
        self.comboBox_method.addItem("")
        self.comboBox_method.setObjectName(u"comboBox_method")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.comboBox_method.sizePolicy().hasHeightForWidth())
        self.comboBox_method.setSizePolicy(sizePolicy2)
        self.comboBox_method.setMinimumSize(QSize(100, 20))

        self.horizontalLayout_2.addWidget(self.comboBox_method)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_time_interval = QLabel(self.groupBox_variable_input)
        self.label_time_interval.setObjectName(u"label_time_interval")
        self.label_time_interval.setMaximumSize(QSize(100, 16777215))
        self.label_time_interval.setFont(font)

        self.horizontalLayout_6.addWidget(self.label_time_interval)

        self.comboBox_time_interval = QComboBox(self.groupBox_variable_input)
        self.comboBox_time_interval.addItem("")
        self.comboBox_time_interval.addItem("")
        self.comboBox_time_interval.addItem("")
        self.comboBox_time_interval.setObjectName(u"comboBox_time_interval")
        self.comboBox_time_interval.setMinimumSize(QSize(60, 20))
        self.comboBox_time_interval.setFont(font1)

        self.horizontalLayout_6.addWidget(self.comboBox_time_interval)


        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_var_name = QLabel(self.groupBox_variable_input)
        self.label_var_name.setObjectName(u"label_var_name")
        self.label_var_name.setMinimumSize(QSize(85, 20))
        self.label_var_name.setFont(font)

        self.horizontalLayout_3.addWidget(self.label_var_name)

        self.comboBox_var_name = QComboBox(self.groupBox_variable_input)
        self.comboBox_var_name.setObjectName(u"comboBox_var_name")
        sizePolicy2.setHeightForWidth(self.comboBox_var_name.sizePolicy().hasHeightForWidth())
        self.comboBox_var_name.setSizePolicy(sizePolicy2)
        self.comboBox_var_name.setMinimumSize(QSize(70, 20))

        self.horizontalLayout_3.addWidget(self.comboBox_var_name)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.checkBox = QCheckBox(self.groupBox_variable_input)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setMinimumSize(QSize(170, 130))
        self.checkBox.setFont(font)
        self.checkBox.setChecked(False)

        self.verticalLayout.addWidget(self.checkBox)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.label_2 = QLabel(self.groupBox_variable_input)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_3 = QLabel(self.groupBox_variable_input)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)

        self.label_longx = QLabel(self.groupBox_variable_input)
        self.label_longx.setObjectName(u"label_longx")

        self.gridLayout.addWidget(self.label_longx, 0, 1, 1, 1)

        self.label_4 = QLabel(self.groupBox_variable_input)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)

        self.label_laty = QLabel(self.groupBox_variable_input)
        self.label_laty.setObjectName(u"label_laty")

        self.gridLayout.addWidget(self.label_laty, 1, 1, 1, 1)

        self.label_5 = QLabel(self.groupBox_variable_input)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 2, 0, 1, 1)

        self.label_time = QLabel(self.groupBox_variable_input)
        self.label_time.setObjectName(u"label_time")

        self.gridLayout.addWidget(self.label_time, 2, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)


        self.horizontalLayout_7.addLayout(self.verticalLayout)


        self.verticalLayout_2.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_time_col = QLabel(self.groupBox_variable_input)
        self.label_time_col.setObjectName(u"label_time_col")
        self.label_time_col.setMinimumSize(QSize(110, 20))
        self.label_time_col.setFont(font)

        self.horizontalLayout_4.addWidget(self.label_time_col)

        self.lineEdit_time_col = QLineEdit(self.groupBox_variable_input)
        self.lineEdit_time_col.setObjectName(u"lineEdit_time_col")
        self.lineEdit_time_col.setMinimumSize(QSize(50, 20))
        self.lineEdit_time_col.setMaximumSize(QSize(70, 16777215))

        self.horizontalLayout_4.addWidget(self.lineEdit_time_col)


        self.horizontalLayout_10.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_lat_col = QLabel(self.groupBox_variable_input)
        self.label_lat_col.setObjectName(u"label_lat_col")
        self.label_lat_col.setMinimumSize(QSize(120, 20))
        self.label_lat_col.setFont(font)

        self.horizontalLayout_8.addWidget(self.label_lat_col)

        self.lineEdit_lat_col = QLineEdit(self.groupBox_variable_input)
        self.lineEdit_lat_col.setObjectName(u"lineEdit_lat_col")
        self.lineEdit_lat_col.setMinimumSize(QSize(50, 20))
        self.lineEdit_lat_col.setMaximumSize(QSize(70, 16777215))

        self.horizontalLayout_8.addWidget(self.lineEdit_lat_col)


        self.horizontalLayout_10.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_lon_col = QLabel(self.groupBox_variable_input)
        self.label_lon_col.setObjectName(u"label_lon_col")
        self.label_lon_col.setMinimumSize(QSize(130, 20))
        self.label_lon_col.setFont(font)

        self.horizontalLayout_9.addWidget(self.label_lon_col)

        self.lineEdit_lon_col = QLineEdit(self.groupBox_variable_input)
        self.lineEdit_lon_col.setObjectName(u"lineEdit_lon_col")
        self.lineEdit_lon_col.setMinimumSize(QSize(50, 20))
        self.lineEdit_lon_col.setMaximumSize(QSize(70, 16777215))

        self.horizontalLayout_9.addWidget(self.lineEdit_lon_col)


        self.horizontalLayout_10.addLayout(self.horizontalLayout_9)


        self.verticalLayout_2.addLayout(self.horizontalLayout_10)


        self.verticalLayout_6.addWidget(self.groupBox_variable_input)

        self.checkBox_variable_input = QCheckBox(Dialog_var_spat_interpol)
        self.checkBox_variable_input.setObjectName(u"checkBox_variable_input")

        self.verticalLayout_6.addWidget(self.checkBox_variable_input)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.groupBox = QGroupBox(Dialog_var_spat_interpol)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setEnabled(False)
        self.verticalLayout_3 = QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")

        self.verticalLayout_3.addLayout(self.horizontalLayout_14)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_var_name_same_val = QLabel(self.groupBox)
        self.label_var_name_same_val.setObjectName(u"label_var_name_same_val")
        self.label_var_name_same_val.setMinimumSize(QSize(85, 20))
        self.label_var_name_same_val.setFont(font)

        self.horizontalLayout_11.addWidget(self.label_var_name_same_val)

        self.comboBox_var_same_val = QComboBox(self.groupBox)
        self.comboBox_var_same_val.setObjectName(u"comboBox_var_same_val")
        sizePolicy2.setHeightForWidth(self.comboBox_var_same_val.sizePolicy().hasHeightForWidth())
        self.comboBox_var_same_val.setSizePolicy(sizePolicy2)
        self.comboBox_var_same_val.setMinimumSize(QSize(70, 20))

        self.horizontalLayout_11.addWidget(self.comboBox_var_same_val)


        self.horizontalLayout_13.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(40, 16777215))

        self.horizontalLayout_12.addWidget(self.label)

        self.lineEdit_same_val = QLineEdit(self.groupBox)
        self.lineEdit_same_val.setObjectName(u"lineEdit_same_val")
        self.lineEdit_same_val.setMinimumSize(QSize(100, 20))
        self.lineEdit_same_val.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_12.addWidget(self.lineEdit_same_val)


        self.horizontalLayout_13.addLayout(self.horizontalLayout_12)


        self.verticalLayout_3.addLayout(self.horizontalLayout_13)


        self.horizontalLayout_15.addWidget(self.groupBox)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer)


        self.verticalLayout_6.addLayout(self.horizontalLayout_15)

        self.checkBox_nc = QCheckBox(Dialog_var_spat_interpol)
        self.checkBox_nc.setObjectName(u"checkBox_nc")

        self.verticalLayout_6.addWidget(self.checkBox_nc)

        self.groupBox_2 = QGroupBox(Dialog_var_spat_interpol)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setEnabled(False)
        self.horizontalLayout_17 = QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.label_nc = QLabel(self.groupBox_2)
        self.label_nc.setObjectName(u"label_nc")
        self.label_nc.setFont(font)

        self.horizontalLayout_18.addWidget(self.label_nc)

        self.lineEdit_nc = QLineEdit(self.groupBox_2)
        self.lineEdit_nc.setObjectName(u"lineEdit_nc")
        self.lineEdit_nc.setMinimumSize(QSize(160, 20))

        self.horizontalLayout_18.addWidget(self.lineEdit_nc)

        self.toolButton_browse_nc = QToolButton(self.groupBox_2)
        self.toolButton_browse_nc.setObjectName(u"toolButton_browse_nc")
        sizePolicy.setHeightForWidth(self.toolButton_browse_nc.sizePolicy().hasHeightForWidth())
        self.toolButton_browse_nc.setSizePolicy(sizePolicy)
        self.toolButton_browse_nc.setMaximumSize(QSize(20, 20))

        self.horizontalLayout_18.addWidget(self.toolButton_browse_nc)

        self.toolButton_refresh_nc = QToolButton(self.groupBox_2)
        self.toolButton_refresh_nc.setObjectName(u"toolButton_refresh_nc")
        self.toolButton_refresh_nc.setMinimumSize(QSize(40, 20))

        self.horizontalLayout_18.addWidget(self.toolButton_refresh_nc)


        self.verticalLayout_5.addLayout(self.horizontalLayout_18)

        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.label_var_name_nc = QLabel(self.groupBox_2)
        self.label_var_name_nc.setObjectName(u"label_var_name_nc")
        self.label_var_name_nc.setMinimumSize(QSize(85, 20))
        self.label_var_name_nc.setFont(font)

        self.horizontalLayout_19.addWidget(self.label_var_name_nc)

        self.comboBox_var_name_nc = QComboBox(self.groupBox_2)
        self.comboBox_var_name_nc.setObjectName(u"comboBox_var_name_nc")
        sizePolicy2.setHeightForWidth(self.comboBox_var_name_nc.sizePolicy().hasHeightForWidth())
        self.comboBox_var_name_nc.setSizePolicy(sizePolicy2)
        self.comboBox_var_name_nc.setMinimumSize(QSize(70, 20))

        self.horizontalLayout_19.addWidget(self.comboBox_var_name_nc)


        self.horizontalLayout_20.addLayout(self.horizontalLayout_19)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer_2)


        self.verticalLayout_5.addLayout(self.horizontalLayout_20)


        self.horizontalLayout_17.addLayout(self.verticalLayout_5)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_9 = QLabel(self.groupBox_2)
        self.label_9.setObjectName(u"label_9")

        self.verticalLayout_4.addWidget(self.label_9)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_6 = QLabel(self.groupBox_2)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_2.addWidget(self.label_6, 0, 0, 1, 1)

        self.label_longx_new = QLabel(self.groupBox_2)
        self.label_longx_new.setObjectName(u"label_longx_new")

        self.gridLayout_2.addWidget(self.label_longx_new, 0, 1, 1, 1)

        self.label_7 = QLabel(self.groupBox_2)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_2.addWidget(self.label_7, 1, 0, 1, 1)

        self.label_laty_new = QLabel(self.groupBox_2)
        self.label_laty_new.setObjectName(u"label_laty_new")

        self.gridLayout_2.addWidget(self.label_laty_new, 1, 1, 1, 1)

        self.label_8 = QLabel(self.groupBox_2)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_2.addWidget(self.label_8, 2, 0, 1, 1)

        self.label_time_new = QLabel(self.groupBox_2)
        self.label_time_new.setObjectName(u"label_time_new")

        self.gridLayout_2.addWidget(self.label_time_new, 2, 1, 1, 1)


        self.verticalLayout_4.addLayout(self.gridLayout_2)


        self.horizontalLayout_17.addLayout(self.verticalLayout_4)


        self.verticalLayout_6.addWidget(self.groupBox_2)

        self.buttonBox_spat_interpol = QDialogButtonBox(Dialog_var_spat_interpol)
        self.buttonBox_spat_interpol.setObjectName(u"buttonBox_spat_interpol")
        self.buttonBox_spat_interpol.setOrientation(Qt.Horizontal)
        self.buttonBox_spat_interpol.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout_6.addWidget(self.buttonBox_spat_interpol)


        self.horizontalLayout_21.addLayout(self.verticalLayout_6)

        self.groupBox_help = QGroupBox(Dialog_var_spat_interpol)
        self.groupBox_help.setObjectName(u"groupBox_help")
        self.groupBox_help.setMinimumSize(QSize(150, 0))
        font3 = QFont()
        font3.setPointSize(9)
        self.groupBox_help.setFont(font3)
        self.groupBox_help.setAutoFillBackground(False)
        self.groupBox_help.setStyleSheet(u"QGroupBox{border:2px solid gray;border-radius:1px;margin-top: 1ex;}\n"
"QGroupBox::title{subcontrol-origin: margin;subcontrol-position:top center;padding:0 3px;}")
        self.groupBox_help.setTitle(u"Help")
        self.groupBox_help.setFlat(False)
        self.horizontalLayout_16 = QHBoxLayout(self.groupBox_help)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.textBrowser_help = QTextBrowser(self.groupBox_help)
        self.textBrowser_help.setObjectName(u"textBrowser_help")
        self.textBrowser_help.setAutoFillBackground(True)
        self.textBrowser_help.setStyleSheet(u"background-color: rgb(240, 240, 240)")
        self.textBrowser_help.setFrameShape(QFrame.WinPanel)
        self.textBrowser_help.setFrameShadow(QFrame.Sunken)
        self.textBrowser_help.setLineWidth(0)
        self.textBrowser_help.setReadOnly(True)

        self.horizontalLayout_16.addWidget(self.textBrowser_help)


        self.horizontalLayout_21.addWidget(self.groupBox_help)


        self.retranslateUi(Dialog_var_spat_interpol)
        self.buttonBox_spat_interpol.accepted.connect(Dialog_var_spat_interpol.accept)
        self.buttonBox_spat_interpol.rejected.connect(Dialog_var_spat_interpol.reject)

        QMetaObject.connectSlotsByName(Dialog_var_spat_interpol)
    # setupUi

    def retranslateUi(self, Dialog_var_spat_interpol):
        Dialog_var_spat_interpol.setWindowTitle(QCoreApplication.translate("Dialog_var_spat_interpol", u"Variable introduction and spatial interpolation", None))
        self.groupBox_variable_input.setTitle(QCoreApplication.translate("Dialog_var_spat_interpol", u"Variable interpolation from a .CSV file", None))
        self.label_xy_raster.setText(QCoreApplication.translate("Dialog_var_spat_interpol", u"Sample Raster", None))
        self.toolButton_browse_xy_raster.setText(QCoreApplication.translate("Dialog_var_spat_interpol", u"...", None))
        self.label_csv.setText(QCoreApplication.translate("Dialog_var_spat_interpol", u"File path (.CSV)", None))
        self.toolButton_browse_csv.setText(QCoreApplication.translate("Dialog_var_spat_interpol", u"...", None))
        self.toolButton_refresh.setText(QCoreApplication.translate("Dialog_var_spat_interpol", u"refresh", None))
        ___qtablewidgetitem = self.tableWidget_intp_method_params.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Dialog_var_spat_interpol", u"Meth. Parameter", None));
        ___qtablewidgetitem1 = self.tableWidget_intp_method_params.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Dialog_var_spat_interpol", u"Value", None));
        self.label_method.setText(QCoreApplication.translate("Dialog_var_spat_interpol", u"Method", None))
        self.comboBox_method.setItemText(0, QCoreApplication.translate("Dialog_var_spat_interpol", u"Inverse Distance", None))
        self.comboBox_method.setItemText(1, QCoreApplication.translate("Dialog_var_spat_interpol", u"Nearest Neighbor", None))
        self.comboBox_method.setItemText(2, QCoreApplication.translate("Dialog_var_spat_interpol", u"ID-NN", None))
        self.comboBox_method.setItemText(3, QCoreApplication.translate("Dialog_var_spat_interpol", u"Linear", None))

        self.label_time_interval.setText(QCoreApplication.translate("Dialog_var_spat_interpol", u"CSV time interval: ", None))
        self.comboBox_time_interval.setItemText(0, QCoreApplication.translate("Dialog_var_spat_interpol", u"Daily", None))
        self.comboBox_time_interval.setItemText(1, QCoreApplication.translate("Dialog_var_spat_interpol", u"Monthly", None))
        self.comboBox_time_interval.setItemText(2, QCoreApplication.translate("Dialog_var_spat_interpol", u"Hourly", None))

        self.label_var_name.setText(QCoreApplication.translate("Dialog_var_spat_interpol", u"Variable name", None))
        self.checkBox.setText(QCoreApplication.translate("Dialog_var_spat_interpol", u"\n"
"In case .CSV time interval is not\n"
"the same as the Database, use \n"
"the same values for valid time\n"
"steps (EX: Temp. vs cumulative\n"
"precipitation)\n"
"", None))
        self.label_2.setText(QCoreApplication.translate("Dialog_var_spat_interpol", u"WaterpyBal Dataset dimension size:", None))
        self.label_3.setText(QCoreApplication.translate("Dialog_var_spat_interpol", u"Long.:", None))
        self.label_longx.setText("")
        self.label_4.setText(QCoreApplication.translate("Dialog_var_spat_interpol", u"Lat.:", None))
        self.label_laty.setText("")
        self.label_5.setText(QCoreApplication.translate("Dialog_var_spat_interpol", u"Time.:", None))
        self.label_time.setText("")
        self.label_time_col.setText(QCoreApplication.translate("Dialog_var_spat_interpol", u"CSV time column", None))
        self.lineEdit_time_col.setText(QCoreApplication.translate("Dialog_var_spat_interpol", u"time", None))
        self.label_lat_col.setText(QCoreApplication.translate("Dialog_var_spat_interpol", u"CSV latitude column", None))
        self.lineEdit_lat_col.setText(QCoreApplication.translate("Dialog_var_spat_interpol", u"lat", None))
        self.label_lon_col.setText(QCoreApplication.translate("Dialog_var_spat_interpol", u"CSV longitude column", None))
        self.lineEdit_lon_col.setText(QCoreApplication.translate("Dialog_var_spat_interpol", u"lon", None))
        self.checkBox_variable_input.setText(QCoreApplication.translate("Dialog_var_spat_interpol", u"Propagate the same value for a variable in all time steps", None))
        self.groupBox.setTitle("")
        self.label_var_name_same_val.setText(QCoreApplication.translate("Dialog_var_spat_interpol", u"Variable name", None))
        self.label.setText(QCoreApplication.translate("Dialog_var_spat_interpol", u"Value", None))
        self.lineEdit_same_val.setText("")
        self.checkBox_nc.setText(QCoreApplication.translate("Dialog_var_spat_interpol", u"Introduce data from a NETCDF dataset", None))
        self.groupBox_2.setTitle("")
        self.label_nc.setText(QCoreApplication.translate("Dialog_var_spat_interpol", u"File path (.nc)", None))
        self.toolButton_browse_nc.setText(QCoreApplication.translate("Dialog_var_spat_interpol", u"...", None))
        self.toolButton_refresh_nc.setText(QCoreApplication.translate("Dialog_var_spat_interpol", u"refresh", None))
        self.label_var_name_nc.setText(QCoreApplication.translate("Dialog_var_spat_interpol", u"Variable name", None))
        self.label_9.setText(QCoreApplication.translate("Dialog_var_spat_interpol", u"NETCDF Dataset dimension size:", None))
        self.label_6.setText(QCoreApplication.translate("Dialog_var_spat_interpol", u"Long.:", None))
        self.label_longx_new.setText("")
        self.label_7.setText(QCoreApplication.translate("Dialog_var_spat_interpol", u"Lat.:", None))
        self.label_laty_new.setText("")
        self.label_8.setText(QCoreApplication.translate("Dialog_var_spat_interpol", u"Time.:", None))
        self.label_time_new.setText("")
        self.textBrowser_help.setHtml(QCoreApplication.translate("Dialog_var_spat_interpol", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.1pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
    # retranslateUi

