from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont, QPixmap
import tkinter as tk
import sys
import freeway_window as Fway


#to get window size
root = tk.Tk()
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
root.destroy()


class Start_Window(QMainWindow):
    def __init__(self):
        super(Start_Window, self).__init__()
        self.setGeometry(0,0,width,height)
        self.setWindowTitle("PyQt_test")
        self.initUI()

    def initUI(self):
        self.main_widget = QWidget()
        self.grid = QGridLayout()
        self.main_widget.setLayout(self.grid)
        self.setCentralWidget(self.main_widget)
        

        #freeway button
        self.fway_button = QPushButton()
        self.fway_button.setText("Freeway")
        self.fway_button.setFont(QFont("Arial", 18))
        self.fway_button.setMaximumWidth(int(width/5))
        self.fway_button.setMaximumHeight(int(height/8))
        self.fway_button.clicked.connect(self.go_to_freeway)
        

        #intersection button
        self.inter_button = QPushButton()
        self.inter_button.setText("Intersection")
        self.inter_button.setFont(QFont("Arial", 18))
        self.inter_button.setMaximumWidth(int(width/5))
        self.inter_button.setMaximumHeight(int(height/8))
        


        #version text
        self.version_text = QLabel()
        self.version_text.setText("Version 0.00")
        self.version_text.setFont(QFont("Arial", 18))
        self.version_text.setAlignment(QtCore.Qt.AlignCenter)


        #title text
        self.title_text = QLabel()
        self.title_text.setText("Carla Driving Simulator")
        self.title_text.setFont(QFont("Arial", 30))
        self.title_text.setAlignment(QtCore.Qt.AlignCenter)


        #spacer
        self.spacer = QSpacerItem(40,40,QtWidgets.QSizePolicy.Maximum,QtWidgets.QSizePolicy.Maximum)

        #grid
        self.grid.addWidget(self.title_text,0,0,3,2)
        self.grid.addWidget(self.fway_button,2,0,1,1)
        self.grid.addWidget(self.inter_button,2,1,1,1)
        self.grid.addWidget(self.version_text,1,0,1,2)
        self.grid.addItem(self.spacer,3,0,1,2)
        

    def go_to_freeway(self):
        new = Fway.Freeway_Window(self)
        self.close()
        new.show()



        


def main():
    app = QApplication(sys.argv)
    win = Start_Window()
    win.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()