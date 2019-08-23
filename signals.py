#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 07:56:47 2019

@author: Ethan
"""
from math import sqrt

class Signal():
    def __init__(self, obj, sky, dark_current=60, read_out=8, gain=2.5, bias=100):
        self.obj = obj #Implicitly assumed in units of electrons
        self.sky = sky #Implicitly assumed in units of electrons
        self.dark_current = dark_current
        self.read_out = read_out
        self.gain = gain
        self.bias = bias
        
        #To be calculated; temp values to control logic
        self.raw = -1
        self.raw_sky = -1
        self.dark_frame = -1
        self.dark_corrected_frame = -1
        self.OSR = -1
    
    def __repr__(self):
        return 'This is a signal!'
        
        
    def data(self):
        print("\n\tThis signals information:\n")
        
        print("The object signal is {} [e-]".format(self.obj))
        print("The sky signal is {} [e-]".format(self.sky))
        print("The dark current is {} [e-]".format(self.dark_current))
        print("The read out noise is {} [rms e-]".format(self.read_out))
        print("The gain is {} [e-/ADU]".format(self.gain))
        print("The bias is {} [ADUs]".format(self.bias) + "\n")
        
        print("The raw signal is {0:.2f} +/- {1:.2f} [ADUs]".format(self.raw, self.raw_noise)\
              if self.raw != -1 else "The raw signal hasn't been calculated yet.")
        print("The dark current signal is {0:.2f} +/- {1:.2f} [ADUs]".format(self.dark_frame, self.dark_noise)\
              if self.dark_frame != -1 else "The dark frame signal hasn't been calculated yet")
        print("The dark corrected signal is {0:.2f} +/- {1:.2f} [ADUs]".format(self.dark_corrected_frame, self.dark_corrected_noise)\
              if self.dark_corrected_frame != -1 else "The correct signal hasn't been calculated yet")
        print("The corrected signal from the sky alone is {0:.2f} +/- {1:.2f} [ADUs]".format(self.sky_dark_corrected_frame, self.sky_dark_corrected_noise)\
              if self.raw_sky != -1 else "The sky only dark corrected signal hasn't been calculated yet")
        print("The OSR for this signal is {}".format(self.OSR) if self.OSR != -1 else "OSR not calculated yet")
        
        
    def get_raw(self):
        self.raw = (self.obj+self.sky)/self.gain + \
        self.dark_current/self.gain + self.bias
        
        self.raw_noise = 1/self.gain * \
        sqrt(sqrt(self.obj+self.sky)**2+sqrt(self.dark_current)**2+self.read_out**2)
        
    
    def get_dark_frame(self, num = 1):
        self.dark_frame = self.dark_current/self.gain + self.bias
        self.dark_noise = 1/self.gain * \
        sqrt(num*(sqrt(self.dark_current)**2+self.read_out**2))/num
        
    
    def get_dark_corrected(self, num = 1):
        if self.raw == -1 or self.dark_frame == -1:
            self.get_raw()
            self.get_dark_frame(num)
            
        self.dark_corrected_frame = self.raw - self.dark_frame
        self.dark_corrected_noise = sqrt(self.raw_noise**2 + self.dark_noise**2)
        
        
    def get_OSR(self):
        self.OSR = self.obj/self.sky
        
    
    def get_sky_only(self):
        self.raw_sky = self.sky/self.gain + \
        self.dark_current/self.gain + self.bias
        
        self.raw_sky_noise = 1/self.gain * \
        sqrt(sqrt(self.sky)**2+sqrt(self.dark_current)**2+self.read_out**2)
        
        self.sky_dark_corrected_frame = self.raw_sky - self.dark_frame
        self.sky_dark_corrected_noise = sqrt(self.raw_sky_noise**2 + self.dark_noise**2)


# Test Signal
signal = Signal(250, 600)
signal.get_dark_corrected(10)
signal.get_OSR()
signal.get_sky_only()
signal.data()