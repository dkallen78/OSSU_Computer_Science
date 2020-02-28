# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 19:51:37 2020

@author: dkallen78
"""

def integerDivision(x, a):
    """
    x: a non-negative integer argument
    a: a positive integer argument

    returns: integer, the integer division of x divided by a.
    """
    count = 0
    while x >= a:
        count += 1
        x = x - a
    return count

print(integerDivision(5, 3))