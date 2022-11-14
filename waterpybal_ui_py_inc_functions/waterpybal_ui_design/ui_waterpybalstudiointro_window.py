# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'waterpybalstudiointro_window.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QHBoxLayout,
    QLabel, QPushButton, QSizePolicy, QSpacerItem,
    QTextBrowser, QVBoxLayout, QWidget)

class Ui_WaterPyBalStudio_intro(object):
    def setupUi(self, WaterPyBalStudio_intro):
        if not WaterPyBalStudio_intro.objectName():
            WaterPyBalStudio_intro.setObjectName(u"WaterPyBalStudio_intro")
        WaterPyBalStudio_intro.resize(1057, 615)
        WaterPyBalStudio_intro.setMinimumSize(QSize(1057, 615))
        self.widget = QWidget(WaterPyBalStudio_intro)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(20, 10, 1011, 602))
        self.horizontalLayout_2 = QHBoxLayout(self.widget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(400, 400))
        self.label.setMaximumSize(QSize(400, 400))
        self.label.setPixmap(QPixmap(u"../cat.jpg"))

        self.verticalLayout.addWidget(self.label)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.pushButton = QPushButton(self.widget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(200, 35))
        self.pushButton.setMaximumSize(QSize(200, 35))

        self.horizontalLayout.addWidget(self.pushButton)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)


        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.textBrowser_help = QTextBrowser(self.widget)
        self.textBrowser_help.setObjectName(u"textBrowser_help")
        self.textBrowser_help.setMinimumSize(QSize(600, 600))
        self.textBrowser_help.setAutoFillBackground(True)
        self.textBrowser_help.setStyleSheet(u"background-color: rgb(240, 240, 240)")
        self.textBrowser_help.setFrameShape(QFrame.WinPanel)
        self.textBrowser_help.setFrameShadow(QFrame.Sunken)
        self.textBrowser_help.setLineWidth(0)
        self.textBrowser_help.setReadOnly(True)

        self.horizontalLayout_2.addWidget(self.textBrowser_help)


        self.retranslateUi(WaterPyBalStudio_intro)

        QMetaObject.connectSlotsByName(WaterPyBalStudio_intro)
    # setupUi

    def retranslateUi(self, WaterPyBalStudio_intro):
        WaterPyBalStudio_intro.setWindowTitle(QCoreApplication.translate("WaterPyBalStudio_intro", u"WaterPyBal Studio", None))
        self.label.setText("")
        self.pushButton.setText(QCoreApplication.translate("WaterPyBalStudio_intro", u"Enter WaterpyBal Studio", None))
        self.textBrowser_help.setHtml(QCoreApplication.translate("WaterPyBalStudio_intro", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.1pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:6px; margin-bottom:6px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
    # retranslateUi

