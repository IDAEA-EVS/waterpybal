# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'infiltration_new.ui'
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

class Ui_Dialog_infiltration(object):
    def setupUi(self, Dialog_infiltration):
        if not Dialog_infiltration.objectName():
            Dialog_infiltration.setObjectName(u"Dialog_infiltration")
        Dialog_infiltration.resize(1000, 875)
        Dialog_infiltration.setMinimumSize(QSize(1000, 875))
        self.horizontalLayout_36 = QHBoxLayout(Dialog_infiltration)
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.groupBox_curve_number = QGroupBox(Dialog_infiltration)
        self.groupBox_curve_number.setObjectName(u"groupBox_curve_number")
        self.groupBox_curve_number.setEnabled(True)
        font = QFont()
        font.setBold(False)
        font.setKerning(True)
        self.groupBox_curve_number.setFont(font)
        self.groupBox_curve_number.setCheckable(True)
        self.groupBox_curve_number.setChecked(True)
        self.verticalLayout_11 = QVBoxLayout(self.groupBox_curve_number)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_cn_csv = QLabel(self.groupBox_curve_number)
        self.label_cn_csv.setObjectName(u"label_cn_csv")
        self.label_cn_csv.setMinimumSize(QSize(200, 20))
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(False)
        font1.setKerning(True)
        self.label_cn_csv.setFont(font1)

        self.horizontalLayout_6.addWidget(self.label_cn_csv)

        self.lineEdit_cn_csv = QLineEdit(self.groupBox_curve_number)
        self.lineEdit_cn_csv.setObjectName(u"lineEdit_cn_csv")
        self.lineEdit_cn_csv.setMinimumSize(QSize(160, 20))

        self.horizontalLayout_6.addWidget(self.lineEdit_cn_csv)

        self.toolButton_browse_cn_csv = QToolButton(self.groupBox_curve_number)
        self.toolButton_browse_cn_csv.setObjectName(u"toolButton_browse_cn_csv")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolButton_browse_cn_csv.sizePolicy().hasHeightForWidth())
        self.toolButton_browse_cn_csv.setSizePolicy(sizePolicy)
        self.toolButton_browse_cn_csv.setMaximumSize(QSize(20, 20))

        self.horizontalLayout_6.addWidget(self.toolButton_browse_cn_csv)


        self.verticalLayout_11.addLayout(self.horizontalLayout_6)

        self.line_5 = QFrame(self.groupBox_curve_number)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.HLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_11.addWidget(self.line_5)

        self.groupBox_raster = QGroupBox(self.groupBox_curve_number)
        self.groupBox_raster.setObjectName(u"groupBox_raster")
        self.groupBox_raster.setMinimumSize(QSize(0, 73))
        self.groupBox_raster.setCheckable(False)
        self.verticalLayout_4 = QVBoxLayout(self.groupBox_raster)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_cn_raster = QLabel(self.groupBox_raster)
        self.label_cn_raster.setObjectName(u"label_cn_raster")
        self.label_cn_raster.setMinimumSize(QSize(200, 20))
        self.label_cn_raster.setFont(font1)

        self.horizontalLayout_7.addWidget(self.label_cn_raster)

        self.lineEdit_cn_raster = QLineEdit(self.groupBox_raster)
        self.lineEdit_cn_raster.setObjectName(u"lineEdit_cn_raster")
        self.lineEdit_cn_raster.setMinimumSize(QSize(160, 20))

        self.horizontalLayout_7.addWidget(self.lineEdit_cn_raster)

        self.toolButton_browse_cn_raster = QToolButton(self.groupBox_raster)
        self.toolButton_browse_cn_raster.setObjectName(u"toolButton_browse_cn_raster")
        sizePolicy.setHeightForWidth(self.toolButton_browse_cn_raster.sizePolicy().hasHeightForWidth())
        self.toolButton_browse_cn_raster.setSizePolicy(sizePolicy)
        self.toolButton_browse_cn_raster.setMaximumSize(QSize(20, 20))

        self.horizontalLayout_7.addWidget(self.toolButton_browse_cn_raster)


        self.verticalLayout_4.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_28 = QHBoxLayout()
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_lu = QLabel(self.groupBox_raster)
        self.label_lu.setObjectName(u"label_lu")
        self.label_lu.setMinimumSize(QSize(60, 20))
        self.label_lu.setMaximumSize(QSize(100, 16777215))
        self.label_lu.setFont(font1)

        self.horizontalLayout_2.addWidget(self.label_lu)

        self.lineEdit_lu = QLineEdit(self.groupBox_raster)
        self.lineEdit_lu.setObjectName(u"lineEdit_lu")
        self.lineEdit_lu.setMinimumSize(QSize(30, 20))
        self.lineEdit_lu.setMaximumSize(QSize(30, 16777215))

        self.horizontalLayout_2.addWidget(self.lineEdit_lu)


        self.horizontalLayout_28.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_hsg = QLabel(self.groupBox_raster)
        self.label_hsg.setObjectName(u"label_hsg")
        self.label_hsg.setMinimumSize(QSize(60, 20))
        self.label_hsg.setMaximumSize(QSize(100, 16777215))
        self.label_hsg.setFont(font1)

        self.horizontalLayout.addWidget(self.label_hsg)

        self.lineEdit_hsg = QLineEdit(self.groupBox_raster)
        self.lineEdit_hsg.setObjectName(u"lineEdit_hsg")
        self.lineEdit_hsg.setMinimumSize(QSize(30, 20))
        self.lineEdit_hsg.setMaximumSize(QSize(30, 16777215))

        self.horizontalLayout.addWidget(self.lineEdit_hsg)


        self.horizontalLayout_28.addLayout(self.horizontalLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_elev = QLabel(self.groupBox_raster)
        self.label_elev.setObjectName(u"label_elev")
        self.label_elev.setMinimumSize(QSize(200, 20))
        self.label_elev.setMaximumSize(QSize(100, 16777215))
        self.label_elev.setFont(font1)

        self.horizontalLayout_3.addWidget(self.label_elev)

        self.lineEdit_elev = QLineEdit(self.groupBox_raster)
        self.lineEdit_elev.setObjectName(u"lineEdit_elev")
        self.lineEdit_elev.setMinimumSize(QSize(30, 20))
        self.lineEdit_elev.setMaximumSize(QSize(30, 16777215))

        self.horizontalLayout_3.addWidget(self.lineEdit_elev)


        self.horizontalLayout_28.addLayout(self.horizontalLayout_3)

        self.checkBox_slope_cat = QCheckBox(self.groupBox_raster)
        self.checkBox_slope_cat.setObjectName(u"checkBox_slope_cat")
        self.checkBox_slope_cat.setMinimumSize(QSize(70, 0))

        self.horizontalLayout_28.addWidget(self.checkBox_slope_cat)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_slope = QLabel(self.groupBox_raster)
        self.label_slope.setObjectName(u"label_slope")
        self.label_slope.setEnabled(False)
        self.label_slope.setMinimumSize(QSize(60, 20))
        self.label_slope.setMaximumSize(QSize(100, 16777215))
        self.label_slope.setFont(font1)

        self.horizontalLayout_14.addWidget(self.label_slope)

        self.lineEdit_slope = QLineEdit(self.groupBox_raster)
        self.lineEdit_slope.setObjectName(u"lineEdit_slope")
        self.lineEdit_slope.setEnabled(False)
        self.lineEdit_slope.setMaximumSize(QSize(60, 16777215))

        self.horizontalLayout_14.addWidget(self.lineEdit_slope)


        self.horizontalLayout_28.addLayout(self.horizontalLayout_14)


        self.verticalLayout_4.addLayout(self.horizontalLayout_28)


        self.verticalLayout_11.addWidget(self.groupBox_raster)

        self.line_3 = QFrame(self.groupBox_curve_number)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_11.addWidget(self.line_3)

        self.horizontalLayout_35 = QHBoxLayout()
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.checkBox_adv_cn = QCheckBox(self.groupBox_curve_number)
        self.checkBox_adv_cn.setObjectName(u"checkBox_adv_cn")
        self.checkBox_adv_cn.setEnabled(True)
        self.checkBox_adv_cn.setMinimumSize(QSize(150, 19))
        self.checkBox_adv_cn.setMaximumSize(QSize(180, 16777215))
        font2 = QFont()
        font2.setPointSize(10)
        self.checkBox_adv_cn.setFont(font2)

        self.verticalLayout_7.addWidget(self.checkBox_adv_cn)

        self.verticalSpacer = QSpacerItem(20, 17, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer)


        self.horizontalLayout_35.addLayout(self.verticalLayout_7)

        self.groupBox_adv_cn = QGroupBox(self.groupBox_curve_number)
        self.groupBox_adv_cn.setObjectName(u"groupBox_adv_cn")
        self.groupBox_adv_cn.setEnabled(False)
        self.groupBox_adv_cn.setMinimumSize(QSize(400, 67))
        self.groupBox_adv_cn.setMaximumSize(QSize(16777215, 200))
        self.gridLayout = QGridLayout(self.groupBox_adv_cn)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout_26 = QHBoxLayout()
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.label_c = QLabel(self.groupBox_adv_cn)
        self.label_c.setObjectName(u"label_c")
        self.label_c.setMinimumSize(QSize(7, 19))
        self.label_c.setMaximumSize(QSize(10, 16777215))
        self.label_c.setFont(font2)

        self.horizontalLayout_26.addWidget(self.label_c)

        self.lineEdit_c = QLineEdit(self.groupBox_adv_cn)
        self.lineEdit_c.setObjectName(u"lineEdit_c")
        self.lineEdit_c.setMinimumSize(QSize(13, 19))
        self.lineEdit_c.setMaximumSize(QSize(30, 16777215))

        self.horizontalLayout_26.addWidget(self.lineEdit_c)


        self.gridLayout.addLayout(self.horizontalLayout_26, 0, 4, 1, 1)

        self.horizontalLayout_30 = QHBoxLayout()
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.label_b = QLabel(self.groupBox_adv_cn)
        self.label_b.setObjectName(u"label_b")
        self.label_b.setMinimumSize(QSize(7, 19))
        self.label_b.setMaximumSize(QSize(10, 16777215))
        self.label_b.setFont(font2)

        self.horizontalLayout_30.addWidget(self.label_b)

        self.lineEdit_b = QLineEdit(self.groupBox_adv_cn)
        self.lineEdit_b.setObjectName(u"lineEdit_b")
        self.lineEdit_b.setMinimumSize(QSize(13, 19))
        self.lineEdit_b.setMaximumSize(QSize(30, 16777215))

        self.horizontalLayout_30.addWidget(self.lineEdit_b)


        self.gridLayout.addLayout(self.horizontalLayout_30, 0, 2, 1, 1)

        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.label_y = QLabel(self.groupBox_adv_cn)
        self.label_y.setObjectName(u"label_y")
        self.label_y.setMinimumSize(QSize(7, 19))
        self.label_y.setMaximumSize(QSize(10, 16777215))
        self.label_y.setFont(font2)

        self.horizontalLayout_23.addWidget(self.label_y)

        self.lineEdit_y = QLineEdit(self.groupBox_adv_cn)
        self.lineEdit_y.setObjectName(u"lineEdit_y")
        self.lineEdit_y.setMinimumSize(QSize(13, 19))
        self.lineEdit_y.setMaximumSize(QSize(30, 16777215))

        self.horizontalLayout_23.addWidget(self.lineEdit_y)


        self.gridLayout.addLayout(self.horizontalLayout_23, 1, 2, 1, 1)

        self.horizontalSpacer_7 = QSpacerItem(30, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_7, 1, 5, 1, 1)

        self.horizontalSpacer_12 = QSpacerItem(31, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_12, 0, 3, 1, 1)

        self.horizontalLayout_27 = QHBoxLayout()
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.label_a = QLabel(self.groupBox_adv_cn)
        self.label_a.setObjectName(u"label_a")
        self.label_a.setMinimumSize(QSize(7, 19))
        self.label_a.setMaximumSize(QSize(10, 16777215))
        self.label_a.setFont(font2)

        self.horizontalLayout_27.addWidget(self.label_a)

        self.lineEdit_a = QLineEdit(self.groupBox_adv_cn)
        self.lineEdit_a.setObjectName(u"lineEdit_a")
        self.lineEdit_a.setMinimumSize(QSize(13, 19))
        self.lineEdit_a.setMaximumSize(QSize(30, 16777215))

        self.horizontalLayout_27.addWidget(self.lineEdit_a)


        self.gridLayout.addLayout(self.horizontalLayout_27, 0, 0, 1, 1)

        self.horizontalLayout_34 = QHBoxLayout()
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.horizontalLayout_25 = QHBoxLayout()
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.label_landa = QLabel(self.groupBox_adv_cn)
        self.label_landa.setObjectName(u"label_landa")
        self.label_landa.setMinimumSize(QSize(49, 19))
        self.label_landa.setMaximumSize(QSize(35, 16777215))
        self.label_landa.setFont(font2)

        self.horizontalLayout_25.addWidget(self.label_landa)

        self.lineEdit_landa = QLineEdit(self.groupBox_adv_cn)
        self.lineEdit_landa.setObjectName(u"lineEdit_landa")
        self.lineEdit_landa.setMinimumSize(QSize(20, 19))
        self.lineEdit_landa.setMaximumSize(QSize(30, 16777215))

        self.horizontalLayout_25.addWidget(self.lineEdit_landa)


        self.horizontalLayout_34.addLayout(self.horizontalLayout_25)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_34.addItem(self.horizontalSpacer_11)


        self.gridLayout.addLayout(self.horizontalLayout_34, 1, 6, 1, 1)

        self.horizontalLayout_24 = QHBoxLayout()
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.label_x = QLabel(self.groupBox_adv_cn)
        self.label_x.setObjectName(u"label_x")
        self.label_x.setMinimumSize(QSize(7, 19))
        self.label_x.setMaximumSize(QSize(10, 16777215))
        self.label_x.setFont(font2)

        self.horizontalLayout_24.addWidget(self.label_x)

        self.lineEdit_x = QLineEdit(self.groupBox_adv_cn)
        self.lineEdit_x.setObjectName(u"lineEdit_x")
        self.lineEdit_x.setMinimumSize(QSize(13, 19))
        self.lineEdit_x.setMaximumSize(QSize(30, 16777215))

        self.horizontalLayout_24.addWidget(self.lineEdit_x)


        self.gridLayout.addLayout(self.horizontalLayout_24, 1, 0, 1, 1)

        self.horizontalLayout_33 = QHBoxLayout()
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.label_d = QLabel(self.groupBox_adv_cn)
        self.label_d.setObjectName(u"label_d")
        self.label_d.setMinimumSize(QSize(7, 19))
        self.label_d.setMaximumSize(QSize(10, 16777215))
        self.label_d.setFont(font2)

        self.horizontalLayout_21.addWidget(self.label_d)

        self.lineEdit_d = QLineEdit(self.groupBox_adv_cn)
        self.lineEdit_d.setObjectName(u"lineEdit_d")
        self.lineEdit_d.setMinimumSize(QSize(13, 19))
        self.lineEdit_d.setMaximumSize(QSize(30, 16777215))

        self.horizontalLayout_21.addWidget(self.lineEdit_d)


        self.horizontalLayout_33.addLayout(self.horizontalLayout_21)

        self.label_advanced_cn_formula = QLabel(self.groupBox_adv_cn)
        self.label_advanced_cn_formula.setObjectName(u"label_advanced_cn_formula")
        self.label_advanced_cn_formula.setMinimumSize(QSize(180, 19))
        self.label_advanced_cn_formula.setMaximumSize(QSize(180, 16777215))

        self.horizontalLayout_33.addWidget(self.label_advanced_cn_formula)


        self.gridLayout.addLayout(self.horizontalLayout_33, 0, 6, 1, 1)

        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.label_z = QLabel(self.groupBox_adv_cn)
        self.label_z.setObjectName(u"label_z")
        self.label_z.setMinimumSize(QSize(7, 19))
        self.label_z.setMaximumSize(QSize(10, 16777215))
        self.label_z.setFont(font2)

        self.horizontalLayout_22.addWidget(self.label_z)

        self.lineEdit_z = QLineEdit(self.groupBox_adv_cn)
        self.lineEdit_z.setObjectName(u"lineEdit_z")
        self.lineEdit_z.setMinimumSize(QSize(13, 19))
        self.lineEdit_z.setMaximumSize(QSize(30, 16777215))

        self.horizontalLayout_22.addWidget(self.lineEdit_z)


        self.gridLayout.addLayout(self.horizontalLayout_22, 1, 4, 1, 1)

        self.horizontalSpacer_13 = QSpacerItem(30, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_13, 0, 1, 1, 1)

        self.horizontalSpacer_14 = QSpacerItem(30, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_14, 0, 5, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(30, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_5, 1, 1, 1, 1)

        self.horizontalSpacer_6 = QSpacerItem(31, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_6, 1, 3, 1, 1)


        self.horizontalLayout_35.addWidget(self.groupBox_adv_cn)


        self.verticalLayout_11.addLayout(self.horizontalLayout_35)

        self.line_4 = QFrame(self.groupBox_curve_number)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_11.addWidget(self.line_4)

        self.groupBox_corrected_cn = QGroupBox(self.groupBox_curve_number)
        self.groupBox_corrected_cn.setObjectName(u"groupBox_corrected_cn")
        self.groupBox_corrected_cn.setMinimumSize(QSize(0, 100))
        self.groupBox_corrected_cn.setCheckable(True)
        self.groupBox_corrected_cn.setChecked(False)
        self.verticalLayout_5 = QVBoxLayout(self.groupBox_corrected_cn)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_advanced_cn_formula_2 = QLabel(self.groupBox_corrected_cn)
        self.label_advanced_cn_formula_2.setObjectName(u"label_advanced_cn_formula_2")
        self.label_advanced_cn_formula_2.setMinimumSize(QSize(145, 0))

        self.verticalLayout_5.addWidget(self.label_advanced_cn_formula_2)

        self.horizontalLayout_40 = QHBoxLayout()
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_amc1 = QLabel(self.groupBox_corrected_cn)
        self.label_amc1.setObjectName(u"label_amc1")
        self.label_amc1.setMinimumSize(QSize(65, 20))
        self.label_amc1.setMaximumSize(QSize(100, 16777215))
        self.label_amc1.setFont(font1)

        self.horizontalLayout_4.addWidget(self.label_amc1)

        self.horizontalLayout_37 = QHBoxLayout()
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.label_amc1_a = QLabel(self.groupBox_corrected_cn)
        self.label_amc1_a.setObjectName(u"label_amc1_a")

        self.horizontalLayout_37.addWidget(self.label_amc1_a)

        self.lineEdit_amc1_a = QLineEdit(self.groupBox_corrected_cn)
        self.lineEdit_amc1_a.setObjectName(u"lineEdit_amc1_a")

        self.horizontalLayout_37.addWidget(self.lineEdit_amc1_a)

        self.label_amc1_b = QLabel(self.groupBox_corrected_cn)
        self.label_amc1_b.setObjectName(u"label_amc1_b")

        self.horizontalLayout_37.addWidget(self.label_amc1_b)

        self.lineEdit_amc1_b = QLineEdit(self.groupBox_corrected_cn)
        self.lineEdit_amc1_b.setObjectName(u"lineEdit_amc1_b")

        self.horizontalLayout_37.addWidget(self.lineEdit_amc1_b)

        self.label_amc1_c = QLabel(self.groupBox_corrected_cn)
        self.label_amc1_c.setObjectName(u"label_amc1_c")

        self.horizontalLayout_37.addWidget(self.label_amc1_c)

        self.lineEdit_amc1_c = QLineEdit(self.groupBox_corrected_cn)
        self.lineEdit_amc1_c.setObjectName(u"lineEdit_amc1_c")

        self.horizontalLayout_37.addWidget(self.lineEdit_amc1_c)


        self.horizontalLayout_4.addLayout(self.horizontalLayout_37)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_amc3 = QLabel(self.groupBox_corrected_cn)
        self.label_amc3.setObjectName(u"label_amc3")
        self.label_amc3.setMinimumSize(QSize(65, 20))
        self.label_amc3.setMaximumSize(QSize(100, 16777215))
        self.label_amc3.setFont(font1)

        self.horizontalLayout_5.addWidget(self.label_amc3)

        self.horizontalLayout_38 = QHBoxLayout()
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.label_amc3_a = QLabel(self.groupBox_corrected_cn)
        self.label_amc3_a.setObjectName(u"label_amc3_a")

        self.horizontalLayout_38.addWidget(self.label_amc3_a)

        self.lineEdit_amc3_a = QLineEdit(self.groupBox_corrected_cn)
        self.lineEdit_amc3_a.setObjectName(u"lineEdit_amc3_a")

        self.horizontalLayout_38.addWidget(self.lineEdit_amc3_a)

        self.label_amc3_b = QLabel(self.groupBox_corrected_cn)
        self.label_amc3_b.setObjectName(u"label_amc3_b")

        self.horizontalLayout_38.addWidget(self.label_amc3_b)

        self.lineEdit_amc3_b = QLineEdit(self.groupBox_corrected_cn)
        self.lineEdit_amc3_b.setObjectName(u"lineEdit_amc3_b")

        self.horizontalLayout_38.addWidget(self.lineEdit_amc3_b)

        self.label_amc3_c = QLabel(self.groupBox_corrected_cn)
        self.label_amc3_c.setObjectName(u"label_amc3_c")

        self.horizontalLayout_38.addWidget(self.label_amc3_c)

        self.lineEdit_amc3_c = QLineEdit(self.groupBox_corrected_cn)
        self.lineEdit_amc3_c.setObjectName(u"lineEdit_amc3_c")

        self.horizontalLayout_38.addWidget(self.lineEdit_amc3_c)


        self.horizontalLayout_5.addLayout(self.horizontalLayout_38)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)


        self.horizontalLayout_40.addLayout(self.verticalLayout_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_dormant_month = QLabel(self.groupBox_corrected_cn)
        self.label_dormant_month.setObjectName(u"label_dormant_month")
        self.label_dormant_month.setMinimumSize(QSize(90, 20))
        self.label_dormant_month.setMaximumSize(QSize(200, 16777215))
        self.label_dormant_month.setFont(font1)

        self.horizontalLayout_8.addWidget(self.label_dormant_month)

        self.lineEdit_dormant_month = QLineEdit(self.groupBox_corrected_cn)
        self.lineEdit_dormant_month.setObjectName(u"lineEdit_dormant_month")
        self.lineEdit_dormant_month.setMinimumSize(QSize(70, 0))

        self.horizontalLayout_8.addWidget(self.lineEdit_dormant_month)


        self.verticalLayout.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_29 = QHBoxLayout()
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.label_dormant_ = QLabel(self.groupBox_corrected_cn)
        self.label_dormant_.setObjectName(u"label_dormant_")
        self.label_dormant_.setMinimumSize(QSize(90, 20))
        self.label_dormant_.setMaximumSize(QSize(200, 16777215))
        self.label_dormant_.setFont(font1)

        self.horizontalLayout_29.addWidget(self.label_dormant_)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_dor_1 = QLabel(self.groupBox_corrected_cn)
        self.label_dor_1.setObjectName(u"label_dor_1")

        self.horizontalLayout_10.addWidget(self.label_dor_1)

        self.lineEdit_dormant_1 = QLineEdit(self.groupBox_corrected_cn)
        self.lineEdit_dormant_1.setObjectName(u"lineEdit_dormant_1")

        self.horizontalLayout_10.addWidget(self.lineEdit_dormant_1)

        self.label_dor_3 = QLabel(self.groupBox_corrected_cn)
        self.label_dor_3.setObjectName(u"label_dor_3")

        self.horizontalLayout_10.addWidget(self.label_dor_3)

        self.lineEdit_dormant_3 = QLineEdit(self.groupBox_corrected_cn)
        self.lineEdit_dormant_3.setObjectName(u"lineEdit_dormant_3")

        self.horizontalLayout_10.addWidget(self.lineEdit_dormant_3)


        self.horizontalLayout_29.addLayout(self.horizontalLayout_10)


        self.verticalLayout.addLayout(self.horizontalLayout_29)


        self.horizontalLayout_40.addLayout(self.verticalLayout)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_growing = QLabel(self.groupBox_corrected_cn)
        self.label_growing.setObjectName(u"label_growing")
        self.label_growing.setMinimumSize(QSize(97, 20))
        self.label_growing.setMaximumSize(QSize(200, 16777215))
        self.label_growing.setFont(font1)

        self.horizontalLayout_9.addWidget(self.label_growing)

        self.horizontalLayout_39 = QHBoxLayout()
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.label_grow_1 = QLabel(self.groupBox_corrected_cn)
        self.label_grow_1.setObjectName(u"label_grow_1")

        self.horizontalLayout_39.addWidget(self.label_grow_1)

        self.lineEdit_grow_1 = QLineEdit(self.groupBox_corrected_cn)
        self.lineEdit_grow_1.setObjectName(u"lineEdit_grow_1")

        self.horizontalLayout_39.addWidget(self.lineEdit_grow_1)

        self.label_grow_3 = QLabel(self.groupBox_corrected_cn)
        self.label_grow_3.setObjectName(u"label_grow_3")

        self.horizontalLayout_39.addWidget(self.label_grow_3)

        self.lineEdit_grow_3 = QLineEdit(self.groupBox_corrected_cn)
        self.lineEdit_grow_3.setObjectName(u"lineEdit_grow_3")

        self.horizontalLayout_39.addWidget(self.lineEdit_grow_3)


        self.horizontalLayout_9.addLayout(self.horizontalLayout_39)


        self.verticalLayout_3.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_average = QLabel(self.groupBox_corrected_cn)
        self.label_average.setObjectName(u"label_average")
        self.label_average.setMinimumSize(QSize(90, 20))
        self.label_average.setMaximumSize(QSize(200, 16777215))
        self.label_average.setFont(font1)

        self.horizontalLayout_11.addWidget(self.label_average)

        self.comboBox_average = QComboBox(self.groupBox_corrected_cn)
        self.comboBox_average.addItem("")
        self.comboBox_average.addItem("")
        self.comboBox_average.setObjectName(u"comboBox_average")
        self.comboBox_average.setMinimumSize(QSize(40, 0))

        self.horizontalLayout_11.addWidget(self.comboBox_average)


        self.horizontalLayout_12.addLayout(self.horizontalLayout_11)


        self.verticalLayout_3.addLayout(self.horizontalLayout_12)


        self.horizontalLayout_40.addLayout(self.verticalLayout_3)


        self.verticalLayout_5.addLayout(self.horizontalLayout_40)


        self.verticalLayout_11.addWidget(self.groupBox_corrected_cn)


        self.verticalLayout_14.addWidget(self.groupBox_curve_number)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.checkBox_cn_value = QCheckBox(Dialog_infiltration)
        self.checkBox_cn_value.setObjectName(u"checkBox_cn_value")

        self.horizontalLayout_13.addWidget(self.checkBox_cn_value)

        self.label_cn_val = QLabel(Dialog_infiltration)
        self.label_cn_val.setObjectName(u"label_cn_val")
        self.label_cn_val.setEnabled(False)
        self.label_cn_val.setMinimumSize(QSize(50, 20))
        self.label_cn_val.setMaximumSize(QSize(60, 16777215))
        self.label_cn_val.setFont(font1)

        self.horizontalLayout_13.addWidget(self.label_cn_val)

        self.lineEdit_CN_Val = QLineEdit(Dialog_infiltration)
        self.lineEdit_CN_Val.setObjectName(u"lineEdit_CN_Val")
        self.lineEdit_CN_Val.setEnabled(False)
        self.lineEdit_CN_Val.setMinimumSize(QSize(30, 20))
        self.lineEdit_CN_Val.setMaximumSize(QSize(30, 16777215))

        self.horizontalLayout_13.addWidget(self.lineEdit_CN_Val)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_3)


        self.verticalLayout_14.addLayout(self.horizontalLayout_13)

        self.verticalSpacer_5 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.verticalLayout_14.addItem(self.verticalSpacer_5)

        self.line = QFrame(Dialog_infiltration)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_14.addWidget(self.line)

        self.groupBox_urban = QGroupBox(Dialog_infiltration)
        self.groupBox_urban.setObjectName(u"groupBox_urban")
        self.groupBox_urban.setEnabled(True)
        self.groupBox_urban.setCheckable(True)
        self.groupBox_urban.setChecked(False)
        self.verticalLayout_12 = QVBoxLayout(self.groupBox_urban)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_urban_zone_raster = QLabel(self.groupBox_urban)
        self.label_urban_zone_raster.setObjectName(u"label_urban_zone_raster")
        self.label_urban_zone_raster.setEnabled(False)
        self.label_urban_zone_raster.setMinimumSize(QSize(200, 20))
        self.label_urban_zone_raster.setFont(font1)

        self.horizontalLayout_16.addWidget(self.label_urban_zone_raster)

        self.lineEdit_urban_zone_raster = QLineEdit(self.groupBox_urban)
        self.lineEdit_urban_zone_raster.setObjectName(u"lineEdit_urban_zone_raster")
        self.lineEdit_urban_zone_raster.setEnabled(False)
        self.lineEdit_urban_zone_raster.setMinimumSize(QSize(160, 20))

        self.horizontalLayout_16.addWidget(self.lineEdit_urban_zone_raster)

        self.toolButton_browse_urban_zone_raster = QToolButton(self.groupBox_urban)
        self.toolButton_browse_urban_zone_raster.setObjectName(u"toolButton_browse_urban_zone_raster")
        self.toolButton_browse_urban_zone_raster.setEnabled(False)
        sizePolicy.setHeightForWidth(self.toolButton_browse_urban_zone_raster.sizePolicy().hasHeightForWidth())
        self.toolButton_browse_urban_zone_raster.setSizePolicy(sizePolicy)
        self.toolButton_browse_urban_zone_raster.setMaximumSize(QSize(20, 20))

        self.horizontalLayout_16.addWidget(self.toolButton_browse_urban_zone_raster)


        self.verticalLayout_12.addLayout(self.horizontalLayout_16)

        self.horizontalLayout_32 = QHBoxLayout()
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.checkBox_urban_cn_correction = QCheckBox(self.groupBox_urban)
        self.checkBox_urban_cn_correction.setObjectName(u"checkBox_urban_cn_correction")
        self.checkBox_urban_cn_correction.setEnabled(False)

        self.verticalLayout_10.addWidget(self.checkBox_urban_cn_correction)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_10.addItem(self.verticalSpacer_4)


        self.horizontalLayout_32.addLayout(self.verticalLayout_10)

        self.groupBox_urban_cn_correction = QGroupBox(self.groupBox_urban)
        self.groupBox_urban_cn_correction.setObjectName(u"groupBox_urban_cn_correction")
        self.groupBox_urban_cn_correction.setEnabled(False)
        self.verticalLayout_9 = QVBoxLayout(self.groupBox_urban_cn_correction)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.checkBox_cia_cn_composite = QCheckBox(self.groupBox_urban_cn_correction)
        self.checkBox_cia_cn_composite.setObjectName(u"checkBox_cia_cn_composite")

        self.verticalLayout_9.addWidget(self.checkBox_cia_cn_composite)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.label_cn_urban_cia_raster = QLabel(self.groupBox_urban_cn_correction)
        self.label_cn_urban_cia_raster.setObjectName(u"label_cn_urban_cia_raster")
        self.label_cn_urban_cia_raster.setMinimumSize(QSize(200, 20))
        self.label_cn_urban_cia_raster.setFont(font1)

        self.horizontalLayout_17.addWidget(self.label_cn_urban_cia_raster)

        self.lineEdit_cn_urban_cia_raster = QLineEdit(self.groupBox_urban_cn_correction)
        self.lineEdit_cn_urban_cia_raster.setObjectName(u"lineEdit_cn_urban_cia_raster")
        self.lineEdit_cn_urban_cia_raster.setMinimumSize(QSize(160, 20))

        self.horizontalLayout_17.addWidget(self.lineEdit_cn_urban_cia_raster)

        self.toolButton_browse_cn_urban_cia_raster = QToolButton(self.groupBox_urban_cn_correction)
        self.toolButton_browse_cn_urban_cia_raster.setObjectName(u"toolButton_browse_cn_urban_cia_raster")
        sizePolicy.setHeightForWidth(self.toolButton_browse_cn_urban_cia_raster.sizePolicy().hasHeightForWidth())
        self.toolButton_browse_cn_urban_cia_raster.setSizePolicy(sizePolicy)
        self.toolButton_browse_cn_urban_cia_raster.setMaximumSize(QSize(20, 20))

        self.horizontalLayout_17.addWidget(self.toolButton_browse_cn_urban_cia_raster)


        self.verticalLayout_9.addLayout(self.horizontalLayout_17)

        self.checkBox_uncia_cn_composite = QCheckBox(self.groupBox_urban_cn_correction)
        self.checkBox_uncia_cn_composite.setObjectName(u"checkBox_uncia_cn_composite")

        self.verticalLayout_9.addWidget(self.checkBox_uncia_cn_composite)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.label_cn_urban_uncia_total_raster = QLabel(self.groupBox_urban_cn_correction)
        self.label_cn_urban_uncia_total_raster.setObjectName(u"label_cn_urban_uncia_total_raster")
        self.label_cn_urban_uncia_total_raster.setMinimumSize(QSize(200, 20))
        self.label_cn_urban_uncia_total_raster.setFont(font1)

        self.horizontalLayout_18.addWidget(self.label_cn_urban_uncia_total_raster)

        self.lineEdit_cn_urban_uncia_total_raster = QLineEdit(self.groupBox_urban_cn_correction)
        self.lineEdit_cn_urban_uncia_total_raster.setObjectName(u"lineEdit_cn_urban_uncia_total_raster")
        self.lineEdit_cn_urban_uncia_total_raster.setMinimumSize(QSize(160, 20))

        self.horizontalLayout_18.addWidget(self.lineEdit_cn_urban_uncia_total_raster)

        self.toolButton_browse_cn_urban_uncia_total_raster = QToolButton(self.groupBox_urban_cn_correction)
        self.toolButton_browse_cn_urban_uncia_total_raster.setObjectName(u"toolButton_browse_cn_urban_uncia_total_raster")
        sizePolicy.setHeightForWidth(self.toolButton_browse_cn_urban_uncia_total_raster.sizePolicy().hasHeightForWidth())
        self.toolButton_browse_cn_urban_uncia_total_raster.setSizePolicy(sizePolicy)
        self.toolButton_browse_cn_urban_uncia_total_raster.setMaximumSize(QSize(20, 20))

        self.horizontalLayout_18.addWidget(self.toolButton_browse_cn_urban_uncia_total_raster)


        self.verticalLayout_9.addLayout(self.horizontalLayout_18)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.label_cn_urban_uncia_raster = QLabel(self.groupBox_urban_cn_correction)
        self.label_cn_urban_uncia_raster.setObjectName(u"label_cn_urban_uncia_raster")
        self.label_cn_urban_uncia_raster.setMinimumSize(QSize(200, 20))
        self.label_cn_urban_uncia_raster.setFont(font1)

        self.horizontalLayout_19.addWidget(self.label_cn_urban_uncia_raster)

        self.lineEdit_cn_urban_uncia_raster = QLineEdit(self.groupBox_urban_cn_correction)
        self.lineEdit_cn_urban_uncia_raster.setObjectName(u"lineEdit_cn_urban_uncia_raster")
        self.lineEdit_cn_urban_uncia_raster.setMinimumSize(QSize(160, 20))

        self.horizontalLayout_19.addWidget(self.lineEdit_cn_urban_uncia_raster)

        self.toolButton_browse_cn_urban_uncia_raster = QToolButton(self.groupBox_urban_cn_correction)
        self.toolButton_browse_cn_urban_uncia_raster.setObjectName(u"toolButton_browse_cn_urban_uncia_raster")
        sizePolicy.setHeightForWidth(self.toolButton_browse_cn_urban_uncia_raster.sizePolicy().hasHeightForWidth())
        self.toolButton_browse_cn_urban_uncia_raster.setSizePolicy(sizePolicy)
        self.toolButton_browse_cn_urban_uncia_raster.setMaximumSize(QSize(20, 20))

        self.horizontalLayout_19.addWidget(self.toolButton_browse_cn_urban_uncia_raster)


        self.verticalLayout_9.addLayout(self.horizontalLayout_19)


        self.horizontalLayout_32.addWidget(self.groupBox_urban_cn_correction)


        self.verticalLayout_12.addLayout(self.horizontalLayout_32)

        self.line_6 = QFrame(self.groupBox_urban)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShape(QFrame.HLine)
        self.line_6.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_12.addWidget(self.line_6)

        self.horizontalLayout_31 = QHBoxLayout()
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.checkBox_urban_cycle = QCheckBox(self.groupBox_urban)
        self.checkBox_urban_cycle.setObjectName(u"checkBox_urban_cycle")
        self.checkBox_urban_cycle.setEnabled(False)

        self.verticalLayout_8.addWidget(self.checkBox_urban_cycle)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_3)


        self.horizontalLayout_31.addLayout(self.verticalLayout_8)

        self.tableWidget_urban = QTableWidget(self.groupBox_urban)
        self.tableWidget_urban.setObjectName(u"tableWidget_urban")
        self.tableWidget_urban.setEnabled(False)
        self.tableWidget_urban.setMinimumSize(QSize(600, 210))

        self.horizontalLayout_31.addWidget(self.tableWidget_urban)


        self.verticalLayout_12.addLayout(self.horizontalLayout_31)


        self.verticalLayout_14.addWidget(self.groupBox_urban)

        self.line_2 = QFrame(Dialog_infiltration)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_14.addWidget(self.line_2)

        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_max_infilt = QLabel(Dialog_infiltration)
        self.label_max_infilt.setObjectName(u"label_max_infilt")
        self.label_max_infilt.setMinimumSize(QSize(250, 20))
        font3 = QFont()
        font3.setPointSize(10)
        font3.setKerning(True)
        self.label_max_infilt.setFont(font3)

        self.horizontalLayout_15.addWidget(self.label_max_infilt)

        self.lineEdit__max_infilt = QLineEdit(Dialog_infiltration)
        self.lineEdit__max_infilt.setObjectName(u"lineEdit__max_infilt")
        self.lineEdit__max_infilt.setMinimumSize(QSize(50, 20))
        self.lineEdit__max_infilt.setMaximumSize(QSize(70, 16777215))

        self.horizontalLayout_15.addWidget(self.lineEdit__max_infilt)


        self.horizontalLayout_20.addLayout(self.horizontalLayout_15)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer_4)

        self.buttonBox = QDialogButtonBox(Dialog_infiltration)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.horizontalLayout_20.addWidget(self.buttonBox)


        self.verticalLayout_14.addLayout(self.horizontalLayout_20)


        self.horizontalLayout_36.addLayout(self.verticalLayout_14)

        self.groupBox_help = QGroupBox(Dialog_infiltration)
        self.groupBox_help.setObjectName(u"groupBox_help")
        self.groupBox_help.setMinimumSize(QSize(250, 0))
        font4 = QFont()
        font4.setPointSize(9)
        self.groupBox_help.setFont(font4)
        self.groupBox_help.setAutoFillBackground(False)
        self.groupBox_help.setStyleSheet(u"QGroupBox{border:2px solid gray;border-radius:1px;margin-top: 1ex;}\n"
"QGroupBox::title{subcontrol-origin: margin;subcontrol-position:top center;padding:0 3px;}")
        self.groupBox_help.setTitle(u"Help")
        self.groupBox_help.setFlat(False)
        self.verticalLayout_13 = QVBoxLayout(self.groupBox_help)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.textBrowser_help = QTextBrowser(self.groupBox_help)
        self.textBrowser_help.setObjectName(u"textBrowser_help")
        self.textBrowser_help.setAutoFillBackground(True)
        self.textBrowser_help.setStyleSheet(u"background-color: rgb(240, 240, 240)")
        self.textBrowser_help.setFrameShape(QFrame.WinPanel)
        self.textBrowser_help.setFrameShadow(QFrame.Sunken)
        self.textBrowser_help.setLineWidth(0)
        self.textBrowser_help.setReadOnly(True)

        self.verticalLayout_13.addWidget(self.textBrowser_help)


        self.horizontalLayout_36.addWidget(self.groupBox_help)


        self.retranslateUi(Dialog_infiltration)
        self.buttonBox.accepted.connect(Dialog_infiltration.accept)
        self.buttonBox.rejected.connect(Dialog_infiltration.reject)

        QMetaObject.connectSlotsByName(Dialog_infiltration)
    # setupUi

    def retranslateUi(self, Dialog_infiltration):
        Dialog_infiltration.setWindowTitle(QCoreApplication.translate("Dialog_infiltration", u"Dialog_infiltration", None))
        self.groupBox_curve_number.setTitle(QCoreApplication.translate("Dialog_infiltration", u"Curve Number Method for Daily Database", None))
        self.label_cn_csv.setText(QCoreApplication.translate("Dialog_infiltration", u"Curve Number source table (.CSV)", None))
        self.toolButton_browse_cn_csv.setText(QCoreApplication.translate("Dialog_infiltration", u"...", None))
        self.groupBox_raster.setTitle(QCoreApplication.translate("Dialog_infiltration", u"Raster", None))
        self.label_cn_raster.setText(QCoreApplication.translate("Dialog_infiltration", u"CN parameters source (raster)", None))
        self.toolButton_browse_cn_raster.setText(QCoreApplication.translate("Dialog_infiltration", u"...", None))
        self.label_lu.setText(QCoreApplication.translate("Dialog_infiltration", u"LU Band:", None))
        self.lineEdit_lu.setText("")
        self.label_hsg.setText(QCoreApplication.translate("Dialog_infiltration", u"HSG Band:", None))
        self.lineEdit_hsg.setText("")
        self.label_elev.setText(QCoreApplication.translate("Dialog_infiltration", u"Hydrologic condition / Slope Cat. Band:", None))
        self.lineEdit_elev.setText("")
        self.checkBox_slope_cat.setText(QCoreApplication.translate("Dialog_infiltration", u"Slope Cat.", None))
        self.label_slope.setText(QCoreApplication.translate("Dialog_infiltration", u"Slope range:", None))
        self.lineEdit_slope.setText(QCoreApplication.translate("Dialog_infiltration", u"1,5,10,20", None))
        self.checkBox_adv_cn.setText(QCoreApplication.translate("Dialog_infiltration", u"Advanced Curve Number Tuning", None))
        self.groupBox_adv_cn.setTitle("")
        self.label_c.setText(QCoreApplication.translate("Dialog_infiltration", u"C", None))
        self.lineEdit_c.setText(QCoreApplication.translate("Dialog_infiltration", u"25400", None))
        self.label_b.setText(QCoreApplication.translate("Dialog_infiltration", u"B", None))
        self.lineEdit_b.setText(QCoreApplication.translate("Dialog_infiltration", u"0", None))
        self.label_y.setText(QCoreApplication.translate("Dialog_infiltration", u"y", None))
        self.lineEdit_y.setText(QCoreApplication.translate("Dialog_infiltration", u"0", None))
        self.label_a.setText(QCoreApplication.translate("Dialog_infiltration", u"A", None))
        self.lineEdit_a.setText(QCoreApplication.translate("Dialog_infiltration", u"0", None))
        self.label_landa.setText(QCoreApplication.translate("Dialog_infiltration", u"LANDA", None))
        self.lineEdit_landa.setText(QCoreApplication.translate("Dialog_infiltration", u"0.2", None))
        self.label_x.setText(QCoreApplication.translate("Dialog_infiltration", u"x", None))
        self.lineEdit_x.setText(QCoreApplication.translate("Dialog_infiltration", u"0", None))
        self.label_d.setText(QCoreApplication.translate("Dialog_infiltration", u"D", None))
        self.lineEdit_d.setText(QCoreApplication.translate("Dialog_infiltration", u"-254", None))
        self.label_advanced_cn_formula.setText(QCoreApplication.translate("Dialog_infiltration", u"S = A CN^x +B CN^y +C CN ^z + D ", None))
        self.label_z.setText(QCoreApplication.translate("Dialog_infiltration", u"z", None))
        self.lineEdit_z.setText(QCoreApplication.translate("Dialog_infiltration", u"-1", None))
        self.groupBox_corrected_cn.setTitle(QCoreApplication.translate("Dialog_infiltration", u"Use Corrected CN Values", None))
        self.label_advanced_cn_formula_2.setText(QCoreApplication.translate("Dialog_infiltration", u"CN2 = A CNi^2 +B CNi +C ", None))
        self.label_amc1.setText(QCoreApplication.translate("Dialog_infiltration", u"AMC1 Coeffs.:", None))
        self.label_amc1_a.setText(QCoreApplication.translate("Dialog_infiltration", u"A", None))
        self.lineEdit_amc1_a.setText(QCoreApplication.translate("Dialog_infiltration", u"0.0069", None))
        self.label_amc1_b.setText(QCoreApplication.translate("Dialog_infiltration", u"B", None))
        self.lineEdit_amc1_b.setText(QCoreApplication.translate("Dialog_infiltration", u"0.2575", None))
        self.label_amc1_c.setText(QCoreApplication.translate("Dialog_infiltration", u"C", None))
        self.lineEdit_amc1_c.setText(QCoreApplication.translate("Dialog_infiltration", u"0", None))
        self.label_amc3.setText(QCoreApplication.translate("Dialog_infiltration", u"AMC3 Coeffs.", None))
        self.label_amc3_a.setText(QCoreApplication.translate("Dialog_infiltration", u"A", None))
        self.lineEdit_amc3_a.setText(QCoreApplication.translate("Dialog_infiltration", u"-0.0086", None))
        self.label_amc3_b.setText(QCoreApplication.translate("Dialog_infiltration", u"B", None))
        self.lineEdit_amc3_b.setText(QCoreApplication.translate("Dialog_infiltration", u"1.8338", None))
        self.label_amc3_c.setText(QCoreApplication.translate("Dialog_infiltration", u"C", None))
        self.lineEdit_amc3_c.setText(QCoreApplication.translate("Dialog_infiltration", u"0", None))
        self.label_dormant_month.setText(QCoreApplication.translate("Dialog_infiltration", u"Dormant month", None))
        self.lineEdit_dormant_month.setText(QCoreApplication.translate("Dialog_infiltration", u"1,2,3,10,11,12", None))
        self.label_dormant_.setText(QCoreApplication.translate("Dialog_infiltration", u"Dormant threshold", None))
        self.label_dor_1.setText(QCoreApplication.translate("Dialog_infiltration", u"1:", None))
        self.lineEdit_dormant_1.setText(QCoreApplication.translate("Dialog_infiltration", u"12.7", None))
        self.label_dor_3.setText(QCoreApplication.translate("Dialog_infiltration", u"3:", None))
        self.lineEdit_dormant_3.setText(QCoreApplication.translate("Dialog_infiltration", u"27.9", None))
        self.label_growing.setText(QCoreApplication.translate("Dialog_infiltration", u"Growing threshold", None))
        self.label_grow_1.setText(QCoreApplication.translate("Dialog_infiltration", u"1:", None))
        self.lineEdit_grow_1.setText(QCoreApplication.translate("Dialog_infiltration", u"36.6", None))
        self.label_grow_3.setText(QCoreApplication.translate("Dialog_infiltration", u"3:", None))
        self.lineEdit_grow_3.setText(QCoreApplication.translate("Dialog_infiltration", u"53.3", None))
        self.label_average.setText(QCoreApplication.translate("Dialog_infiltration", u"Average threshold", None))
        self.comboBox_average.setItemText(0, QCoreApplication.translate("Dialog_infiltration", u"Yes", None))
        self.comboBox_average.setItemText(1, QCoreApplication.translate("Dialog_infiltration", u"No", None))

        self.checkBox_cn_value.setText("")
        self.label_cn_val.setText(QCoreApplication.translate("Dialog_infiltration", u"CN Value", None))
        self.lineEdit_CN_Val.setText("")
        self.groupBox_urban.setTitle(QCoreApplication.translate("Dialog_infiltration", u"Urban Infiltration", None))
        self.label_urban_zone_raster.setText(QCoreApplication.translate("Dialog_infiltration", u"Urban Zones Identifier (raster)", None))
        self.toolButton_browse_urban_zone_raster.setText(QCoreApplication.translate("Dialog_infiltration", u"...", None))
        self.checkBox_urban_cn_correction.setText(QCoreApplication.translate("Dialog_infiltration", u"Urban Composite Curve Number Correction", None))
        self.groupBox_urban_cn_correction.setTitle("")
        self.checkBox_cia_cn_composite.setText(QCoreApplication.translate("Dialog_infiltration", u"Connected Impervious area Composite CN correction", None))
        self.label_cn_urban_cia_raster.setText(QCoreApplication.translate("Dialog_infiltration", u"Connected Impervious Area % (raster)", None))
        self.toolButton_browse_cn_urban_cia_raster.setText(QCoreApplication.translate("Dialog_infiltration", u"...", None))
        self.checkBox_uncia_cn_composite.setText(QCoreApplication.translate("Dialog_infiltration", u"Unconnected Impervious area Composite CN correction", None))
        self.label_cn_urban_uncia_total_raster.setText(QCoreApplication.translate("Dialog_infiltration", u"Total Impervious Area % (raster)", None))
        self.toolButton_browse_cn_urban_uncia_total_raster.setText(QCoreApplication.translate("Dialog_infiltration", u"...", None))
        self.label_cn_urban_uncia_raster.setText(QCoreApplication.translate("Dialog_infiltration", u"Unconnected Impervious Area % (raster)", None))
        self.toolButton_browse_cn_urban_uncia_raster.setText(QCoreApplication.translate("Dialog_infiltration", u"...", None))
        self.checkBox_urban_cycle.setText(QCoreApplication.translate("Dialog_infiltration", u"Urban Cycle", None))
        self.label_max_infilt.setText(QCoreApplication.translate("Dialog_infiltration", u"Maximum Infiltration Threshold Value per Timestep", None))
        self.lineEdit__max_infilt.setText("")
        self.textBrowser_help.setHtml(QCoreApplication.translate("Dialog_infiltration", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.1pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
    # retranslateUi

