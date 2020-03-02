# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 10:14:40 2020

@author: dkallen78
"""

def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    if aStr == "":
        return False
    elif len(aStr) <= 1 and char != aStr[len(aStr)//2]:
        return False
    elif char == aStr[len(aStr)//2]:
        return True
    elif char < aStr[len(aStr)//2]:
        return isIn(char, aStr[:len(aStr)//2])
    else:
        return isIn(char, aStr[len(aStr)//2:])
    
string1 = "abcdefghijklmnopqrstuvwxyz"
string2 = "acegikmoqsuwy"

