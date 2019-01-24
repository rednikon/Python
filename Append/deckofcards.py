#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 19:37:15 2019

@author: veemac
"""

# Lecture 2 Classwork, completed as a group
# Create a deck of cards

# building suits: Clubs, Diamonds, Spades, Hearts
SUITS = 'C D S H'
SUITS = SUITS.split()

# creating card values
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'
RANKS = RANKS.split()

# Be pythonic (the Python style)
# nested loops for printing out rank and suit of card
for rank in RANKS:
    for suit in SUITS:
        card = rank+suit
        print(card)

# using tuples instead of str objects
for rank in RANKS:
    for suit in SUITS:
        card = (rank, suit)
        print(card)
        
# make a list object of tuples that is the deck of cards
DECK = []

for rank in RANKS:
    for suit in SUITS:
        card = (rank, suit)
        # DECK = DECK + [card]
        DECK.append(card)
print("Here is our deck:")
print(DECK)
print("The deck has", len(DECK))

message = 'The deck has ' + str(len(DECK)) + ' cards'
print(message)

# pop a card from the end of the list
print(DECK.pop())
print("This deck now has", len(DECK), "cards")

# deal card while we still have cards in the deck
print("Let's shuffle a deck.")
while len(DECK) > 0:
    mycard = DECK.pop()
    print("We are delt", mycard)


# create a new deck so we can shuffle it before dealing    
DECK = []

for rank in RANKS:
    for suit in SUITS:
        card = (rank, suit)
        # DECK = DECK + [card]
        DECK.append(card) 

# importing the random method, and shuffling our new deck in place, destructive
import random
random.shuffle(DECK)

#while len(DECK) > 0:
#while bool(DECK):
while DECK: #because DECK is a list, it will become empty
    mycard = DECK.pop()
    print("We are delt", mycard)










