from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QFont, QPixmap
import tkinter as tk
import sys
import edit_section

import gui_test as primary

class ExtendedQLabel(QLabel):
    def __init__(self, parent):
        QLabel.__init__(self, parent)

    clicked=pyqtSignal()
    def mouseReleaseEvent(self, ev):
        self.clicked.emit()


class Page(QWidget):
    def __init__(self,parent):
        super(Page, self).__init__(parent)
        self.setGeometry(0,0,primary.width,primary.height)




class Freeway_Window(QMainWindow):
    def __init__(self,parent=None):
        super(Freeway_Window, self).__init__(parent)
        self.setGeometry(0,0,primary.width,primary.height)
        self.setWindowTitle("Freeway")
        self.initUI()


    def initUI(self):
        """
        self.main_widget = QWidget() #widget for general settings page
        self.grid = QGridLayout() #set grid to layout for general settings
        self.main_widget.setLayout(self.grid)
        self.setCentralWidget(self.main_widget) #set freeway window central_widget to main_widget
        """

        self.stack = QStackedLayout()
        self.main_widget = QWidget()
        self.main_widget.setLayout(self.stack)
        self.setCentralWidget(self.main_widget)

        self.general_settings_widget = QWidget()
        self.grid = QGridLayout()
        self.general_settings_widget.setLayout(self.grid)
        self.stack.addWidget(self.general_settings_widget)

        self.new = edit_section.Edit_Section_Window()
        self.new2 = edit_section.Edit_Section_Window()

        self.list1 = list()
        for i in range(0,10):
            new = edit_section.Edit_Section_Window()
            self.list1.append(new)
            self.stack.addWidget(self.list1[i])

        

        #back button
        self.back_button = QPushButton()
        self.back_button.setText("Back to Start")
        self.back_button.clicked.connect(self.back_to_start)
        self.back_button.setFont(QFont("Arial", 18))
        self.back_button.setMaximumWidth(primary.width/10)
        self.back_button.setMaximumHeight(primary.height/26)


        #General Settings text
        self.general_settings = QLabel()
        self.general_settings.setText("General Settings")
        self.general_settings.setFont(QFont("Arial", 24))
        self.general_settings.setAlignment(QtCore.Qt.AlignCenter)
        self.general_settings.setMaximumHeight(primary.height/10)


        #Number of Freeway Sections
        self.num_sections_text = QLabel()
        self.num_sections_text.setText("Number of Freeway Sections")
        self.num_sections_text.setFont(QFont("Arial", 18))
        self.num_sections_text.setMinimumWidth(primary.width/4) #controls dist between input boxes and input text

        self.num_sections = QTextEdit()
        self.num_sections.setMaximumHeight(primary.height/20)
        self.num_sections.setMaximumWidth(primary.height/20)
        self.num_sections.setMinimumHeight(primary.height/20)
        self.num_sections.setMinimumWidth(primary.height/20)
        self.num_sections.setPlaceholderText("40")



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
        self.min_speed.setPlaceholderText("0")


        #Max Speed
        self.max_speed_text = QLabel()
        self.max_speed_text.setText("Maximum Speed (km/h)")
        self.max_speed_text.setFont(QFont("Arial", 18))

        self.max_speed = QTextEdit()
        self.max_speed.setMaximumHeight(primary.height/20)
        self.max_speed.setMaximumWidth(primary.height/20)
        self.max_speed.setMinimumHeight(primary.height/20)
        self.max_speed.setMinimumWidth(primary.height/20)
        self.max_speed.setPlaceholderText("100")


        #Section Distance
        self.section_distance_text = QLabel()
        self.section_distance_text.setText("Section Distance (km)")
        self.section_distance_text.setFont(QFont("Arial", 18))

        self.section_distance = QTextEdit()
        self.section_distance.setMaximumHeight(primary.height/20)
        self.section_distance.setMaximumWidth(primary.height/20)
        self.section_distance.setMinimumHeight(primary.height/20)
        self.section_distance.setMinimumWidth(primary.height/20)
        self.section_distance.setPlaceholderText("1000")


        #Safety Distance
        self.safety_distance_text = QLabel()
        self.safety_distance_text.setText("Safety Distance (m)")
        self.safety_distance_text.setFont(QFont("Arial", 18))

        self.safety_distance = QTextEdit()
        self.safety_distance.setMaximumHeight(primary.height/20)
        self.safety_distance.setMaximumWidth(primary.height/20)
        self.safety_distance.setMinimumHeight(primary.height/20)
        self.safety_distance.setMinimumWidth(primary.height/20)
        self.safety_distance.setPlaceholderText("10")


        #Edit Simulation
        self.edit_simulation = QPushButton()
        self.edit_simulation.setText("Edit Simulation")
        self.edit_simulation.setFont(QFont("Arial", 14))
        self.edit_simulation.setMaximumWidth(primary.width/6)
        self.edit_simulation.setMinimumHeight(primary.height/25)
        self.edit_simulation.clicked.connect(self.go_to_edit_section)



        #Start Simulation
        self.start_simulation = QPushButton()
        self.start_simulation.setText("Start Simulation")
        self.start_simulation.setFont(QFont("Arial", 14))
        self.start_simulation.setMaximumWidth(primary.width/6)
        self.start_simulation.setMinimumHeight(primary.height/25)



        #Map Images

            #widget
        self.map_widget = QWidget()
        self.map_widget.setMinimumWidth(primary.width/2.1)
        self.map_widget.setMinimumHeight(primary.height/2.5)

            #background color
        self.map_background = QLabel(self.map_widget)
        self.map_background.setStyleSheet("background-color: #cccac6;")
        self.map_background.setMinimumHeight(primary.height/2.25)
        self.map_background.setMinimumWidth(primary.width/2.75)

            #maps
        self.pixmap = QPixmap('road.gif')
        self.pixmap = self.pixmap.scaledToHeight(primary.height/2.5)

        self.map1 = QLabel(self.map_widget)
        self.map1.setPixmap(self.pixmap)
        self.map2 = QLabel(self.map_widget)
        self.map2.setPixmap(self.pixmap)
        self.map3 = QLabel(self.map_widget)
        self.map3.setPixmap(self.pixmap)
        self.map4 = QLabel(self.map_widget)
        self.map4.setPixmap(self.pixmap)
        self.map5 = QLabel(self.map_widget)
        self.map5.setPixmap(self.pixmap)

            #arrows
        self.arrow_pixmap = QPixmap('next.png')
        self.arrow_pixmap = self.arrow_pixmap.scaledToHeight(primary.height/12)
        self.arrow_pixmap_left = self.arrow_pixmap.transformed(QtGui.QTransform().scale(-1,1))
        self.double_arrow_pixmap = QPixmap('double_next.png')
        self.double_arrow_pixmap = self.double_arrow_pixmap.scaledToHeight(primary.height/12)
        self.double_arrow_pixmap_left = self.double_arrow_pixmap.transformed(QtGui.QTransform().scale(-1,1))

        self.right_arrow = ExtendedQLabel(self.map_widget)
        self.right_arrow.setPixmap(self.arrow_pixmap)
        self.right_arrow.clicked.connect(self.single_right)
        self.double_arrow_right = ExtendedQLabel(self.map_widget)
        self.double_arrow_right.setPixmap(self.double_arrow_pixmap)
        self.double_arrow_right.clicked.connect(self.double_right)

        self.left_arrow = ExtendedQLabel(self.map_widget)
        self.left_arrow.setPixmap(self.arrow_pixmap_left)
        self.left_arrow.clicked.connect(self.single_left)
        self.double_arrow_left = ExtendedQLabel(self.map_widget)
        self.double_arrow_left.setPixmap(self.double_arrow_pixmap_left)
        self.double_arrow_left.clicked.connect(self.double_left)


            #road buttons
        self.road_array = [1,2,3,4,5]

        self.road_button1 = QPushButton(self.map_widget)
        self.road_button1.setMaximumWidth(primary.width/40)
        self.road_button1.setStyleSheet("background-color: orange;") 
        self.road_button1.setText(str(self.road_array[0]))

        self.road_button2 = QPushButton(self.map_widget)
        self.road_button2.setMaximumWidth(primary.width/40)
        self.road_button2.setStyleSheet("background-color: orange;") 
        self.road_button2.setText(str(self.road_array[1]))

        self.road_button3 = QPushButton(self.map_widget)
        self.road_button3.setMaximumWidth(primary.width/40)
        self.road_button3.setStyleSheet("background-color: orange;") 
        self.road_button3.setText(str(self.road_array[2]))

        self.road_button4 = QPushButton(self.map_widget)
        self.road_button4.setMaximumWidth(primary.width/40)
        self.road_button4.setStyleSheet("background-color: orange;") 
        self.road_button4.setText(str(self.road_array[3]))

        self.road_button5 = QPushButton(self.map_widget)
        self.road_button5.setMaximumWidth(primary.width/40)
        self.road_button5.setStyleSheet("background-color: orange;") 
        self.road_button5.setText(str(self.road_array[4]))






        #GRID SETTINGS

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
        self.grid.addWidget(self.min_speed,            4,1,1,1)
        self.grid.addWidget(self.max_speed,            5,1,1,1)
        self.grid.addWidget(self.section_distance,     6,1,1,1)
        self.grid.addWidget(self.safety_distance,      7,1,1,1)



            #map
        move_dist = (primary.width/12)
        self.grid.addWidget(self.map_widget,          2,2,-1,-1)
        self.map_background.move(primary.width/12,0)
        self.map1.move(move_dist*1.2,primary.height/40)
        self.map2.move(move_dist*2.0,primary.height/40)
        self.map3.move(move_dist*2.8,primary.height/40)
        self.map4.move(move_dist*3.6,primary.height/40)
        self.map5.move(move_dist*4.4,primary.height/40)

            #arrows
        self.right_arrow.move(primary.width/2.37,primary.height/6)
        self.left_arrow.move(primary.width/17.37, primary.height/6)
        self.double_arrow_right.move(primary.width/2.18,primary.height/6)
        self.double_arrow_left.move(primary.width/26.37, primary.height/6)


            #road buttons
        self.road_button1.move(primary.width/8.5,primary.height/5.1)
        self.road_button2.move(primary.width/5.4,primary.height/5.1)
        self.road_button3.move(primary.width/3.95,primary.height/5.1)
        self.road_button4.move(primary.width/3.15,primary.height/5.1)
        self.road_button5.move(primary.width/2.6,primary.height/5.1)






    def road_button_reset(self):
        self.road_button1.setText(str(self.road_array[0]))
        self.road_button2.setText(str(self.road_array[1]))
        self.road_button3.setText(str(self.road_array[2]))
        self.road_button4.setText(str(self.road_array[3]))
        self.road_button5.setText(str(self.road_array[4]))


    def single_left(self):
        if self.road_array[0] == 1:
            return
        
        self.road_array[0] -= 1
        self.road_array[1] -= 1
        self.road_array[2] -= 1
        self.road_array[3] -= 1
        self.road_array[4] -= 1
        self.road_button_reset()
        


    def single_right(self):
        if self.num_sections.toPlainText() == "":
            val = 40
        else:
            val = int(self.num_sections.toPlainText())

        if self.road_array[-1] == val:
            return

        self.road_array[0] += 1
        self.road_array[1] += 1
        self.road_array[2] += 1
        self.road_array[3] += 1
        self.road_array[4] += 1
        self.road_button_reset()

    def double_left(self):
        if self.road_array[0] == 1:
            return
        
        self.road_array[0] = 1
        self.road_array[1] = 2
        self.road_array[2] = 3
        self.road_array[3] = 4
        self.road_array[4] = 5
        self.road_button_reset()

    def double_right(self):
        if self.num_sections.toPlainText() == "":
            val = 40
        else:
            val = int(self.num_sections.toPlainText())

        if self.road_array[-1] == val:
            return
        
        self.road_array[0] = val-4
        self.road_array[1] = val-3
        self.road_array[2] = val-2
        self.road_array[3] = val-1
        self.road_array[4] = val
        self.road_button_reset()

    
    def back_to_start(self):
        self.new = primary.Start_Window()
        self.close()
        self.new.show()


    def go_to_edit_section(self):
        QtWidgets.QStackedLayout.setCurrentWidget(self.stack,self.list1[9])





def main():
    primary.main()

if __name__ == "__main__":
    main()