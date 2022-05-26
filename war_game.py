'''
Second milestone project of Complete Python Bootcamp Udemy course.
Author: Nicolau Santos
'''

# Import libraries
import random 

# Create card_values dictionary
ranks = ["ace", "king", "queen", "jack", "ten", "nine", "eight", "seven", "six", "five", "four", "three", "two"]
suits = ["Hearts","Spades","Diamonds","Clubs"]
card_values = {"ace":14, "king": 13, "queen":12, "jack":11, "ten":10, "nine":9, "eight":8, "seven":7, "six":6, "five":5, "four":4, "three":3, "two":2}

# Create Card Class

class Card:
    ''''
    Class for card objects.

    Atributes: rank, suit, and value
    Methods: print
    '''

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.value = card_values[rank]
    
    def __string__(self):
        # print function for the card object
        return f"{self.rank} of {self.suit}"

# Create Deck Class

class Deck:
    '''
    Class for deck objects.

    Attributes: number(?)
    Methods: create, shuffle, deal
    '''

    def __init__(self, number):
        self.number = number
    
    def create(self)

# Create Player Class