from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QFont, QPixmap
import edit_section
import freeway_window
import gui_test as primary
import carla_vehicle_list



class Start_Sim_Pop_Up(QDialog):
    def __init__(self,parent=None):
        super(Start_Sim_Pop_Up, self).__init__(parent)
        self.parent_window = parent
        self.setWindowTitle("Start Simulation")
        self.initUI()

    def initUI(self):
        self.grid = QGridLayout()
        self.setLayout(self.grid)
        self.grid.setContentsMargins(10,0,10,0)


        self.setMinimumHeight(primary.height/3)
        self.setMinimumWidth(primary.width/4)
        self.setMaximumHeight(primary.height/3)
        self.setMaximumWidth(primary.width/4)



        #gap size
        self.choose_view_text = QLabel()
        self.choose_view_text.setText("Choose View Type")

        self.choose_view = QComboBox()
        self.choose_view.addItem("First Person")
        self.choose_view.addItem("Third Person")
        self.choose_view.addItem("Free Roam")



        #vehicle model
        self.choose_control_text = QLabel()
        self.choose_control_text.setText("Choose Control Type")

        self.choose_control = QComboBox()
        self.choose_control.addItem("Drive Automatically")
        self.choose_control.addItem("Drive Manually")
        self.choose_control.currentIndexChanged.connect(self.choose_manual)
        
        

        self.start_simulation_button = QPushButton()
        self.start_simulation_button.setText("Start Simulation")
        self.start_simulation_button.clicked.connect(self.process_start)


        #GRID SETTINGS
        self.grid.addWidget(self.choose_view_text, 1,0,1,1)
        self.grid.addWidget(self.choose_view, 1,2,1,1)
        self.grid.addWidget(self.choose_control_text, 2,0,1,1)
        self.grid.addWidget(self.choose_control, 2,2,1,1)
        self.grid.addWidget(self.start_simulation_button, 3,1,1,1)
        
        

    def process_start(self):
        self.parent_window.run()
    
    def choose_manual(self):
        if self.choose_control.currentIndex() == 1:
            self.choose_view.setCurrentIndex(0)
            self.choose_view.setEnabled(False)
        else:
            self.choose_view.setEnabled(True)


        











def main():
    primary.main()


if __name__ == "__main__":
    main()