from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QFont, QPixmap
import sys
import edit_section
import freeway_window
import gui_test as primary

class Vehicle(QFrame):
    def __init__(self,parent=None):
        super(Vehicle, self).__init__(parent)
        self.parent_window = parent
        self.initUI()


    def initUI(self):
        self.setMinimumHeight(primary.height/22)
        self.setMinimumWidth(primary.width/65)
        self.setMaximumHeight(primary.height/22)
        self.setMaximumWidth(primary.width/65)
        self.setFrameStyle(1)







def main():
    primary.main()


if __name__ == "__main__":
    main()