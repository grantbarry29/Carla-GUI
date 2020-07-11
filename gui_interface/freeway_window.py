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
        self.setWindowTitle("Freeway")
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
        self.back_button.setFont(QFont("Arial", 18))


        #General Settings text
        self.general_settings = QLabel()
        self.general_settings.setText("General Settings")
        self.general_settings.setFont(QFont("Arial", 18))
        self.general_settings.setAlignment(QtCore.Qt.AlignCenter)


        #Number of Freeway Sections
        self.num_sections_text = QLabel()
        self.num_sections_text.setText("Number of Freeway Sections")
        self.num_sections_text.setFont(QFont("Arial", 18))

        self.num_sections = QTextEdit()
        self.num_sections.setMaximumHeight(primary.height/20)
        self.num_sections.setMaximumWidth(primary.height/20)
        self.num_sections.setMinimumHeight(primary.height/20)
        self.num_sections.setMinimumWidth(primary.height/20)


        #Allow Collisions
        self.allow_collisions_text = QLabel()
        self.allow_collisions_text.setText("Allow Collisions")
        self.allow_collisions_text.setFont(QFont("Arial", 18))

        self.allow_collisions = QCheckBox()
        self.allow_collisions.setMaximumHeight(primary.height/20)
        self.allow_collisions.setMaximumWidth(primary.height/20)
        self.allow_collisions.setMinimumHeight(primary.height/20)
        self.allow_collisions.setMinimumWidth(primary.height/20)


        #Min Speed
        self.min_speed_text = QLabel()
        self.min_speed_text.setText("Minimum Speed (km/h)")
        self.min_speed_text.setFont(QFont("Arial", 18))

        self.min_speed = QTextEdit()
        self.min_speed.setMaximumHeight(primary.height/20)
        self.min_speed.setMaximumWidth(primary.height/20)
        self.min_speed.setMinimumHeight(primary.height/20)
        self.min_speed.setMinimumWidth(primary.height/20)


        #Max Speed
        self.max_speed_text = QLabel()
        self.max_speed_text.setText("Maximum Speed (km/h)")
        self.max_speed_text.setFont(QFont("Arial", 18))

        self.max_speed = QTextEdit()
        self.max_speed.setMaximumHeight(primary.height/20)
        self.max_speed.setMaximumWidth(primary.height/20)
        self.max_speed.setMinimumHeight(primary.height/20)
        self.max_speed.setMinimumWidth(primary.height/20)


        #Section Distance
        self.section_distance_text = QLabel()
        self.section_distance_text.setText("Section Distance (km)")
        self.section_distance_text.setFont(QFont("Arial", 18))

        self.section_distance = QTextEdit()
        self.section_distance.setMaximumHeight(primary.height/20)
        self.section_distance.setMaximumWidth(primary.height/20)
        self.section_distance.setMinimumHeight(primary.height/20)
        self.section_distance.setMinimumWidth(primary.height/20)


        #Safety Distance
        self.safety_distance_text = QLabel()
        self.safety_distance_text.setText("Safety Distance (m)")
        self.safety_distance_text.setFont(QFont("Arial", 18))

        self.safety_distance = QTextEdit()
        self.safety_distance.setMaximumHeight(primary.height/20)
        self.safety_distance.setMaximumWidth(primary.height/20)
        self.safety_distance.setMinimumHeight(primary.height/20)
        self.safety_distance.setMinimumWidth(primary.height/20)


        #Edit Simulation
        self.edit_simulation = QPushButton()
        self.edit_simulation.setText("Edit Simulation")
        self.edit_simulation.setFont(QFont("Arial", 14))


        #Start Simulation
        self.start_simulation = QPushButton()
        self.start_simulation.setText("Edit Simulation")
        self.start_simulation.setFont(QFont("Arial", 14))


        #Map Images
        self.map_grid = QHBoxLayout()

        self.pixmap = QPixmap('road.gif')
        self.pixmap = self.pixmap.scaledToHeight(primary.height/2)

        self.map1 = QLabel()
        self.map1.setPixmap(self.pixmap)

        self.map2 = QLabel()
        self.map2.setPixmap(self.pixmap)

        self.map3 = QLabel()
        self.map3.setPixmap(self.pixmap)

        self.map4 = QLabel()
        self.map4.setPixmap(self.pixmap)

        self.map5 = QLabel()
        self.map5.setPixmap(self.pixmap)


        #Grid

            #labels and text
        self.grid.addWidget(self.back_button,          0,0,1,1)
        self.grid.addWidget(self.general_settings,     1,0,1,1)
        self.grid.addWidget(self.num_sections_text,    2,0,1,1)
        self.grid.addWidget(self.allow_collisions_text,3,0,1,1)
        self.grid.addWidget(self.min_speed_text,       4,0,1,1)
        self.grid.addWidget(self.max_speed_text,       5,0,1,1)
        self.grid.addWidget(self.section_distance_text,6,0,1,1)
        self.grid.addWidget(self.safety_distance_text, 7,0,1,1)
        self.grid.addWidget(self.edit_simulation,      8,0,1,1)
        self.grid.addWidget(self.start_simulation,     9,0,1,1)

            #input boxes
        self.grid.addWidget(self.num_sections,         2,1,1,1)
        self.grid.addWidget(self.allow_collisions,     3,1,1,1)
        self.grid.addWidget(self.max_speed,            4,1,1,1)
        self.grid.addWidget(self.section_distance,     5,1,1,1)
        self.grid.addWidget(self.safety_distance,      6,1,1,1)

            #map
        self.grid.addLayout(self.map_grid, 2,2,6,4)
        self.map_grid.addWidget(self.map1,                 0)
        self.map_grid.addWidget(self.map2,                 1)
        self.map_grid.addWidget(self.map3,                 2)
        self.map_grid.addWidget(self.map4,                 3)
        self.map_grid.addWidget(self.map5,                 4)




    
    def back_to_start(self):
        self.new = primary.Start_Window()
        self.close()
        self.new.show()



def main():
    primary.main()

if __name__ == "__main__":
    main()