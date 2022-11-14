from PyQt6 import QtCore
import os

def loadhelp(self, help_file_name):
    
    self.ui.textBrowser_help.setOpenExternalLinks(True)
    fileName = QtCore.QUrl(os.path.join("gui_help",help_file_name))
    self.ui.textBrowser_help.setSource(fileName)

def loadhelp_intro(self, help_file_name):
    
    self.textBrowser_help.setOpenExternalLinks(True)
    fileName = QtCore.QUrl(os.path.join("gui_help",help_file_name))
    self.textBrowser_help.setSource(fileName)
