from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QFont, QPixmap
import tkinter as tk
import sys
import freeway_window

import gui_test as primary



class Edit_Section_Window(QWidget):
    def __init__(self,parent=None):
        super(Edit_Section_Window, self).__init__(parent)
        self.setGeometry(0,0,primary.width,primary.height)
        self.setWindowTitle("Edit")
        self.initUI()


    def initUI(self):
        self.grid = QGridLayout()
        self.setLayout(self.grid)


        #back button
        self.back_button = QPushButton()
        self.back_button.setText("Back to General Settings")
        self.back_button.setFont(QFont("Arial", 18))
        self.back_button.setMaximumWidth(primary.width/10)
        self.back_button.setMaximumHeight(primary.height/26)

        #label
        self.lab = QLabel()
        self.lab.setText("balls1")




        #GRID SETTINGS
        self.grid.addWidget(self.back_button,0,0,1,1)
        self.grid.addWidget(self.lab)





        

        




def main():
    primary.main()


if __name__ == "__main__":
    main()