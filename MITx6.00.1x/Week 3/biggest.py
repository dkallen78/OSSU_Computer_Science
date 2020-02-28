# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 16:24:32 2020

@author: dkallen78
"""

def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    bigger = ""
    longest = 0
    
    for i in aDict:
        if len(aDict[i]) > longest:
            longest = len(aDict[i])
            bigger = i
    return bigger


test = {'B': [15], 'u': [10, 15, 5, 2, 6]}
print(biggest(test))
