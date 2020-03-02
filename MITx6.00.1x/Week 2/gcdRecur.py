# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 09:10:08 2020

@author: dkallen78
"""

def gcdRecur(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    if a > b:
        larger = a
        smaller = b
    elif b > a:
        larger = b
        smaller = a
    else:
        return a
    
    if smaller == 0:
        return larger
    else:
        return gcdRecur(smaller, larger % smaller)