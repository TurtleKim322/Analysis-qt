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
import qtawesome as qta
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

        fileToolBar = self.addToolBar('파일')
        self.fileAction = QAction(qta.icon('ei.folder-open',size=16,color='#fd0'),'&파일열기',self)
        self.trainAction = QAction(qta.icon('ei.file-new', size = 16, color ='#000000'),'&좌표 파일',self )
        self.mapclearAction = QAction(qta.icon('mdi.eraser', size = 16, color ='#FF75AE'),'&지도 지우기',self )
        self.fileAction.triggered.connect(self.file_open)
        self.trainAction.triggered.connect(self.train_open)
        self.mapclearAction.triggered.connect(self.map_clear)
        fileToolBar.addAction(self.fileAction)
        fileToolBar.addAction(self.trainAction)
        fileToolBar.addAction(self.mapclearAction)


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
    app.setStyle('Fusion')
    myWindow = WindowClass()
    myWindow.showMaximized()
    app.exec()
