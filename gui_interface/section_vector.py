from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QFont, QPixmap
import tkinter as tk
import sys
import edit_section
import gui_test as primary


page_list = []  # type: List[int]


def populate(vec, val):
    for i in range(0,val):
        new = edit_section.Edit_Section_Window()
        vec.append(new)