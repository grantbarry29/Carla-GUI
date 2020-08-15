from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QFont, QPixmap
import sys
import edit_section
import freeway_window
import gui_test as primary


page_list = []  # type: List[int]


def populate(vec, val, window):
    for i in range(len(vec),val+1):
        new = edit_section.Edit_Section_Window(i,window)
        vec.append(new)

def remove(vec,val):
    for i in range(0,val):
        vec.pop()

        
