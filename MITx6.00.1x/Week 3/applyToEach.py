# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 14:52:47 2020

@author: dkallen78
"""

def applyToEach(L, f):
    for i in range(len(L)):
        L[i] = f(L[i])
        
testList = [1, -4, 8, -9]

def f1(integer):
    return integer * 5

def f2(integer):
    return abs(integer)

def f3(integer):
    return integer + 1

def f4(integer):
    return integer**2

applyToEach(testList, f4)

print(testList)


