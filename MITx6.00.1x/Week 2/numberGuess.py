# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 19:23:13 2020

@author: espeg
"""

userInput = ""
validInput = "hlc"
highNumber = 100
lowNumber = 0

print("Please think of a number between 0 and 100!")
while True:
    guess = (highNumber + lowNumber)//2
    print("Is your secret number " + str(guess) + "?")
    userInput = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    if userInput not in validInput:
        print("Sorry, I did not understand your input.")
        continue
    elif userInput == "l":
        lowNumber = guess
    elif userInput == "h":
        highNumber = guess
    else:
        print("Game over. Your secret number was: " + str(guess))
        break