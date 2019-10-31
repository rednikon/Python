#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 21:32:44 2019

@author: veemac

Our second module. Calculates volume and area of a box. 
We define two functions: Volume and Area

"""

# Pylot: vmcclur1 Vee

__author__ = 'vmcclur1'


def volume(w, d, h):
    """Returns the volume of a box with dimensions w x d x h.

    >>> volume(5, 10, 3)
    150
    """

    return w * d * h



def area(w, d, h, has_top=False):
    """
    Returns the surface of a box.  The box migh not have a top.
    Surface area without top
    >>> area(3, 4, 5, has_top=False)
    82

    Surface area with top

    >>> area(3, 4, 5, has_top=True)
    94

    """

    side = d * h
    front = w * h
    bottom = w * d


    # default is without top
    total = 2 * side + 2 * front + bottom

    if has_top:
        total += bottom

    return total    

if __name__ == '__main__':
    import doctest
    doctest.testmod()
