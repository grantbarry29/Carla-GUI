from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QFont, QPixmap
import freeway_window
import vehicle
import add_vehicles
import edit_vehicle

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
        self.section_text.setText("Edit Freeway Section")
        self.section_text.setAlignment(QtCore.Qt.AlignCenter)
        self.section_text.setSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        self.section_text.setFont(QFont("Arial", 20))
        #self.section_text.setStyleSheet("background-color: #cccac6;")
        self.section_text.setMaximumHeight(primary.height/6)
        self.section_text.setMaximumWidth(primary.width/5)





        #back button
        self.back_button = QPushButton()
        self.back_button.setText("General Settings")
        self.back_button.setFont(QFont("Arial", 16))
        self.back_button.setMaximumWidth(primary.width/10)
        self.back_button.setMaximumHeight(primary.height/26)
        self.back_button.clicked.connect(self.freeway_window.go_to_general_settings)



        #intersection id
        self.section_id_text = QLabel()
        self.section_id_text.setText("Section ID")
        self.section_id_text.setFont(QFont("Arial", 16))
        self.section_id_text.setMaximumHeight(primary.height/15)
        self.section_id_text.setAlignment(QtCore.Qt.AlignCenter)
        #self.section_id_text.setStyleSheet("background-color: #cccac6;")

        self.section_id = QComboBox()
        self.section_id.setFont(QFont("Arial", 16))
        self.section_id.setMaximumWidth(primary.width/9)
        for i in range(0,self.freeway_window.num_sections.value()):
            self.section_id.addItem("Section {}".format(i+1))
        self.section_id.currentIndexChanged.connect(self.go_to_page)

        self.view2 = QtWidgets.QListView()
        self.view2.setLayoutMode(1)
        self.view2.setBatchSize(15)
        self.section_id.setView(self.view2)


            



        #import settings
        self.import_settings_button = QPushButton()
        self.import_settings_button.setText("Import Settings")
        self.import_settings_button.setFont(QFont("Arial", 16))
        

        self.import_settings = QComboBox()
        self.import_settings.setFont(QFont("Arial", 16))
        self.import_settings.addItem("Custom (Default)")
        for i in range(0,self.freeway_window.num_sections.value()):
            self.import_settings.addItem("Section {}".format(i+1))

        self.view3 = QtWidgets.QListView()
        self.view3.setLayoutMode(1)
        self.view3.setBatchSize(15)
        self.import_settings.setView(self.view3)
        



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
        self.map_background.move(primary.width/6,primary.height/200)
        self.map_layout = QHBoxLayout()
        self.map_background.setLayout(self.map_layout)

    
        #map
        self.pixmap = QPixmap('images/road.gif')
        self.pixmap = self.pixmap.scaledToHeight(primary.height/1.5)

        self.map1 = QLabel(self.map_widget)
        self.map1.setPixmap(self.pixmap)
        self.map_layout.addWidget(self.map1)
        self.map1.setAlignment(QtCore.Qt.AlignCenter)


        #ego vehicle
        self.ego_vehicle = vehicle.Vehicle(0,1,"","","222","180","55",self.map_background)
        self.ego_vehicle.setText("Ego")
        self.ego_vehicle.setFont(QFont("Arial", 10))
        self.ego_vehicle.move(self.map_background.width()/1.48,primary.height/3.06)
        self.ego_vehicle.clicked.connect(self.show_edit_ego_vehicle)



        #bottom spacer
        self.spacer = QLabel()
        self.spacer.setMaximumHeight(primary.height/8)
        #self.spacer.setStyleSheet("background-color: red;")



        #right side spacer
        self.spacer2 = QLabel()
        self.spacer2.setMaximumWidth(primary.width/3)
        self.spacer2.setMinimumWidth(primary.width/15)
        #self.spacer2.setStyleSheet("background-color: green;")




        #EDIT EGO VEHICLE WINDOW
        self.edit_vehicle_window = edit_vehicle.Edit_Vehicle_Widget(self)
        self.edit_vehicle_window.hide()

        #EDIT VEHICLE WINDOWS
        self.edit_vehicle_list = list()



        #ADD VEHICLES


        #add vehicles button
        self.add_vehicles = QPushButton()
        self.add_vehicles.setText("Add Vehicles")
        self.add_vehicles.setFont(QFont("Arial", 16))
        self.add_vehicles.clicked.connect(self.freeway_window.show_add_vehicles)

        
        


        #GRID SETTINGS
        self.grid.addWidget(self.back_button,             0,0,1,1)
        self.grid.addWidget(self.section_text,            1,0,1,2)
        self.grid.addWidget(self.section_id_text,         2,0,1,1)
        self.grid.addWidget(self.section_id,              2,1,1,1)
        self.grid.addWidget(self.add_vehicles,            3,0,1,1)
        self.grid.addWidget(self.spacer,                  4,0,1,1)
        self.grid.addWidget(self.import_settings_button,  5,0,1,1)
        self.grid.addWidget(self.import_settings,         5,1,1,1) 
        


        self.grid.addWidget(self.map_widget,              1,2,5,1)
        self.grid.addWidget(self.spacer2,                 2,3,1,1)


        
    def go_to_page(self):
        next_page_index = int(self.section_id.currentText()[8:])
        self.freeway_window.go_to_page(next_page_index)

    def show_edit_ego_vehicle(self):
        self.freeway_window.edit_ego_vehicle.show()
        self.freeway_window.edit_ego_vehicle.raise_()







        




def main():
    primary.main()


if __name__ == "__main__":
    main()