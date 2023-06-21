# -*- coding: utf-8 -*-
"""
Created on Thu Jun 15 13:07:02 2023

@author: P102MNPH1
"""

from deck.deck import Deck
from player.player import Player
import random

class Dealer(Player):
    
    def __init__(self):
        self.__set_deck()

    def __set_deck(self):
        d = Deck()
        self.deck = d.deck
        self.Shuffle()

    def Shuffle(self):
        random.shuffle(self.deck)

    # def Distribute_Cards(self):
        