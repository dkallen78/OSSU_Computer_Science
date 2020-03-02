# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""

s = 'azcbobobegghakl'
s = "abcdabcdefqzabcdefgh"
currentString = s[0]
longString = ""
for i in range(1,len(s)):
    if ord(s[i]) >= ord(s[i-1]):
        currentString += s[i]
        if len(currentString) > len(longString):
            longString = currentString  
    else:
        currentString = s[i]
print("Longest substring in alphabetical order is: " + longString)