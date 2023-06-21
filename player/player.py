# -*- coding: utf-8 -*-
"""
Created on Thu Jun 15 13:16:01 2023

@author: P102MNPH1
"""
from deck.deck import Deck
import random


class Player:
    ''''''
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.total_value = 0
        self.pot = 1000

    def __str__(self):
        on_hand = []
        for card in self.hand:
            x = f'{card.rank}{card.suit}'
            on_hand.append(x)
        _on_hand = ", ".join(on_hand)
        return f'Name: {self.name}\nOn-Hand: {_on_hand}\nPot: {self.pot}\nValue: {self.total_value}\n'

    def receive_Card(self,card):
        self.hand.append(card)
        self.total_value += card.value
    
    def show_Hand(self):
        if len(self.hand) == 0:
            return ''
        else:
            return ", ".join([f'{card.rank}{card.suit}' for card in self.hand])

    def drop_On_Hand(self):
        l = self.hand
        self.hand = []
        self.total_value = 0
        return l
    
    def place_Bet(self):
        is_num = False
        is_exceed = True
        while not is_num or is_exceed:
            try:
                print(f"\n{self.name}'s pot: {self.pot}")
                bet = int(input(f"Place your bet {self.name}: "))
                if 0 <= bet <= self.pot:
                    return bet
                else:
                    print('Place bet less than or equal to your pot')
                    print(f'Pot: {self.pot}')
                    is_exceed = True
            except ValueError:
                print('Numbers only!')
    
    def wins(self,bet):
        self.pot += bet
    
    def lost(self,bet):
        self.pot -= bet
        
#    def hit_card(self):
        
        

class Dealer(Player):
    
    def __init__(self,name):
        Player.__init__(self, name)
        self.__set_deck()
        self.graveyard = []

    def __set_deck(self):
        self.__deck = Deck()
        self.deck = self.__deck.deck
        self.shuffle()

    # def __str__(self):
    #     return f'Name: {self.name}\n{self.__show_deck_info()}'

    def __repr__(self):
        return f'Name: {self.name}\n{self.__show_deck_info()}'
        # on_hand = []
        # for card in self.hand:
        #     x = f'{card.rank}{card.suit}'
        #     on_hand.append(x)
        # _on_hand = ", ".join(on_hand)
        # return f'Name: {self.name}\nOn-Hand: {_on_hand}\nPot: {self.pot}\nValue: {self.total_value}\n'
    
    def __show_deck_info(self):
        string = f'Deck : {len(self.deck)}\nUnique Cards: {len(set(self.deck))}\nGraveyard: {len(self.graveyard)}\n'
        return string

    def shuffle(self):
        if len(self.deck) != 52:
            print("Can't Shuffle deck. finish game first")
            print("Cards on Deck: {len(self.deck)}")
            print("Cards on Graveyard : {len(self.graveyard)}")
        else:
            random.shuffle(self.deck)

    def deal_Card(self,player):
        card = self.deck[0]
        print(f"Your Card: {card}")
        self.deck.remove(card)
        player.receive_Card(card)
    
    def get_Card(self):
        card = self.deck[0]
        self.deck.remove(card)
        self.receive_Card(card)
    
    def cards_To_Graveyard(self,players):
        self.graveyard += self.drop_On_Hand()
        for player in players:
            self.graveyard += player.drop_On_Hand()
    
    def collect_From_Graveyard(self):
        self.deck += self.graveyard
        self.graveyard = []
        self.__show_deck_info()
        print(f'graveyard: {len(self.graveyard)}')
    
    def will_Get_Card(self):
        _onhand = len(self.hand)
        if _onhand < 4 and self.total_value <19:
            print('Dealer will get card')
            self.get_Card()
        else:
            print('Dealer will not get additional card')
            
        input("")
        
        
            