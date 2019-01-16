#!/usr/bin/env python

#Mod 5 Assignment, converting Centimeters to Inches

#Welcoming the user to the program
print("Welcome to Vee's Centimeters to Inches conversion program.")

#Creating the loop for the conversion calculator
goAgain = 1
while goAgain == 1:
    Centimeters = int(input("Please enter a measurement in Centimeters for conversion: "))
    #Building the formula that converts cm to in
    Inches = Centimeters/2.54
    print(Centimeters, "centimeters equals", Inches, "inches.")
    goAgain = int(input("Type 1 to enter another centimeter measurement for conversion, or type any other number to quit the program: "))
    
