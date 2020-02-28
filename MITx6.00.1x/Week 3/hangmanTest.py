# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 16:41:27 2020

@author: dkallen78
"""

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    for i in secretWord:
        if i not in lettersGuessed:
            return False
    return True

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    string = ""
    for i in secretWord:
        if i in lettersGuessed:
            string += i
        else:
            string += "_ "
    return string

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    letters = "abcdefghijklmnopqrstuvwxyz"
    string = ""
    for i in letters:
        if i not in lettersGuessed:
            string += i
        else:
            string += " "
    return string

secretWord = 'apple' 
lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']

print(getAvailableLetters(lettersGuessed))