from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QFont, QPixmap
import freeway_window
import vehicle
import add_vehicles

import gui_test as primary

class Edit_Vehicle_Ego_Widget(QFrame):
    def __init__(self,parent=None):
        super(Edit_Vehicle_Ego_Widget, self).__init__(parent)
        self.parent_window = parent
        self.initUI()


    def initUI(self):
        self.grid = QGridLayout()
        self.setLayout(self.grid)
        self.grid.setContentsMargins(0,0,0,0)

        self.setFrameStyle(1)
        self.setAutoFillBackground(True)

        self.setMinimumWidth(primary.width/3.5)
        self.setMaximumHeight(primary.height)
        self.setMinimumHeight(primary.height)
        self.setMaximumWidth(primary.width/3.5)

        #close button
        self.close_button = QPushButton(self)
        self.close_button.move(primary.width/100,primary.height/100)
        self.close_button.setText("Close")
        self.close_button.setMaximumWidth(primary.width/15)
        self.close_button.clicked.connect(self.close)


        #title text
        self.title_text = QLabel()
        self.title_text.setText("Edit Ego Vehicle")
        self.title_text.setFont(QFont("Arial", 20))
        self.title_text.setMaximumHeight(primary.height/20)
        self.title_text.setAlignment(QtCore.Qt.AlignHCenter)
        #self.title_text.setStyleSheet("background-color: yellow;")


     
        #vehicle model
        self.vehicle_model_text = QLabel()
        self.vehicle_model_text.setText("Model")
        self.vehicle_model_text.setAlignment(QtCore.Qt.AlignCenter)

        self.vehicle_model = QComboBox()
        self.vehicle_model.setMaximumWidth(primary.width/6)
        self.vehicle_model.addItem("Tesla Model S")
        self.vehicle_model.addItem("Audi A2")
        


        #safety distance
        self.safety_distance_text = QLabel()
        self.safety_distance_text.setText("Safety Distance (m)")
        self.safety_distance_text.setAlignment(QtCore.Qt.AlignCenter)
        self.safety_distance_text.setMinimumWidth(primary.width/9)
        #self.safety_distance_text.setStyleSheet("background-color: red;")

        self.safety_distance = QTextEdit()
        self.safety_distance.setMaximumWidth(primary.width/30)
        self.safety_distance.setMaximumHeight(primary.height/30)
        self.safety_distance.setAlignment(QtCore.Qt.AlignCenter)
        self.safety_distance.setText("10")

        self.safety_distance_widget = QWidget()
        self.safety_distance_widget.setMaximumHeight(primary.height/10)

        self.temp_layout = QHBoxLayout()
        self.spacer_label = QLabel()
        self.spacer_label_2 = QLabel()

        self.safety_distance_widget.setLayout(self.temp_layout)

        self.temp_layout.addWidget(self.spacer_label)
        self.temp_layout.addWidget(self.safety_distance)
        self.temp_layout.addWidget(self.spacer_label_2)



        #vehicle color
        self.vehicle_color_text = QLabel()
        self.vehicle_color_text.setText("Color (RGB)")
        self.vehicle_color_text.setAlignment(QtCore.Qt.AlignCenter)

        self.vehicle_color = QWidget()
        self.horiz_layout = QHBoxLayout()
        self.vehicle_color.setLayout(self.horiz_layout)
        self.vehicle_color.setMaximumHeight(primary.height/12)

        self.vehicle_color_r = QTextEdit()
        self.vehicle_color_g = QTextEdit()
        self.vehicle_color_b = QTextEdit()

        self.vehicle_color_r.setAlignment(QtCore.Qt.AlignCenter)
        self.vehicle_color_g.setAlignment(QtCore.Qt.AlignCenter)
        self.vehicle_color_b.setAlignment(QtCore.Qt.AlignCenter)

        self.vehicle_color_r.setMaximumWidth(primary.width/30)
        self.vehicle_color_r.setMaximumHeight(primary.height/30)
        self.vehicle_color_g.setMaximumWidth(primary.width/30)
        self.vehicle_color_g.setMaximumHeight(primary.height/30)
        self.vehicle_color_b.setMaximumWidth(primary.width/30)
        self.vehicle_color_b.setMaximumHeight(primary.height/30)

        self.vehicle_color_r.setFont(QFont("Arial", 12))
        self.vehicle_color_g.setFont(QFont("Arial", 12))
        self.vehicle_color_b.setFont(QFont("Arial", 12))

        self.vehicle_color_r.setText("255")
        self.vehicle_color_g.setText("255")
        self.vehicle_color_b.setText("255")

        self.horiz_layout.addWidget(self.vehicle_color_r)
        self.horiz_layout.addWidget(self.vehicle_color_g)
        self.horiz_layout.addWidget(self.vehicle_color_b)


        #spacer
        self.spacer = QWidget()
        self.spacer.setMaximumHeight(primary.height/15)
        #self.spacer.setStyleSheet("background-color: red;")



        #GRID SETTINGS
        #self.grid.addWidget(self.close_button,             0,0,1,1)
        self.grid.addWidget(self.title_text,               1,0,1,2)
        self.grid.addWidget(self.vehicle_model_text,       2,0,1,1)
        self.grid.addWidget(self.vehicle_model,            2,1,1,1)
        self.grid.addWidget(self.safety_distance_text,     4,0,1,1)
        self.grid.addWidget(self.safety_distance_widget,   4,1,1,1)
        self.grid.addWidget(self.vehicle_color_text,       3,0,1,1)
        self.grid.addWidget(self.vehicle_color,            3,1,1,1)
        self.grid.addWidget(self.spacer,                   5,0,1,1)



        





    def close(self):
        self.hide()
        self.parent_window.hide()
        self.parent_window.show()









def main():
    primary.main()


if __name__ == "__main__":
    main()