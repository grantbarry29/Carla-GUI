from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QFont, QPixmap
import tkinter as tk
import sys
import edit_section
import section_vector
import add_vehicles

import gui_test as primary

class ExtendedQLabel(QLabel):
    def __init__(self, parent):
        QLabel.__init__(self, parent)

    clicked=pyqtSignal()
    def mouseReleaseEvent(self, ev):
        self.clicked.emit()



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

        section_vector.page_list.append(self.general_settings_widget)


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
        self.num_sections.setPlaceholderText("-")
        self.num_sections.textChanged.connect(self.validate_input)
        self.num_sections.textChanged.connect(self.double_right)




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

        #Add Vehicles
        self.add_vehicles = QPushButton()
        self.add_vehicles.setText("Add Vehicles")
        self.add_vehicles.setFont(QFont("Arial", 14))
        self.add_vehicles.setMaximumWidth(primary.width/6)
        self.add_vehicles.setMinimumHeight(primary.height/25)
        self.add_vehicles.clicked.connect(self.show_add_vehicles)



        #Edit Simulation
        self.edit_simulation = QPushButton()
        self.edit_simulation.setText("Edit Simulation")
        self.edit_simulation.setFont(QFont("Arial", 14))
        self.edit_simulation.setMaximumWidth(primary.width/6)
        self.edit_simulation.setMinimumHeight(primary.height/25)
        self.edit_simulation.clicked.connect(self.vec_populate)
        self.edit_simulation.clicked.connect(self.go_to_edit_section)



        #Start Simulation
        self.start_simulation = QPushButton()
        self.start_simulation.setText("Start Simulation")
        self.start_simulation.setFont(QFont("Arial", 14))
        self.start_simulation.setMaximumWidth(primary.width/6)
        self.start_simulation.setMinimumHeight(primary.height/25)
        self.start_simulation.clicked.connect(self.gather)



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
        self.road_array = ["-","-","-","-","-"]

        self.road_button1 = QPushButton(self.map_widget)
        self.road_button1.setMaximumWidth(primary.width/30)
        self.road_button1.setMinimumWidth(primary.width/30)
        self.road_button1.setMaximumHeight(primary.height/25)
        self.road_button1.setMinimumHeight(primary.height/25)
        self.road_button1.setText(str(self.road_array[0]))
        self.road_button1.clicked.connect(self.road_button_click_1)
        

        self.road_button2 = QPushButton(self.map_widget)
        self.road_button2.setMaximumWidth(primary.width/30)
        self.road_button2.setMinimumWidth(primary.width/30)
        self.road_button2.setMaximumHeight(primary.height/25)
        self.road_button2.setMinimumHeight(primary.height/25)
        self.road_button2.setText(str(self.road_array[1]))
        self.road_button2.clicked.connect(self.road_button_click_2)

        self.road_button3 = QPushButton(self.map_widget)
        self.road_button3.setMaximumWidth(primary.width/30)
        self.road_button3.setMinimumWidth(primary.width/30)
        self.road_button3.setMaximumHeight(primary.height/25)
        self.road_button3.setMinimumHeight(primary.height/25)
        self.road_button3.setText(str(self.road_array[2]))
        self.road_button3.clicked.connect(self.road_button_click_3)

        self.road_button4 = QPushButton(self.map_widget)
        self.road_button4.setMaximumWidth(primary.width/30)
        self.road_button4.setMinimumWidth(primary.width/30)
        self.road_button4.setMaximumHeight(primary.height/25)
        self.road_button4.setMinimumHeight(primary.height/25)
        self.road_button4.setText(str(self.road_array[3]))
        self.road_button4.clicked.connect(self.road_button_click_4)

        self.road_button5 = QPushButton(self.map_widget)
        self.road_button5.setMaximumWidth(primary.width/30)
        self.road_button5.setMinimumWidth(primary.width/30)
        self.road_button5.setMaximumHeight(primary.height/25)
        self.road_button5.setMinimumHeight(primary.height/25)
        self.road_button5.setText(str(self.road_array[4]))
        self.road_button5.clicked.connect(self.road_button_click_5)


        #ADD VEHICLES
        self.add_vehicles_widget = add_vehicles.Add_Vehicles_Window(self,self)
        self.add_vehicles_widget.hide()








        #GRID SETTINGS

            #labels and text
        self.grid.addWidget(self.back_button,          0,0,1,1)
        self.grid.addWidget(self.general_settings,     1,0,1,1)
        self.grid.addWidget(self.num_sections_text,    2,0,1,1)
        self.grid.addWidget(self.allow_collisions_text,3,0,1,1)
        self.grid.addWidget(self.min_speed_text,       4,0,1,1)
        self.grid.addWidget(self.max_speed_text,       5,0,1,1)
        self.grid.addWidget(self.safety_distance_text, 6,0,1,1)
        self.grid.addWidget(self.add_vehicles,         7,0,1,1)
        self.grid.addWidget(self.edit_simulation,      8,0,1,1)
        self.grid.addWidget(self.start_simulation,     9,0,1,1)

            #input boxes
        self.grid.addWidget(self.num_sections,         2,1,1,1)
        self.grid.addWidget(self.allow_collisions,     3,1,1,1)
        self.grid.addWidget(self.min_speed,            4,1,1,1)
        self.grid.addWidget(self.max_speed,            5,1,1,1)
        self.grid.addWidget(self.safety_distance,      6,1,1,1)



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
        self.road_button1.move(primary.width/8.7,primary.height/5.1)
        self.road_button2.move(primary.width/5.55,primary.height/5.1)
        self.road_button3.move(primary.width/4.05,primary.height/5.1)
        self.road_button4.move(primary.width/3.18,primary.height/5.1)
        self.road_button5.move(primary.width/2.62,primary.height/5.1)






    def road_button_reset(self):
        self.road_button1.setText(str(self.road_array[0]))
        self.road_button2.setText(str(self.road_array[1]))
        self.road_button3.setText(str(self.road_array[2]))
        self.road_button4.setText(str(self.road_array[3]))
        self.road_button5.setText(str(self.road_array[4]))

    def road_button_click_helper(self,index):
        if index == "-":
            return
        else:
            index = int(index)
        self.vec_populate()
        QtWidgets.QStackedLayout.setCurrentWidget(self.stack,section_vector.page_list[index])
        section_vector.page_list[index].section_id.setCurrentText("Section {}".format(index))

    def road_button_click_1(self):
        index = self.road_button1.text()
        self.road_button_click_helper(index)
        

    def road_button_click_2(self):
        index = self.road_button2.text()
        self.road_button_click_helper(index)

    def road_button_click_3(self):
        index = self.road_button3.text()
        self.road_button_click_helper(index)

    def road_button_click_4(self):
        index = self.road_button4.text()
        self.road_button_click_helper(index)

    def road_button_click_5(self):
        index = self.road_button5.text()
        self.road_button_click_helper(index)


    def single_left(self):
        if self.road_array[0] == "-" or self.road_array[0] == 1:
            return

        
        self.road_array[0] -= 1
        self.road_array[1] -= 1
        self.road_array[2] -= 1
        self.road_array[3] -= 1
        self.road_array[4] -= 1
        self.road_button_reset()
        


    def single_right(self):
        if self.road_array[0] == "-":
            return
        if self.num_sections.toPlainText() == "":
            val = "-"
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
        if self.road_array[0] == '-':
            return
        
        self.road_array[0] = 1
        self.road_array[1] = 2
        self.road_array[2] = 3
        self.road_array[3] = 4
        self.road_array[4] = 5
        self.road_button_reset()


    def double_right(self):
        if self.num_sections.toPlainText() == "":
            val = 0
        else:
            val = int(self.num_sections.toPlainText())

        if self.road_array[-1] == val:
            return

        j = 4
        for i in range(0,5):
            self.road_array[i] = val - j
            j = j - 1
            if val - j <= 1:
                self.road_array[i] = '-'

        self.road_button_reset()

    
    def back_to_start(self):
        if self.stack.count() > 1:
            for i in range(0,int(self.num_sections.toPlainText())):
                self.stack.widget(i).destroy()
        section_vector.page_list.clear()
        self.new = primary.Start_Window()
        self.destroy()
        self.new.show()


    def go_to_edit_section(self):
        if len(section_vector.page_list) == 1:
            return
        QtWidgets.QStackedLayout.setCurrentWidget(self.stack,section_vector.page_list[1])


    def go_to_general_settings(self):
        QtWidgets.QStackedLayout.setCurrentWidget(self.stack,section_vector.page_list[0])


    def go_to_page(self, val):
        QtWidgets.QStackedLayout.setCurrentWidget(self.stack,section_vector.page_list[val])
        section_vector.page_list[val].section_id.setCurrentText("Section {}".format(val))

    def show_add_vehicles(self):
        self.add_vehicles_widget.show()

    def hide_add_vehicles(self):
        self.add_vehicles_widget.setVisible(False)
        self.hide()
        self.show()
        


    def vec_populate(self): 
        if self.num_sections.toPlainText() == "":
            val = 0
        else:
            val = int(self.num_sections.toPlainText())

        if val == len(section_vector.page_list)-1:
            return

        if val > len(section_vector.page_list)-1:
            start_len = len(section_vector.page_list)
            section_vector.populate(section_vector.page_list,val,self)
        
            for i in section_vector.page_list:
                self.stack.addWidget(i)
        
            """for k in range(1,start_len):
                for j in range(start_len,len(section_vector.page_list)-1):
                    section_vector.page_list[k].section_id.addItem("Section {}".format(j+1))"""


            

        if val < len(section_vector.page_list)-1:
            remove_value = len(section_vector.page_list) -1 - val
            i = len(section_vector.page_list)-1
            i_copy = i
            section_vector.remove(section_vector.page_list,remove_value)

            while(remove_value > 0):
                self.stack.removeWidget(self.stack.widget(i))
                i = i - 1
                remove_value = remove_value - 1


            for k in range(1,len(section_vector.page_list)):
                for j in range(len(section_vector.page_list),i_copy):
                    print(j)
                    section_vector.page_list[k].section_id.removeItem(j)
                    section_vector.page_list[k].section_id.removeItem(j-1)
                    section_vector.page_list[k].section_id.removeItem(j+1)
                print("\n")

        

        

    def validate_input(self):
        text = self.num_sections.toPlainText()

        if text == "":
            return

        if text.isdigit() == False:
            self.num_sections.setText("")
        
        if int(text) > 100:
            self.num_sections.setText("100")

    
    def gather(self):
        number_freeway_sections = self.num_sections.toPlainText()
        allow_collisions = self.allow_collisions.isChecked()
        minimum_speed = self.min_speed.toPlainText()
        max_speed = self.max_speed.toPlainText()
        safety_distance = self.safety_distance.toPlainText()



        print("---SETUP INFO---")
        print("number of sections:",number_freeway_sections)
        print("allow collisions (t/f):",allow_collisions)
        print("minimum speed:",minimum_speed)
        print("maximum speed:",max_speed)
        print("safety distance:",safety_distance,"\n")



        #left lane car info in tuple form (gap,model,lead(t/f),red,green,blue)
        left_cars = list()
        for i in self.add_vehicles_widget.left_vehicle_list:
            data = tuple((i.gap,i.model,i.lead,i.color_r,i.color_g,i.color_b))
            left_cars.append(data)

        #right lane car info in tuple form (gap,model,lead(t/f),red,green,blue)
        subject_cars = list()
        for i in self.add_vehicles_widget.subject_vehicle_list:
            data = tuple((i.gap,i.model,i.lead,i.color_r,i.color_g,i.color_b))
            subject_cars.append(data)

        print("---LEFT LANE INFO---")
        for index,car in enumerate(left_cars):
            print("vehicle {}:".format(index+1))
            print("color: ({},{},{})".format(car[3],car[4],car[5]))
            print("gap:",car[0])
            print("model:",car[1])
            print("lead:",car[2],"\n")

        print("---SUBJECT LANE INFO---")
        for index,car in enumerate(subject_cars):
            print("vehicle {}:".format(index+1))
            print("color: ({},{},{})".format(car[3],car[4],car[5]))
            print("gap:",car[0])
            print("model:",car[1])
            print("lead:",car[2],"\n")







def main():
    primary.main()

if __name__ == "__main__":
    main()