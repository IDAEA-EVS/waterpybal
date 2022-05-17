import sys
from PyQt6.QtWidgets import QDialog,QApplication
from first_app_test import *

class Myapp(QDialog):
    def __init__(self):
        super().__init__()
        self.ui=Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.selectFile1)
        self.ui.pushButton_2.clicked.connect(self.selectFile2)
        self.show()

    def selectFile1(self):
        #print (QtWidgets.QFileDialog.getOpenFileName())
        self.ui.lineEdit.setText(QtWidgets.QFileDialog.getOpenFileName()[0])
    def selectFile2(self):
        #print (QtWidgets.QFileDialog.getOpenFileName())
        self.ui.lineEdit_3.setText(QtWidgets.QFileDialog.getOpenFileName()[0])
        
if __name__=="__main__":
    app=QApplication(sys.argv)
    w=Myapp()
    w.show()
    sys.exit(app.exec())


import sys
from PySide6.QtWidgets import QApplication, QPushButton
from PySide6.QtCore import QObject, Signal, Slot


class Communicate(QObject):
    # create two new signals on the fly: one will handle
    # int type, the other will handle strings
    speak = Signal((int,), (str,))

    def __init__(self, parent=None):
        super().__init__(self, parent)

        self.speak[int].connect(self.say_something)
        self.speak[str].connect(self.say_something)

    # define a new slot that receives a C 'int' or a 'str'
    # and has 'say_something' as its name
    @Slot(int)
    @Slot(str)
    def say_something(self, arg):
        if isinstance(arg, int):
            print("This is a number:", arg)
        elif isinstance(arg, str):
            print("This is a string:", arg)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    someone = Communicate()

    # emit 'speak' signal with different arguments.
    # we have to specify the str as int is the default
    someone.speak.emit(10)
    someone.speak[str].emit("Hello everybody!")