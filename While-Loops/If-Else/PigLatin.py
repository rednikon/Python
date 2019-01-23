#!/usr/bin/env python

# Pig Latin Converter

# welcoming the user
print("Welcome to the Pig Latin translator.")
pig = "ay"
original = ""

#creating user input and the translation
while original != "exit":
    original = input("Enter a word to translate or type exit to quit: ")
    if len(original) > 0 and original.isalpha():
        word = original.lower()
        first = word[0]
        if (first == "a" or first == "e" or first == "i" or first == "o" or first == "u"): #pig latin triggers
            pigWord = word + pig
            print(pigWord)
        else:
            pigWord = word[1:] + first + pig
            print(pigWord)
    else:
        print("Invalid input. Please try again.")
