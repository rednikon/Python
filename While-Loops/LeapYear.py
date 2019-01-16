#!/usr/bin/env python
# Mod 6 assignement, Identifying Leap Years on Mars
# There are 6 leap years in each decade on Mars. A leap year happens on every odd year and years that are divisible by 10.

year = "" # setting initial year input

while year != "exit":
    year = input("Enter a year or type exit: ")
    if year.isnumeric(): # building the requirement that the input is numeric
        year = int(year)
        if year%2 != 0: # establishing that a Marian year is an odd number
            print(year, "is a Martian leap year.")
        else:
            if year%10 == 0:
                print(year, "is a Martian leap year.")
            else:
                if year%2 == 0:  # telling the user when a year is not a Martian leap year 
                    print(year, "is not a leap year.")
                    print(year, "is not an odd number or divisible by 10.\n")
    else:
        if year.lower() == "exit":
            year = year.lower()
            print("Goodbye.")  # building a way for the user to exit the program
        else:
            print("Input invalid. Please try again.\n")
            
            
