#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 18:49:56 2019

@author: veemac
"""
# Learning sets

rainbow = {'red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet'}

print(type(rainbow))

len(rainbow)
# 7

'violet' in rainbow
# True

A = {'red', 'orange', 'yellow'}
B = {'yellow', 'green', 'blue' }
C = {'indigo', 'violet'}


# The union of two sets.
A.union(B) == A | B == {'red', 'orange', 'yellow', 'green', 'blue'}
# True

#Intersection of two sets.
A.intersection(B) == A & B == {'yellow'}
# True


#Set difference
A - B == {'red', 'orange'}
# True

B - A  == {'green', 'blue'}
True

# Exclusive OR
A ^ B == (A-B | B-A) == {'blue', 'red', 'orange', 'green'}
#True

A|B|C == rainbow
# True

B & C
# set()

len(B&C)
# 0

UNIVERSE = {'cat', 'dog', 'python', 'parrot'}

mypets = {'cat', 'python'}

# What is the Complement of the mypets set?

UNIVERSE - mypets  == {'dog', 'parrot'}
# True

