# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'var_from_tiff.ui'
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
    QDialog, QDialogButtonBox, QHBoxLayout, QLabel,
    QLineEdit, QSizePolicy, QSpacerItem, QToolButton,
    QVBoxLayout, QWidget)

class Ui_Dialog_var_from_tiff(object):
    def setupUi(self, Dialog_var_from_tiff):
        if not Dialog_var_from_tiff.objectName():
            Dialog_var_from_tiff.setObjectName(u"Dialog_var_from_tiff")
        Dialog_var_from_tiff.resize(391, 200)
        Dialog_var_from_tiff.setMaximumSize(QSize(16777215, 200))
        self.verticalLayout = QVBoxLayout(Dialog_var_from_tiff)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_from_tiffs = QLabel(Dialog_var_from_tiff)
        self.label_from_tiffs.setObjectName(u"label_from_tiffs")
        font = QFont()
        font.setPointSize(10)
        self.label_from_tiffs.setFont(font)

        self.verticalLayout.addWidget(self.label_from_tiffs)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_var_path = QLabel(Dialog_var_from_tiff)
        self.label_var_path.setObjectName(u"label_var_path")
        self.label_var_path.setMinimumSize(QSize(70, 20))
        self.label_var_path.setFont(font)

        self.horizontalLayout_2.addWidget(self.label_var_path)

        self.lineEdit_var_path = QLineEdit(Dialog_var_from_tiff)
        self.lineEdit_var_path.setObjectName(u"lineEdit_var_path")
        self.lineEdit_var_path.setMinimumSize(QSize(150, 20))

        self.horizontalLayout_2.addWidget(self.lineEdit_var_path)

        self.toolButton = QToolButton(Dialog_var_from_tiff)
        self.toolButton.setObjectName(u"toolButton")
        self.toolButton.setMinimumSize(QSize(0, 20))
        self.toolButton.setMaximumSize(QSize(30, 20))

        self.horizontalLayout_2.addWidget(self.toolButton)


        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_var_name = QLabel(Dialog_var_from_tiff)
        self.label_var_name.setObjectName(u"label_var_name")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_var_name.sizePolicy().hasHeightForWidth())
        self.label_var_name.setSizePolicy(sizePolicy)
        self.label_var_name.setMinimumSize(QSize(70, 20))
        self.label_var_name.setFont(font)
        self.label_var_name.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.label_var_name)

        self.comboBox = QComboBox(Dialog_var_from_tiff)
        self.comboBox.setObjectName(u"comboBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy1)
        self.comboBox.setMinimumSize(QSize(50, 20))
        self.comboBox.setMaximumSize(QSize(90, 16777215))

        self.horizontalLayout.addWidget(self.comboBox)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.checkBox = QCheckBox(Dialog_var_from_tiff)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setFont(font)
        self.checkBox.setChecked(False)

        self.verticalLayout.addWidget(self.checkBox)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.buttonBox_from_tiff = QDialogButtonBox(Dialog_var_from_tiff)
        self.buttonBox_from_tiff.setObjectName(u"buttonBox_from_tiff")
        self.buttonBox_from_tiff.setOrientation(Qt.Horizontal)
        self.buttonBox_from_tiff.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox_from_tiff)


        self.retranslateUi(Dialog_var_from_tiff)
        self.buttonBox_from_tiff.accepted.connect(Dialog_var_from_tiff.accept)
        self.buttonBox_from_tiff.rejected.connect(Dialog_var_from_tiff.reject)

        QMetaObject.connectSlotsByName(Dialog_var_from_tiff)
    # setupUi

    def retranslateUi(self, Dialog_var_from_tiff):
        Dialog_var_from_tiff.setWindowTitle(QCoreApplication.translate("Dialog_var_from_tiff", u"Import data from TIFF archives", None))
        self.label_from_tiffs.setText(QCoreApplication.translate("Dialog_var_from_tiff", u"Introduce variables from single band tiffs:", None))
        self.label_var_path.setText(QCoreApplication.translate("Dialog_var_from_tiff", u"Folder path", None))
        self.toolButton.setText(QCoreApplication.translate("Dialog_var_from_tiff", u"...", None))
        self.label_var_name.setText(QCoreApplication.translate("Dialog_var_from_tiff", u"Variable name", None))
        self.checkBox.setText(QCoreApplication.translate("Dialog_var_from_tiff", u"In case time interval of .CSV is not the same as the Database, Use the \n"
"same values for valid time steps(EX: Temp. vs accumulated precipitation)", None))
    # retranslateUi

