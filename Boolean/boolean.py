#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 21:05:16 2019

@author: veemac
"""

# Exercises on the bool type
# "Boolean" after George Boole

# finding the type
print(type(True))

print(type(False))

# any int casts to boolean as 'True' except 0, which casts as False
print(bool(0))

print(bool(1))


# boolean and while loops
n = 5
while bool(n):
    print(n)
    n -= 1  #decrement n by 1
    

# The while statement will always cast the object as bool, so...
n = 5
while n:
    print(n)
    n -= 1


# boolean and lists
L = ['a', 'b', 'c']
while L:
    letter = L.pop()
    print(letter)
    

# printing the list as you decrement it
L = ['a', 'b', 'c']
while L:
    print(L)
    L.pop()
    

# str objects and list objects can be 'sliced'
s = "ABCDEF"
print(s)

# slice the first 3 elements in the list
print(s[0:3])

# shorter notation but same as s[0:3]
print(s[:3])

# are they the same / equal to each other? yes.
print(s[:3] == s[0:3])

# show the sliced that starts at index 3
print(s[3:])

# remember how slicing works, where it starts and stops its count
print(s[:3] + s[3:])

# we can use a variable
i = 4
print(s[:i])














