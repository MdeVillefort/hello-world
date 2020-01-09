#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 06:23:41 2019

@author: EMR
"""

import matplotlib.pyplot as plt
plt.style.use('ggplot')
#from scipy.spatial import distance as dist
#from sklearn.linear_modal import LinearRegression

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
        x_val = float(x[i])
        y_val = float(y[i])
        diff += (y_val - ((m * x_val )+ b))
        
    b_gradient = -(2.0 / N) * diff  
    return b_gradient

def get_gradient_at_m(x, y, b, m):
    """Function which calculates the gradient (slope) wrt slope (m) of the loss
    function between data and modal.
    """
    
    N = len(x)
    diff = 0
    for i in range(N):
        x_val = float(x[i])
        y_val = float(y[i])
        diff += x_val * (y_val - ((m * x_val) + b))
    m_gradient = -(2.0 / N) * diff  
    return m_gradient

def step_gradient(x, y, m_current, b_current, learning_rate):
    """Function which takes a single step defined by the gradients at m and b 
    torward reducing loss.
    """
    
    b_gradient = get_gradient_at_b(x, y, b_current, m_current)
    m_gradient = get_gradient_at_m(x, y, b_current, m_current)
    b = b_current - (learning_rate * b_gradient)
    m = m_current - (learning_rate * m_gradient)
    
    return b, m

def gradient_descent(x, y, learning_rate, num_iterations):
    """Function which performs the gradient descent regression algorithm iterating 
    with the given learing_rate num_iterations times.
    """
    
    b = 0
    m = 0
    
    for i in range(num_iterations):
        b, m = step_gradient(x, y, m, b, learning_rate)
    
    return b, m

def plot_conv(x, y, learning_rate, num_iterations, param = 'm'):
    """Fuction which will plot the convergence of the parameter 'param' for a
    partiuclar run of the gradient descent regression algorithm.
    """
    
    fig = plt.figure()
    ax = fig.add_subplot(111)
    
    b = 0; m = 0
    ms = []; bs = []
    for i in range(num_iterations):
        b, m = step_gradient(x, y, m, b, learning_rate)
        ms.append(m)
        bs.append(b)
    
    if param == 'm':
        ax.plot(range(num_iterations), ms)
        ax.set(title = 'convergence of m', xlabel = 'iteration', ylabel = 'slope')
    elif param == 'b':
        ax.plot(range(num_iterations), bs)
        ax.set(title = 'convergence of b', xlabel = 'iteration', ylabel = 'intercept')
    
    plt.show()

 # TEST #
months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
revenue = [52, 74, 79, 95, 115, 110, 129, 126, 147, 146, 156, 184]

b, m = gradient_descent(months, revenue, 0.01, 1000)
y = [float(m)*x + b for x in months]

# Plot data and modal predicted values
fig = plt.figure(num = 1)
ax = fig.add_subplot(111)
ax.plot(months, revenue, "o", label = 'data')
ax.plot(months, y, label = 'model')
ax.legend()
plt.show()

# Plot convergences
plot_conv(months, revenue, 0.01, 1000, param = 'm')
plot_conv(months, revenue, 0.01, 1000, param = 'b')