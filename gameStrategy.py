# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 21:46:52 2020

@author: antho
"""
from hand import Hand

""" (dumb) strategy to pick cards and decline other bets """
class GameStrategy:
    def insurance(self, hand: Hand) -> bool:
        return False
    
    def split(self, hand: Hand) -> bool:
        return False
    
    def double(self, hand: Hand) -> bool:
        return False
    
    def hit(self, hand: Hand) -> bool:
        return sum(c.hard for c in hand.cards) <= 17
    
dumb = GameStrategy()