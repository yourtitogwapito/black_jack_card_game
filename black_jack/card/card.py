# -*- coding: utf-8 -*-
"""
Created on Thu Jun 15 11:07:19 2023

@author: P102MNPH1
"""

class Card:
    ''''''
    __values = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7,
              '8':8, '9':9, '10':10, 'A':1,
              'J':10, 'Q':10, 'K':10}
    def __init__(self, rank, suit):
        self.rank = rank.upper()
        self.suit = suit
        self.__set_value(rank)

    def __set_value(self, rank):
        self.value = Card.__values[rank]
        
    def __str__(self):
        return f'{self.rank}{self.suit} : {self.value}'
    
    def __repr__(self):
        return f'{self.rank}{self.suit}'