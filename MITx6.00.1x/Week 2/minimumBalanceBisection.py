# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 13:00:21 2020

@author: dkallen78
"""

def minimumBalance(balance, annualInterestRate):
    
    initialBalance = balance
    monthlyRate = annualInterestRate / 12
    lowerBound = round(balance / 12, 2)
    upperBound = round((balance * (1 + monthlyRate)**12) / 12, 2)
        
    while True:
        balance = initialBalance
        seedPayment = (upperBound + lowerBound) / 2
        
        for month in range(1, 13):
            balance -= seedPayment
            balance += balance * (annualInterestRate / 12)
        
        if round(balance, 2) == 0:
            return seedPayment
        elif balance > 0:
            lowerBound = seedPayment
            continue
        else:
            upperBound = seedPayment
            continue
        
balance = 999999
rate = 0.18

print("Lowest Payment: " + str(round(minimumBalance(balance, rate), 2)))