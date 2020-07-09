from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont, QPixmap
import tkinter as tk
import sys

import gui_test as primary

class Intersection_Window(QMainWindow):
    def __init__(self,parent=None):
        super(Intersection_Window, self).__init__(parent)
        self.setGeometry(0,0,primary.width,primary.height)
        self.setWindowTitle("Intersection")
        self.initUI()


    def initUI(self):
        self.main_widget = QWidget()
        self.grid = QGridLayout()
        self.main_widget.setLayout(self.grid)
        self.setCentralWidget(self.main_widget)


        #back button
        self.back_button = QPushButton()
        self.back_button.setText("Back to Start")
        self.back_button.clicked.connect(self.back_to_start)


        #grid
        self.grid.addWidget(self.back_button)
    

    def back_to_start(self):
        self.new = primary.Start_Window()
        self.close()
        self.new.show()