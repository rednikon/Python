#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 18:21:50 2019

@author: veemac
"""

# Write a program that accepts words and writes them to a file.

DATAFILE = '~/myacronyms.txt'

# What functions will be useful?

def is_old_acronym(s):
    """
    >>> is_old_acronym('ISO')
    
    """
    # Open a file as readable
    with open(DATAFILE, 'r') as fdin:
        for line in fdin:
            line = line.strip()
            if s == line:
                return True
            return False

def append_acronym(s):
        """Appends the acronym s to our datafile.txt,
        if it's not already there.
        """
        s = s.upper()
        
        with open(DATAFILE, 'a') as fdin:
            print(s, file = fdin)
        
def interactive():
    """Asks the user for an acronym
    and adds it to out DATAFILE
    if it's not already there.
    """
    
    # Welcome and prompt the user
    WELCOME = "\nWelcome to my interactive acronym appender program!\n"
    PROMT = "Please input an acronym: "
    
    print(Welcome)
    
    
    while True:
        reply = input(PROMPT)
        if not reply:  #that's the most Pythonic way to say if len(reply) == 0 
            break
        
        