#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 19:57:28 2019

@author: veemac
"""

# Explain the outputs of these four functions.
name = "Vee"

# the result is None, and it prints the string without quotes
def hello1(name):
    greeting = 'hi there ' + name
    print(greeting)

# the result is 'hi there Vee, and it has quotes
def hello2(name):
    greeting = 'hi there ' + name
    return greeting

# there is a result, and it also gets printed out
def hello3(name):
    greeting = 'hi there ' + name
    print(greeting)
    return greeting

# because the return statement happens first, the greeting does not get printed
def hello4(name):
    greeting = 'hi there ' + name
    return greeting
    print(greeting)
