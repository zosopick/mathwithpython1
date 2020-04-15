'''
Consider a deck of 52 playing cards, your challenge here is to create a program which suffles the deck.
To keep the implementation simple start with the integers 1,2,3,...,52 to represent the deck.
Every time you run it it ought to output a shuffled deck.

For start just with integers

>>> import random
>>> x=[1,2,3,4]
>>> random.shuffle(x)
>>> x
[3, 4, 2, 1]

If we want to use this program in a cards game we will need a way to map back the integers
to the specific suit and rank of each card. One way to do this is to create a Python class to
represent a single card.

class Card:
     def __init__(self,suit.rank):
          self.suit=suit
          self.rank=rank

'''

import random

class Card:
     def __init__(self,suit,rank):
          self.suit=suit
          self.rank=rank

def initialize_deck():
     suits=['Clubs','Diamonds','Hearts','Spades']
     ranks=['Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King']
     cards=[]
     for suit in suits:
          for rank in ranks:
               card=Card(suit,rank)
               cards.append(card)
     return cards

def shuffle_and_print(cards):
     random.shuffle(cards)
     for card in cards:
          print('{0} of {1}'.format(card.rank,card.suit))

if __name__=='__main__':
                cards=initialize_deck()
                shuffle_and_print(cards)
