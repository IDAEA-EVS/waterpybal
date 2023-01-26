# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'visual.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDialog,
    QFrame, QGroupBox, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QTextBrowser, QToolButton, QVBoxLayout, QWidget)

class Ui_Dialog_visual(object):
    def setupUi(self, Dialog_visual):
        if not Dialog_visual.objectName():
            Dialog_visual.setObjectName(u"Dialog_visual")
        Dialog_visual.resize(950, 650)
        Dialog_visual.setMinimumSize(QSize(950, 650))
        Dialog_visual.setMaximumSize(QSize(1500, 1000))
        self.horizontalLayout_24 = QHBoxLayout(Dialog_visual)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_dataset_dir = QLabel(Dialog_visual)
        self.label_dataset_dir.setObjectName(u"label_dataset_dir")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_dataset_dir.sizePolicy().hasHeightForWidth())
        self.label_dataset_dir.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(10)
        self.label_dataset_dir.setFont(font)

        self.horizontalLayout_9.addWidget(self.label_dataset_dir)

        self.lineEdit_dataset_path = QLineEdit(Dialog_visual)
        self.lineEdit_dataset_path.setObjectName(u"lineEdit_dataset_path")
        font1 = QFont()
        font1.setPointSize(8)
        self.lineEdit_dataset_path.setFont(font1)

        self.horizontalLayout_9.addWidget(self.lineEdit_dataset_path)

        self.toolButton_path = QToolButton(Dialog_visual)
        self.toolButton_path.setObjectName(u"toolButton_path")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.toolButton_path.sizePolicy().hasHeightForWidth())
        self.toolButton_path.setSizePolicy(sizePolicy1)
        self.toolButton_path.setMaximumSize(QSize(20, 20))
        self.toolButton_path.setFont(font)

        self.horizontalLayout_9.addWidget(self.toolButton_path)

        self.toolButton_refresh = QToolButton(Dialog_visual)
        self.toolButton_refresh.setObjectName(u"toolButton_refresh")
        self.toolButton_refresh.setMinimumSize(QSize(0, 20))

        self.horizontalLayout_9.addWidget(self.toolButton_refresh)


        self.verticalLayout_5.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_save_path = QLabel(Dialog_visual)
        self.label_save_path.setObjectName(u"label_save_path")
        sizePolicy.setHeightForWidth(self.label_save_path.sizePolicy().hasHeightForWidth())
        self.label_save_path.setSizePolicy(sizePolicy)
        self.label_save_path.setFont(font)

        self.horizontalLayout_13.addWidget(self.label_save_path)

        self.lineEdit_save_path = QLineEdit(Dialog_visual)
        self.lineEdit_save_path.setObjectName(u"lineEdit_save_path")
        self.lineEdit_save_path.setFont(font1)

        self.horizontalLayout_13.addWidget(self.lineEdit_save_path)

        self.toolButton_path_2 = QToolButton(Dialog_visual)
        self.toolButton_path_2.setObjectName(u"toolButton_path_2")
        sizePolicy1.setHeightForWidth(self.toolButton_path_2.sizePolicy().hasHeightForWidth())
        self.toolButton_path_2.setSizePolicy(sizePolicy1)
        self.toolButton_path_2.setMaximumSize(QSize(20, 20))
        self.toolButton_path_2.setFont(font)

        self.horizontalLayout_13.addWidget(self.toolButton_path_2)


        self.verticalLayout_5.addLayout(self.horizontalLayout_13)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_var_name = QLabel(Dialog_visual)
        self.label_var_name.setObjectName(u"label_var_name")
        self.label_var_name.setMinimumSize(QSize(85, 20))
        self.label_var_name.setFont(font)

        self.horizontalLayout_7.addWidget(self.label_var_name)

        self.comboBox_var_name = QComboBox(Dialog_visual)
        self.comboBox_var_name.setObjectName(u"comboBox_var_name")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.comboBox_var_name.sizePolicy().hasHeightForWidth())
        self.comboBox_var_name.setSizePolicy(sizePolicy2)
        self.comboBox_var_name.setMinimumSize(QSize(70, 20))

        self.horizontalLayout_7.addWidget(self.comboBox_var_name)


        self.verticalLayout_2.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_2)

        self.checkBox_all_vars = QCheckBox(Dialog_visual)
        self.checkBox_all_vars.setObjectName(u"checkBox_all_vars")
        self.checkBox_all_vars.setMinimumSize(QSize(80, 20))
        font2 = QFont()
        font2.setPointSize(10)
        font2.setKerning(True)
        self.checkBox_all_vars.setFont(font2)
        self.checkBox_all_vars.setIconSize(QSize(20, 20))

        self.horizontalLayout_16.addWidget(self.checkBox_all_vars)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_3)


        self.verticalLayout_2.addLayout(self.horizontalLayout_16)


        self.horizontalLayout_17.addLayout(self.verticalLayout_2)

        self.horizontalSpacer_7 = QSpacerItem(13, 71, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_17.addItem(self.horizontalSpacer_7)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalSpacer_5 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.horizontalLayout.addItem(self.verticalSpacer_5)

        self.label_hour = QLabel(Dialog_visual)
        self.label_hour.setObjectName(u"label_hour")
        self.label_hour.setMinimumSize(QSize(50, 20))
        self.label_hour.setMaximumSize(QSize(40, 20))
        self.label_hour.setFont(font)

        self.horizontalLayout.addWidget(self.label_hour)

        self.label_day = QLabel(Dialog_visual)
        self.label_day.setObjectName(u"label_day")
        self.label_day.setMinimumSize(QSize(50, 20))
        self.label_day.setMaximumSize(QSize(40, 20))
        self.label_day.setFont(font)

        self.horizontalLayout.addWidget(self.label_day)

        self.label_month = QLabel(Dialog_visual)
        self.label_month.setObjectName(u"label_month")
        self.label_month.setMinimumSize(QSize(50, 20))
        self.label_month.setMaximumSize(QSize(40, 20))
        self.label_month.setFont(font)

        self.horizontalLayout.addWidget(self.label_month)

        self.label_year = QLabel(Dialog_visual)
        self.label_year.setObjectName(u"label_year")
        self.label_year.setMinimumSize(QSize(50, 20))
        self.label_year.setMaximumSize(QSize(40, 20))
        self.label_year.setFont(font)

        self.horizontalLayout.addWidget(self.label_year)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_start_time = QLabel(Dialog_visual)
        self.label_start_time.setObjectName(u"label_start_time")
        self.label_start_time.setMinimumSize(QSize(50, 20))
        self.label_start_time.setFont(font)
        self.label_start_time.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_8.addWidget(self.label_start_time)

        self.comboBox_start_hour = QComboBox(Dialog_visual)
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
        self.comboBox_start_hour.setMinimumSize(QSize(50, 20))
        self.comboBox_start_hour.setFont(font1)

        self.horizontalLayout_8.addWidget(self.comboBox_start_hour)

        self.comboBox_start_day = QComboBox(Dialog_visual)
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
        self.comboBox_start_day.setMinimumSize(QSize(50, 20))
        self.comboBox_start_day.setFont(font1)

        self.horizontalLayout_8.addWidget(self.comboBox_start_day)

        self.comboBox_start_month = QComboBox(Dialog_visual)
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
        self.comboBox_start_month.setMinimumSize(QSize(50, 20))
        self.comboBox_start_month.setFont(font1)

        self.horizontalLayout_8.addWidget(self.comboBox_start_month)

        self.lineEdit_start_year = QLineEdit(Dialog_visual)
        self.lineEdit_start_year.setObjectName(u"lineEdit_start_year")
        self.lineEdit_start_year.setMinimumSize(QSize(50, 20))
        self.lineEdit_start_year.setMaximumSize(QSize(40, 20))

        self.horizontalLayout_8.addWidget(self.lineEdit_start_year)


        self.verticalLayout.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_end_time = QLabel(Dialog_visual)
        self.label_end_time.setObjectName(u"label_end_time")
        self.label_end_time.setMinimumSize(QSize(50, 20))
        self.label_end_time.setFont(font)

        self.horizontalLayout_15.addWidget(self.label_end_time)

        self.comboBox_end_hour = QComboBox(Dialog_visual)
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
        self.comboBox_end_hour.setMinimumSize(QSize(50, 20))
        self.comboBox_end_hour.setFont(font1)

        self.horizontalLayout_15.addWidget(self.comboBox_end_hour)

        self.comboBox_end_day = QComboBox(Dialog_visual)
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
        self.comboBox_end_day.setMinimumSize(QSize(50, 20))
        self.comboBox_end_day.setFont(font1)

        self.horizontalLayout_15.addWidget(self.comboBox_end_day)

        self.comboBox_end_month = QComboBox(Dialog_visual)
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
        self.comboBox_end_month.setMinimumSize(QSize(50, 20))
        self.comboBox_end_month.setFont(font1)

        self.horizontalLayout_15.addWidget(self.comboBox_end_month)

        self.lineEdit_end_year = QLineEdit(Dialog_visual)
        self.lineEdit_end_year.setObjectName(u"lineEdit_end_year")
        self.lineEdit_end_year.setMinimumSize(QSize(50, 20))
        self.lineEdit_end_year.setMaximumSize(QSize(40, 20))

        self.horizontalLayout_15.addWidget(self.lineEdit_end_year)


        self.verticalLayout.addLayout(self.horizontalLayout_15)


        self.horizontalLayout_17.addLayout(self.verticalLayout)

        self.horizontalSpacer_8 = QSpacerItem(13, 71, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_17.addItem(self.horizontalSpacer_8)


        self.verticalLayout_5.addLayout(self.horizontalLayout_17)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.groupBox = QGroupBox(Dialog_visual)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy3)
        self.groupBox.setMinimumSize(QSize(220, 140))
        self.groupBox.setMaximumSize(QSize(300, 200))
        self.verticalLayout_6 = QVBoxLayout(self.groupBox)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_lat_name = QLabel(self.groupBox)
        self.label_lat_name.setObjectName(u"label_lat_name")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.label_lat_name.sizePolicy().hasHeightForWidth())
        self.label_lat_name.setSizePolicy(sizePolicy4)
        self.label_lat_name.setMinimumSize(QSize(50, 20))
        self.label_lat_name.setMaximumSize(QSize(100, 16777215))
        self.label_lat_name.setFont(font)

        self.horizontalLayout_11.addWidget(self.label_lat_name)

        self.lineEdit_lat_name = QLineEdit(self.groupBox)
        self.lineEdit_lat_name.setObjectName(u"lineEdit_lat_name")
        self.lineEdit_lat_name.setMinimumSize(QSize(40, 20))
        self.lineEdit_lat_name.setMaximumSize(QSize(30, 16777215))

        self.horizontalLayout_11.addWidget(self.lineEdit_lat_name)


        self.horizontalLayout_12.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_lon_name = QLabel(self.groupBox)
        self.label_lon_name.setObjectName(u"label_lon_name")
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.label_lon_name.sizePolicy().hasHeightForWidth())
        self.label_lon_name.setSizePolicy(sizePolicy5)
        self.label_lon_name.setMinimumSize(QSize(50, 20))
        self.label_lon_name.setMaximumSize(QSize(100, 16777215))
        self.label_lon_name.setFont(font)

        self.horizontalLayout_14.addWidget(self.label_lon_name)

        self.lineEdit_lon_name = QLineEdit(self.groupBox)
        self.lineEdit_lon_name.setObjectName(u"lineEdit_lon_name")
        self.lineEdit_lon_name.setMinimumSize(QSize(40, 20))
        self.lineEdit_lon_name.setMaximumSize(QSize(30, 16777215))

        self.horizontalLayout_14.addWidget(self.lineEdit_lon_name)


        self.horizontalLayout_12.addLayout(self.horizontalLayout_14)


        self.verticalLayout_6.addLayout(self.horizontalLayout_12)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_3)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_lat = QLabel(self.groupBox)
        self.label_lat.setObjectName(u"label_lat")
        self.label_lat.setMinimumSize(QSize(30, 20))
        self.label_lat.setMaximumSize(QSize(100, 16777215))
        self.label_lat.setFont(font)

        self.horizontalLayout_3.addWidget(self.label_lat)

        self.lineEdit_lat = QLineEdit(self.groupBox)
        self.lineEdit_lat.setObjectName(u"lineEdit_lat")
        self.lineEdit_lat.setMinimumSize(QSize(60, 20))
        self.lineEdit_lat.setMaximumSize(QSize(30, 16777215))

        self.horizontalLayout_3.addWidget(self.lineEdit_lat)


        self.horizontalLayout_6.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_lon = QLabel(self.groupBox)
        self.label_lon.setObjectName(u"label_lon")
        self.label_lon.setMinimumSize(QSize(30, 20))
        self.label_lon.setMaximumSize(QSize(100, 16777215))
        self.label_lon.setFont(font)

        self.horizontalLayout_2.addWidget(self.label_lon)

        self.lineEdit_lon = QLineEdit(self.groupBox)
        self.lineEdit_lon.setObjectName(u"lineEdit_lon")
        self.lineEdit_lon.setMinimumSize(QSize(60, 20))
        self.lineEdit_lon.setMaximumSize(QSize(30, 16777215))

        self.horizontalLayout_2.addWidget(self.lineEdit_lon)


        self.horizontalLayout_6.addLayout(self.horizontalLayout_2)


        self.verticalLayout_6.addLayout(self.horizontalLayout_6)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_2)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer)

        self.pushButton_point_time_excel = QPushButton(self.groupBox)
        self.pushButton_point_time_excel.setObjectName(u"pushButton_point_time_excel")
        sizePolicy2.setHeightForWidth(self.pushButton_point_time_excel.sizePolicy().hasHeightForWidth())
        self.pushButton_point_time_excel.setSizePolicy(sizePolicy2)
        self.pushButton_point_time_excel.setMinimumSize(QSize(0, 25))
        self.pushButton_point_time_excel.setFont(font)

        self.horizontalLayout_5.addWidget(self.pushButton_point_time_excel)

        self.pushButton_point_time_plot = QPushButton(self.groupBox)
        self.pushButton_point_time_plot.setObjectName(u"pushButton_point_time_plot")
        sizePolicy2.setHeightForWidth(self.pushButton_point_time_plot.sizePolicy().hasHeightForWidth())
        self.pushButton_point_time_plot.setSizePolicy(sizePolicy2)
        self.pushButton_point_time_plot.setMinimumSize(QSize(0, 25))
        self.pushButton_point_time_plot.setFont(font)

        self.horizontalLayout_5.addWidget(self.pushButton_point_time_plot)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_9)


        self.verticalLayout_6.addLayout(self.horizontalLayout_5)

        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.verticalLayout_6.addWidget(self.label)


        self.horizontalLayout_10.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(Dialog_visual)
        self.groupBox_2.setObjectName(u"groupBox_2")
        sizePolicy3.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy3)
        self.groupBox_2.setMinimumSize(QSize(200, 140))
        self.groupBox_2.setMaximumSize(QSize(300, 200))
        self.verticalLayout_7 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_4)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.pushButton_maps_raster = QPushButton(self.groupBox_2)
        self.pushButton_maps_raster.setObjectName(u"pushButton_maps_raster")
        sizePolicy6 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.pushButton_maps_raster.sizePolicy().hasHeightForWidth())
        self.pushButton_maps_raster.setSizePolicy(sizePolicy6)
        self.pushButton_maps_raster.setMinimumSize(QSize(80, 0))
        self.pushButton_maps_raster.setFont(font)

        self.horizontalLayout_4.addWidget(self.pushButton_maps_raster)

        self.pushButton_map_figure = QPushButton(self.groupBox_2)
        self.pushButton_map_figure.setObjectName(u"pushButton_map_figure")
        sizePolicy6.setHeightForWidth(self.pushButton_map_figure.sizePolicy().hasHeightForWidth())
        self.pushButton_map_figure.setSizePolicy(sizePolicy6)
        self.pushButton_map_figure.setMinimumSize(QSize(80, 25))
        self.pushButton_map_figure.setFont(font)

        self.horizontalLayout_4.addWidget(self.pushButton_map_figure)


        self.verticalLayout_7.addLayout(self.horizontalLayout_4)

        self.verticalSpacer = QSpacerItem(20, 58, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer)

        self.label_2 = QLabel(self.groupBox_2)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_7.addWidget(self.label_2)


        self.horizontalLayout_10.addWidget(self.groupBox_2)


        self.verticalLayout_5.addLayout(self.horizontalLayout_10)

        self.groupBox_report = QGroupBox(Dialog_visual)
        self.groupBox_report.setObjectName(u"groupBox_report")
        self.verticalLayout_4 = QVBoxLayout(self.groupBox_report)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.groupBox_report_raster = QGroupBox(self.groupBox_report)
        self.groupBox_report_raster.setObjectName(u"groupBox_report_raster")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_report_raster)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.checkBox_regions_raster = QCheckBox(self.groupBox_report_raster)
        self.checkBox_regions_raster.setObjectName(u"checkBox_regions_raster")
        self.checkBox_regions_raster.setFont(font)

        self.horizontalLayout_21.addWidget(self.checkBox_regions_raster)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_21.addItem(self.horizontalSpacer_10)


        self.verticalLayout_3.addLayout(self.horizontalLayout_21)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.label_regions_raster = QLabel(self.groupBox_report_raster)
        self.label_regions_raster.setObjectName(u"label_regions_raster")
        self.label_regions_raster.setEnabled(False)
        sizePolicy.setHeightForWidth(self.label_regions_raster.sizePolicy().hasHeightForWidth())
        self.label_regions_raster.setSizePolicy(sizePolicy)
        self.label_regions_raster.setFont(font)

        self.horizontalLayout_18.addWidget(self.label_regions_raster)

        self.lineEdit_regions_raster = QLineEdit(self.groupBox_report_raster)
        self.lineEdit_regions_raster.setObjectName(u"lineEdit_regions_raster")
        self.lineEdit_regions_raster.setEnabled(False)
        self.lineEdit_regions_raster.setFont(font1)

        self.horizontalLayout_18.addWidget(self.lineEdit_regions_raster)

        self.toolButton_regions_raster = QToolButton(self.groupBox_report_raster)
        self.toolButton_regions_raster.setObjectName(u"toolButton_regions_raster")
        self.toolButton_regions_raster.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.toolButton_regions_raster.sizePolicy().hasHeightForWidth())
        self.toolButton_regions_raster.setSizePolicy(sizePolicy1)
        self.toolButton_regions_raster.setMaximumSize(QSize(20, 20))
        self.toolButton_regions_raster.setFont(font)

        self.horizontalLayout_18.addWidget(self.toolButton_regions_raster)

        self.toolButton_refresh_regions_raster = QToolButton(self.groupBox_report_raster)
        self.toolButton_refresh_regions_raster.setObjectName(u"toolButton_refresh_regions_raster")
        self.toolButton_refresh_regions_raster.setEnabled(False)
        self.toolButton_refresh_regions_raster.setMinimumSize(QSize(0, 20))

        self.horizontalLayout_18.addWidget(self.toolButton_refresh_regions_raster)


        self.verticalLayout_3.addLayout(self.horizontalLayout_18)

        self.horizontalSpacer_11 = QSpacerItem(490, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout_3.addItem(self.horizontalSpacer_11)

        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer_5)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.label_region = QLabel(self.groupBox_report_raster)
        self.label_region.setObjectName(u"label_region")
        self.label_region.setEnabled(False)
        self.label_region.setMinimumSize(QSize(40, 20))
        self.label_region.setFont(font)

        self.horizontalLayout_19.addWidget(self.label_region)

        self.comboBox_region = QComboBox(self.groupBox_report_raster)
        self.comboBox_region.setObjectName(u"comboBox_region")
        self.comboBox_region.setEnabled(False)
        sizePolicy2.setHeightForWidth(self.comboBox_region.sizePolicy().hasHeightForWidth())
        self.comboBox_region.setSizePolicy(sizePolicy2)
        self.comboBox_region.setMinimumSize(QSize(70, 20))

        self.horizontalLayout_19.addWidget(self.comboBox_region)


        self.horizontalLayout_20.addLayout(self.horizontalLayout_19)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer_4)


        self.verticalLayout_3.addLayout(self.horizontalLayout_20)


        self.verticalLayout_4.addWidget(self.groupBox_report_raster)

        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_22.addItem(self.horizontalSpacer_6)

        self.pushButton_report_excel = QPushButton(self.groupBox_report)
        self.pushButton_report_excel.setObjectName(u"pushButton_report_excel")
        sizePolicy2.setHeightForWidth(self.pushButton_report_excel.sizePolicy().hasHeightForWidth())
        self.pushButton_report_excel.setSizePolicy(sizePolicy2)
        self.pushButton_report_excel.setMinimumSize(QSize(0, 25))
        self.pushButton_report_excel.setMaximumSize(QSize(150, 16777215))
        self.pushButton_report_excel.setFont(font)

        self.horizontalLayout_22.addWidget(self.pushButton_report_excel)


        self.verticalLayout_4.addLayout(self.horizontalLayout_22)


        self.verticalLayout_5.addWidget(self.groupBox_report)


        self.horizontalLayout_24.addLayout(self.verticalLayout_5)

        self.groupBox_help = QGroupBox(Dialog_visual)
        self.groupBox_help.setObjectName(u"groupBox_help")
        sizePolicy7 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.groupBox_help.sizePolicy().hasHeightForWidth())
        self.groupBox_help.setSizePolicy(sizePolicy7)
        self.groupBox_help.setMinimumSize(QSize(450, 0))
        font3 = QFont()
        font3.setPointSize(9)
        self.groupBox_help.setFont(font3)
        self.groupBox_help.setAutoFillBackground(False)
        self.groupBox_help.setStyleSheet(u"QGroupBox{border:2px solid gray;border-radius:1px;margin-top: 1ex;}\n"
"QGroupBox::title{subcontrol-origin: margin;subcontrol-position:top center;padding:0 3px;}")
        self.groupBox_help.setTitle(u"Help")
        self.groupBox_help.setFlat(False)
        self.horizontalLayout_23 = QHBoxLayout(self.groupBox_help)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.textBrowser_help = QTextBrowser(self.groupBox_help)
        self.textBrowser_help.setObjectName(u"textBrowser_help")
        self.textBrowser_help.setAutoFillBackground(True)
        self.textBrowser_help.setStyleSheet(u"background-color: rgb(240, 240, 240)")
        self.textBrowser_help.setFrameShape(QFrame.WinPanel)
        self.textBrowser_help.setFrameShadow(QFrame.Sunken)
        self.textBrowser_help.setLineWidth(0)
        self.textBrowser_help.setReadOnly(True)

        self.horizontalLayout_23.addWidget(self.textBrowser_help)


        self.horizontalLayout_24.addWidget(self.groupBox_help)

#if QT_CONFIG(shortcut)
        self.label_dataset_dir.setBuddy(self.lineEdit_dataset_path)
        self.label_save_path.setBuddy(self.lineEdit_dataset_path)
        self.label_regions_raster.setBuddy(self.lineEdit_dataset_path)
#endif // QT_CONFIG(shortcut)

        self.retranslateUi(Dialog_visual)

        QMetaObject.connectSlotsByName(Dialog_visual)
    # setupUi

    def retranslateUi(self, Dialog_visual):
        Dialog_visual.setWindowTitle(QCoreApplication.translate("Dialog_visual", u"Visualization and outputs", None))
        self.label_dataset_dir.setText(QCoreApplication.translate("Dialog_visual", u"Dataset path", None))
        self.toolButton_path.setText(QCoreApplication.translate("Dialog_visual", u"...", None))
        self.toolButton_refresh.setText(QCoreApplication.translate("Dialog_visual", u"refresh", None))
        self.label_save_path.setText(QCoreApplication.translate("Dialog_visual", u"Output path", None))
        self.toolButton_path_2.setText(QCoreApplication.translate("Dialog_visual", u"...", None))
        self.label_var_name.setText(QCoreApplication.translate("Dialog_visual", u"Variable name", None))
        self.checkBox_all_vars.setText(QCoreApplication.translate("Dialog_visual", u"All Variables", None))
        self.label_hour.setText(QCoreApplication.translate("Dialog_visual", u"Hour", None))
        self.label_day.setText(QCoreApplication.translate("Dialog_visual", u"Day", None))
        self.label_month.setText(QCoreApplication.translate("Dialog_visual", u"Month", None))
        self.label_year.setText(QCoreApplication.translate("Dialog_visual", u"Year", None))
        self.label_start_time.setText(QCoreApplication.translate("Dialog_visual", u"Start", None))
        self.comboBox_start_hour.setItemText(0, QCoreApplication.translate("Dialog_visual", u"00", None))
        self.comboBox_start_hour.setItemText(1, QCoreApplication.translate("Dialog_visual", u"01", None))
        self.comboBox_start_hour.setItemText(2, QCoreApplication.translate("Dialog_visual", u"02", None))
        self.comboBox_start_hour.setItemText(3, QCoreApplication.translate("Dialog_visual", u"03", None))
        self.comboBox_start_hour.setItemText(4, QCoreApplication.translate("Dialog_visual", u"04", None))
        self.comboBox_start_hour.setItemText(5, QCoreApplication.translate("Dialog_visual", u"05", None))
        self.comboBox_start_hour.setItemText(6, QCoreApplication.translate("Dialog_visual", u"06", None))
        self.comboBox_start_hour.setItemText(7, QCoreApplication.translate("Dialog_visual", u"07", None))
        self.comboBox_start_hour.setItemText(8, QCoreApplication.translate("Dialog_visual", u"08", None))
        self.comboBox_start_hour.setItemText(9, QCoreApplication.translate("Dialog_visual", u"09", None))
        self.comboBox_start_hour.setItemText(10, QCoreApplication.translate("Dialog_visual", u"10", None))
        self.comboBox_start_hour.setItemText(11, QCoreApplication.translate("Dialog_visual", u"11", None))
        self.comboBox_start_hour.setItemText(12, QCoreApplication.translate("Dialog_visual", u"12", None))
        self.comboBox_start_hour.setItemText(13, QCoreApplication.translate("Dialog_visual", u"13", None))
        self.comboBox_start_hour.setItemText(14, QCoreApplication.translate("Dialog_visual", u"14", None))
        self.comboBox_start_hour.setItemText(15, QCoreApplication.translate("Dialog_visual", u"15", None))
        self.comboBox_start_hour.setItemText(16, QCoreApplication.translate("Dialog_visual", u"16", None))
        self.comboBox_start_hour.setItemText(17, QCoreApplication.translate("Dialog_visual", u"17", None))
        self.comboBox_start_hour.setItemText(18, QCoreApplication.translate("Dialog_visual", u"18", None))
        self.comboBox_start_hour.setItemText(19, QCoreApplication.translate("Dialog_visual", u"19", None))
        self.comboBox_start_hour.setItemText(20, QCoreApplication.translate("Dialog_visual", u"20", None))
        self.comboBox_start_hour.setItemText(21, QCoreApplication.translate("Dialog_visual", u"21", None))
        self.comboBox_start_hour.setItemText(22, QCoreApplication.translate("Dialog_visual", u"22", None))
        self.comboBox_start_hour.setItemText(23, QCoreApplication.translate("Dialog_visual", u"23", None))

        self.comboBox_start_day.setItemText(0, QCoreApplication.translate("Dialog_visual", u"01", None))
        self.comboBox_start_day.setItemText(1, QCoreApplication.translate("Dialog_visual", u"02", None))
        self.comboBox_start_day.setItemText(2, QCoreApplication.translate("Dialog_visual", u"03", None))
        self.comboBox_start_day.setItemText(3, QCoreApplication.translate("Dialog_visual", u"04", None))
        self.comboBox_start_day.setItemText(4, QCoreApplication.translate("Dialog_visual", u"05", None))
        self.comboBox_start_day.setItemText(5, QCoreApplication.translate("Dialog_visual", u"06", None))
        self.comboBox_start_day.setItemText(6, QCoreApplication.translate("Dialog_visual", u"07", None))
        self.comboBox_start_day.setItemText(7, QCoreApplication.translate("Dialog_visual", u"08", None))
        self.comboBox_start_day.setItemText(8, QCoreApplication.translate("Dialog_visual", u"09", None))
        self.comboBox_start_day.setItemText(9, QCoreApplication.translate("Dialog_visual", u"10", None))
        self.comboBox_start_day.setItemText(10, QCoreApplication.translate("Dialog_visual", u"11", None))
        self.comboBox_start_day.setItemText(11, QCoreApplication.translate("Dialog_visual", u"12", None))
        self.comboBox_start_day.setItemText(12, QCoreApplication.translate("Dialog_visual", u"13", None))
        self.comboBox_start_day.setItemText(13, QCoreApplication.translate("Dialog_visual", u"14", None))
        self.comboBox_start_day.setItemText(14, QCoreApplication.translate("Dialog_visual", u"15", None))
        self.comboBox_start_day.setItemText(15, QCoreApplication.translate("Dialog_visual", u"16", None))
        self.comboBox_start_day.setItemText(16, QCoreApplication.translate("Dialog_visual", u"17", None))
        self.comboBox_start_day.setItemText(17, QCoreApplication.translate("Dialog_visual", u"18", None))
        self.comboBox_start_day.setItemText(18, QCoreApplication.translate("Dialog_visual", u"19", None))
        self.comboBox_start_day.setItemText(19, QCoreApplication.translate("Dialog_visual", u"20", None))
        self.comboBox_start_day.setItemText(20, QCoreApplication.translate("Dialog_visual", u"21", None))
        self.comboBox_start_day.setItemText(21, QCoreApplication.translate("Dialog_visual", u"22", None))
        self.comboBox_start_day.setItemText(22, QCoreApplication.translate("Dialog_visual", u"23", None))
        self.comboBox_start_day.setItemText(23, QCoreApplication.translate("Dialog_visual", u"24", None))
        self.comboBox_start_day.setItemText(24, QCoreApplication.translate("Dialog_visual", u"25", None))
        self.comboBox_start_day.setItemText(25, QCoreApplication.translate("Dialog_visual", u"26", None))
        self.comboBox_start_day.setItemText(26, QCoreApplication.translate("Dialog_visual", u"27", None))
        self.comboBox_start_day.setItemText(27, QCoreApplication.translate("Dialog_visual", u"28", None))
        self.comboBox_start_day.setItemText(28, QCoreApplication.translate("Dialog_visual", u"29", None))
        self.comboBox_start_day.setItemText(29, QCoreApplication.translate("Dialog_visual", u"30", None))

        self.comboBox_start_month.setItemText(0, QCoreApplication.translate("Dialog_visual", u"01", None))
        self.comboBox_start_month.setItemText(1, QCoreApplication.translate("Dialog_visual", u"02", None))
        self.comboBox_start_month.setItemText(2, QCoreApplication.translate("Dialog_visual", u"03", None))
        self.comboBox_start_month.setItemText(3, QCoreApplication.translate("Dialog_visual", u"04", None))
        self.comboBox_start_month.setItemText(4, QCoreApplication.translate("Dialog_visual", u"05", None))
        self.comboBox_start_month.setItemText(5, QCoreApplication.translate("Dialog_visual", u"06", None))
        self.comboBox_start_month.setItemText(6, QCoreApplication.translate("Dialog_visual", u"07", None))
        self.comboBox_start_month.setItemText(7, QCoreApplication.translate("Dialog_visual", u"08", None))
        self.comboBox_start_month.setItemText(8, QCoreApplication.translate("Dialog_visual", u"09", None))
        self.comboBox_start_month.setItemText(9, QCoreApplication.translate("Dialog_visual", u"010", None))
        self.comboBox_start_month.setItemText(10, QCoreApplication.translate("Dialog_visual", u"11", None))
        self.comboBox_start_month.setItemText(11, QCoreApplication.translate("Dialog_visual", u"12", None))

        self.label_end_time.setText(QCoreApplication.translate("Dialog_visual", u"End", None))
        self.comboBox_end_hour.setItemText(0, QCoreApplication.translate("Dialog_visual", u"00", None))
        self.comboBox_end_hour.setItemText(1, QCoreApplication.translate("Dialog_visual", u"01", None))
        self.comboBox_end_hour.setItemText(2, QCoreApplication.translate("Dialog_visual", u"02", None))
        self.comboBox_end_hour.setItemText(3, QCoreApplication.translate("Dialog_visual", u"03", None))
        self.comboBox_end_hour.setItemText(4, QCoreApplication.translate("Dialog_visual", u"04", None))
        self.comboBox_end_hour.setItemText(5, QCoreApplication.translate("Dialog_visual", u"05", None))
        self.comboBox_end_hour.setItemText(6, QCoreApplication.translate("Dialog_visual", u"06", None))
        self.comboBox_end_hour.setItemText(7, QCoreApplication.translate("Dialog_visual", u"07", None))
        self.comboBox_end_hour.setItemText(8, QCoreApplication.translate("Dialog_visual", u"08", None))
        self.comboBox_end_hour.setItemText(9, QCoreApplication.translate("Dialog_visual", u"09", None))
        self.comboBox_end_hour.setItemText(10, QCoreApplication.translate("Dialog_visual", u"10", None))
        self.comboBox_end_hour.setItemText(11, QCoreApplication.translate("Dialog_visual", u"11", None))
        self.comboBox_end_hour.setItemText(12, QCoreApplication.translate("Dialog_visual", u"12", None))
        self.comboBox_end_hour.setItemText(13, QCoreApplication.translate("Dialog_visual", u"13", None))
        self.comboBox_end_hour.setItemText(14, QCoreApplication.translate("Dialog_visual", u"14", None))
        self.comboBox_end_hour.setItemText(15, QCoreApplication.translate("Dialog_visual", u"15", None))
        self.comboBox_end_hour.setItemText(16, QCoreApplication.translate("Dialog_visual", u"16", None))
        self.comboBox_end_hour.setItemText(17, QCoreApplication.translate("Dialog_visual", u"17", None))
        self.comboBox_end_hour.setItemText(18, QCoreApplication.translate("Dialog_visual", u"18", None))
        self.comboBox_end_hour.setItemText(19, QCoreApplication.translate("Dialog_visual", u"19", None))
        self.comboBox_end_hour.setItemText(20, QCoreApplication.translate("Dialog_visual", u"20", None))
        self.comboBox_end_hour.setItemText(21, QCoreApplication.translate("Dialog_visual", u"21", None))
        self.comboBox_end_hour.setItemText(22, QCoreApplication.translate("Dialog_visual", u"22", None))
        self.comboBox_end_hour.setItemText(23, QCoreApplication.translate("Dialog_visual", u"23", None))

        self.comboBox_end_day.setItemText(0, QCoreApplication.translate("Dialog_visual", u"01", None))
        self.comboBox_end_day.setItemText(1, QCoreApplication.translate("Dialog_visual", u"02", None))
        self.comboBox_end_day.setItemText(2, QCoreApplication.translate("Dialog_visual", u"03", None))
        self.comboBox_end_day.setItemText(3, QCoreApplication.translate("Dialog_visual", u"04", None))
        self.comboBox_end_day.setItemText(4, QCoreApplication.translate("Dialog_visual", u"05", None))
        self.comboBox_end_day.setItemText(5, QCoreApplication.translate("Dialog_visual", u"06", None))
        self.comboBox_end_day.setItemText(6, QCoreApplication.translate("Dialog_visual", u"07", None))
        self.comboBox_end_day.setItemText(7, QCoreApplication.translate("Dialog_visual", u"08", None))
        self.comboBox_end_day.setItemText(8, QCoreApplication.translate("Dialog_visual", u"09", None))
        self.comboBox_end_day.setItemText(9, QCoreApplication.translate("Dialog_visual", u"10", None))
        self.comboBox_end_day.setItemText(10, QCoreApplication.translate("Dialog_visual", u"11", None))
        self.comboBox_end_day.setItemText(11, QCoreApplication.translate("Dialog_visual", u"12", None))
        self.comboBox_end_day.setItemText(12, QCoreApplication.translate("Dialog_visual", u"13", None))
        self.comboBox_end_day.setItemText(13, QCoreApplication.translate("Dialog_visual", u"14", None))
        self.comboBox_end_day.setItemText(14, QCoreApplication.translate("Dialog_visual", u"15", None))
        self.comboBox_end_day.setItemText(15, QCoreApplication.translate("Dialog_visual", u"16", None))
        self.comboBox_end_day.setItemText(16, QCoreApplication.translate("Dialog_visual", u"17", None))
        self.comboBox_end_day.setItemText(17, QCoreApplication.translate("Dialog_visual", u"18", None))
        self.comboBox_end_day.setItemText(18, QCoreApplication.translate("Dialog_visual", u"19", None))
        self.comboBox_end_day.setItemText(19, QCoreApplication.translate("Dialog_visual", u"20", None))
        self.comboBox_end_day.setItemText(20, QCoreApplication.translate("Dialog_visual", u"21", None))
        self.comboBox_end_day.setItemText(21, QCoreApplication.translate("Dialog_visual", u"22", None))
        self.comboBox_end_day.setItemText(22, QCoreApplication.translate("Dialog_visual", u"23", None))
        self.comboBox_end_day.setItemText(23, QCoreApplication.translate("Dialog_visual", u"24", None))
        self.comboBox_end_day.setItemText(24, QCoreApplication.translate("Dialog_visual", u"25", None))
        self.comboBox_end_day.setItemText(25, QCoreApplication.translate("Dialog_visual", u"26", None))
        self.comboBox_end_day.setItemText(26, QCoreApplication.translate("Dialog_visual", u"27", None))
        self.comboBox_end_day.setItemText(27, QCoreApplication.translate("Dialog_visual", u"28", None))
        self.comboBox_end_day.setItemText(28, QCoreApplication.translate("Dialog_visual", u"29", None))
        self.comboBox_end_day.setItemText(29, QCoreApplication.translate("Dialog_visual", u"30", None))

        self.comboBox_end_month.setItemText(0, QCoreApplication.translate("Dialog_visual", u"01", None))
        self.comboBox_end_month.setItemText(1, QCoreApplication.translate("Dialog_visual", u"02", None))
        self.comboBox_end_month.setItemText(2, QCoreApplication.translate("Dialog_visual", u"03", None))
        self.comboBox_end_month.setItemText(3, QCoreApplication.translate("Dialog_visual", u"04", None))
        self.comboBox_end_month.setItemText(4, QCoreApplication.translate("Dialog_visual", u"05", None))
        self.comboBox_end_month.setItemText(5, QCoreApplication.translate("Dialog_visual", u"06", None))
        self.comboBox_end_month.setItemText(6, QCoreApplication.translate("Dialog_visual", u"07", None))
        self.comboBox_end_month.setItemText(7, QCoreApplication.translate("Dialog_visual", u"08", None))
        self.comboBox_end_month.setItemText(8, QCoreApplication.translate("Dialog_visual", u"09", None))
        self.comboBox_end_month.setItemText(9, QCoreApplication.translate("Dialog_visual", u"10", None))
        self.comboBox_end_month.setItemText(10, QCoreApplication.translate("Dialog_visual", u"11", None))
        self.comboBox_end_month.setItemText(11, QCoreApplication.translate("Dialog_visual", u"12", None))

        self.groupBox.setTitle(QCoreApplication.translate("Dialog_visual", u"Time series of a point", None))
        self.label_lat_name.setText(QCoreApplication.translate("Dialog_visual", u"Lat. name", None))
        self.lineEdit_lat_name.setText(QCoreApplication.translate("Dialog_visual", u"lat", None))
        self.label_lon_name.setText(QCoreApplication.translate("Dialog_visual", u"Lon. name", None))
        self.lineEdit_lon_name.setText(QCoreApplication.translate("Dialog_visual", u"lon", None))
        self.label_lat.setText(QCoreApplication.translate("Dialog_visual", u"Lat.", None))
        self.lineEdit_lat.setText("")
        self.label_lon.setText(QCoreApplication.translate("Dialog_visual", u"Lon.", None))
        self.lineEdit_lon.setText("")
        self.pushButton_point_time_excel.setText(QCoreApplication.translate("Dialog_visual", u"Excel", None))
        self.pushButton_point_time_plot.setText(QCoreApplication.translate("Dialog_visual", u"Figure", None))
        self.label.setText("")
        self.groupBox_2.setTitle(QCoreApplication.translate("Dialog_visual", u"Maps", None))
        self.pushButton_maps_raster.setText(QCoreApplication.translate("Dialog_visual", u"Raster", None))
        self.pushButton_map_figure.setText(QCoreApplication.translate("Dialog_visual", u"Map (.png)", None))
        self.label_2.setText("")
        self.groupBox_report.setTitle(QCoreApplication.translate("Dialog_visual", u"Report", None))
        self.groupBox_report_raster.setTitle("")
        self.checkBox_regions_raster.setText(QCoreApplication.translate("Dialog_visual", u"Create the report by regions", None))
        self.label_regions_raster.setText(QCoreApplication.translate("Dialog_visual", u"Region Identifier Raster", None))
        self.toolButton_regions_raster.setText(QCoreApplication.translate("Dialog_visual", u"...", None))
        self.toolButton_refresh_regions_raster.setText(QCoreApplication.translate("Dialog_visual", u"refresh", None))
        self.label_region.setText(QCoreApplication.translate("Dialog_visual", u"Region", None))
        self.pushButton_report_excel.setText(QCoreApplication.translate("Dialog_visual", u"Generate Excel Report", None))
        self.textBrowser_help.setHtml(QCoreApplication.translate("Dialog_visual", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.1pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
    # retranslateUi

