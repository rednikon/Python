#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: veemac

The fist set of challenges from "The Self-Taught Programmer", Chapters 1 - 3
"""
# 1. Print a string
print("The Self-Taught Programmer Exercises")


# 2. Print a message if a variable is less than 10, and another message if the veriable is equal or greater than 10
var_one = input("Please enter a whole number: ")
x = int(var_one)

if x < 10:
    print("The variable you entered is less than than 10.")
else: 
    print("The variable you entered is 10 or greater.")


# 3. Print a message if a variable is equal or less than 10, another if it's greater than 10 but less than or equal to 25, and the last if it's greater than 25
var_two = input("Please enter another whole number: ")
y = int(var_two)

# use if-elif-else ladder since there are 3 conditions
if  y <= 10:
    print("The variable you entered is less than or equal to 10.")
elif 10 < y <= 25:
    print("The variable you entered is between 10 and 25.")
else:
    print("The variable you entered is greater than 25.")

# 4. Create a program that divides two variables and prints the remainder. 
<<<<<<< HEAD
print("\nLet's divide some numbers.")
numerator = input("Please enter a numerator: ")
n = int(numerator)

denominator = input("Please enter a denominator: ")
d = int(denominator)

print("The remainder is: ", n%d)

# 5. Create a program that takes two variables, divides them, and prints the quotient. 
print("The quotient is: ", n/d)
    
# 6. Write a program with a variable 'age' assigned to an integer that prints different strings depending on what ingeger 'age' is
age = input("What's your age? ")
a = int(age)

if  a <= 18:
    print("Stay in school.")

elif 18 < a < 35:
    print("Enjoy your youth.")

else:
    print("You're hitting your stride.")

