#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 14:05:31 2019

@author: veemac

Exercises from Chapter 4

"""

# 4.1 Write a function that takes a number as an input and returns that number squared. 

base_number = int(input("What number would you like squared? "))

def squared(x):
    """
    Returns x**2.
    :param x: int.
    :return: int square of x.
    """
    return x**2

result = squared(base_number)
print(result)

# 4.2 Create a function that accepts a string as a parameter and prints it. 

user_string = input("What's your favorite saying? ")

def echo(y):
    """
    Returns y.
    :param y: str.
    :return: user string.
    """
    print(y)
    
echo(user_string)

# 4.3 Write a function that takes three required parameters and two optional parameters. 

first_name = input("What is your first name? ")
last_name = input("What is your last name? ")
location = input("Where are you located? ")
middle_name = input("Enter a middle name if you have one. ")
age = int(input("How old are you? Leave blank if you prefer not to say. "))


def personal_info(first_name, last_name, location, middle_name = "n/a", age = "prefer not to say"):
    """
    Returns first_name, last_name, location
    :param first_name: str.
    :param last_name: str.
    :param location: str.
    :return: list of first_name, last_name, location.
    """
    print("Personal Details: ", first_name, middle_name, last_name, location, age)
    
personal_info(first_name, last_name, location, middle_name, age)
    


# 4.4 Write a program with two functions. The first function should take an integer as a parameter and return the result of the integer divided by 2. 
#  The second function should take an integer as a parameter and return the result of the integer multiplied by 4.
#  Call the first function, save the result as a variable, and pass it as a parameter to the second function. 

first = int(input("Please provide a number: "))

def first_function(e):
    """
    Returns e / 2.
    :param e: int.
    :return: int of e divided by 2.
    """
    return e / 2

step_one = first_function(first)

def second_function(s):
    """
    Returns step_one * 4.
    :param step_one: int.
    :return: int of step_one multiplied by 4.
    """
    return step_one * 4

result = second_function(step_one)
print(result)

# 4.5 Write a function that converts a string to a float and returns the result. Use exception handling to catch the exception that could occur. 

number = False

while type(number) is not int:
    try:
        number = int(input("Please enter one last number: "))
    
    except ValueError:
        print("Please provide a number.")

def string_to_int(z):
    z = int(z)
    return z


print("You chose:", string_to_int(number))


# 4.6 Add docstrings to each of the functions you created above










