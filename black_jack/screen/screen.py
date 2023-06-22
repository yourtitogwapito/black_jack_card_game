# -*- coding: utf-8 -*-
"""
Created on Wed Jun 21 10:41:41 2023

@author: P102MNPH1
"""
import os, sys

class Screen:
    def __init__(self):
        self.length = 70

    def clear_screen(self):
        os.system('cls')
        os.system('clear')
        
    
    def upper_box(self,players,dealer):
        l_indent = "|  " #len = 3
        r_indent = "  |" #len = 3
        deck = "Deck: {}".format(len(dealer.deck))
        graveyard = "Graveyard: {}".format(len(dealer.graveyard))
        pot_money = "Pot Money"
        mid_space = get_mid_space(l_indent,deck,graveyard,r_indent,length=70)
        a_line = "-"*70
        b_line = l_indent+" "*64 + r_indent
        c_line = "{}{}{}{}{}".format(l_indent, deck,mid_space,graveyard,r_indent )
        d_line = "{}{}{}{}".format(l_indent,pot_money,get_mid_space(l_indent,r_indent,pot_money,length=70),r_indent)
        e_line = ""
        for player in players:
            name_pot = f'    {player.name}: {player.pot}'
            mid_space = get_mid_space(l_indent,name_pot,r_indent,length=70)
            if player == players[-1]:
                e_line = e_line + l_indent + name_pot + mid_space + r_indent
            else:
                e_line = e_line + l_indent + name_pot + mid_space + r_indent + os.linesep
    
        top_box_=f"{a_line}\n{b_line}\n{c_line}\n{b_line}\n{d_line}\n{e_line}\n{b_line}\n{a_line}"
        return top_box_        
    
    def mid_box(self, players,dealer,bets):
        """
        |<--name---><-:-><-bets-><----hand----><-------value------->|
        3<----10----><-4-><--10--><---20-------><--------20--------->3
        """
        l_indent = "|  " #len = 3
        r_indent = "  |" #len = 3
        a_line = "-"*70
        b_line = l_indent+" "*64 + r_indent
        
        colon = " :  "
        bet =  "Bets      "
        hand = "Hand                "
        tot_value = "Value" + get_mid_space("value", length= 20)
        c_line = l_indent + (" "*10) + (" "*4) +  bet + hand + tot_value + r_indent
        
        dealer_ = '{}{}'.format(get_mid_space(dealer.name, length = 10),dealer.name,)
        dealer_bets = "----      "
        show_hand = dealer.show_Hand()
        dealer_hand = '{}{}'.format(show_hand, get_mid_space(show_hand, length = 20))
        dealer_value = '{}{}'.format(dealer.total_value, get_mid_space(str(dealer.total_value), length = 20))
        
        d_line = l_indent + dealer_ + colon + dealer_bets + dealer_hand +  dealer_value + r_indent
        
        e_line = ""
        for player in players:
            name = '{}{}'.format(get_mid_space(player.name, length=10),player.name,)
            if len(bets) == 0:
                bet = ' '*10
            else:
                bet = '{}{}'.format(bets[player], get_mid_space(str(bets[player]), length=10))
            show_hand = player.show_Hand()
            hand = show_hand + get_mid_space(show_hand, length=20)
            value = '{}{}'.format(str(player.total_value), get_mid_space(str(player.total_value), length=20))
            if player == players[-1]:
                e_line = e_line + l_indent + name + colon + bet + hand + value + r_indent
            else:
                e_line = e_line + l_indent + name + colon + bet + hand + value + r_indent + os.linesep
        
        return f'{b_line}\n{c_line}\n{d_line}\n{e_line}\n{b_line}\n{a_line}'        
        
        
def get_mid_space(*args, length):
    string = ''.join(args)
    return " "*(length-len(string))        
        

        

