import numpy as np
from PyQt6.QtWidgets import QMainWindow, QApplication
from PyQt6.QtCore import QEvent, Qt
from PyQt6 import QtCore
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
