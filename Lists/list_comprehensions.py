#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 21:14:07 2019

@author: veemac
"""

# List comprehension

# read 'for n in range' to understand what we're starting with, then go to the front of the statement to see what happens to n
print([n for n in range(4)])

print([n**2 for n in range(1, 5)])


# making tuples
print([(n, n**2) for n in range(1, 5)])


# filtering so only the squares larger than 5
print([(n, n**2) for n in range(1, 5) if n **2 > 5])


# only odd n values
print([(n, n**2) for n in range(1, 5) if n % 2 == 1])


# Create a list that shows the number of letters in each month
months = 'january february march april may'.split()
print([(m, len(m)) for m in months])


# Make a list of months that have less than six letters
print([m.capitalize() for m in months if len(m) < 6])


# Create a list like [A1, A2, ...]
LETTERS = 'AB'
DIGITS = '123'

print([letter+digit for letter in LETTERS for digit in DIGITS])


# The Genetic Code
LETTERS = 'ACGT'

# The 'words' have 3 letters each and are called "codons".
# We want a list of all of the codons (there are 64)
print([x+y+z for x in LETTERS for y in LETTERS for z in LETTERS])
