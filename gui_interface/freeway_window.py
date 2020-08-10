from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QFont, QPixmap
from functools import partial
import tkinter as tk
import sys
import edit_section
import section_vector
import add_vehicles
import vehicle
import edit_vehicle
import edit_vehicle_ego

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
        self.num_sections.textChanged.connect(self.validate_input)
        self.num_sections.textChanged.connect(self.double_right)
        self.num_sections.setPlaceholderText("7")




        #Allow Collisions
        self.allow_collisions_text = QLabel()
        self.allow_collisions_text.setText("Allow Collisions")
        self.allow_collisions_text.setFont(QFont("Arial", 18))

        self.allow_collisions = QCheckBox()
        self.allow_collisions.setChecked(True)
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
        self.min_speed.setText("54")


        #Max Speed
        self.max_speed_text = QLabel()
        self.max_speed_text.setText("Maximum Speed (km/h)")
        self.max_speed_text.setFont(QFont("Arial", 18))

        self.max_speed = QTextEdit()
        self.max_speed.setMaximumHeight(primary.height/20)
        self.max_speed.setMaximumWidth(primary.height/20)
        self.max_speed.setMinimumHeight(primary.height/20)
        self.max_speed.setMinimumWidth(primary.height/20)
        self.max_speed.setText("108")



        #Safety Distance
        self.safety_distance_text = QLabel()
        self.safety_distance_text.setText("Safety Distance (m)")
        self.safety_distance_text.setFont(QFont("Arial", 18))

        self.safety_distance = QTextEdit()
        self.safety_distance.setMaximumHeight(primary.height/20)
        self.safety_distance.setMaximumWidth(primary.height/20)
        self.safety_distance.setMinimumHeight(primary.height/20)
        self.safety_distance.setMinimumWidth(primary.height/20)
        self.safety_distance.setText("15")




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
        self.road_button1.clicked.connect(self.copy_map_to_sections)

        

        self.road_button2 = QPushButton(self.map_widget)
        self.road_button2.setMaximumWidth(primary.width/30)
        self.road_button2.setMinimumWidth(primary.width/30)
        self.road_button2.setMaximumHeight(primary.height/25)
        self.road_button2.setMinimumHeight(primary.height/25)
        self.road_button2.setText(str(self.road_array[1]))
        self.road_button2.clicked.connect(self.road_button_click_2)
        self.road_button2.clicked.connect(self.copy_map_to_sections)

        self.road_button3 = QPushButton(self.map_widget)
        self.road_button3.setMaximumWidth(primary.width/30)
        self.road_button3.setMinimumWidth(primary.width/30)
        self.road_button3.setMaximumHeight(primary.height/25)
        self.road_button3.setMinimumHeight(primary.height/25)
        self.road_button3.setText(str(self.road_array[2]))
        self.road_button3.clicked.connect(self.road_button_click_3)
        self.road_button3.clicked.connect(self.copy_map_to_sections)

        self.road_button4 = QPushButton(self.map_widget)
        self.road_button4.setMaximumWidth(primary.width/30)
        self.road_button4.setMinimumWidth(primary.width/30)
        self.road_button4.setMaximumHeight(primary.height/25)
        self.road_button4.setMinimumHeight(primary.height/25)
        self.road_button4.setText(str(self.road_array[3]))
        self.road_button4.clicked.connect(self.road_button_click_4)
        self.road_button4.clicked.connect(self.copy_map_to_sections)

        self.road_button5 = QPushButton(self.map_widget)
        self.road_button5.setMaximumWidth(primary.width/30)
        self.road_button5.setMinimumWidth(primary.width/30)
        self.road_button5.setMaximumHeight(primary.height/25)
        self.road_button5.setMinimumHeight(primary.height/25)
        self.road_button5.setText(str(self.road_array[4]))
        self.road_button5.clicked.connect(self.road_button_click_5)
        self.road_button5.clicked.connect(self.copy_map_to_sections)


        #ADD VEHICLES
        self.add_vehicles_widget = add_vehicles.Add_Vehicles_Window(self,self)
        self.add_vehicles_widget.hide()

        #EDIT EGO VEHICLE
        self.edit_ego_vehicle = edit_vehicle_ego.Edit_Vehicle_Ego_Widget(self)
        self.edit_ego_vehicle.hide()





        #GRID SETTINGS

            #labels and text
        self.grid.addWidget(self.back_button,          0,0,1,1)
        self.grid.addWidget(self.general_settings,     1,0,1,1)
        self.grid.addWidget(self.allow_collisions_text,2,0,1,1)
        self.grid.addWidget(self.num_sections_text,    3,0,1,1)
        self.grid.addWidget(self.min_speed_text,       4,0,1,1)
        self.grid.addWidget(self.max_speed_text,       5,0,1,1)
        self.grid.addWidget(self.safety_distance_text, 6,0,1,1)
        #self.grid.addWidget(self.edit_simulation,      7,0,1,1)
        self.grid.addWidget(self.start_simulation,     7,0,1,1)

            #input boxes
        self.grid.addWidget(self.allow_collisions,     2,1,1,1)
        self.grid.addWidget(self.num_sections,         3,1,1,1)
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



    def show_add_vehicles(self):
        self.add_vehicles_widget.show()
        

    def hide_add_vehicles(self):
        self.add_vehicles_widget.setVisible(False)
        self.hide()
        self.show()


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
                    section_vector.page_list[k].section_id.removeItem(j)

        

        

    def validate_input(self):
        text = self.num_sections.toPlainText()

        if text == "":
            return

        if text.isdigit() == False:
            self.num_sections.setText("")
        
        if int(text) > 100:
            self.num_sections.setText("100")



    def copy_map_to_sections(self):

        #connect to edit sections click
        car_attribute_list = list()
        for widget in self.add_vehicles_widget.map_widget.children():
            if widget.objectName() == "car":
                lane = widget.lane
                lead = widget.lead
                gap = widget.gap
                model = widget.model
                r = widget.color_r
                g = widget.color_g
                b = widget.color_b
                tupl = tuple((lane,lead,gap,model,r,g,b))
                car_attribute_list.append(tupl)

        
        for i in range(1,len(section_vector.page_list)):

            z = 1
            subject_lead_count = 0
            subject_follow_count = 0
            left_lead_count = 0
            left_follow_count = 0
            for settings in car_attribute_list:
                gap = int(settings[2])
                car_copy = vehicle.Vehicle(settings[0],settings[1],settings[2],settings[3],settings[4],settings[5],settings[6])
                car_copy.setParent(section_vector.page_list[i].map_widget)


                self.left_follow_gaps = self.add_vehicles_widget.left_follow_gaps
                self.subject_follow_gaps = self.add_vehicles_widget.subject_follow_gaps
                self.left_lead_gaps = self.add_vehicles_widget.left_lead_gaps
                self.subject_lead_gaps = self.add_vehicles_widget.subject_lead_gaps

                if car_copy.lead == 0:
                    if car_copy.lane == "subject":
                        car_copy.move(primary.width/3.745, self.subject_lead_gaps[subject_lead_count])
                        subject_lead_count += 1
                    else:
                        car_copy.move(primary.width/4.05, self.left_lead_gaps[left_lead_count])
                        left_lead_count += 1

                else:
                    if car_copy.lane == "subject":
                        car_copy.move(primary.width/3.745, self.subject_follow_gaps[subject_follow_count])
                        subject_follow_count += 1
                    else:
                        car_copy.move(primary.width/4.05, self.left_follow_gaps[left_follow_count])
                        left_follow_count += 1
                

                car_copy.clicked.connect(partial(self.do,i,z-1) )    
                car_copy.setObjectName("car")
                car_copy.setText(str(z))
                z+=1
                car_copy.show()

    def add_vehicle_edit_windows(self):

        car_count = 0
        for widget in self.add_vehicles_widget.map_widget.children():
            if widget.objectName() == "car":
                car_count += 1

        for page in range(1,len(section_vector.page_list)):
            for car_index in range(0,car_count):
                edit_car = edit_vehicle.Edit_Vehicle_Widget(car_index+1,section_vector.page_list[page])
                edit_car.setParent(section_vector.page_list[page])
                edit_car.car_index = car_index
                edit_car.setObjectName("edit")
                edit_car.safety_distance.setText(self.safety_distance.toPlainText())  
                edit_car.hide()
                section_vector.page_list[page].edit_vehicle_list.append(edit_car)


    def do(self,page_index,car_index):
        section_vector.page_list[page_index].edit_vehicle_list[car_index].show()
        section_vector.page_list[page_index].edit_vehicle_list[car_index].raise_()

    
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
            print("Vehicle {}:".format(index+1))
            print("Color: ({},{},{})".format(car[3],car[4],car[5]))
            print("Gap:",car[0])
            print("Model:",car[1])
            print("Lead:",car[2],"\n")

        print("---SUBJECT LANE INFO---")
        for index,car in enumerate(subject_cars):
            print("Vehicle {}:".format(index+1))
            print("Color: ({},{},{})".format(car[3],car[4],car[5]))
            print("Gap:",car[0])
            print("Model:",car[1])
            print("Lead:",car[2],"\n")


        print("---EGO VEHICLE SETTINGS---")
        ego = self.edit_ego_vehicle
        print("Model:", ego.vehicle_model.currentText())
        print("Color: ({},{},{})".format(ego.vehicle_color_r.toPlainText(),ego.vehicle_color_g.toPlainText(),ego.vehicle_color_b.toPlainText()))
        print("Safety distance:", ego.safety_distance.toPlainText())
        print("\n")


        print("---VEHICLE BEHAVIOR INFO---")
        for i in range(1,len(section_vector.page_list)):
            print("\n--Section {}--".format(i))
            for j in section_vector.page_list[i].edit_vehicle_list:
                print("-Vehicle {}-".format(j.car_index + 1))
                print("Vary Speed:", j.vary_speed_button.isChecked())
                print("Maintain Speed:", j.maintain_speed_button.isChecked())
                print("Lane Change:", j.lane_change_yes.isChecked())
                if j.lane_change_yes.isChecked():
                    print("Lane Change Time:", j.lane_change_time.toPlainText())
                print("Safety Distance:", j.safety_distance.toPlainText())
                if j.vehicle_color_r.toPlainText() == "":
                    print("Color: Default")
                else:
                    print("Color: ({},{},{})".format(j.vehicle_color_r.toPlainText(),j.vehicle_color_g.toPlainText(),j.vehicle_color_b.toPlainText()))








def main():
    primary.main()

if __name__ == "__main__":
    main()