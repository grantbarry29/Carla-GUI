from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QFont, QPixmap
import edit_section
import freeway_window
import gui_test as primary



class Drop_Down_Window_Add(QFrame):
    def __init__(self,parent=None):
        super(Drop_Down_Window_Add, self).__init__(parent)
        self.parent_window = parent
        self.initUI()


    def initUI(self):
        self.grid = QGridLayout()
        self.setLayout(self.grid)
        self.grid.setContentsMargins(0,0,0,0)

        self.setFrameStyle(1)
        self.setAutoFillBackground(True)

        self.setMinimumHeight(primary.height/3)
        self.setMinimumWidth(primary.width/8)
        self.setMaximumHeight(primary.height/3)
        self.setMaximumWidth(primary.width/8)

        #close button
        self.close_button = QPushButton()
        self.close_button.setText("Close")
        self.close_button.clicked.connect(self.close)

        #add button
        self.add_button = QPushButton()
        self.add_button.setText("Add")
        self.add_button.clicked.connect(self.parent_window.add_vehicle)


        #GRID SETTINGS
        self.grid.addWidget(self.close_button, 0,0,1,1)
        self.grid.addWidget(self.add_button, 0,1,1,1)



    def close(self):
        self.hide()
        self.parent_window.hide()
        self.parent_window.show()
        











def main():
    primary.main()


if __name__ == "__main__":
    main()