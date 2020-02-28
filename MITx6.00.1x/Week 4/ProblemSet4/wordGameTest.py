# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 21:29:14 2020

@author: dkallen78
"""

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # wordList: list of strings
    wordList = []
    for line in inFile:
        wordList.append(line.strip().lower())
    print("  ", len(wordList), "words loaded.")
    return wordList

def displayHand(hand):
    """
    Displays the letters currently in the hand.

    For example:
    >>> displayHand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    for letter in hand.keys():
        for j in range(hand[letter]):
             print(letter,end=" ")       # print all on the same line
    print()                         

def calculateHandlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string-> int)
    returns: integer
    """
    total = 0
    for letter in hand:
        total += hand[letter]
    return total

def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    if word not in wordList:
        return False
    
    newHand = dict.copy(hand)
    for letter in word:
        if not newHand.get(letter, 0) or newHand[letter] == 0:
            return False
        else:
            newHand[letter] -= 1
            
    return True

def playHand(hand, wordList, n):
    
    # Keep track of the total score
    score = 0
    
    # As long as there are still letters left in the hand:
    while calculateHandlen(hand) > 0:
    
        # Display the hand
        print("Current Hand: ", end = "")
        displayHand(hand)
        # Ask user for input
        guessedWord = input('Enter word, or a "." to indicate that you are finished: ')
        # If the input is a single period:
        if guessedWord == ".":
            # End the game (break out of the loop)
            break
            
        # Otherwise (the input is not a single period):
        else:
            # If the word is not valid:
            if not isValidWord(guessedWord, hand, wordList):
                # Reject invalid word (print a message followed by a blank line)
                print("Invalid word, please try again.\n")
            # Otherwise (the word is valid):
            else:
                # Tell the user how many points the word earned, and the updated total score, in one line followed by a blank line
                score += getWordScore(guessedWord, n)
                print('"' + guessedWord + '" earned', getWordScore(guessedWord, n), 'points. Total:', score, 'points')
                # Update the hand 
                hand = updateHand(hand, guessedWord)

    # Game is over (user entered a '.' or ran out of letters), so tell user the total score
    if guessedWord == ".":
        print("Goodbye! Total score:", score, "points.")
    else:
        print("Run out of letters. Total score:", score, "points.")
        
wordList = loadWords()
hand = {'n':1, 'e':1, 't':1, 'a':1, 'r':1, 'i':2}
n = 8

playHand(hand, wordList, n)
