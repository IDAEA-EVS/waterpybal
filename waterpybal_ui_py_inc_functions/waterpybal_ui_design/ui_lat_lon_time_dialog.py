# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'lat_lon_time_dialog.ui'
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
    QDialog, QDialogButtonBox, QFrame, QGroupBox,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QSizePolicy, QSpacerItem, QSplitter, QTableWidget,
    QTableWidgetItem, QTextBrowser, QToolButton, QVBoxLayout,
    QWidget)

class Ui_Dialog_lat_lon_time(object):
    def setupUi(self, Dialog_lat_lon_time):
        if not Dialog_lat_lon_time.objectName():
            Dialog_lat_lon_time.setObjectName(u"Dialog_lat_lon_time")
        Dialog_lat_lon_time.resize(1150, 550)
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog_lat_lon_time.sizePolicy().hasHeightForWidth())
        Dialog_lat_lon_time.setSizePolicy(sizePolicy)
        Dialog_lat_lon_time.setMinimumSize(QSize(1150, 550))
        Dialog_lat_lon_time.setMaximumSize(QSize(10000, 10000))
        self.horizontalLayout_6 = QHBoxLayout(Dialog_lat_lon_time)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.groupBox_spatialtemporal = QGroupBox(Dialog_lat_lon_time)
        self.groupBox_spatialtemporal.setObjectName(u"groupBox_spatialtemporal")
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.groupBox_spatialtemporal.sizePolicy().hasHeightForWidth())
        self.groupBox_spatialtemporal.setSizePolicy(sizePolicy1)
        self.groupBox_spatialtemporal.setMaximumSize(QSize(550, 16777215))
        font = QFont()
        font.setPointSize(12)
        self.groupBox_spatialtemporal.setFont(font)
        self.verticalLayout_7 = QVBoxLayout(self.groupBox_spatialtemporal)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_xy_raster = QLabel(self.groupBox_spatialtemporal)
        self.label_xy_raster.setObjectName(u"label_xy_raster")
        font1 = QFont()
        font1.setPointSize(10)
        self.label_xy_raster.setFont(font1)

        self.horizontalLayout_2.addWidget(self.label_xy_raster)

        self.lineEdit_xyraster = QLineEdit(self.groupBox_spatialtemporal)
        self.lineEdit_xyraster.setObjectName(u"lineEdit_xyraster")
        sizePolicy2 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.lineEdit_xyraster.sizePolicy().hasHeightForWidth())
        self.lineEdit_xyraster.setSizePolicy(sizePolicy2)
        self.lineEdit_xyraster.setMinimumSize(QSize(160, 20))
        font2 = QFont()
        font2.setPointSize(8)
        self.lineEdit_xyraster.setFont(font2)

        self.horizontalLayout_2.addWidget(self.lineEdit_xyraster)

        self.toolButton_browse_xy_raster = QToolButton(self.groupBox_spatialtemporal)
        self.toolButton_browse_xy_raster.setObjectName(u"toolButton_browse_xy_raster")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.toolButton_browse_xy_raster.sizePolicy().hasHeightForWidth())
        self.toolButton_browse_xy_raster.setSizePolicy(sizePolicy3)
        self.toolButton_browse_xy_raster.setMaximumSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.toolButton_browse_xy_raster)


        self.verticalLayout_7.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.checkBox_single_point = QCheckBox(self.groupBox_spatialtemporal)
        self.checkBox_single_point.setObjectName(u"checkBox_single_point")
        self.checkBox_single_point.setFont(font1)

        self.horizontalLayout_5.addWidget(self.checkBox_single_point)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_2)

        self.checkBox_urban = QCheckBox(self.groupBox_spatialtemporal)
        self.checkBox_urban.setObjectName(u"checkBox_urban")
        self.checkBox_urban.setFont(font1)

        self.horizontalLayout_5.addWidget(self.checkBox_urban)


        self.verticalLayout_7.addLayout(self.horizontalLayout_5)

        self.verticalSpacer_2 = QSpacerItem(471, 0, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.verticalLayout_7.addItem(self.verticalSpacer_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_8)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_4)

        self.label_time_interval = QLabel(self.groupBox_spatialtemporal)
        self.label_time_interval.setObjectName(u"label_time_interval")
        self.label_time_interval.setFont(font1)

        self.horizontalLayout_3.addWidget(self.label_time_interval)

        self.comboBox_time_interval = QComboBox(self.groupBox_spatialtemporal)
        self.comboBox_time_interval.addItem("")
        self.comboBox_time_interval.addItem("")
        self.comboBox_time_interval.addItem("")
        self.comboBox_time_interval.setObjectName(u"comboBox_time_interval")
        self.comboBox_time_interval.setMinimumSize(QSize(60, 20))
        self.comboBox_time_interval.setFont(font1)

        self.horizontalLayout_3.addWidget(self.comboBox_time_interval)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_10)


        self.verticalLayout_6.addLayout(self.horizontalLayout_3)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.verticalLayout_6.addItem(self.verticalSpacer)

        self.splitter = QSplitter(self.groupBox_spatialtemporal)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Vertical)
        self.layoutWidget_4 = QWidget(self.splitter)
        self.layoutWidget_4.setObjectName(u"layoutWidget_4")
        self.horizontalLayout_7 = QHBoxLayout(self.layoutWidget_4)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.verticalLayout_5.addItem(self.horizontalSpacer_11)

        self.label_start_time = QLabel(self.layoutWidget_4)
        self.label_start_time.setObjectName(u"label_start_time")
        self.label_start_time.setMinimumSize(QSize(35, 20))
        self.label_start_time.setFont(font1)

        self.verticalLayout_5.addWidget(self.label_start_time)

        self.label_end_time = QLabel(self.layoutWidget_4)
        self.label_end_time.setObjectName(u"label_end_time")
        self.label_end_time.setMinimumSize(QSize(35, 20))
        self.label_end_time.setFont(font1)

        self.verticalLayout_5.addWidget(self.label_end_time)


        self.horizontalLayout_7.addLayout(self.verticalLayout_5)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_hour = QLabel(self.layoutWidget_4)
        self.label_hour.setObjectName(u"label_hour")
        self.label_hour.setMinimumSize(QSize(50, 20))
        self.label_hour.setMaximumSize(QSize(40, 20))
        self.label_hour.setFont(font1)

        self.verticalLayout.addWidget(self.label_hour)

        self.comboBox_start_hour = QComboBox(self.layoutWidget_4)
        self.comboBox_start_hour.addItem("")
        self.comboBox_start_hour.addItem("")
        self.comboBox_start_hour.addItem("")
        self.comboBox_start_hour.addItem("")
        self.comboBox_start_hour.addItem("")
        self.comboBox_start_hour.addItem("")
        self.comboBox_start_hour.addItem("")
        self.comboBox_start_hour.addItem("")
        self.comboBox_start_hour.addItem("")
        self.comboBox_start_hour.addItem("")
        self.comboBox_start_hour.addItem("")
        self.comboBox_start_hour.addItem("")
        self.comboBox_start_hour.addItem("")
        self.comboBox_start_hour.addItem("")
        self.comboBox_start_hour.addItem("")
        self.comboBox_start_hour.addItem("")
        self.comboBox_start_hour.addItem("")
        self.comboBox_start_hour.addItem("")
        self.comboBox_start_hour.addItem("")
        self.comboBox_start_hour.addItem("")
        self.comboBox_start_hour.addItem("")
        self.comboBox_start_hour.addItem("")
        self.comboBox_start_hour.addItem("")
        self.comboBox_start_hour.addItem("")
        self.comboBox_start_hour.setObjectName(u"comboBox_start_hour")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.comboBox_start_hour.sizePolicy().hasHeightForWidth())
        self.comboBox_start_hour.setSizePolicy(sizePolicy4)
        self.comboBox_start_hour.setMinimumSize(QSize(50, 20))
        self.comboBox_start_hour.setFont(font2)

        self.verticalLayout.addWidget(self.comboBox_start_hour)

        self.comboBox_end_hour = QComboBox(self.layoutWidget_4)
        self.comboBox_end_hour.addItem("")
        self.comboBox_end_hour.addItem("")
        self.comboBox_end_hour.addItem("")
        self.comboBox_end_hour.addItem("")
        self.comboBox_end_hour.addItem("")
        self.comboBox_end_hour.addItem("")
        self.comboBox_end_hour.addItem("")
        self.comboBox_end_hour.addItem("")
        self.comboBox_end_hour.addItem("")
        self.comboBox_end_hour.addItem("")
        self.comboBox_end_hour.addItem("")
        self.comboBox_end_hour.addItem("")
        self.comboBox_end_hour.addItem("")
        self.comboBox_end_hour.addItem("")
        self.comboBox_end_hour.addItem("")
        self.comboBox_end_hour.addItem("")
        self.comboBox_end_hour.addItem("")
        self.comboBox_end_hour.addItem("")
        self.comboBox_end_hour.addItem("")
        self.comboBox_end_hour.addItem("")
        self.comboBox_end_hour.addItem("")
        self.comboBox_end_hour.addItem("")
        self.comboBox_end_hour.addItem("")
        self.comboBox_end_hour.addItem("")
        self.comboBox_end_hour.setObjectName(u"comboBox_end_hour")
        sizePolicy4.setHeightForWidth(self.comboBox_end_hour.sizePolicy().hasHeightForWidth())
        self.comboBox_end_hour.setSizePolicy(sizePolicy4)
        self.comboBox_end_hour.setMinimumSize(QSize(50, 20))
        self.comboBox_end_hour.setFont(font2)

        self.verticalLayout.addWidget(self.comboBox_end_hour)


        self.horizontalLayout_7.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_day = QLabel(self.layoutWidget_4)
        self.label_day.setObjectName(u"label_day")
        self.label_day.setMinimumSize(QSize(50, 20))
        self.label_day.setMaximumSize(QSize(40, 20))
        self.label_day.setFont(font1)

        self.verticalLayout_2.addWidget(self.label_day)

        self.comboBox_start_day = QComboBox(self.layoutWidget_4)
        self.comboBox_start_day.addItem("")
        self.comboBox_start_day.addItem("")
        self.comboBox_start_day.addItem("")
        self.comboBox_start_day.addItem("")
        self.comboBox_start_day.addItem("")
        self.comboBox_start_day.addItem("")
        self.comboBox_start_day.addItem("")
        self.comboBox_start_day.addItem("")
        self.comboBox_start_day.addItem("")
        self.comboBox_start_day.addItem("")
        self.comboBox_start_day.addItem("")
        self.comboBox_start_day.addItem("")
        self.comboBox_start_day.addItem("")
        self.comboBox_start_day.addItem("")
        self.comboBox_start_day.addItem("")
        self.comboBox_start_day.addItem("")
        self.comboBox_start_day.addItem("")
        self.comboBox_start_day.addItem("")
        self.comboBox_start_day.addItem("")
        self.comboBox_start_day.addItem("")
        self.comboBox_start_day.addItem("")
        self.comboBox_start_day.addItem("")
        self.comboBox_start_day.addItem("")
        self.comboBox_start_day.addItem("")
        self.comboBox_start_day.addItem("")
        self.comboBox_start_day.addItem("")
        self.comboBox_start_day.addItem("")
        self.comboBox_start_day.addItem("")
        self.comboBox_start_day.addItem("")
        self.comboBox_start_day.addItem("")
        self.comboBox_start_day.setObjectName(u"comboBox_start_day")
        sizePolicy4.setHeightForWidth(self.comboBox_start_day.sizePolicy().hasHeightForWidth())
        self.comboBox_start_day.setSizePolicy(sizePolicy4)
        self.comboBox_start_day.setMinimumSize(QSize(50, 20))
        self.comboBox_start_day.setFont(font2)

        self.verticalLayout_2.addWidget(self.comboBox_start_day)

        self.comboBox_end_day = QComboBox(self.layoutWidget_4)
        self.comboBox_end_day.addItem("")
        self.comboBox_end_day.addItem("")
        self.comboBox_end_day.addItem("")
        self.comboBox_end_day.addItem("")
        self.comboBox_end_day.addItem("")
        self.comboBox_end_day.addItem("")
        self.comboBox_end_day.addItem("")
        self.comboBox_end_day.addItem("")
        self.comboBox_end_day.addItem("")
        self.comboBox_end_day.addItem("")
        self.comboBox_end_day.addItem("")
        self.comboBox_end_day.addItem("")
        self.comboBox_end_day.addItem("")
        self.comboBox_end_day.addItem("")
        self.comboBox_end_day.addItem("")
        self.comboBox_end_day.addItem("")
        self.comboBox_end_day.addItem("")
        self.comboBox_end_day.addItem("")
        self.comboBox_end_day.addItem("")
        self.comboBox_end_day.addItem("")
        self.comboBox_end_day.addItem("")
        self.comboBox_end_day.addItem("")
        self.comboBox_end_day.addItem("")
        self.comboBox_end_day.addItem("")
        self.comboBox_end_day.addItem("")
        self.comboBox_end_day.addItem("")
        self.comboBox_end_day.addItem("")
        self.comboBox_end_day.addItem("")
        self.comboBox_end_day.addItem("")
        self.comboBox_end_day.addItem("")
        self.comboBox_end_day.setObjectName(u"comboBox_end_day")
        sizePolicy4.setHeightForWidth(self.comboBox_end_day.sizePolicy().hasHeightForWidth())
        self.comboBox_end_day.setSizePolicy(sizePolicy4)
        self.comboBox_end_day.setMinimumSize(QSize(50, 20))
        self.comboBox_end_day.setFont(font2)

        self.verticalLayout_2.addWidget(self.comboBox_end_day)


        self.horizontalLayout_7.addLayout(self.verticalLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_month = QLabel(self.layoutWidget_4)
        self.label_month.setObjectName(u"label_month")
        self.label_month.setMinimumSize(QSize(50, 20))
        self.label_month.setMaximumSize(QSize(50, 20))
        self.label_month.setFont(font1)

        self.verticalLayout_3.addWidget(self.label_month)

        self.comboBox_start_month = QComboBox(self.layoutWidget_4)
        self.comboBox_start_month.addItem("")
        self.comboBox_start_month.addItem("")
        self.comboBox_start_month.addItem("")
        self.comboBox_start_month.addItem("")
        self.comboBox_start_month.addItem("")
        self.comboBox_start_month.addItem("")
        self.comboBox_start_month.addItem("")
        self.comboBox_start_month.addItem("")
        self.comboBox_start_month.addItem("")
        self.comboBox_start_month.addItem("")
        self.comboBox_start_month.addItem("")
        self.comboBox_start_month.addItem("")
        self.comboBox_start_month.setObjectName(u"comboBox_start_month")
        sizePolicy4.setHeightForWidth(self.comboBox_start_month.sizePolicy().hasHeightForWidth())
        self.comboBox_start_month.setSizePolicy(sizePolicy4)
        self.comboBox_start_month.setMinimumSize(QSize(50, 20))
        self.comboBox_start_month.setFont(font2)

        self.verticalLayout_3.addWidget(self.comboBox_start_month)

        self.comboBox_end_month = QComboBox(self.layoutWidget_4)
        self.comboBox_end_month.addItem("")
        self.comboBox_end_month.addItem("")
        self.comboBox_end_month.addItem("")
        self.comboBox_end_month.addItem("")
        self.comboBox_end_month.addItem("")
        self.comboBox_end_month.addItem("")
        self.comboBox_end_month.addItem("")
        self.comboBox_end_month.addItem("")
        self.comboBox_end_month.addItem("")
        self.comboBox_end_month.addItem("")
        self.comboBox_end_month.addItem("")
        self.comboBox_end_month.addItem("")
        self.comboBox_end_month.setObjectName(u"comboBox_end_month")
        sizePolicy4.setHeightForWidth(self.comboBox_end_month.sizePolicy().hasHeightForWidth())
        self.comboBox_end_month.setSizePolicy(sizePolicy4)
        self.comboBox_end_month.setMinimumSize(QSize(50, 20))
        self.comboBox_end_month.setFont(font2)

        self.verticalLayout_3.addWidget(self.comboBox_end_month)


        self.horizontalLayout_7.addLayout(self.verticalLayout_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_year = QLabel(self.layoutWidget_4)
        self.label_year.setObjectName(u"label_year")
        self.label_year.setMinimumSize(QSize(50, 20))
        self.label_year.setMaximumSize(QSize(40, 20))
        self.label_year.setFont(font1)

        self.verticalLayout_4.addWidget(self.label_year)

        self.lineEdit_start_year = QLineEdit(self.layoutWidget_4)
        self.lineEdit_start_year.setObjectName(u"lineEdit_start_year")
        self.lineEdit_start_year.setMinimumSize(QSize(50, 20))
        self.lineEdit_start_year.setMaximumSize(QSize(40, 20))
        self.lineEdit_start_year.setFont(font2)

        self.verticalLayout_4.addWidget(self.lineEdit_start_year)

        self.lineEdit_end_year = QLineEdit(self.layoutWidget_4)
        self.lineEdit_end_year.setObjectName(u"lineEdit_end_year")
        self.lineEdit_end_year.setMinimumSize(QSize(50, 20))
        self.lineEdit_end_year.setMaximumSize(QSize(40, 20))
        self.lineEdit_end_year.setFont(font2)

        self.verticalLayout_4.addWidget(self.lineEdit_end_year)


        self.horizontalLayout_7.addLayout(self.verticalLayout_4)

        self.splitter.addWidget(self.layoutWidget_4)

        self.verticalLayout_6.addWidget(self.splitter)


        self.horizontalLayout_4.addLayout(self.verticalLayout_6)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_12)


        self.verticalLayout_7.addLayout(self.horizontalLayout_4)


        self.verticalLayout_8.addWidget(self.groupBox_spatialtemporal)

        self.verticalSpacer_3 = QSpacerItem(20, 1, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_3)

        self.groupBox_additional_vars = QGroupBox(Dialog_lat_lon_time)
        self.groupBox_additional_vars.setObjectName(u"groupBox_additional_vars")
        sizePolicy1.setHeightForWidth(self.groupBox_additional_vars.sizePolicy().hasHeightForWidth())
        self.groupBox_additional_vars.setSizePolicy(sizePolicy1)
        self.groupBox_additional_vars.setMinimumSize(QSize(275, 235))
        self.groupBox_additional_vars.setMaximumSize(QSize(550, 16777215))
        self.groupBox_additional_vars.setFont(font)
        self.horizontalLayout = QHBoxLayout(self.groupBox_additional_vars)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_7 = QSpacerItem(60, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_7)

        self.tableWidget_additional_vars_3 = QTableWidget(self.groupBox_additional_vars)
        if (self.tableWidget_additional_vars_3.columnCount() < 2):
            self.tableWidget_additional_vars_3.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget_additional_vars_3.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget_additional_vars_3.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.tableWidget_additional_vars_3.setObjectName(u"tableWidget_additional_vars_3")

        self.horizontalLayout.addWidget(self.tableWidget_additional_vars_3)

        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_15.addItem(self.verticalSpacer_7)

        self.toolButton_new_3 = QToolButton(self.groupBox_additional_vars)
        self.toolButton_new_3.setObjectName(u"toolButton_new_3")
        self.toolButton_new_3.setMinimumSize(QSize(70, 25))
        self.toolButton_new_3.setFont(font1)
        self.toolButton_new_3.setArrowType(Qt.NoArrow)

        self.verticalLayout_15.addWidget(self.toolButton_new_3)

        self.toolButton_remove_3 = QToolButton(self.groupBox_additional_vars)
        self.toolButton_remove_3.setObjectName(u"toolButton_remove_3")
        self.toolButton_remove_3.setMinimumSize(QSize(70, 25))
        self.toolButton_remove_3.setFont(font1)

        self.verticalLayout_15.addWidget(self.toolButton_remove_3)


        self.verticalLayout_14.addLayout(self.verticalLayout_15)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_14.addItem(self.verticalSpacer_8)


        self.horizontalLayout.addLayout(self.verticalLayout_14)

        self.horizontalSpacer_3 = QSpacerItem(60, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)


        self.verticalLayout_8.addWidget(self.groupBox_additional_vars)

        self.buttonBox = QDialogButtonBox(Dialog_lat_lon_time)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setMaximumSize(QSize(480, 16777215))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout_8.addWidget(self.buttonBox)


        self.horizontalLayout_6.addLayout(self.verticalLayout_8)

        self.groupBox_help = QGroupBox(Dialog_lat_lon_time)
        self.groupBox_help.setObjectName(u"groupBox_help")
        sizePolicy.setHeightForWidth(self.groupBox_help.sizePolicy().hasHeightForWidth())
        self.groupBox_help.setSizePolicy(sizePolicy)
        self.groupBox_help.setMinimumSize(QSize(650, 500))
        self.groupBox_help.setMaximumSize(QSize(16777215, 16777215))
        font3 = QFont()
        font3.setPointSize(9)
        self.groupBox_help.setFont(font3)
        self.groupBox_help.setAutoFillBackground(False)
        self.groupBox_help.setStyleSheet(u"QGroupBox{border:2px solid gray;border-radius:1px;margin-top: 1ex;}\n"
"QGroupBox::title{subcontrol-origin: margin;subcontrol-position:top center;padding:0 3px;}")
        self.groupBox_help.setTitle(u"Help")
        self.groupBox_help.setFlat(False)
        self.verticalLayout_9 = QVBoxLayout(self.groupBox_help)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.textBrowser_help = QTextBrowser(self.groupBox_help)
        self.textBrowser_help.setObjectName(u"textBrowser_help")
        self.textBrowser_help.setAutoFillBackground(True)
        self.textBrowser_help.setStyleSheet(u"background-color: rgb(240, 240, 240)")
        self.textBrowser_help.setFrameShape(QFrame.WinPanel)
        self.textBrowser_help.setFrameShadow(QFrame.Sunken)
        self.textBrowser_help.setLineWidth(0)
        self.textBrowser_help.setReadOnly(True)

        self.verticalLayout_9.addWidget(self.textBrowser_help)


        self.horizontalLayout_6.addWidget(self.groupBox_help)


        self.retranslateUi(Dialog_lat_lon_time)
        self.buttonBox.accepted.connect(Dialog_lat_lon_time.accept)
        self.buttonBox.rejected.connect(Dialog_lat_lon_time.reject)

        QMetaObject.connectSlotsByName(Dialog_lat_lon_time)
    # setupUi

    def retranslateUi(self, Dialog_lat_lon_time):
        Dialog_lat_lon_time.setWindowTitle(QCoreApplication.translate("Dialog_lat_lon_time", u"Spatial -Temporal properties", None))
        self.groupBox_spatialtemporal.setTitle(QCoreApplication.translate("Dialog_lat_lon_time", u"Spatial -Temporal properties", None))
        self.label_xy_raster.setText(QCoreApplication.translate("Dialog_lat_lon_time", u"Raster to determine Spatial properties (X and Y) :", None))
        self.toolButton_browse_xy_raster.setText(QCoreApplication.translate("Dialog_lat_lon_time", u"...", None))
        self.checkBox_single_point.setText(QCoreApplication.translate("Dialog_lat_lon_time", u"Single Point", None))
        self.checkBox_urban.setText(QCoreApplication.translate("Dialog_lat_lon_time", u"Include Urban zone variables in the dataset", None))
        self.label_time_interval.setText(QCoreApplication.translate("Dialog_lat_lon_time", u"Time interval: ", None))
        self.comboBox_time_interval.setItemText(0, QCoreApplication.translate("Dialog_lat_lon_time", u"Daily", None))
        self.comboBox_time_interval.setItemText(1, QCoreApplication.translate("Dialog_lat_lon_time", u"Monthly", None))
        self.comboBox_time_interval.setItemText(2, QCoreApplication.translate("Dialog_lat_lon_time", u"Hourly", None))

        self.label_start_time.setText(QCoreApplication.translate("Dialog_lat_lon_time", u"Start", None))
        self.label_end_time.setText(QCoreApplication.translate("Dialog_lat_lon_time", u"End", None))
        self.label_hour.setText(QCoreApplication.translate("Dialog_lat_lon_time", u"Hour", None))
        self.comboBox_start_hour.setItemText(0, QCoreApplication.translate("Dialog_lat_lon_time", u"00", None))
        self.comboBox_start_hour.setItemText(1, QCoreApplication.translate("Dialog_lat_lon_time", u"01", None))
        self.comboBox_start_hour.setItemText(2, QCoreApplication.translate("Dialog_lat_lon_time", u"02", None))
        self.comboBox_start_hour.setItemText(3, QCoreApplication.translate("Dialog_lat_lon_time", u"03", None))
        self.comboBox_start_hour.setItemText(4, QCoreApplication.translate("Dialog_lat_lon_time", u"04", None))
        self.comboBox_start_hour.setItemText(5, QCoreApplication.translate("Dialog_lat_lon_time", u"05", None))
        self.comboBox_start_hour.setItemText(6, QCoreApplication.translate("Dialog_lat_lon_time", u"06", None))
        self.comboBox_start_hour.setItemText(7, QCoreApplication.translate("Dialog_lat_lon_time", u"07", None))
        self.comboBox_start_hour.setItemText(8, QCoreApplication.translate("Dialog_lat_lon_time", u"08", None))
        self.comboBox_start_hour.setItemText(9, QCoreApplication.translate("Dialog_lat_lon_time", u"09", None))
        self.comboBox_start_hour.setItemText(10, QCoreApplication.translate("Dialog_lat_lon_time", u"10", None))
        self.comboBox_start_hour.setItemText(11, QCoreApplication.translate("Dialog_lat_lon_time", u"11", None))
        self.comboBox_start_hour.setItemText(12, QCoreApplication.translate("Dialog_lat_lon_time", u"12", None))
        self.comboBox_start_hour.setItemText(13, QCoreApplication.translate("Dialog_lat_lon_time", u"13", None))
        self.comboBox_start_hour.setItemText(14, QCoreApplication.translate("Dialog_lat_lon_time", u"14", None))
        self.comboBox_start_hour.setItemText(15, QCoreApplication.translate("Dialog_lat_lon_time", u"15", None))
        self.comboBox_start_hour.setItemText(16, QCoreApplication.translate("Dialog_lat_lon_time", u"16", None))
        self.comboBox_start_hour.setItemText(17, QCoreApplication.translate("Dialog_lat_lon_time", u"17", None))
        self.comboBox_start_hour.setItemText(18, QCoreApplication.translate("Dialog_lat_lon_time", u"18", None))
        self.comboBox_start_hour.setItemText(19, QCoreApplication.translate("Dialog_lat_lon_time", u"19", None))
        self.comboBox_start_hour.setItemText(20, QCoreApplication.translate("Dialog_lat_lon_time", u"20", None))
        self.comboBox_start_hour.setItemText(21, QCoreApplication.translate("Dialog_lat_lon_time", u"21", None))
        self.comboBox_start_hour.setItemText(22, QCoreApplication.translate("Dialog_lat_lon_time", u"22", None))
        self.comboBox_start_hour.setItemText(23, QCoreApplication.translate("Dialog_lat_lon_time", u"23", None))

        self.comboBox_end_hour.setItemText(0, QCoreApplication.translate("Dialog_lat_lon_time", u"00", None))
        self.comboBox_end_hour.setItemText(1, QCoreApplication.translate("Dialog_lat_lon_time", u"01", None))
        self.comboBox_end_hour.setItemText(2, QCoreApplication.translate("Dialog_lat_lon_time", u"02", None))
        self.comboBox_end_hour.setItemText(3, QCoreApplication.translate("Dialog_lat_lon_time", u"03", None))
        self.comboBox_end_hour.setItemText(4, QCoreApplication.translate("Dialog_lat_lon_time", u"04", None))
        self.comboBox_end_hour.setItemText(5, QCoreApplication.translate("Dialog_lat_lon_time", u"05", None))
        self.comboBox_end_hour.setItemText(6, QCoreApplication.translate("Dialog_lat_lon_time", u"06", None))
        self.comboBox_end_hour.setItemText(7, QCoreApplication.translate("Dialog_lat_lon_time", u"07", None))
        self.comboBox_end_hour.setItemText(8, QCoreApplication.translate("Dialog_lat_lon_time", u"08", None))
        self.comboBox_end_hour.setItemText(9, QCoreApplication.translate("Dialog_lat_lon_time", u"09", None))
        self.comboBox_end_hour.setItemText(10, QCoreApplication.translate("Dialog_lat_lon_time", u"10", None))
        self.comboBox_end_hour.setItemText(11, QCoreApplication.translate("Dialog_lat_lon_time", u"11", None))
        self.comboBox_end_hour.setItemText(12, QCoreApplication.translate("Dialog_lat_lon_time", u"12", None))
        self.comboBox_end_hour.setItemText(13, QCoreApplication.translate("Dialog_lat_lon_time", u"13", None))
        self.comboBox_end_hour.setItemText(14, QCoreApplication.translate("Dialog_lat_lon_time", u"14", None))
        self.comboBox_end_hour.setItemText(15, QCoreApplication.translate("Dialog_lat_lon_time", u"15", None))
        self.comboBox_end_hour.setItemText(16, QCoreApplication.translate("Dialog_lat_lon_time", u"16", None))
        self.comboBox_end_hour.setItemText(17, QCoreApplication.translate("Dialog_lat_lon_time", u"17", None))
        self.comboBox_end_hour.setItemText(18, QCoreApplication.translate("Dialog_lat_lon_time", u"18", None))
        self.comboBox_end_hour.setItemText(19, QCoreApplication.translate("Dialog_lat_lon_time", u"19", None))
        self.comboBox_end_hour.setItemText(20, QCoreApplication.translate("Dialog_lat_lon_time", u"20", None))
        self.comboBox_end_hour.setItemText(21, QCoreApplication.translate("Dialog_lat_lon_time", u"21", None))
        self.comboBox_end_hour.setItemText(22, QCoreApplication.translate("Dialog_lat_lon_time", u"22", None))
        self.comboBox_end_hour.setItemText(23, QCoreApplication.translate("Dialog_lat_lon_time", u"23", None))

        self.label_day.setText(QCoreApplication.translate("Dialog_lat_lon_time", u"Day", None))
        self.comboBox_start_day.setItemText(0, QCoreApplication.translate("Dialog_lat_lon_time", u"01", None))
        self.comboBox_start_day.setItemText(1, QCoreApplication.translate("Dialog_lat_lon_time", u"02", None))
        self.comboBox_start_day.setItemText(2, QCoreApplication.translate("Dialog_lat_lon_time", u"03", None))
        self.comboBox_start_day.setItemText(3, QCoreApplication.translate("Dialog_lat_lon_time", u"04", None))
        self.comboBox_start_day.setItemText(4, QCoreApplication.translate("Dialog_lat_lon_time", u"05", None))
        self.comboBox_start_day.setItemText(5, QCoreApplication.translate("Dialog_lat_lon_time", u"06", None))
        self.comboBox_start_day.setItemText(6, QCoreApplication.translate("Dialog_lat_lon_time", u"07", None))
        self.comboBox_start_day.setItemText(7, QCoreApplication.translate("Dialog_lat_lon_time", u"08", None))
        self.comboBox_start_day.setItemText(8, QCoreApplication.translate("Dialog_lat_lon_time", u"09", None))
        self.comboBox_start_day.setItemText(9, QCoreApplication.translate("Dialog_lat_lon_time", u"10", None))
        self.comboBox_start_day.setItemText(10, QCoreApplication.translate("Dialog_lat_lon_time", u"11", None))
        self.comboBox_start_day.setItemText(11, QCoreApplication.translate("Dialog_lat_lon_time", u"12", None))
        self.comboBox_start_day.setItemText(12, QCoreApplication.translate("Dialog_lat_lon_time", u"13", None))
        self.comboBox_start_day.setItemText(13, QCoreApplication.translate("Dialog_lat_lon_time", u"14", None))
        self.comboBox_start_day.setItemText(14, QCoreApplication.translate("Dialog_lat_lon_time", u"15", None))
        self.comboBox_start_day.setItemText(15, QCoreApplication.translate("Dialog_lat_lon_time", u"16", None))
        self.comboBox_start_day.setItemText(16, QCoreApplication.translate("Dialog_lat_lon_time", u"17", None))
        self.comboBox_start_day.setItemText(17, QCoreApplication.translate("Dialog_lat_lon_time", u"18", None))
        self.comboBox_start_day.setItemText(18, QCoreApplication.translate("Dialog_lat_lon_time", u"19", None))
        self.comboBox_start_day.setItemText(19, QCoreApplication.translate("Dialog_lat_lon_time", u"20", None))
        self.comboBox_start_day.setItemText(20, QCoreApplication.translate("Dialog_lat_lon_time", u"21", None))
        self.comboBox_start_day.setItemText(21, QCoreApplication.translate("Dialog_lat_lon_time", u"22", None))
        self.comboBox_start_day.setItemText(22, QCoreApplication.translate("Dialog_lat_lon_time", u"23", None))
        self.comboBox_start_day.setItemText(23, QCoreApplication.translate("Dialog_lat_lon_time", u"24", None))
        self.comboBox_start_day.setItemText(24, QCoreApplication.translate("Dialog_lat_lon_time", u"25", None))
        self.comboBox_start_day.setItemText(25, QCoreApplication.translate("Dialog_lat_lon_time", u"26", None))
        self.comboBox_start_day.setItemText(26, QCoreApplication.translate("Dialog_lat_lon_time", u"27", None))
        self.comboBox_start_day.setItemText(27, QCoreApplication.translate("Dialog_lat_lon_time", u"28", None))
        self.comboBox_start_day.setItemText(28, QCoreApplication.translate("Dialog_lat_lon_time", u"29", None))
        self.comboBox_start_day.setItemText(29, QCoreApplication.translate("Dialog_lat_lon_time", u"30", None))

        self.comboBox_end_day.setItemText(0, QCoreApplication.translate("Dialog_lat_lon_time", u"01", None))
        self.comboBox_end_day.setItemText(1, QCoreApplication.translate("Dialog_lat_lon_time", u"02", None))
        self.comboBox_end_day.setItemText(2, QCoreApplication.translate("Dialog_lat_lon_time", u"03", None))
        self.comboBox_end_day.setItemText(3, QCoreApplication.translate("Dialog_lat_lon_time", u"04", None))
        self.comboBox_end_day.setItemText(4, QCoreApplication.translate("Dialog_lat_lon_time", u"05", None))
        self.comboBox_end_day.setItemText(5, QCoreApplication.translate("Dialog_lat_lon_time", u"06", None))
        self.comboBox_end_day.setItemText(6, QCoreApplication.translate("Dialog_lat_lon_time", u"07", None))
        self.comboBox_end_day.setItemText(7, QCoreApplication.translate("Dialog_lat_lon_time", u"08", None))
        self.comboBox_end_day.setItemText(8, QCoreApplication.translate("Dialog_lat_lon_time", u"09", None))
        self.comboBox_end_day.setItemText(9, QCoreApplication.translate("Dialog_lat_lon_time", u"10", None))
        self.comboBox_end_day.setItemText(10, QCoreApplication.translate("Dialog_lat_lon_time", u"11", None))
        self.comboBox_end_day.setItemText(11, QCoreApplication.translate("Dialog_lat_lon_time", u"12", None))
        self.comboBox_end_day.setItemText(12, QCoreApplication.translate("Dialog_lat_lon_time", u"13", None))
        self.comboBox_end_day.setItemText(13, QCoreApplication.translate("Dialog_lat_lon_time", u"14", None))
        self.comboBox_end_day.setItemText(14, QCoreApplication.translate("Dialog_lat_lon_time", u"15", None))
        self.comboBox_end_day.setItemText(15, QCoreApplication.translate("Dialog_lat_lon_time", u"16", None))
        self.comboBox_end_day.setItemText(16, QCoreApplication.translate("Dialog_lat_lon_time", u"17", None))
        self.comboBox_end_day.setItemText(17, QCoreApplication.translate("Dialog_lat_lon_time", u"18", None))
        self.comboBox_end_day.setItemText(18, QCoreApplication.translate("Dialog_lat_lon_time", u"19", None))
        self.comboBox_end_day.setItemText(19, QCoreApplication.translate("Dialog_lat_lon_time", u"20", None))
        self.comboBox_end_day.setItemText(20, QCoreApplication.translate("Dialog_lat_lon_time", u"21", None))
        self.comboBox_end_day.setItemText(21, QCoreApplication.translate("Dialog_lat_lon_time", u"22", None))
        self.comboBox_end_day.setItemText(22, QCoreApplication.translate("Dialog_lat_lon_time", u"23", None))
        self.comboBox_end_day.setItemText(23, QCoreApplication.translate("Dialog_lat_lon_time", u"24", None))
        self.comboBox_end_day.setItemText(24, QCoreApplication.translate("Dialog_lat_lon_time", u"25", None))
        self.comboBox_end_day.setItemText(25, QCoreApplication.translate("Dialog_lat_lon_time", u"26", None))
        self.comboBox_end_day.setItemText(26, QCoreApplication.translate("Dialog_lat_lon_time", u"27", None))
        self.comboBox_end_day.setItemText(27, QCoreApplication.translate("Dialog_lat_lon_time", u"28", None))
        self.comboBox_end_day.setItemText(28, QCoreApplication.translate("Dialog_lat_lon_time", u"29", None))
        self.comboBox_end_day.setItemText(29, QCoreApplication.translate("Dialog_lat_lon_time", u"30", None))

        self.label_month.setText(QCoreApplication.translate("Dialog_lat_lon_time", u"Month", None))
        self.comboBox_start_month.setItemText(0, QCoreApplication.translate("Dialog_lat_lon_time", u"01", None))
        self.comboBox_start_month.setItemText(1, QCoreApplication.translate("Dialog_lat_lon_time", u"02", None))
        self.comboBox_start_month.setItemText(2, QCoreApplication.translate("Dialog_lat_lon_time", u"03", None))
        self.comboBox_start_month.setItemText(3, QCoreApplication.translate("Dialog_lat_lon_time", u"04", None))
        self.comboBox_start_month.setItemText(4, QCoreApplication.translate("Dialog_lat_lon_time", u"05", None))
        self.comboBox_start_month.setItemText(5, QCoreApplication.translate("Dialog_lat_lon_time", u"06", None))
        self.comboBox_start_month.setItemText(6, QCoreApplication.translate("Dialog_lat_lon_time", u"07", None))
        self.comboBox_start_month.setItemText(7, QCoreApplication.translate("Dialog_lat_lon_time", u"08", None))
        self.comboBox_start_month.setItemText(8, QCoreApplication.translate("Dialog_lat_lon_time", u"09", None))
        self.comboBox_start_month.setItemText(9, QCoreApplication.translate("Dialog_lat_lon_time", u"010", None))
        self.comboBox_start_month.setItemText(10, QCoreApplication.translate("Dialog_lat_lon_time", u"11", None))
        self.comboBox_start_month.setItemText(11, QCoreApplication.translate("Dialog_lat_lon_time", u"12", None))

        self.comboBox_end_month.setItemText(0, QCoreApplication.translate("Dialog_lat_lon_time", u"01", None))
        self.comboBox_end_month.setItemText(1, QCoreApplication.translate("Dialog_lat_lon_time", u"02", None))
        self.comboBox_end_month.setItemText(2, QCoreApplication.translate("Dialog_lat_lon_time", u"03", None))
        self.comboBox_end_month.setItemText(3, QCoreApplication.translate("Dialog_lat_lon_time", u"04", None))
        self.comboBox_end_month.setItemText(4, QCoreApplication.translate("Dialog_lat_lon_time", u"05", None))
        self.comboBox_end_month.setItemText(5, QCoreApplication.translate("Dialog_lat_lon_time", u"06", None))
        self.comboBox_end_month.setItemText(6, QCoreApplication.translate("Dialog_lat_lon_time", u"07", None))
        self.comboBox_end_month.setItemText(7, QCoreApplication.translate("Dialog_lat_lon_time", u"08", None))
        self.comboBox_end_month.setItemText(8, QCoreApplication.translate("Dialog_lat_lon_time", u"09", None))
        self.comboBox_end_month.setItemText(9, QCoreApplication.translate("Dialog_lat_lon_time", u"10", None))
        self.comboBox_end_month.setItemText(10, QCoreApplication.translate("Dialog_lat_lon_time", u"11", None))
        self.comboBox_end_month.setItemText(11, QCoreApplication.translate("Dialog_lat_lon_time", u"12", None))

        self.label_year.setText(QCoreApplication.translate("Dialog_lat_lon_time", u"Year", None))
        self.groupBox_additional_vars.setTitle(QCoreApplication.translate("Dialog_lat_lon_time", u"Additional Variables", None))
        ___qtablewidgetitem = self.tableWidget_additional_vars_3.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Dialog_lat_lon_time", u"Var. Name", None));
        ___qtablewidgetitem1 = self.tableWidget_additional_vars_3.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Dialog_lat_lon_time", u"Var. Unit", None));
        self.toolButton_new_3.setText(QCoreApplication.translate("Dialog_lat_lon_time", u"New", None))
        self.toolButton_remove_3.setText(QCoreApplication.translate("Dialog_lat_lon_time", u"Remove", None))
        self.textBrowser_help.setHtml(QCoreApplication.translate("Dialog_lat_lon_time", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.1pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
    # retranslateUi

