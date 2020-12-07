# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 21:46:25 2020

@author: antho
"""
""" Example of unpleasent init method"""
from table import Table
from bettingStrategy import BettingStrategy
from gameStrategy import GameStrategy

class Player:
    def __init__(
            self,
            table: Table,
            bet_strategy: BettingStrategy,
            game_strategy:GameStrategy
            ) -> None:
        
        self.bet_strategy = bet_strategy
        self.game_strategy = game_strategy
        self.table = table
        
    def game(self):
        self.table.place_bet(self.bet_strategy.bet())
        self.hand = self.table_get_hand()
        if self.table.can_insure(self.hand):
            if self.game_strategy.insurance(self.hand):
                self.table.insure(self.bet_strategy.bet())
                

table = Table()
flat_bet = Flat()
dumb = GameStrategy()
p = Player(table, flat_bet, dumb)
p.game()

""" Implement keyword argument values """
class Player2(Player):
    def __init__(self, **kwargs) -> None:
        self.bet_strategy: BettingStrategy = kwargs['bet_strategy']
        self.game_strategy: GameStrategy = kwargs['game_strategy']
        self.table: Table = kwargs['table']
        
    def game(self) -> None:
        self.table.place_bet(self.bet_strategy.bet())
        self.hand =  self.table.get_hand()

p2 = Player2(table=table, bet_strategy=flat_bet, game_strategy=dumb)

class Player3(Player):
    def __init__(
            self,
            table: Table,
            bet_strategy: BettingStrategy,
            game_strategy: GameStrategy,
            **extras,
            ) -> None:
        
        self.bet_strategy = bet_strategy
        self.game_strategy = game_strategy
        self.table = table
        self.log_name: str = extras.pop("log_name", self.__class__.__name__)
        if extras:
            raise TypeError(f"Extra arguments: {extras!r}")