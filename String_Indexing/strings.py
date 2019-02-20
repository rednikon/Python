#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 19:02:03 2019

@author: veemac
"""

# indexing strings

s = 'santa fe'

print(s[0])

print(s[1])

print(s[2])

print(s[-1])

print(s[-2])

# slicing strings
print(s[0:3])

print(s[:3])

print(s[1:4])

a = s[:5]
b = s[5:]
print(a + b)

# slices with steps
s ='ABCDEFGH'
print(s[::-1])

print(s[::2])

print(s[1:5:2])


# how many letter 'S' does it have?
s = 'MISSISSIPPI'
print(s.count('S'))