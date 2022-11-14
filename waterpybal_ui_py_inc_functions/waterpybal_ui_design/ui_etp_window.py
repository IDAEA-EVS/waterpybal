# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'etp_window.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QComboBox, QDialog,
    QDialogButtonBox, QFrame, QGroupBox, QHBoxLayout,
    QHeaderView, QLabel, QSizePolicy, QSpacerItem,
    QTableWidget, QTableWidgetItem, QTextBrowser, QVBoxLayout,
    QWidget)

class Ui_Dialog_etp(object):
    def setupUi(self, Dialog_etp):
        if not Dialog_etp.objectName():
            Dialog_etp.setObjectName(u"Dialog_etp")
        Dialog_etp.resize(591, 270)
        Dialog_etp.setMinimumSize(QSize(590, 270))
        self.horizontalLayout_2 = QHBoxLayout(Dialog_etp)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.label_method = QLabel(Dialog_etp)
        self.label_method.setObjectName(u"label_method")
        self.label_method.setMinimumSize(QSize(45, 20))
        self.label_method.setMaximumSize(QSize(70, 16777215))
        font = QFont()
        font.setPointSize(10)
        self.label_method.setFont(font)

        self.horizontalLayout.addWidget(self.label_method)

        self.comboBox_etp_method = QComboBox(Dialog_etp)
        self.comboBox_etp_method.setObjectName(u"comboBox_etp_method")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_etp_method.sizePolicy().hasHeightForWidth())
        self.comboBox_etp_method.setSizePolicy(sizePolicy)
        self.comboBox_etp_method.setMinimumSize(QSize(70, 20))
        self.comboBox_etp_method.setMaximumSize(QSize(360, 16777215))

        self.horizontalLayout.addWidget(self.comboBox_etp_method)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.tableWidget_etp_method_params = QTableWidget(Dialog_etp)
        if (self.tableWidget_etp_method_params.columnCount() < 3):
            self.tableWidget_etp_method_params.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget_etp_method_params.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget_etp_method_params.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget_etp_method_params.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.tableWidget_etp_method_params.setObjectName(u"tableWidget_etp_method_params")
        self.tableWidget_etp_method_params.setMinimumSize(QSize(300, 0))
        self.tableWidget_etp_method_params.setMaximumSize(QSize(500, 16777215))
        self.tableWidget_etp_method_params.horizontalHeader().setDefaultSectionSize(90)

        self.verticalLayout.addWidget(self.tableWidget_etp_method_params)

        self.buttonBox = QDialogButtonBox(Dialog_etp)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setMaximumSize(QSize(500, 16777215))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.groupBox_help = QGroupBox(Dialog_etp)
        self.groupBox_help.setObjectName(u"groupBox_help")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.groupBox_help.sizePolicy().hasHeightForWidth())
        self.groupBox_help.setSizePolicy(sizePolicy1)
        self.groupBox_help.setMinimumSize(QSize(150, 0))
        font1 = QFont()
        font1.setPointSize(9)
        self.groupBox_help.setFont(font1)
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


        self.horizontalLayout_2.addWidget(self.groupBox_help)


        self.retranslateUi(Dialog_etp)
        self.buttonBox.accepted.connect(Dialog_etp.accept)
        self.buttonBox.rejected.connect(Dialog_etp.reject)

        QMetaObject.connectSlotsByName(Dialog_etp)
    # setupUi

    def retranslateUi(self, Dialog_etp):
        Dialog_etp.setWindowTitle(QCoreApplication.translate("Dialog_etp", u"ETP Calculation", None))
        self.label_method.setText(QCoreApplication.translate("Dialog_etp", u"Method", None))
        ___qtablewidgetitem = self.tableWidget_etp_method_params.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Dialog_etp", u"Parameter", None));
        ___qtablewidgetitem1 = self.tableWidget_etp_method_params.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Dialog_etp", u"Type", None));
        ___qtablewidgetitem2 = self.tableWidget_etp_method_params.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Dialog_etp", u"Value or Path", None));
        self.textBrowser_help.setHtml(QCoreApplication.translate("Dialog_etp", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.1pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
    # retranslateUi

