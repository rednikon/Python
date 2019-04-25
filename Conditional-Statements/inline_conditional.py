#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 18:20:09 2019

@author: veemac
"""

#shortest way to write if else statements
n = 8
'even' if n % 2 == 0 else 'odd'

n=7
'even' if n % 2 == 0 else 'odd'

def parity(n):
    return 'even' if n% 2 == 0 else 'odd'

for n in [2, 3, 4, 0]:
    print(f"n={n} has parity: {parity(n)}")

for s in ['Lisa', 'Bob', '', 'Alice']:
    name = s.upper() if s else 'unknown'
    print(s, name)
 
# traditional way to write if else statments
for s in ['Lisa', 'Bob', '', 'Alice']:
    if s:
        name = s.upper()
    else:
        s = 'unknown'
        name = s.upper() if s else 'unknown'
        print(f"{s:8s} {name:8s}")