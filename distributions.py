#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 12:16:29 2019

@author: EthanR
"""

import random
from math import log, cos, sqrt, pi

class Normal():
    
    """Class for normal distributions
    To generate the distribution, we add 20 randomly generated numbers
    from a uniform distribution between 0 and 1 to approximate the normal distribution.
    
    This method was taken from The Scientist and Engineer's Guide to 
    Digital Signal Processing, Chapter 2: Statistics, Probability, and Noise
    Section: Digital Noise Generation
    """
    
    def __init__(self, mu = 0, sigma = 1, size = 1000):
        """Initialize Normal instance
        mu: Mean of distribution
        sigma: Standard deviation of distribution
        size: Number of samples in distribution
        """
        
        self.mu = mu
        self.sigma = sigma
        
        signal = []
        for j in range(size):
            X = 0
            for i in range(20):
                X += random.uniform(0,1)
            X -= 10
            X *= sigma
            X += mu
            signal.append(X)
        self.signal = signal


class Normal2():
    
    """Another class for normal distributions
    To generate each number in the distribution, we grab 2 numbers from a 
    unifrom distribution between 0 and 1 and apply an equation.
    
    This method and the equation were taken from The Scientist and Engineer's 
    Guide to Digital Signal Processing, Chapter 2: Statistics, Probability, and 
    Noise, Section: Digital Noise Generation.
    """
    
    def __init__(self, mu=0, sigma=1, size=1000):
        """Initialize Normal2 instance
        mu: Mean of distribution
        sigma: Standard deviation of distribution
        size: Number of samples in distribution
        """
        
        self.mu = mu
        self.sigma = sigma
        
        signal = []
        for j in range(size):
            R1 = random.uniform(0,1)
            R2 = random.uniform(0,1)
            
            X = sqrt(-2*log(R1)) * cos(2*pi*R2) #signal with mu=0, sigma=1
            X *= self.sigma
            X += self.mu
            signal.append(X)
        self.signal = signal





