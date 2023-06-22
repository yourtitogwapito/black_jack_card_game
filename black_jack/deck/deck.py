# -*- coding: utf-8 -*-
"""
Created on Thu Jun 15 11:15:50 2023

@author: P102MNPH1
"""
from card.card import Card

class Deck:
    __ranks = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
    __suits = ['♣','♦','♥','♠']

    def __init__(self):
        self.__create_deck()
        
    def __create_deck(self):
        self.deck = []
        for rank in Deck.__ranks:
            for suit in Deck.__suits:
                card = Card(rank, suit)
                self.deck.append(card)

    def __str__(self):
        cards = []
        for card in self.deck:
            string = f'{card.rank}{card.suit}'
            cards.append(string)
        return f'Deck : {len(cards)} Cards\nCards: {", ".join(cards)}'
    