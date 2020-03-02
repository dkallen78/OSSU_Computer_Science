# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 21:52:59 2020

@author: dkallen78
"""

class intSet(object):
    """An intSet is a set of integers
    The value is represented by a list of ints, self.vals.
    Each int in the set occurs in self.vals exactly once."""

    def __init__(self):
        """Create an empty set of integers"""
        self.vals = []

    def insert(self, e):
        """Assumes e is an integer and inserts e into self""" 
        if not e in self.vals:
            self.vals.append(e)

    def member(self, e):
        """Assumes e is an integer
           Returns True if e is in self, and False otherwise"""
        return e in self.vals

    def remove(self, e):
        """Assumes e is an integer and removes e from self
           Raises ValueError if e is not in self"""
        try:
            self.vals.remove(e)
        except:
            raise ValueError(str(e) + ' not found')

    def __str__(self):
        """Returns a string representation of self"""
        self.vals.sort()
        return '{' + ','.join([str(e) for e in self.vals]) + '}'
    
    def intersect(self, other):
        newSet = []
        newIntSet = intSet()
        for number in self.vals:
            if number in other.vals:
                newSet.append(number)
        newIntSet.vals = newSet
        return newIntSet
    
    def __len__(self):
        return len(self.vals)
    
setA = intSet()
setB = intSet()

setA.vals = [-17,-16,-10,-8,2,3,14,15]
setB.vals = [-16,-11,-10,-8,-4,4,19]

setC = setA.intersect(setB)
print(setC)
