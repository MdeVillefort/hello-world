#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 04:58:34 2019

@author: user
"""

import functools
import time
import math
import random

def do_twice(func):
    @functools.wraps(func)
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)
    return wrapper_do_twice

def add_mod(func):
    @functools.wraps(func)
    def wrapper_add_mod(*args, **kwargs):
        print('the answer is...')
        return func(*args, **kwargs)
    return wrapper_add_mod

def timer(func):
    """print the runtime of the decorated function"""
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        print(f"Finished {func.__name__!r} in {run_time: .4f} secs")
        return value
    return wrapper_timer

def debug(func):
    """print the function signature and return value"""
    @functools.wraps(func)
    def wrapper_debug(*args, **kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={v!r}]" for k, v in kwargs.items()]
        signature = ", ".join(args_repr + kwargs_repr)
        print(f"Calling {func.__name__}({signature})")
        value = func(*args, **kwargs)
        print(f"{func.__name__!r} returned {value!r}")
        return value
    return wrapper_debug

def slow_down(func):
    """sleep 1 second before calling function"""
    @functools.wraps(func)
    def wrapper_slow_down(*args, **kwargs):
        time.sleep(1)
        return func(*args, **kwargs)
    return wrapper_slow_down

PLUGINS = dict()
def register(func):
    """Register a function as a plug-in"""
    PLUGINS[func.__name__] = func
    return func

##############################################################################

# Test Functions
    
@timer
def waste_time(num_times):
    for _ in range(num_times):
        sum([i**2 for i in range(10000)])
@debug
def make_greeting(name, age=None):
    if age is None:
        return f"Howdy {name}!"
    else:
        return f"Whoa {name}! {age} already, you are growing up"

math.factorial = debug(math.factorial) # Can apply decorators to pre-defined functions

def approximate_e(terms=18):
    return sum(1 / math.factorial(n) for n in range(terms))

@slow_down
def countdown(from_number):
    if from_number < 1:
        print("Liftoff!")
    else:
        print(from_number)
        countdown(from_number - 1) # recursively call decorated function countdown

