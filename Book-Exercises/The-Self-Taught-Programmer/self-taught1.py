#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: veemac

The fist set of challenges from "The Self-Taught Programmer", Chapters 1 - 3
"""
# 1. Print a string
print("The Self-Taught Programmer Exercises")


# 2. Print a message if a variable is less than 10, and another message if the variable is equal or greater than 10
get_variable_one = input("Please enter a whole number: ")
variable_one = int(get_variable_one)

if variable_one < 10:
    print("The variable you entered is less than than 10.")
else:
    print("The variable you entered is 10 or greater.")


# 3. Print a message if a variable is equal or less than 10, another if it's greater than 10 but less than or equal to 25, and the last if it's greater than 25
get_variable_two = input("Please enter another whole number: ")
variable_two = int(get_variable_two)

# use if-elif-else ladder since there are 3 conditions
if  variable_two <= 10:
    print("The variable you entered is less than or equal to 10.")
elif 10 < variable_two <= 25:
    print("The variable you entered is between 10 and 25.")
else:
    print("The variable you entered is greater than 25.")

# 4. Create a program that divides two variables and prints the remainder.
<<<<<<< HEAD
print("\nLet's divide some numbers.")
get_numerator = input("Please enter a numerator: ")
n = int(get_numerator)

get_denominator = input("Please enter a denominator: ")
d = int(get_denominator)

print("The remainder is: ", n%d)

# 5. Create a program that takes two variables, divides them, and prints the quotient.
print("The quotient is: ", n/d)

# 6. Write a program with a variable 'age' assigned to an integer that prints different strings depending on what ingeger 'age' is
get_age = input("What's your age? ")
age = int(get_age)

if  age <= 18:
    print("Stay in school.")

elif 18 < age < 35:
    print("Enjoy your youth.")

else:
    print("You're hitting your stride.")
