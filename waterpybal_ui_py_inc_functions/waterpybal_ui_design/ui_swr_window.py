# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'swr_window.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QCheckBox, QDialog,
    QDialogButtonBox, QFrame, QGroupBox, QHBoxLayout,
    QLabel, QLineEdit, QSizePolicy, QSpacerItem,
    QTextBrowser, QToolButton, QVBoxLayout, QWidget)

class Ui_Dialog_swr(object):
    def setupUi(self, Dialog_swr):
        if not Dialog_swr.objectName():
            Dialog_swr.setObjectName(u"Dialog_swr")
        Dialog_swr.resize(902, 241)
        Dialog_swr.setMinimumSize(QSize(600, 0))
        self.horizontalLayout_11 = QHBoxLayout(Dialog_swr)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.checkbox_ds_vals = QCheckBox(Dialog_swr)
        self.checkbox_ds_vals.setObjectName(u"checkbox_ds_vals")

        self.verticalLayout_3.addWidget(self.checkbox_ds_vals)

        self.verticalSpacer = QSpacerItem(20, 18, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.checkBox_raster = QCheckBox(Dialog_swr)
        self.checkBox_raster.setObjectName(u"checkBox_raster")

        self.verticalLayout_3.addWidget(self.checkBox_raster)

        self.groupBox_raster = QGroupBox(Dialog_swr)
        self.groupBox_raster.setObjectName(u"groupBox_raster")
        self.groupBox_raster.setCheckable(False)
        self.verticalLayout = QVBoxLayout(self.groupBox_raster)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_csv = QLabel(self.groupBox_raster)
        self.label_csv.setObjectName(u"label_csv")
        font = QFont()
        font.setPointSize(10)
        self.label_csv.setFont(font)

        self.horizontalLayout_5.addWidget(self.label_csv)

        self.lineEdit_csv = QLineEdit(self.groupBox_raster)
        self.lineEdit_csv.setObjectName(u"lineEdit_csv")
        self.lineEdit_csv.setMinimumSize(QSize(160, 20))

        self.horizontalLayout_5.addWidget(self.lineEdit_csv)

        self.toolButton_browse_csv = QToolButton(self.groupBox_raster)
        self.toolButton_browse_csv.setObjectName(u"toolButton_browse_csv")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolButton_browse_csv.sizePolicy().hasHeightForWidth())
        self.toolButton_browse_csv.setSizePolicy(sizePolicy)
        self.toolButton_browse_csv.setMaximumSize(QSize(20, 20))

        self.horizontalLayout_5.addWidget(self.toolButton_browse_csv)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_cc = QLabel(self.groupBox_raster)
        self.label_cc.setObjectName(u"label_cc")
        self.label_cc.setMinimumSize(QSize(60, 20))
        self.label_cc.setMaximumSize(QSize(100, 16777215))
        self.label_cc.setFont(font)

        self.horizontalLayout_2.addWidget(self.label_cc)

        self.lineEdit_cc = QLineEdit(self.groupBox_raster)
        self.lineEdit_cc.setObjectName(u"lineEdit_cc")
        self.lineEdit_cc.setMinimumSize(QSize(10, 20))
        self.lineEdit_cc.setMaximumSize(QSize(30, 16777215))

        self.horizontalLayout_2.addWidget(self.lineEdit_cc)


        self.horizontalLayout_8.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_pwp = QLabel(self.groupBox_raster)
        self.label_pwp.setObjectName(u"label_pwp")
        self.label_pwp.setMinimumSize(QSize(60, 20))
        self.label_pwp.setMaximumSize(QSize(100, 16777215))
        self.label_pwp.setFont(font)

        self.horizontalLayout.addWidget(self.label_pwp)

        self.lineEdit_pwp = QLineEdit(self.groupBox_raster)
        self.lineEdit_pwp.setObjectName(u"lineEdit_pwp")
        self.lineEdit_pwp.setMinimumSize(QSize(10, 20))
        self.lineEdit_pwp.setMaximumSize(QSize(30, 16777215))

        self.horizontalLayout.addWidget(self.lineEdit_pwp)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_rrt = QLabel(self.groupBox_raster)
        self.label_rrt.setObjectName(u"label_rrt")
        self.label_rrt.setMinimumSize(QSize(60, 20))
        self.label_rrt.setMaximumSize(QSize(100, 16777215))
        self.label_rrt.setFont(font)

        self.horizontalLayout_3.addWidget(self.label_rrt)

        self.lineEdit_rrt = QLineEdit(self.groupBox_raster)
        self.lineEdit_rrt.setObjectName(u"lineEdit_rrt")
        self.lineEdit_rrt.setMinimumSize(QSize(10, 20))
        self.lineEdit_rrt.setMaximumSize(QSize(30, 16777215))

        self.horizontalLayout_3.addWidget(self.lineEdit_rrt)


        self.horizontalLayout.addLayout(self.horizontalLayout_3)


        self.horizontalLayout_8.addLayout(self.horizontalLayout)


        self.verticalLayout.addLayout(self.horizontalLayout_8)


        self.verticalLayout_3.addWidget(self.groupBox_raster)

        self.verticalSpacer_2 = QSpacerItem(20, 18, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)

        self.groupBox_single_values = QGroupBox(Dialog_swr)
        self.groupBox_single_values.setObjectName(u"groupBox_single_values")
        self.groupBox_single_values.setEnabled(False)
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_single_values)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_cc_2 = QLabel(self.groupBox_single_values)
        self.label_cc_2.setObjectName(u"label_cc_2")
        self.label_cc_2.setMinimumSize(QSize(60, 20))
        self.label_cc_2.setMaximumSize(QSize(100, 16777215))
        self.label_cc_2.setFont(font)

        self.horizontalLayout_6.addWidget(self.label_cc_2)

        self.lineEdit_cc_val = QLineEdit(self.groupBox_single_values)
        self.lineEdit_cc_val.setObjectName(u"lineEdit_cc_val")
        self.lineEdit_cc_val.setMinimumSize(QSize(10, 20))
        self.lineEdit_cc_val.setMaximumSize(QSize(30, 16777215))

        self.horizontalLayout_6.addWidget(self.lineEdit_cc_val)


        self.horizontalLayout_9.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_pwp_2 = QLabel(self.groupBox_single_values)
        self.label_pwp_2.setObjectName(u"label_pwp_2")
        self.label_pwp_2.setMinimumSize(QSize(60, 20))
        self.label_pwp_2.setMaximumSize(QSize(100, 16777215))
        self.label_pwp_2.setFont(font)

        self.horizontalLayout_4.addWidget(self.label_pwp_2)

        self.lineEdit_pwp_val = QLineEdit(self.groupBox_single_values)
        self.lineEdit_pwp_val.setObjectName(u"lineEdit_pwp_val")
        self.lineEdit_pwp_val.setMinimumSize(QSize(10, 20))
        self.lineEdit_pwp_val.setMaximumSize(QSize(30, 16777215))

        self.horizontalLayout_4.addWidget(self.lineEdit_pwp_val)


        self.horizontalLayout_9.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_rrt_2 = QLabel(self.groupBox_single_values)
        self.label_rrt_2.setObjectName(u"label_rrt_2")
        self.label_rrt_2.setMinimumSize(QSize(60, 20))
        self.label_rrt_2.setMaximumSize(QSize(100, 16777215))
        self.label_rrt_2.setFont(font)

        self.horizontalLayout_7.addWidget(self.label_rrt_2)

        self.lineEdit_rrt_val = QLineEdit(self.groupBox_single_values)
        self.lineEdit_rrt_val.setObjectName(u"lineEdit_rrt_val")
        self.lineEdit_rrt_val.setMinimumSize(QSize(10, 20))
        self.lineEdit_rrt_val.setMaximumSize(QSize(30, 16777215))

        self.horizontalLayout_7.addWidget(self.lineEdit_rrt_val)


        self.horizontalLayout_9.addLayout(self.horizontalLayout_7)


        self.verticalLayout_2.addLayout(self.horizontalLayout_9)


        self.verticalLayout_3.addWidget(self.groupBox_single_values)

        self.buttonBox = QDialogButtonBox(Dialog_swr)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout_3.addWidget(self.buttonBox)


        self.horizontalLayout_11.addLayout(self.verticalLayout_3)

        self.groupBox_help = QGroupBox(Dialog_swr)
        self.groupBox_help.setObjectName(u"groupBox_help")
        self.groupBox_help.setMinimumSize(QSize(150, 0))
        font1 = QFont()
        font1.setPointSize(9)
        self.groupBox_help.setFont(font1)
        self.groupBox_help.setAutoFillBackground(False)
        self.groupBox_help.setStyleSheet(u"QGroupBox{border:2px solid gray;border-radius:1px;margin-top: 1ex;}\n"
"QGroupBox::title{subcontrol-origin: margin;subcontrol-position:top center;padding:0 3px;}")
        self.groupBox_help.setTitle(u"Help")
        self.groupBox_help.setFlat(False)
        self.horizontalLayout_10 = QHBoxLayout(self.groupBox_help)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.textBrowser_help = QTextBrowser(self.groupBox_help)
        self.textBrowser_help.setObjectName(u"textBrowser_help")
        self.textBrowser_help.setAutoFillBackground(True)
        self.textBrowser_help.setStyleSheet(u"background-color: rgb(240, 240, 240)")
        self.textBrowser_help.setFrameShape(QFrame.WinPanel)
        self.textBrowser_help.setFrameShadow(QFrame.Sunken)
        self.textBrowser_help.setLineWidth(0)
        self.textBrowser_help.setReadOnly(True)

        self.horizontalLayout_10.addWidget(self.textBrowser_help)


        self.horizontalLayout_11.addWidget(self.groupBox_help)


        self.retranslateUi(Dialog_swr)
        self.buttonBox.accepted.connect(Dialog_swr.accept)
        self.buttonBox.rejected.connect(Dialog_swr.reject)

        QMetaObject.connectSlotsByName(Dialog_swr)
    # setupUi

    def retranslateUi(self, Dialog_swr):
        Dialog_swr.setWindowTitle(QCoreApplication.translate("Dialog_swr", u"Soil Water Reserve Calculation", None))
        self.checkbox_ds_vals.setText(QCoreApplication.translate("Dialog_swr", u"Use the dataset CC, PWP & RRT values", None))
        self.checkBox_raster.setText(QCoreApplication.translate("Dialog_swr", u"Raster", None))
        self.groupBox_raster.setTitle("")
        self.label_csv.setText(QCoreApplication.translate("Dialog_swr", u"File path (raster)", None))
        self.toolButton_browse_csv.setText(QCoreApplication.translate("Dialog_swr", u"...", None))
        self.label_cc.setText(QCoreApplication.translate("Dialog_swr", u"CC Band", None))
        self.lineEdit_cc.setText("")
        self.label_pwp.setText(QCoreApplication.translate("Dialog_swr", u"PWP Band", None))
        self.lineEdit_pwp.setText("")
        self.label_rrt.setText(QCoreApplication.translate("Dialog_swr", u"RRT Band", None))
        self.lineEdit_rrt.setText("")
        self.groupBox_single_values.setTitle("")
        self.label_cc_2.setText(QCoreApplication.translate("Dialog_swr", u"CC Value", None))
        self.lineEdit_cc_val.setText("")
        self.label_pwp_2.setText(QCoreApplication.translate("Dialog_swr", u"PWP Value", None))
        self.lineEdit_pwp_val.setText("")
        self.label_rrt_2.setText(QCoreApplication.translate("Dialog_swr", u"RRT Value", None))
        self.lineEdit_rrt_val.setText("")
        self.textBrowser_help.setHtml(QCoreApplication.translate("Dialog_swr", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.1pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
    # retranslateUi

