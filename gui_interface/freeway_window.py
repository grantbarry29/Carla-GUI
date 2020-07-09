from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont, QPixmap
import tkinter as tk
import sys

import gui_test as primary

class Freeway_Window(QMainWindow):
    def __init__(self,parent=None):
        super(Freeway_Window, self).__init__(parent)
        self.setGeometry(0,0,primary.width,primary.height)
        self.setWindowTitle("PyQt_test")
        self.initUI()


    def initUI(self):
        self.main_widget = QWidget()
        self.grid = QGridLayout()
        self.main_widget.setLayout(self.grid)
        self.setCentralWidget(self.main_widget)