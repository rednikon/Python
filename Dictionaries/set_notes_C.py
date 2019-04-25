#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 18:58:14 2019

@author: veemac
"""

# Working with words
text = 'I AM WHAT I AM POP EYE THE SAILOR MAN'

text.split()
# ['I', 'AM', 'WHAT', 'I', 'AM', 'POP', 'EYE', 'THE', 'SAILOR', 'MAN']

# casting it as a set to get rid of duplicates. The sorted function always returns a list
sorted(set(text.split()))
# ['AM', 'EYE', 'I', 'MAN', 'POP', 'SAILOR', 'THE', 'WHAT']

# Letter frequency
s = 'abracadabra'
for letter in s :
    print(letter, s.count(letter))

# Set comes to the rescue
print(set(s))
print(sorted(set(s)))

for letter in sorted(set(s)):
    print(letter,s.count(letter))

# What if we want to be able to use those frequencies?
# Create an empty dictionary
freq = dict()
for letter in s:
    if letter in freq:
        freq[letter] += 1
    else:
        freq[letter] = 1    #initializing

print(freq)

# Here is another approach
freq = dict()
for letter in s:
    freq[letter] = 0
for letter in s:
    freq[letter] += 1

print(freq)

# Building a dictionary for any word
def freqdict(word):
    letters = set(word)
    d = {letter : word.count(letter) for letter in letters}
    return d

print(freqdict('santa anna'))

# Looking up frequencies in a dictionary
d = {'a': 5, 'd': 1, 'c': 1, 'r': 2, 'b': 2}
print(d['a'])
print(d['b'])

# What if we asked about d['e']?
# It will give us an error because 'e' is not a key in our dict d

# Throwing an exception
try:
    print(['e'])
except Exception as err:
    err
print('We are still fine!')

    