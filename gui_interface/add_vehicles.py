from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QFont, QPixmap
import tkinter as tk
import sys
import freeway_window
import drop_down_window_add
import vehicle

import gui_test as primary



class Add_Vehicles_Window(QWidget):
    def __init__(self,freeway_window,parent=None):
        super(Add_Vehicles_Window, self).__init__(parent)
        self.setGeometry(0,0,primary.width,primary.height)
        self.freeway_window = freeway_window
        self.initUI()


    def initUI(self):
        self.grid = QGridLayout()
        self.setLayout(self.grid)
        self.grid.setContentsMargins(0,0,0,0)
        self.setAutoFillBackground(True)





        #back button
        self.back_button = QPushButton()
        self.back_button.setText("Back")
        self.back_button.setFont(QFont("Arial", 16))
        self.back_button.setMaximumWidth(primary.width/10)
        self.back_button.setMaximumHeight(primary.height/26)
        self.back_button.clicked.connect(self.freeway_window.hide_add_vehicles)




        #map widget
        self.map_widget = QWidget()
        self.map_widget.setMinimumWidth(primary.width/3)
        self.map_widget.setMaximumWidth(primary.width/3)
        self.map_widget.setMinimumHeight(primary.height/1.4)
        self.map_widget.setMaximumHeight(primary.height/1.4)
        #self.map_widget.setStyleSheet("background-color: yellow;")
        


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


        #ego vehicle
        self.ego_vehicle = vehicle.Vehicle(self.map_widget)
        self.ego_vehicle.setStyleSheet("background-color: #deb437;")
        self.ego_vehicle.move(primary.width/4.04,primary.height/3.1)




        #right side spacer
        self.spacer = QLabel()
        self.spacer.setMaximumHeight(primary.height/4)
        #self.spacer.setStyleSheet("background-color: yellow;")


        #bottom spacer
        self.spacer_bottom = QLabel()
        self.spacer_bottom.setMaximumWidth(primary.width/3)
        self.spacer_bottom.setMinimumWidth(primary.width/15)
        #self.spacer_bottom.setStyleSheet("background-color: green;")




        #ADD VEHICLES

        

            #add vehicle widget
        
        self.add_vehicles_widget = QWidget()


        self.add_vehicles_widget.setMaximumHeight(primary.height/1.5)
        self.add_vehicles_widget.setMinimumHeight(primary.height/1.5)
        self.add_vehicles_widget.setMinimumWidth(primary.width/2.5)        
        self.add_vehicles_widget.setMaximumWidth(primary.width/2.5)


            #background color
        self.background = QLabel(self.add_vehicles_widget)
        self.background.setMinimumWidth(self.add_vehicles_widget.width())
        self.background.setMinimumHeight(self.add_vehicles_widget.height())
        self.background.setAutoFillBackground(True)



            #add vehicles title
        self.add_vehicles_title = QLabel(self.add_vehicles_widget)
        self.add_vehicles_title.setText("Add Vehicles")
        self.add_vehicles_title.setFont(QFont("Arial", 20))
        self.add_vehicles_title.move(primary.width/11,primary.height/10)


            #subject lane
        self.subject_lane_text = QLabel(self.add_vehicles_widget)
        self.subject_lane_text.setText("Subject Lane")
        self.subject_lane_text.setFont(QFont("Arial",18))
        self.subject_lane_text.setStyleSheet("border: 0.5px solid black;") 
        self.subject_lane_text.move(primary.width/25,primary.height/4.9)

                #add vehicle
        self.subject_lane_add_vehicle = QPushButton(self.add_vehicles_widget)
        self.subject_lane_add_vehicle.setText("Add Vehicle")
        self.subject_lane_add_vehicle.setFont(QFont("Arial",16))
        self.subject_lane_add_vehicle.setMinimumWidth(primary.width/10)
        self.subject_lane_add_vehicle.move(primary.width/6,primary.height/5)
        self.subject_lane_add_vehicle.clicked.connect(self.add_vehicle_subject_lane_click)

                #edit lane
        self.subject_lane_edit_lane = QPushButton(self.add_vehicles_widget)
        self.subject_lane_edit_lane.setText("Edit Lane")
        self.subject_lane_edit_lane.setFont(QFont("Arial",16))
        self.subject_lane_edit_lane.setMinimumWidth(primary.width/10)
        self.subject_lane_edit_lane.move(primary.width/6,primary.height/4)



            #left lane
        self.left_lane_text = QLabel(self.add_vehicles_widget)
        self.left_lane_text.setText("Left Lane")
        self.left_lane_text.setFont(QFont("Arial",18))
        self.left_lane_text.setStyleSheet("border: 0.5px solid black;") 
        self.left_lane_text.move(primary.width/25,primary.height/2.5)


                #add vehicle
        self.left_lane_add_vehicle = QPushButton(self.add_vehicles_widget)
        self.left_lane_add_vehicle.setText("Add Vehicle")
        self.left_lane_add_vehicle.setFont(QFont("Arial",16))
        self.left_lane_add_vehicle.setMinimumWidth(primary.width/10)
        self.left_lane_add_vehicle.move(primary.width/6,primary.height/2.5)
        self.left_lane_add_vehicle.clicked.connect(self.add_vehicle_left_lane_click)

                #edit lane
        self.left_lane_edit_lane = QPushButton(self.add_vehicles_widget)
        self.left_lane_edit_lane.setText("Edit Lane")
        self.left_lane_edit_lane.setFont(QFont("Arial",16))
        self.left_lane_edit_lane.setMinimumWidth(primary.width/10)
        self.left_lane_edit_lane.move(primary.width/6,primary.height/2.2)






        #GRID SETTINGS
        self.grid.addWidget(self.back_button,             0,0,1,1)
        self.grid.addWidget(self.add_vehicles_widget,     1,0,1,1)
        self.grid.addWidget(self.spacer,                  1,2,-1,-1)
        self.grid.addWidget(self.spacer_bottom,           2,1,-1,-1)
        self.grid.addWidget(self.map_widget,              1,1,-1,-1)
        
    



    def add_vehicles_clicked(self):
        self.add_vehicles_widget.setHidden(False)
        self.add_vehicles_widget.raise_()


    def hide_add_vehicles(self):
        self.add_vehicles_widget.hide()
        self.freeway_window.go_to_general_settings()
        self.go_to_page()

    def add_vehicle_subject_lane_click(self):
        self.small_widget = drop_down_window_add.Drop_Down_Window_Add(self)

        self.small_widget.show()
        self.small_widget.move(primary.width/6,primary.height/4)


    def add_vehicle_left_lane_click(self):
        self.small_widget = drop_down_window_add.Drop_Down_Window_Add(self)

        self.small_widget.show()
        self.small_widget.move(primary.width/6,primary.height/2.5)





    def add_vehicle(self):
        self.car = vehicle.Vehicle(self)
        self.car.setStyleSheet("background-color: red;")


        self.car.move(400,200)

        self.car.show()

        



        




def main():
    primary.main()


if __name__ == "__main__":
    main()