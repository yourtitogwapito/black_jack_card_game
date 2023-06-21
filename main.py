# -*- coding: utf-8 -*-
"""
Created on Thu Jun 15 14:22:59 2023

@author: P102MNPH1
"""

from player.player import Player, Dealer
from screen.screen import Screen

class Game():
    
    def __init__(self):
        self.screen = Screen()
        self.__get_number_of_players()
        self.dealer = Dealer('Dealer')
        self.scores = {}
        self.__create_players()
        self.player_bets = {}
        self.start_Game()
        #self.start_Game()

    def __get_number_of_players(self):
        self.screen.clear_screen()
        isnumber = False
        while not isnumber:
            try:
                self.number_of_players = int(input("Number of players: "))
                if self.number_of_players in [1,2]:
                    isnumber = True
                else:
                    isnumber =False
            except ValueError:
                print("Numbers only from 1 to 2")
                print("Try again")
                isnumber = False
                
    def __create_players(self):
        self.players = []
        for x in range(self.number_of_players):
            name = input(f'Player {x+1} name: ')
            player = Player(name)
            self.players.append(player)
    def __has_remaining_cards(self):
        total_players = len(self.players) +1
        minimum_cards = total_players * 4
        if len(self.dealer.deck) >= minimum_cards:
            return True
        else:
            return False

    def __has_remaining_pot(self):
        has_remaining_pot = True
        for player in self.players:
            if player.pot <= 0:
                print(f"{player.name}'s pot is 0")
                return False
                break
            else:
                return True
                
                
    def __compare_scores(self,player):
        '''return values:
            1 - player wins
            0 - tie
            -1 - dealer wins
        '''
        # print(self.dealer.show_Hand()
        scr_dealer = self.dealer.total_value
        scr_player = player.total_value
        
        if scr_dealer==scr_player or (scr_dealer>21 and scr_player>21):
            return 0
        elif (scr_dealer<22 and scr_dealer>scr_player) or (scr_dealer == 21 and scr_player != 21) or scr_player >21:
            return -1
        elif (scr_player<22 and scr_dealer<scr_player) or (scr_player == 21 and scr_dealer != 21) or scr_dealer >21:
            return 1
        else:
            print('outside [-1,0,1]')

    def __new_game(self):
        x = input("Press Y to start a new game: ").upper()
        if x == "Y":
            self.dealer.collect_From_Graveyard()
            return True
        else:
            print("Game Over!")
            print("Thanks for playing")
            input("")
            return False

    def show_all_player_details(self):
        for player in self.players:
            print(player)

    def show_all_hands(self):
        self.dealer.show_Hand()                
        for player in self.players:
            player.show_Hand()

    def first_deal(self):
        for x in range(2):
            self.dealer.get_Card()
            for player in self.players:
                self.dealer.deal_Card(player)
        #self.show_all_hands()

    def second_third_deal(self):
        for player in self.players:
            self.flash_screen()
            self.will_get_card(player)
            input("")
        self.flash_screen()
        self.dealer.will_Get_Card()
        #self.show_all_hands()

    def place_bets(self):#should be private
        for player in self.players:
            self.player_bets[player] = player.place_Bet()

    def show_bets(self):
        print('Player Bets:\n')
        for x in self.player_bets:
            print(f'{x.name} : {self.player_bets[x]}')

    def will_get_card(self, player):
        is_yes_or_no = False
        while not is_yes_or_no:
            print(f"{player.name}'s turn!\n1. Yes\n0. No")
            try:
                x = int(input("Get Card? (1/0): "))
                if x == 0:
                    print(f'\n{player.name} will not get card')
                    is_yes_or_no = True
                elif x == 1:
                    if len(player.hand) >= 4:
                        print('\nAlready with 4 cards or more')
                    else:
                        self.dealer.deal_Card(player)
                    is_yes_or_no = True
                else:
                    print('\n1 or 2 only')
                    is_yes_or_no = False
            except ValueError:
                print('\n1 or 2 only')
                is_yes_or_no = False
            
    # def start_Game(self):
    #     ''''''
    #     new_game = True
    #     while new_game:
    #         print("New Game!")
    #         self.dealer.shuffle()
    #         has_remaining_cards = True
    #         has_remaining_pot = True
    #         i = 1
    #         while has_remaining_cards and has_remaining_pot:
    #             print(f'Match {i}')
    #             print(self.dealer)
    #             self.show_all_hands()
    #             input("")
    #             self.place_bets()
    #             input("")
    #             self.first_deal()
    #             input("")
    #             self.show_bets()
    #             input("")
    #             for x in range(2): #second and third deal
    #                 self.second_third_deal()
    #                 input("")
    #             for player in self.players: # Compare total scores to see who wins
    #                 x = self.__compare_scores(player)
    #                 if x == 1:
    #                     player.wins(self.player_bets[player])
    #                     print(f'{player.name} wins!')
    #                 elif x == -1:
    #                     player.lost(self.player_bets[player])
    #                     print(f'{player.name} lost')
    #                 elif x == 0:
    #                     print(f'Dealer is tied with {player.name}')
    #                 else:
    #                     print(x)
    #                 print(f"{player.name}'s pot: {player.pot}\n")
    #                 print(f'Dealer: {self.dealer.total_value}')
    #                 print(f'{player.name}: {player.total_value}\n')    
    #                 self.player_bets[player]=0
    #                 input("")
    #             self.dealer.cards_To_Graveyard(self.players)
    #             input("")
    #             i += 1
    #             has_remaining_cards = self.__has_remaining_cards()
    #             has_remaining_pot = self.__has_remaining_pot()
            
    #         print(self.dealer)
    #         self.show_all_player_details()
    #         self.dealer.collect_From_Graveyard()
    #         new_game = self.__new_game()

    def start_Game(self):
        new_game = True
        while new_game:
            self.dealer.shuffle()
            has_remaining_cards = True
            has_remaining_pot = True
            while has_remaining_cards and has_remaining_pot:
                self.flash_screen()
                self.place_bets()
                
                self.flash_screen()
                self.first_deal()
                
                for x in range(2):
                    self.flash_screen()
                    self.second_third_deal()
                    self.flash_screen()
                    
                for player in self.players:
                    x = self.__compare_scores(player)
                    if x == 1:
                        player.wins(self.player_bets[player])
                        print(f'{player.name} wins!')
                    elif x == -1:
                        player.lost(self.player_bets[player])
                        print(f'{player.name} lost')
                    elif x == 0:
                        print(f'Dealer is tied with {player.name}')
                    else:
                        print(x)
                    self.player_bets[player]=0
                input("")
                
                self.flash_screen()
                self.dealer.cards_To_Graveyard(self.players)
                self.flash_screen()

                has_remaining_cards = self.__has_remaining_cards()
                has_remaining_pot = self.__has_remaining_pot()
                
            new_game = self.__new_game()
            
    def flash_screen(self):
        self.screen.clear_screen()
        print(self.screen.upper_box(self.players, self.dealer))
        print(self.screen.mid_box(self.players, self.dealer, self.player_bets))

if __name__ == '__main__':
    g = Game()