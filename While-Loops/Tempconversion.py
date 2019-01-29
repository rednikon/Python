#!/usr/bin/env python

#Mod 5 Assignment, converting Celcius to Fahrenheit

#Welcoming the user to the program
userName = input("What is your name? ")
print("Welcome to the temperature conversion program,", userName)

#Creating a Loop for the user
goAgain = 1
while goAgain == 1:
    Celcius = int(input("Enter a temperature in Celcius: "))
    #Establishing conversion formula
    Fahrenheit = 9.0/5.0*Celcius+32
    print("The temperature", Celcius, "degrees given in Celcius, equals", Fahrenheit, "degrees in Fahrenheit.")
    goAgain = int(input("Type 1 to enter another temperature in Celcius, or any other number to quit: "))
