#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 12:48:38 2019

@author: veemac
"""


"""This is my mymodA module in my mynamespack package.
   It defines some functions that create acronyms.
"""

BLANK = ''

# First, we define two slightly different functions, acronym1 and acronym2.


def acronym1(s):
    """Given a string s, returns an acronym based on the first letter of each  word in the string.

    >>> acronym1('Environmental Protection Agency')
    'EPA'
    >>> acronym1('Supreme Court of the United States')
    'SCOTUS'
    """

    # REPLACE THE pass BELOW WITH YOUR OWN CODE
    return (BLANK.join(l[0].upper() for l in s.split()))


def acronym2(s):
    """Given a string s, returns an acronym based on all uppercase letters in the string.

    >>> acronym2('FaceBook')
    'FB'
    >>> acronym2('City College of San Franciso')
    'CCSF'
    >>> acronym2('HyperText Markup Language')
    'HTML'

    """

    # REPLACE THE pass BELOW WITH YOUR OWN CODE
    return (BLANK.join(u[0] for u in s if u.isupper()))
