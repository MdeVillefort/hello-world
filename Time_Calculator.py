#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 08:15:43 2019

@author: Ethan Ross
Time Calculator
"""

from datetime import datetime
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow

class Window(QMainWindow):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)
        self.setGeometry(50,50,500,300)
        self.setWindowTitle("Testing")
        self.show


app = QApplication(sys.argv)
GUI = Window()

#sys.exit(app.exec_())

hour1 = raw_input("Enter hour of arrival (0-24): ")
hour1 = int(hour1)
minute1 = raw_input("Enter minute of arrival (0-60): ")
minute1 = int(minute1)

#Get current time from computer
now = datetime.now()
now_hour = now.hour
now_minute = now.minute

""" Enter current time manually!
hour2 = raw_input("Enter hour of departure (0-24): ")
hour2 = int(hour2)
minute2 = raw_input("Enter minute of departure (0-60): ")
minute2 = int(minute2)
"""

lunch = raw_input("Did you take a lunch? (y/n) ")

if lunch == 'y':
    lunch_hour = raw_input("How many hours for lunch? ")
    lunch_hour = int(lunch_hour)
    lunch_minute = raw_input("How many minutes for lunch? ")
    lunch_minute = int(lunch_minute)
    time_diff = round((now_hour + now_minute/60.0) - (hour1 + minute1/60.0) \
                      - (lunch_hour + lunch_minute/60.0), 1)
    print "Your time today is {} hours".format(time_diff)
elif lunch == 'n':
    time_diff = round((now_hour + now_minute/60.0) - (hour1 + minute1/60.0), 1)
    print "Your time today is {} hours".format(time_diff)
else:
    print "Something's wrong!"
