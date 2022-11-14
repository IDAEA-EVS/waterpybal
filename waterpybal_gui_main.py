from waterpybal_ui_py_inc_functions.waterpybal_ui_py.waterpybalstudiointro_window import Ui_WaterPyBalStudio_intro
from waterpybal_ui_py_inc_functions.main_window_inc_functions import waterpybalMainwindow
from PyQt6 import QtWidgets,QtGui
import os
import sys
from gui_help.gui_help_load import loadhelp_intro
basedir = os.path.dirname(__file__)

class Ui_WaterPyBalStudio_intro_(QtWidgets.QDialog):

    def __init__(self):
        
        super().__init__()

        self.ui = Ui_WaterPyBalStudio_intro()
        
        self.ui.setupUi(self)
        self.show()
        ##############

        loadhelp_intro(self.ui,"intro_window_help.md")
        self.ui.label.setPixmap(QtGui.QPixmap("7_resized.png"))

        self.ui.pushButton.clicked.connect(self.open_main_window)

        

    def open_main_window(self):

        self.ui_main_win= waterpybalMainwindow()
        self.close()



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    app.setWindowIcon(QtGui.QIcon(os.path.join(basedir, '8.ico')))
    application = Ui_WaterPyBalStudio_intro_()   
    app.exec()
