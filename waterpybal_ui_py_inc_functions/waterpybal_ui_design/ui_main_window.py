# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGroupBox, QHBoxLayout,
    QLabel, QLayout, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QStatusBar,
    QTextBrowser, QToolButton, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1114, 480)
        MainWindow.setMinimumSize(QSize(1100, 480))
        MainWindow.setMaximumSize(QSize(1500, 700))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_12 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setSizeConstraint(QLayout.SetMinimumSize)
        self.groupBox_newds = QGroupBox(self.centralwidget)
        self.groupBox_newds.setObjectName(u"groupBox_newds")
        self.groupBox_newds.setMinimumSize(QSize(310, 105))
        self.groupBox_newds.setMaximumSize(QSize(16777215, 156))
        font = QFont()
        font.setPointSize(9)
        self.groupBox_newds.setFont(font)
        self.groupBox_newds.setAutoFillBackground(False)
        self.groupBox_newds.setStyleSheet(u"QGroupBox{border:2px solid gray;border-radius:1px;margin-top: 1ex;}\n"
"QGroupBox::title{subcontrol-origin: margin;subcontrol-position:top center;padding:0 3px;}")
        self.groupBox_newds.setTitle(u"Create a new WaterPyBal dataset")
        self.groupBox_newds.setFlat(False)
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_newds)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_dataset_name = QLabel(self.groupBox_newds)
        self.label_dataset_name.setObjectName(u"label_dataset_name")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_dataset_name.sizePolicy().hasHeightForWidth())
        self.label_dataset_name.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(False)
        self.label_dataset_name.setFont(font1)

        self.horizontalLayout_10.addWidget(self.label_dataset_name)

        self.lineEdit_name = QLineEdit(self.groupBox_newds)
        self.lineEdit_name.setObjectName(u"lineEdit_name")
        self.lineEdit_name.setMinimumSize(QSize(230, 22))
        font2 = QFont()
        font2.setPointSize(8)
        font2.setBold(False)
        self.lineEdit_name.setFont(font2)

        self.horizontalLayout_10.addWidget(self.lineEdit_name)


        self.verticalLayout_2.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_dataset_dir = QLabel(self.groupBox_newds)
        self.label_dataset_dir.setObjectName(u"label_dataset_dir")
        sizePolicy.setHeightForWidth(self.label_dataset_dir.sizePolicy().hasHeightForWidth())
        self.label_dataset_dir.setSizePolicy(sizePolicy)
        self.label_dataset_dir.setFont(font1)

        self.horizontalLayout_3.addWidget(self.label_dataset_dir)

        self.lineEdit_path = QLineEdit(self.groupBox_newds)
        self.lineEdit_path.setObjectName(u"lineEdit_path")
        self.lineEdit_path.setMinimumSize(QSize(230, 22))
        font3 = QFont()
        font3.setPointSize(7)
        font3.setBold(False)
        self.lineEdit_path.setFont(font3)

        self.horizontalLayout_3.addWidget(self.lineEdit_path)

        self.toolButton_path = QToolButton(self.groupBox_newds)
        self.toolButton_path.setObjectName(u"toolButton_path")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.toolButton_path.sizePolicy().hasHeightForWidth())
        self.toolButton_path.setSizePolicy(sizePolicy1)
        self.toolButton_path.setMaximumSize(QSize(20, 20))
        self.toolButton_path.setFont(font1)

        self.horizontalLayout_3.addWidget(self.toolButton_path)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton_to_lat_lon_time = QPushButton(self.groupBox_newds)
        self.pushButton_to_lat_lon_time.setObjectName(u"pushButton_to_lat_lon_time")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.pushButton_to_lat_lon_time.sizePolicy().hasHeightForWidth())
        self.pushButton_to_lat_lon_time.setSizePolicy(sizePolicy2)
        self.pushButton_to_lat_lon_time.setMinimumSize(QSize(150, 28))
        self.pushButton_to_lat_lon_time.setMaximumSize(QSize(16777215, 30))
        self.pushButton_to_lat_lon_time.setFont(font1)

        self.horizontalLayout.addWidget(self.pushButton_to_lat_lon_time)

        self.label_to_lat_lon_time = QLabel(self.groupBox_newds)
        self.label_to_lat_lon_time.setObjectName(u"label_to_lat_lon_time")
        self.label_to_lat_lon_time.setEnabled(True)
        self.label_to_lat_lon_time.setMinimumSize(QSize(60, 0))
        self.label_to_lat_lon_time.setMaximumSize(QSize(70, 20))
        font4 = QFont()
        font4.setPointSize(8)
        font4.setBold(True)
        font4.setItalic(True)
        self.label_to_lat_lon_time.setFont(font4)
        self.label_to_lat_lon_time.setFrameShape(QFrame.Box)
        self.label_to_lat_lon_time.setFrameShadow(QFrame.Plain)
        self.label_to_lat_lon_time.setLineWidth(0)
        self.label_to_lat_lon_time.setMidLineWidth(0)
        self.label_to_lat_lon_time.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label_to_lat_lon_time)


        self.verticalLayout_2.addLayout(self.horizontalLayout)


        self.horizontalLayout_9.addWidget(self.groupBox_newds)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.pushButton_open_dataset = QPushButton(self.centralwidget)
        self.pushButton_open_dataset.setObjectName(u"pushButton_open_dataset")
        sizePolicy3 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.pushButton_open_dataset.sizePolicy().hasHeightForWidth())
        self.pushButton_open_dataset.setSizePolicy(sizePolicy3)
        self.pushButton_open_dataset.setMinimumSize(QSize(100, 60))
        self.pushButton_open_dataset.setMaximumSize(QSize(150, 80))
        self.pushButton_open_dataset.setFont(font)

        self.verticalLayout.addWidget(self.pushButton_open_dataset)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)


        self.horizontalLayout_9.addLayout(self.verticalLayout)


        self.verticalLayout_3.addLayout(self.horizontalLayout_9)

        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_3.addWidget(self.line)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(15, 16777215))
        font5 = QFont()
        font5.setBold(False)
        self.label.setFont(font5)

        self.horizontalLayout_4.addWidget(self.label)

        self.pushButton_to_var_spat_interpol = QPushButton(self.centralwidget)
        self.pushButton_to_var_spat_interpol.setObjectName(u"pushButton_to_var_spat_interpol")
        sizePolicy2.setHeightForWidth(self.pushButton_to_var_spat_interpol.sizePolicy().hasHeightForWidth())
        self.pushButton_to_var_spat_interpol.setSizePolicy(sizePolicy2)
        self.pushButton_to_var_spat_interpol.setMinimumSize(QSize(280, 28))
        self.pushButton_to_var_spat_interpol.setMaximumSize(QSize(16777215, 30))
        font6 = QFont()
        font6.setPointSize(10)
        self.pushButton_to_var_spat_interpol.setFont(font6)
        self.pushButton_to_var_spat_interpol.setFlat(False)

        self.horizontalLayout_4.addWidget(self.pushButton_to_var_spat_interpol)

        self.label_to_var_spat_interpol = QLabel(self.centralwidget)
        self.label_to_var_spat_interpol.setObjectName(u"label_to_var_spat_interpol")
        self.label_to_var_spat_interpol.setMinimumSize(QSize(60, 0))
        self.label_to_var_spat_interpol.setMaximumSize(QSize(70, 20))
        font7 = QFont()
        font7.setBold(True)
        font7.setItalic(True)
        self.label_to_var_spat_interpol.setFont(font7)
        self.label_to_var_spat_interpol.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label_to_var_spat_interpol)


        self.verticalLayout_3.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(15, 16777215))
        self.label_2.setFont(font5)

        self.horizontalLayout_5.addWidget(self.label_2)

        self.pushButton_to_var_from_tiff = QPushButton(self.centralwidget)
        self.pushButton_to_var_from_tiff.setObjectName(u"pushButton_to_var_from_tiff")
        sizePolicy2.setHeightForWidth(self.pushButton_to_var_from_tiff.sizePolicy().hasHeightForWidth())
        self.pushButton_to_var_from_tiff.setSizePolicy(sizePolicy2)
        self.pushButton_to_var_from_tiff.setMinimumSize(QSize(280, 28))
        self.pushButton_to_var_from_tiff.setMaximumSize(QSize(16777215, 30))
        self.pushButton_to_var_from_tiff.setFont(font6)

        self.horizontalLayout_5.addWidget(self.pushButton_to_var_from_tiff)

        self.label_to_var_from_tiff = QLabel(self.centralwidget)
        self.label_to_var_from_tiff.setObjectName(u"label_to_var_from_tiff")
        self.label_to_var_from_tiff.setMinimumSize(QSize(60, 0))
        self.label_to_var_from_tiff.setMaximumSize(QSize(70, 20))
        self.label_to_var_from_tiff.setFont(font7)
        self.label_to_var_from_tiff.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.label_to_var_from_tiff)


        self.verticalLayout_3.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(15, 16777215))
        self.label_3.setFont(font5)

        self.horizontalLayout_6.addWidget(self.label_3)

        self.pushButton_to_swr = QPushButton(self.centralwidget)
        self.pushButton_to_swr.setObjectName(u"pushButton_to_swr")
        sizePolicy2.setHeightForWidth(self.pushButton_to_swr.sizePolicy().hasHeightForWidth())
        self.pushButton_to_swr.setSizePolicy(sizePolicy2)
        self.pushButton_to_swr.setMinimumSize(QSize(280, 28))
        self.pushButton_to_swr.setMaximumSize(QSize(16777215, 30))
        self.pushButton_to_swr.setFont(font6)

        self.horizontalLayout_6.addWidget(self.pushButton_to_swr)

        self.label_to_swr = QLabel(self.centralwidget)
        self.label_to_swr.setObjectName(u"label_to_swr")
        self.label_to_swr.setMinimumSize(QSize(60, 0))
        self.label_to_swr.setMaximumSize(QSize(70, 20))
        self.label_to_swr.setFont(font7)
        self.label_to_swr.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.label_to_swr)


        self.verticalLayout_3.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(15, 16777215))
        self.label_4.setFont(font5)

        self.horizontalLayout_7.addWidget(self.label_4)

        self.pushButton_to_etp = QPushButton(self.centralwidget)
        self.pushButton_to_etp.setObjectName(u"pushButton_to_etp")
        sizePolicy2.setHeightForWidth(self.pushButton_to_etp.sizePolicy().hasHeightForWidth())
        self.pushButton_to_etp.setSizePolicy(sizePolicy2)
        self.pushButton_to_etp.setMinimumSize(QSize(280, 28))
        self.pushButton_to_etp.setMaximumSize(QSize(16777215, 30))
        self.pushButton_to_etp.setFont(font6)

        self.horizontalLayout_7.addWidget(self.pushButton_to_etp)

        self.label_to_infiltration = QLabel(self.centralwidget)
        self.label_to_infiltration.setObjectName(u"label_to_infiltration")
        self.label_to_infiltration.setMinimumSize(QSize(60, 0))
        self.label_to_infiltration.setMaximumSize(QSize(70, 20))
        self.label_to_infiltration.setFont(font7)
        self.label_to_infiltration.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_7.addWidget(self.label_to_infiltration)


        self.verticalLayout_3.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(15, 16777215))
        self.label_5.setFont(font5)

        self.horizontalLayout_8.addWidget(self.label_5)

        self.pushButton_to_infiltration = QPushButton(self.centralwidget)
        self.pushButton_to_infiltration.setObjectName(u"pushButton_to_infiltration")
        sizePolicy2.setHeightForWidth(self.pushButton_to_infiltration.sizePolicy().hasHeightForWidth())
        self.pushButton_to_infiltration.setSizePolicy(sizePolicy2)
        self.pushButton_to_infiltration.setMinimumSize(QSize(280, 28))
        self.pushButton_to_infiltration.setMaximumSize(QSize(16777215, 30))
        self.pushButton_to_infiltration.setFont(font6)

        self.horizontalLayout_8.addWidget(self.pushButton_to_infiltration)

        self.label_to_etp = QLabel(self.centralwidget)
        self.label_to_etp.setObjectName(u"label_to_etp")
        self.label_to_etp.setMinimumSize(QSize(60, 0))
        self.label_to_etp.setMaximumSize(QSize(70, 20))
        self.label_to_etp.setFont(font7)
        self.label_to_etp.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_8.addWidget(self.label_to_etp)


        self.verticalLayout_3.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMaximumSize(QSize(15, 16777215))
        self.label_6.setFont(font5)

        self.horizontalLayout_11.addWidget(self.label_6)

        self.pushButton_to_Balance = QPushButton(self.centralwidget)
        self.pushButton_to_Balance.setObjectName(u"pushButton_to_Balance")
        sizePolicy2.setHeightForWidth(self.pushButton_to_Balance.sizePolicy().hasHeightForWidth())
        self.pushButton_to_Balance.setSizePolicy(sizePolicy2)
        self.pushButton_to_Balance.setMinimumSize(QSize(280, 25))
        self.pushButton_to_Balance.setMaximumSize(QSize(16777215, 25))
        self.pushButton_to_Balance.setFont(font6)

        self.horizontalLayout_11.addWidget(self.pushButton_to_Balance)

        self.label_to_Balance = QLabel(self.centralwidget)
        self.label_to_Balance.setObjectName(u"label_to_Balance")
        self.label_to_Balance.setMinimumSize(QSize(60, 0))
        self.label_to_Balance.setMaximumSize(QSize(70, 20))
        self.label_to_Balance.setFont(font7)
        self.label_to_Balance.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_11.addWidget(self.label_to_Balance)


        self.verticalLayout_3.addLayout(self.horizontalLayout_11)

        self.pushButton_to_visualization = QPushButton(self.centralwidget)
        self.pushButton_to_visualization.setObjectName(u"pushButton_to_visualization")
        sizePolicy2.setHeightForWidth(self.pushButton_to_visualization.sizePolicy().hasHeightForWidth())
        self.pushButton_to_visualization.setSizePolicy(sizePolicy2)
        self.pushButton_to_visualization.setMinimumSize(QSize(300, 28))
        self.pushButton_to_visualization.setMaximumSize(QSize(16777215, 30))
        self.pushButton_to_visualization.setFont(font6)

        self.verticalLayout_3.addWidget(self.pushButton_to_visualization)

        self.line_2 = QFrame(self.centralwidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_3.addWidget(self.line_2)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_2 = QSpacerItem(90, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.pushButton_save_dataset = QPushButton(self.centralwidget)
        self.pushButton_save_dataset.setObjectName(u"pushButton_save_dataset")
        self.pushButton_save_dataset.setMinimumSize(QSize(190, 28))
        self.pushButton_save_dataset.setMaximumSize(QSize(250, 30))
        self.pushButton_save_dataset.setFont(font6)

        self.horizontalLayout_2.addWidget(self.pushButton_save_dataset)

        self.horizontalSpacer_3 = QSpacerItem(90, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)


        self.horizontalLayout_12.addLayout(self.verticalLayout_3)

        self.groupBox_help = QGroupBox(self.centralwidget)
        self.groupBox_help.setObjectName(u"groupBox_help")
        self.groupBox_help.setMinimumSize(QSize(570, 450))
        self.groupBox_help.setFont(font)
        self.groupBox_help.setAutoFillBackground(False)
        self.groupBox_help.setStyleSheet(u"QGroupBox{border:2px solid gray;border-radius:1px;margin-top: 1ex;}\n"
"QGroupBox::title{subcontrol-origin: margin;subcontrol-position:top center;padding:0 3px;}")
        self.groupBox_help.setTitle(u"Help")
        self.groupBox_help.setFlat(False)
        self.verticalLayout_4 = QVBoxLayout(self.groupBox_help)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.textBrowser_help = QTextBrowser(self.groupBox_help)
        self.textBrowser_help.setObjectName(u"textBrowser_help")
        self.textBrowser_help.setMinimumSize(QSize(550, 375))
        self.textBrowser_help.setAutoFillBackground(True)
        self.textBrowser_help.setStyleSheet(u"background-color: rgb(240, 240, 240)")
        self.textBrowser_help.setFrameShape(QFrame.WinPanel)
        self.textBrowser_help.setFrameShadow(QFrame.Sunken)
        self.textBrowser_help.setLineWidth(0)
        self.textBrowser_help.setReadOnly(True)

        self.verticalLayout_4.addWidget(self.textBrowser_help)


        self.horizontalLayout_12.addWidget(self.groupBox_help)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
#if QT_CONFIG(shortcut)
        self.label_dataset_name.setBuddy(self.lineEdit_name)
        self.label_dataset_dir.setBuddy(self.lineEdit_path)
#endif // QT_CONFIG(shortcut)
        QWidget.setTabOrder(self.pushButton_to_var_spat_interpol, self.pushButton_to_var_from_tiff)
        QWidget.setTabOrder(self.pushButton_to_var_from_tiff, self.pushButton_to_swr)
        QWidget.setTabOrder(self.pushButton_to_swr, self.pushButton_to_visualization)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"WaterPyBal Interface Main Window", None))
        self.label_dataset_name.setText(QCoreApplication.translate("MainWindow", u"Dataset &name", None))
        self.label_dataset_dir.setText(QCoreApplication.translate("MainWindow", u"Dataset &path", None))
        self.toolButton_path.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.pushButton_to_lat_lon_time.setText(QCoreApplication.translate("MainWindow", u"New dataset properties ...", None))
        self.label_to_lat_lon_time.setText("")
        self.pushButton_open_dataset.setText(QCoreApplication.translate("MainWindow", u"Open an existing\n"
" WaterPyBal\n"
" dataset ...", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"1.", None))
        self.pushButton_to_var_spat_interpol.setText(QCoreApplication.translate("MainWindow", u"Variable introduction and spatial interpolation", None))
        self.label_to_var_spat_interpol.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"2.", None))
        self.pushButton_to_var_from_tiff.setText(QCoreApplication.translate("MainWindow", u"Import data from a tiff archive", None))
        self.label_to_var_from_tiff.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"3.", None))
        self.pushButton_to_swr.setText(QCoreApplication.translate("MainWindow", u"Soil Water Reserve Calculation", None))
        self.label_to_swr.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"4.", None))
        self.pushButton_to_etp.setText(QCoreApplication.translate("MainWindow", u"ETP Calculation", None))
        self.label_to_infiltration.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"5.", None))
        self.pushButton_to_infiltration.setText(QCoreApplication.translate("MainWindow", u"Infiltration Calculation", None))
        self.label_to_etp.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"6.", None))
        self.pushButton_to_Balance.setText(QCoreApplication.translate("MainWindow", u"Balance Calculation", None))
        self.label_to_Balance.setText("")
        self.pushButton_to_visualization.setText(QCoreApplication.translate("MainWindow", u"Visualization and outputs", None))
        self.pushButton_save_dataset.setText(QCoreApplication.translate("MainWindow", u"&Save and close WaterPyBal dataset", None))
        self.textBrowser_help.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.1pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
    # retranslateUi

