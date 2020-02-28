# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 12:16:51 2020

@author: dkallen78
"""

def findBalance(balance, annualInterestRate, monthlyPaymentRate):
    for month in range(1, 13):
        balance -= round(balance * monthlyPaymentRate, 2)
        balance += round(balance * (annualInterestRate / 12), 2)
    return balance
print("Remaining balance: " + str(round(findBalance(balance, annualInterestRate, monthlyPaymentRate), 2)))