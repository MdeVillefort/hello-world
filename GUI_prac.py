#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 14:37:52 2019

@author: user
"""

"""
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette

app = QApplication([])
app.setStyle('Windows')
palette = QPalette()
palette.setColor(QPalette.ButtonText, Qt.green)
app.setPalette(palette)
button = QPushButton('Hello')

def on_button_clicked():
    alert = QMessageBox()
    alert.setText('You did something!')
    alert.exec_()

button.clicked.connect(on_button_clicked)
button.show()
app.exec_()
"""

import wx

class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title="Hello World")
        panel = wx.Panel(self)
        
        self.text_ctrl = wx.TextCtrl(panel, pos=(5,5))
        my_btn = wx.Button(panel, label="Press Me", pos=(5,55))
        
        self.Show()
        
if __name__ == "__main__":
    app = wx.App()
    frame = MyFrame()
    app.MainLoop()