import sys
sys.path.insert(0, "D:\WindowsNoEditor\PythonAPI\examples\gui intersection")


from PyQt5 import QtWidgets,QtCore, QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont, QPixmap
import front
import intersection



intersections = [0, 1, 2, 3, 4, 5, 6]
widgetmaps = []

#helper function, get label text
def ExtractText(label):
    temp = QTextEdit()
    temp.setText(label.text())
    text = temp.toPlainText()
    del temp
    return text



class Main(QMainWindow):
    
    
    
    def __init__(self):
        super(Main, self).__init__()
        # build ui
        self.ui = front.Ui_Form()
        self.ui.setupUi()
        self.ui.show()
        self.inter = intersection.Ui_Form()
        self.inter.setupUi()
        self.TrafLit = intersection.Ui_TrafLightSet()
        self.TrafLit.setupUi()
        self.EditLane = intersection.Ui_EditLane()
        self.EditLane.setupUi()
        self.addVeh = intersection.Ui_AddVehicle()
        self.addVeh.setupUi()

        



        #add 6 widget maps in list
        widgetmaps.append(self.ui.widget3Fro)
        widgetmaps.append(self.ui.widget4Fro)
        widgetmaps.append(self.ui.widget5Fro)
        widgetmaps.append(self.ui.widget6Fro)
        widgetmaps.append(self.ui.widget7Fro)
        widgetmaps.append(self.ui.widget8Fro)

        #link buttons and input
        self.ui.RightFro.clicked.connect(self.right)
        self.ui.LeftFro.clicked.connect(self.left)
        self.ui.RightMostFro.clicked.connect(self.rightMost)
        self.ui.LeftMostFro.clicked.connect(self.leftMost)
        self.ui.spinBoxNumIntFro.valueChanged.connect(self.change_int)
        self.ui.Int1Fro.clicked.connect(self.front_inter)
        self.inter.backButtonInt.clicked.connect(self.inter_front)
        self.inter.TrafLightInt.clicked.connect(self.inter_Light)
        self.inter.backButtonLit.clicked.connect(self.Light_inter)
        self.inter.backButtonSpa.clicked.connect(self.spawn_inter)
        self.inter.AddVehInt.clicked.connect(self.inter_spawn)
        self.inter.set1Lit.clicked.connect(self.OpenTrafLit)
        self.inter.EditSubSpa.clicked.connect(self.OpenLane)
        self.inter.AddSubSpa.clicked.connect(self.OpenAddVeh)
        self.inter.CarSub.clicked.connect(self.any_vehicle)
        self.inter.backButtonVeh.clicked.connect(self.vehicle_any)
        

    def show_win(self):
        if len(intersections) > 6:
            self.ui.RightFro.show()
            self.ui.RightMostFro.show()
            self.ui.LeftFro.show()
            self.ui.LeftMostFro.show()
            for i in range(6):
                Button = widgetmaps[i].findChild(QPushButton)
                Button.show()
            
            


            if ExtractText(self.ui.Int1Fro) == "1":
                self.ui.LeftFro.hide()
                self.ui.LeftMostFro.hide()
            if ExtractText(self.ui.Int6Fro) == str(len(intersections)):
                self.ui.RightFro.hide()
                self.ui.RightMostFro.hide()

        else:


            self.ui.RightFro.hide()
            self.ui.RightMostFro.hide()
            self.ui.LeftFro.hide()
            self.ui.LeftMostFro.hide()

            for i in range(len(intersections)):
                Button = widgetmaps[i].findChild(QPushButton)

                Button.show()


            for i in range(len(intersections), 6):
                Button = widgetmaps[i].findChild(QPushButton)

                Button.hide()

    def right(self):
        for i in self.ui.label_num:
            num = int(ExtractText(i))
            num += 1
            i.setText(str(num))
        self.show_win()
    
    def left(self):
        for i in self.ui.label_num:
            num = int(ExtractText(i))
            num -= 1
            i.setText(str(num))
        self.show_win()

    def rightMost(self):
        for i in self.ui.label_num:
            num = len(intersections) - 5
            num += self.ui.label_num.index(i)
            i.setText(str(num))
        self.show_win()
    
    def leftMost(self):
        for i in self.ui.label_num:
            num = 1
            num += self.ui.label_num.index(i)
            i.setText(str(num))
        self.show_win()

    def change_int(self):
        
        
        num = self.ui.spinBoxNumIntFro.value()

        while num < len(intersections):
            intersections.pop()
        while num > len(intersections):
            intersections.append(0)
        
        self.show_win()

    def front_inter(self):
        self.ui.hide()
        self.inter.show()

    def inter_front(self):
        self.inter.hide()
        self.ui.show()
    
    def inter_Light(self):
        self.inter.widgetInt.hide()
        self.inter.widgetLit.show()

    def Light_inter(self):
        self.inter.widgetInt.show()
        self.inter.widgetLit.hide()
    
    def inter_spawn(self):
        self.inter.widgetInt.hide()
        self.inter.widgetSpa.show()

    def spawn_inter(self):
        self.inter.widgetInt.show()
        self.inter.widgetSpa.hide()

    def any_vehicle(self):
        tmpWidget = None
        for i in self.inter.widgets:
            if not i.isHidden():
                tmpWidget = i
            
        self.inter.widgetVeh.show()
        if tmpWidget != None:
            tmpWidget.hide()
    
    def vehicle_any(self):
        self.inter.widgetVeh.hide()
        self.inter.widgetInt.show()


    def OpenTrafLit(self):
        self.TrafLit.show()

            
    def OpenLane(self):
        self.EditLane.show()

    def OpenAddVeh(self):
        self.addVeh.show()

    
        


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Main()
    

    sys.exit(app.exec_())


