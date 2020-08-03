from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QFont, QPixmap
import sys
import edit_section
import freeway_window
import gui_test as primary

class Vehicle(QLabel):
    def __init__(self,lane,lead,gap,model,r,g,b,parent=None):
        super(Vehicle, self).__init__(parent)
        self.parent_window = parent
        self.lane = lane
        self.lead = lead
        self.gap = gap
        self.model = model
        self.color_r = r
        self.color_g = g
        self.color_b = b
        self.initUI()


    def initUI(self):
        self.setMinimumHeight(primary.height/22)
        self.setMinimumWidth(primary.width/65)
        self.setMaximumHeight(primary.height/22)
        self.setMaximumWidth(primary.width/65)
        self.setAlignment(QtCore.Qt.AlignCenter)
        self.setFrameStyle(1)

        #calculate luminance
        luminance = 0.2126 * int(self.color_r) + 0.7152 * int(self.color_g) + 0.0722 * int(self.color_b)
        text_color = "white"
        if luminance > 128:
            text_color = "black"

        self.setFont(QFont("Arial",12))
        self.setStyleSheet("background:rgb({},{},{}); color:{};".format(self.color_r,self.color_g,self.color_b,text_color))
        

    clicked=pyqtSignal()
    def mouseReleaseEvent(self, ev):
        self.clicked.emit()





def main():
    primary.main()


if __name__ == "__main__":
    main()