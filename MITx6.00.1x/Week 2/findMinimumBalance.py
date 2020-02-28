# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 12:40:16 2020

@author: dkallen78
"""

def findMinimumPayment(balance, annualInterestRate):
    seedPayment = (balance // 120) * 10
    initialBalance = balance
    while True:
        balance = initialBalance
        for month in range(1, 13):
            balance -= seedPayment
            balance += round(balance * (annualInterestRate / 12), 2)
        if balance <= 0:
            return seedPayment
        elif seedPayment > initialBalance:
            break
        else:
            seedPayment += 1
            
print("Lowest Payment: " + str(findMinimumPayment(3926, .2)))