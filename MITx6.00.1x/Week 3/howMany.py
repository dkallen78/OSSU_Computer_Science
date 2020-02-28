# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 15:41:02 2020

@author: dkallen78
"""

def how_many(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    count = 0
    for i in aDict:
        count += len(aDict[i])
    return count

test = {'B': [15], 'u': [10, 15, 5, 2, 6]}

print(how_many(test))