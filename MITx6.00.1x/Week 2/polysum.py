# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 12:00:11 2020

@author: dkallen78
"""

import math

def polysum(n, s):
     area = (0.25 * n * s**2)/(math.tan(math.pi/n))
     perimeter = n * s
     return round(area + perimeter**2, 4)
