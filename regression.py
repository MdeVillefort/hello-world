#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 06:23:41 2019

@author: EMR
"""

import matplotlib.pyplot as plt
from scipy.spatial import distance as dist

def euclidean_distance(pt1, pt2):
    """Function to compute euclidean distances between two points
    represented as iterables.
    In scipy, scipy.spatial.distance.euclidean
    """
    
    distance = 0
    for i in range(len(pt1)):
        distance += (pt1[i] - pt2[i])**2
    distance = distance**0.5
    return distance

def manhattan_distance(pt1, pt2):
    """Function to compute manhattan distance between two points
    represented as iterables.
    In scipy, scipy.spatial.distance.cityblock
    """
    
    distance = 0
    for i in range(len(pt1)):
        distance += abs(pt1[i] - pt2[i])
    return distance

def hamming_distance(pt1, pt2):
    """Function to compute the hamming distance between two points
    represented as iterables.
    In scipy, scipy.spatial.distance.hamming
    """
    
    distance = 0
    for i in range(len(pt1)):
        if pt1[i] != pt2[i]:
            distance += 1
    return distance

def find_loss(y_actual, y_predicted):
    """Function to calculate loss between actual values and values predicted
    by a regression algorithm.
    
    loss = sum((y_actual - y_predicted)**2)
    """
    
    loss = 0
    for i in range(len(y_actual)):
        loss += (y_actual[i] - y_predicted[i])**2
    return loss

def get_gradient_at_b(x, y, b, m):
    """Function which calculates the gradient (slope) wrt intercept of the loss
    function between data and modal.
    """
    
    N = len(x)
    
    diff = 0
    for i in range(N):
        x_val = x[i]
        y_val = y[i]
        diff += (y_val - ((m * x_val )+ b))
        
    b_gradient = -(2/N) * diff  
    return b_gradient

def get_gradient_at_m(x, y, b, m):
    """Function which calculates the gradient (slope) wrt slope (m) of the loss
    function between data and modal.
    """
    
    N = len(x)
    diff = 0
    for i in range(N):
        x_val = x[i]
        y_val = y[i]
        diff += x_val * (y_val - ((m * x_val) + b))
    m_gradient = -(2/N) * diff  
    return m_gradient

def step_gradient(b_current, m_current, x, y, learning_rate):
    
    b_gradient = get_gradient_at_b(x, y, b_current, m_current)
    m_gradient = get_gradient_at_m(x, y, b_current, m_current)
    b = b_current - (learning_rate * b_gradient)
    m = m_current - (learning_rate * m_gradient)
    
    return b, m
  
#Your gradient_descent function here:  
def gradient_descent(x, y, learning_rate, num_iterations):
    b = 0
    m = 0
    
    for i in range(num_iterations):
        b, m = step_gradient(b, m, x, y, learning_rate)
    
    return b, m


months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
revenue = [52, 74, 79, 95, 115, 110, 129, 126, 147, 146, 156, 184]

#Uncomment the line below to run your gradient_descent function
b, m = gradient_descent(months, revenue, 0.01, 1000)

#Uncomment the lines below to see the line you've settled upon!
y = [m*x + b for x in months]

plt.plot(months, revenue, "o", label = 'data')
plt.plot(months, y, label = 'model')
plt.legend()

plt.show()
