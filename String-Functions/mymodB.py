#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  9 17:21:10 2019

@author: veemac
"""
COMMA = ','
SPACE = ' '
BLANK = ''
PERIOD = '.'
name = "Alexandria Ocasio-Cortez"


def initials(name):
    """Given a name returns the initials.

    >>> initials('Elon Reeve Musk')
    'E.R.M.'

    >>> initials('Lyndon Baines Johnson')
    'L.B.J.'

    >>> initials('Franklin Delano Roosevelt')
    'F.D.R.'

    >>> initials('Alexandria Ocasio-Cortez')
    'A.O.C.'

    """

    # REPLACE THE pass BELOW WITH YOUR OWN CODE
    return (PERIOD.join(name[0].upper() for name in name if name.isupper()) + PERIOD)


def name2tuple(name):
    """Given a comma-separated name, returns a tuple of the form (firstnames, lastnames).

    >>> tvhost = "Maddow, Rachel Anne"
    >>> name2tuple(tvhost)
    ('Rachel Anne', 'Maddow')

    >>> author = "Borges Acevedo, Jorge Francisco Isidoro Luis"
    >>> name2tuple(author)
    ('Jorge Francisco Isidoro Luis', 'Borges Acevedo')
    """

    # REPLACE THE pass BELOW WITH YOUR OWN CODE
    return (COMMA.join(name.split(SPACE)[::-1]))