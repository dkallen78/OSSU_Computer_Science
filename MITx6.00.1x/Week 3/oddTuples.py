# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 13:45:34 2020

@author: dkallen78
"""

def oddTuples(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
    
    newTup = ()
    
    for i in range(0,len(aTup),2):
        newTup = newTup + (aTup[i],)
        
    return newTup

def oddTuples2(aTup):
    
    return aTup[::2]

aTup = ('I', 'am', 'a', 'test', 'tuple')

newTup = oddTuples2(aTup)
print(newTup)