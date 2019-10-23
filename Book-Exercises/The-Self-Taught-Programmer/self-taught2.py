#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 14:05:31 2019

@author: veemac

Exercises from Chapters 4 & 5

"""

# 4.1 Write a function that takes a number as an input and returns that number squared. 

base_number = int(input("What number would you like squared? "))

def squared(x):
    return x**2

result = squared(base_number)
print(result)

# 4.2 Create a function that accepts a string as a parameter and prints it. 

user_string = input("What's your favorite saying? ")

def echo(x):
    print(x)
    
echo(user_string)

# 4.3 Write a function that takes three required parameters and two optional parameters. 


# 4.4 Write a program with two functions. The first function should take an integer as a parameter and return the result of the integer divided by 2. 
#  The second function should take an integer as a parameter and return the result of the integer multiplied by 4.
#  Call the first function, save the result as a variable, and pass it as a parameter to the second function. 
