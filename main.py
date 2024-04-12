import numpy as np
from PyQt6.QtWidgets import QMainWindow, QApplication
from PyQt6.QtCore import QEvent, Qt
from PyQt6 import QtCore
from PyQt6 import QtWidgets, QtGui
from PyQt6.QtWidgets import QApplication, QMainWindow, QTreeWidget, QTreeWidgetItem, QMenu
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtGui import QIcon,QAction
import pandas as pd
from datetime import datetime, timedelta
from PyQt6.QtGui import QIcon,QAction
from PyQt6 import uic
import os, io,sys


currentdir = os.path.dirname(os.path.realpath(__file__))
ui_filename = '/'.join((currentdir, 'main_ui.ui'))

form_class = uic.loadUiType(ui_filename)[0]


class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.mdiArea.setViewMode(QMdiArea.ViewMode.SubWindowView)
        self.mdiArea.setTabPosition(QTabWidget.TabPosition.North)
        self.mdiArea.setTabsMovable(True)
        self.mdiArea.setTabsClosable(True)


    def closeEvent(self, event):
        result = QMessageBox.question(self, "Confirm Exit",
                                      "Are you sure you want to exit ?",
                                      QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                                      QMessageBox.StandardButton.No)
        if result == QMessageBox.StandardButton.Yes:
            event.accept()
        else:
            event.ignore()


if __name__ == "__main__" :
    app = QApplication(sys.argv)
    if 1 : 
        app.setStyle('Fusion')
    else :
        css ="""
         QToolTip {
                border: 1px solid darkkhaki;
                padding: 1px;
                border-radius: 1px;
                opacity: 200;
                color : white;
                }
            QMenuBar::item {
                padding: 10px 4px;
                background: transparent;
                border-radius: 4px;
            }
            /*
            QMenu::icon {
                padding-left: 20px;
            }
            */
            QMenu::item {
                padding-left: 30px;
            }
        """
    myWindow = WindowClass()
    myWindow.showMaximized()
    app.exec()
