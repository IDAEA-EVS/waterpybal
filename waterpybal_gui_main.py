from waterpybal_ui_py_inc_functions.waterpybal_ui_py.waterpybalstudiointro_window import Ui_WaterPyBalStudio_intro
from waterpybal_ui_py_inc_functions.main_window_inc_functions import waterpybalMainwindow
from PyQt6 import QtWidgets,QtGui
import os
import sys
from gui_help.gui_help_load import loadhelp_intro
import qdarktheme

basedir = os.path.dirname(__file__)

class Ui_WaterPyBalStudio_intro_(QtWidgets.QDialog):

    def __init__(self):
        
        super().__init__()
        #self.setStyleSheet("background-color: white;")

        self.ui = Ui_WaterPyBalStudio_intro()
        self.ui.setupUi(self)

        stylesheet = qdarktheme.load_stylesheet("light")
        QtWidgets.QApplication.instance().setStyleSheet(stylesheet)


        self.show()
        ##############

        loadhelp_intro(self.ui,"intro_window_help.md")
        self.ui.label.setPixmap(QtGui.QPixmap("light_theme_2_resized.png"))
        #self.ui.textBrowser_help.setStyleSheet("border: 1px solid black; background-color: white;")     
        
        self.ui.radioButton_light.setChecked(True)
        self.ui.radioButton_light.toggled.connect(lambda: self.theme_activate("light"))
        self.ui.radioButton_dark.toggled.connect(lambda: self.theme_activate("dark"))
        self.ui.pushButton.clicked.connect(self.open_main_window)

    
    def theme_activate(self,theme):

        if theme=="light": self.ui.label.setPixmap(QtGui.QPixmap("light_theme_2_resized.png"))
        
        else: self.ui.label.setPixmap(QtGui.QPixmap("dark_theme_2_resized.png"))

        
        stylesheet = qdarktheme.load_stylesheet(theme)
        QtWidgets.QApplication.instance().setStyleSheet(stylesheet)



    def open_main_window(self):

        self.ui_main_win= waterpybalMainwindow()
        self.close()



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    app.setWindowIcon(QtGui.QIcon(os.path.join(basedir, 'waterpybal_studio_logo.ico')))
    application = Ui_WaterPyBalStudio_intro_()   
    app.exec()
