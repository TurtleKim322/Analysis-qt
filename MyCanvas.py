from matplotlib import pyplot as plt
from matplotlib import animation
import numpy as np
import math
from matplotlib import ticker
import matplotlib.patches as patches
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from os.path import dirname, realpath, join
from PyQt6.QtGui import *
from os.path import dirname, realpath, join
import pandas as pd
from matplotlib.figure import Figure

class MplCanvas(FigureCanvas):
    def __init__(self, figure=None):
        self.fig = Figure()
        FigureCanvas.__init__(self, self.fig)

    def plot(self, x, y, x_label, y_label, title, legend):
        self.fig.clear()
        ax = self.fig.add_subplot(111)
        ax.set_xlabel(x_label)
        ax.set_ylabel(y_label)
        ax.set_title(title)
        ax.plot(x, y, label=legend)
        ax.legend()
        self.draw()
    
    def plot2(self, xarray, yarray):
        self.fig.clear()
        ax = self.fig.add_subplot(111)
        self.ax.scatter(xarray, yarray, color = 'b', marker = '.')
        self.ax.xaxis.set_major_locator(ticker.MultipleLocator(integers=True))
        self.ax.yaxis.set_major_locator(ticker.MultipleLocator(integers=True))
        self.ax.grid(True)
        self.ax.set_xlabel('x')
        self.ax.set_ylabel('y')
        self.draw()