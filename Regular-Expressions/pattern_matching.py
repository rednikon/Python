#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 18:23:03 2019

@author: veemac
"""

# Pattern matching using the Standard-Library module named "re"

import re

# Functions from the re module

#re.match(pattern, string)
    #returns a "match object" if the pattern matches the string
    # otherwise, it returns None
    
#re.split

#re.sub

#re.findall(pattern, string)
    #returns a list of all matching substrings of string
    
    # We will need special characters such as...
    #  \d  digit
    #  \D  non-digit
    #  \b  word boundary
    #  ^   beginning of a string
    #  $   end of a string
    #  ?   means zero or one of what comes before the question mark
            # The pattern "books?" means "book" or "books"
            
#define the pattern
ExampleA = W12345678
ExampleB = S12345678
    
pat1 = 'W/d{8}'
pat2 = 'S\d{8}'

# One pattern is enough if we use the (small) character set

pat = "[WS]\d{8}"

# Now we try and do some matching

sid1 = 'W12345678'
m = re.match(pat, sid1)