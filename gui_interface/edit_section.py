from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QFont, QPixmap
import tkinter as tk
import sys
import freeway_window

import gui_test as primary



class Edit_Section_Window(QWidget):
    def __init__(self,val,freeway_window,parent=None):
        super(Edit_Section_Window, self).__init__(parent)
        self.setGeometry(0,0,primary.width,primary.height)
        self.section_index = val
        self.freeway_window = freeway_window
        self.initUI()


    def initUI(self):
        self.grid = QGridLayout()
        self.setLayout(self.grid)
        self.grid.setContentsMargins(0,0,0,0)


        #title text
        self.section_text = QLabel()
        self.section_text.setText("Edit Section {}".format(self.section_index+1))
        self.section_text.setAlignment(QtCore.Qt.AlignCenter)
        self.section_text.setSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        self.section_text.setFont(QFont("Arial", 24))
        #self.section_text.setStyleSheet("background-color: #cccac6;")
        self.section_text.setMaximumHeight(primary.height/6)
        self.section_text.setMaximumWidth(primary.width/5)


        #back button
        self.back_button = QPushButton()
        self.back_button.setText("Back")
        self.back_button.setFont(QFont("Arial", 16))
        self.back_button.setMaximumWidth(primary.width/10)
        self.back_button.setMaximumHeight(primary.height/26)
        self.back_button.clicked.connect(self.freeway_window.go_to_general_settings)



        #intersection id
        self.section_id_text = QLabel()
        self.section_id_text.setText("Section ID")
        self.section_id_text.setFont(QFont("Arial", 16))
        self.section_id_text.setMaximumHeight(primary.height/15)
        #self.section_id_text.setStyleSheet("background-color: #cccac6;")

        self.section_id = QComboBox()
        self.section_id.setFont(QFont("Arial", 16))
        self.section_id.setMaximumWidth(primary.width/6)
        self.section_id.addItem("Section {}".format(self.section_index+1))
        for i in range(0,int(self.freeway_window.num_sections.toPlainText())):
            if i == self.section_index:
                continue
            self.section_id.addItem("Section {}".format(i+1))
        self.section_id.currentIndexChanged.connect(self.go_to_page)
            



        #import settings
        self.import_settings_text = QLabel()
        self.import_settings_text.setText("Import Settings")
        self.import_settings_text.setFont(QFont("Arial", 16))
        #self.import_settings_text.setStyleSheet("background-color: #cccac6;")

        self.import_settings = QComboBox()



        #same as previous
        self.same_as_prev = QPushButton()
        self.same_as_prev.setText("Same as Previous")
        self.same_as_prev.setFont(QFont("Arial", 16))
        #self.same_as_prev.setStyleSheet("background-color: #cccac6;")


        #bottom spacer
        self.spacer = QLabel()
        #self.spacer.setStyleSheet("background-color: #cccac6;")
        self.spacer.setMaximumHeight(primary.height/4)



        #add vehicles
        self.add_vehicles = QPushButton()
        self.add_vehicles.setText("Add Vehicles")
        self.add_vehicles.setFont(QFont("Arial", 16))
        #self.add_vehicles.setStyleSheet("background-color: #cccac6;")



        #map widget
        self.map_widget = QWidget()
        self.map_widget.setMinimumWidth(primary.width/2.1)
        self.map_widget.setMinimumHeight(primary.height/2.5)
        #self.map_widget.setStyleSheet("background-color: yellow;")
        self.map_widget.setMaximumWidth(primary.width/5)


        #background color
        self.map_background = QLabel(self.map_widget)
        self.map_background.setStyleSheet("background-color: #cccac6;")
        self.map_background.setMinimumHeight(primary.height/1.41)
        self.map_background.setMinimumWidth(primary.width/7)
        self.map_background.move(primary.width/6.75,0)


        #map
        self.pixmap = QPixmap('road.gif')
        self.pixmap = self.pixmap.scaledToHeight(primary.height/1.5)

        self.map1 = QLabel(self.map_widget)
        self.map1.setPixmap(self.pixmap)
        self.map1.move( int(primary.width/6) , int(primary.height/50) )

        #right side spacer
        self.spacer2 = QLabel()
        #self.spacer2.setStyleSheet("background-color: green;")
        self.spacer2.setMaximumWidth(primary.width/5)




        #GRID SETTINGS
        self.grid.addWidget(self.back_button,             0,0,1,1)
        self.grid.addWidget(self.section_text,            1,0,1,2)
        self.grid.addWidget(self.section_id_text,         2,0,1,1)
        self.grid.addWidget(self.section_id,              2,1,1,1)
        self.grid.addWidget(self.import_settings_text,    3,0,1,1)
        self.grid.addWidget(self.import_settings,         3,1,1,1)
        self.grid.addWidget(self.same_as_prev,            4,0,1,1)
        self.grid.addWidget(self.spacer,                  5,0,1,1)
        self.grid.addWidget(self.add_vehicles,            6,0,1,1)


        self.grid.addWidget(self.map_widget,              1,2,6,1)
        self.grid.addWidget(self.spacer2,                 2,3,1,1)



        
        
    def go_to_page(self):
        next_page_index = int(self.section_id.currentText()[8:])
        self.freeway_window.go_to_page(next_page_index)



        




def main():
    primary.main()


if __name__ == "__main__":
    main()