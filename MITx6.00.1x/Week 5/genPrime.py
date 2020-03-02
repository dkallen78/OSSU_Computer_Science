# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 10:33:53 2020

@author: dkallen78
"""

def genPrimes():
    primes = []
    prime = True
    currentNumber = 2
    
    while True:
        prime = True
        for i in primes:
            if not currentNumber % i != 0:
                prime = False
        if not prime:
            currentNumber += 1
            continue
        else:
            yield currentNumber
            primes.append(currentNumber)
            currentNumber += 1