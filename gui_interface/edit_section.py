from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QFont, QPixmap
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
        self.section_text.setText("Edit Freeway Section")
        self.section_text.setAlignment(QtCore.Qt.AlignCenter)
        self.section_text.setSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        self.section_text.setFont(QFont("Arial", 24))
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
        #self.section_id_text.setStyleSheet("background-color: #cccac6;")

        self.section_id = QComboBox()
        self.section_id.setFont(QFont("Arial", 16))
        self.section_id.setMaximumWidth(primary.width/6)
        for i in range(0,int(self.freeway_window.num_sections.toPlainText())):
            self.section_id.addItem("Section {}".format(i+1))
        self.section_id.currentIndexChanged.connect(self.go_to_page)

            



        #import settings
        self.import_settings_text = QLabel()
        self.import_settings_text.setText("Import Settings")
        self.import_settings_text.setFont(QFont("Arial", 16))
        

        self.import_settings = QComboBox()
        self.import_settings.setFont(QFont("Arial", 16))
        self.import_settings.addItem("Custom (Default)")
        for i in range(0,int(self.freeway_window.num_sections.toPlainText())):
            self.import_settings.addItem("Section {}".format(i+1))





        #Edit vehicles
        self.edit_vehicles = QPushButton()
        self.edit_vehicles.setText("Edit Vehicle Behavior")
        self.edit_vehicles.setFont(QFont("Arial", 16))
        self.edit_vehicles.clicked.connect(self.edit_vehicles_clicked)
        #self.edit_vehicles.setStyleSheet("background-color: #cccac6;")



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


        #bottom spacer
        self.spacer = QLabel()
        self.spacer.setMaximumHeight(primary.height/3)
        #self.spacer.setStyleSheet("background-color: red;")


        #right side spacer
        self.spacer2 = QLabel()
        self.spacer2.setMaximumWidth(primary.width/3)
        self.spacer2.setMinimumWidth(primary.width/15)
        #self.spacer2.setStyleSheet("background-color: green;")




        #ADD VEHICLES

            #add vehicle widget
        
        self.edit_vehicles_widget = QWidget(self)
        self.edit_vehicles_widget.setHidden(True)

        self.edit_vehicles_widget.setMaximumHeight(primary.height/1.5)
        self.edit_vehicles_widget.setMinimumHeight(primary.height/1.5)
        self.edit_vehicles_widget.setMinimumWidth(primary.width/2.5)        
        self.edit_vehicles_widget.setMaximumWidth(primary.width/2.5)


            #background color
        self.background = QLabel(self.edit_vehicles_widget)
        self.background.setMinimumWidth(self.edit_vehicles_widget.width())
        self.background.setMinimumHeight(self.edit_vehicles_widget.height())
        self.background.setAutoFillBackground(True)


            #new back button
        self.edit_vehicles_back_button = QPushButton(self.edit_vehicles_widget)
        self.edit_vehicles_back_button.clicked.connect(self.hide_edit_vehicles)
        self.edit_vehicles_back_button.setText("Back to Section Choice")
        self.edit_vehicles_back_button.setFont(QFont("Arial", 16))
        self.edit_vehicles_back_button.move(primary.height/100,primary.width/100)

            #add vehicles title
        self.edit_vehicles_title = QLabel(self.edit_vehicles_widget)
        self.edit_vehicles_title.setText("Edit Vehicle Behavior")
        self.edit_vehicles_title.setFont(QFont("Arial", 20))
        self.edit_vehicles_title.move(primary.width/11,primary.height/10)

            #click on vehicle to edit
        self.edit_vehicle_label = QLabel(self.edit_vehicles_widget)
        self.edit_vehicle_label.setText("Click on a vehicle to edit...")
        self.edit_vehicle_label.setFont(QFont("Arial", 16))
        self.edit_vehicle_label.move(primary.width/30,primary.height/3)







        #GRID SETTINGS
        self.grid.addWidget(self.back_button,             0,0,1,1)
        self.grid.addWidget(self.section_text,            1,0,1,2)
        self.grid.addWidget(self.section_id_text,         2,0,1,1)
        self.grid.addWidget(self.section_id,              2,1,1,1)
        self.grid.addWidget(self.import_settings_text,    3,0,1,1)
        self.grid.addWidget(self.import_settings,         3,1,1,1)
        #self.grid.addWidget(self.same_as_prev,            4,0,1,1)
        self.grid.addWidget(self.edit_vehicles,            4,0,1,1)
        self.grid.addWidget(self.spacer,                  5,0,1,1)
        


        self.grid.addWidget(self.map_widget,              1,2,5,1)
        self.grid.addWidget(self.spacer2,                 2,3,1,1)



        
        
    def go_to_page(self):
        next_page_index = int(self.section_id.currentText()[8:])
        self.freeway_window.go_to_page(next_page_index)


    def edit_vehicles_clicked(self):
        self.edit_vehicles_widget.setHidden(False)
        self.edit_vehicles_widget.raise_()



    def hide_edit_vehicles(self):
        self.edit_vehicles_widget.hide()
        self.freeway_window.go_to_general_settings()
        self.go_to_page()



        



        




def main():
    primary.main()


if __name__ == "__main__":
    main()