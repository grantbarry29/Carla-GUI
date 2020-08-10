from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QFont, QPixmap
import freeway_window
import vehicle
import add_vehicles

import gui_test as primary

class Edit_Vehicle_Widget(QFrame):
    def __init__(self,car_index,parent=None):
        super(Edit_Vehicle_Widget, self).__init__(parent)
        self.parent_window = parent
        self.car_index = car_index
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
        self.close_button = QPushButton()
        self.close_button.setText("Close")
        self.close_button.setMaximumWidth(primary.width/15)
        self.close_button.clicked.connect(self.close)


        #title text
        self.title_text = QLabel()
        self.title_text.setText("Edit Vehicle {}".format(self.car_index))
        self.title_text.setFont(QFont("Arial", 20))
        self.title_text.setMaximumHeight(primary.height/20)
        self.title_text.setAlignment(QtCore.Qt.AlignHCenter)
        #self.title_text.setStyleSheet("background-color: yellow;")


        #vary speed by range
        self.vary_speed_range_text = QLabel()
        self.vary_speed_range_text.setText("Vary Speed by Range")
        self.vary_speed_range_text.setMaximumHeight(primary.height/20)

        self.vary_speed_button = QRadioButton()
        self.vary_speed_button.setStyleSheet("margin-left:50%; margin-right:50%;")


        #maintain max speed test
        self.maintain_max_speed_text = QLabel()
        self.maintain_max_speed_text.setText("Maintain Max Speed")
        self.maintain_max_speed_text.setMaximumHeight(primary.height/20)

        self.maintain_speed_button = QRadioButton()
        self.maintain_speed_button.setStyleSheet("margin-left:50%; margin-right:50%;")
        self.maintain_speed_button.setChecked(True)


        #lane change   
        self.lane_change_text = QLabel()
        self.lane_change_text.setText("Lane Change")

        self.lane_change_no = QRadioButton()
        self.lane_change_no.setText("No")
        self.lane_change_no.setChecked(True)
        self.lane_change_no.clicked.connect(self.lane_no_click)

        self.lane_change_yes = QRadioButton()
        self.lane_change_yes.setText("Yes")
        self.lane_change_yes.clicked.connect(self.lane_yes_click)
        

        self.lane_change_widget = QWidget()
        self.lane_change_grid = QHBoxLayout()

        self.lane_change_widget.setLayout(self.lane_change_grid)
        self.lane_change_widget.setMaximumHeight(primary.height/8)


        self.lane_change_grid.addWidget(self.lane_change_yes)
        self.lane_change_grid.addWidget(self.lane_change_no)



        #lane change time
        self.lane_change_time_text = QLabel()
        self.lane_change_time_text.setText("Lane Change Time (s)")
        self.lane_change_time_text.setDisabled(True)

        self.lane_change_time = QTextEdit()
        self.lane_change_time.setMaximumHeight(primary.height/25)
        self.lane_change_time.setMaximumWidth(primary.width/25)
        self.lane_change_time.setAlignment(QtCore.Qt.AlignCenter)
        self.lane_change_time.setDisabled(True)


        #safety distance
        self.safety_distance_text = QLabel()
        self.safety_distance_text.setText("Safety Distance (m)")

        self.safety_distance = QTextEdit()
        self.safety_distance.setMaximumHeight(primary.height/25)
        self.safety_distance.setMaximumWidth(primary.width/25)
        self.safety_distance.setAlignment(QtCore.Qt.AlignCenter)


        #delete button
        self.delete_button = QPushButton()
        self.delete_button.setText("Delete")
        self.delete_button.setMaximumWidth(primary.width/15)


        #vehicle color
        self.vehicle_color_text = QLabel()
        self.vehicle_color_text.setText("Color (RGB)")

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

        self.vehicle_color_r.setMinimumWidth(primary.width/50)
        self.vehicle_color_r.setMaximumHeight(primary.height/30)
        self.vehicle_color_g.setMinimumWidth(primary.width/50)
        self.vehicle_color_g.setMaximumHeight(primary.height/30)
        self.vehicle_color_b.setMinimumWidth(primary.width/50)
        self.vehicle_color_b.setMaximumHeight(primary.height/30)

        self.vehicle_color_r.setFont(QFont("Arial", 12))
        self.vehicle_color_g.setFont(QFont("Arial", 12))
        self.vehicle_color_b.setFont(QFont("Arial", 12))

        self.vehicle_color_r.setPlaceholderText("255")
        self.vehicle_color_g.setPlaceholderText("255")
        self.vehicle_color_b.setPlaceholderText("255")

        self.horiz_layout.addWidget(self.vehicle_color_r)
        self.horiz_layout.addWidget(self.vehicle_color_g)
        self.horiz_layout.addWidget(self.vehicle_color_b)


        #spacer
        self.spacer = QWidget()
        self.spacer.setMaximumHeight(primary.height/15)
        #self.spacer.setStyleSheet("background-color: red;")



        #GRID SETTINGS
        self.grid.addWidget(self.close_button,             0,0,1,1)
        self.grid.addWidget(self.spacer,                   1,0,1,1)
        self.grid.addWidget(self.title_text,               2,0,1,3)
        self.grid.addWidget(self.vary_speed_range_text,    3,0,1,1)
        self.grid.addWidget(self.maintain_max_speed_text,  3,1,1,1)
        self.grid.addWidget(self.vary_speed_button,        4,0,1,1)
        self.grid.addWidget(self.maintain_speed_button,    4,1,1,1)
        self.grid.addWidget(self.lane_change_text,         5,0,1,1)
        self.grid.addWidget(self.lane_change_widget,       5,1,1,2)
        self.grid.addWidget(self.lane_change_time_text,    6,0,1,1)
        self.grid.addWidget(self.lane_change_time,         6,1,1,2)
        self.grid.addWidget(self.safety_distance_text,     7,0,1,1)
        self.grid.addWidget(self.safety_distance,          7,1,1,2)
        self.grid.addWidget(self.vehicle_color_text,       8,0,1,1)
        self.grid.addWidget(self.vehicle_color,            8,1,1,1)
        self.grid.addWidget(self.delete_button,            9,0,1,1)
        





    def close(self):
        self.hide()
        self.parent().hide()
        self.parent().show()


    def lane_no_click(self):
        self.lane_change_time.setDisabled(True)
        self.lane_change_time_text.setDisabled(True)

    def lane_yes_click(self):
        self.lane_change_time.setDisabled(False)
        self.lane_change_time_text.setDisabled(False)









def main():
    primary.main()


if __name__ == "__main__":
    main()