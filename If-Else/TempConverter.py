#!/usr/bin/env python

#Mod 6 Assignment, building a Temp Converter
# Build a converter that is interactive, that will accept temps from the user in either Celcius or Fahrenheit

#Welcome the user to the program
print("Hello. Welcome to the Temperature Converter.")
temp = ""

# while loop to continue the program until the user directs us to exit
while temp != "exit":
    temp = input("Do you want to convert from Celsius or Fahrenheit? Please enter 'C' or 'F'. Or type 'exit' to quit: ")
    # if-else ladder for celsius or fahrenheit inputs
    if (temp == "F" or temp == "f"):
        temp = input("What is your temperature in Fahrenheit? ")
        if temp.isnumeric():
            temp = int(temp)
            c = (temp - 32)*5.0/9.0
            print("The terperature given converts to", c, "degrees in Celsius")
        else:
            print("Input invalid. Please enter 'C' or 'F'.\n")
    elif (temp == "C" or temp == "c"):
        temp = input("Enter a temperature in Celsius: ")
        if temp.isnumeric():
            temp = int(temp)
            f = 9.0/5.0*temp + 32
            print("The temperature given converts to", f, "degrees Fahrenheit")
        else:
            print("Input invalid. Please enter 'C' or 'F'.\n")
    else:
        if temp.lower() == "exit":
            temp = temp.lower()
            print("Goodbye.")
        else:
            print("Invalid input. Please try again.\n")
                          
