# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 21:43:23 2020

@author: antho
"""
""" Wrapping a collection class"""
import random
from card import card, Suit, Card

class Deck:
	def __init__(self) -> None: 
		self._cards = [card(r+1, s) for r in range(13)
					for s in iter(Suit)]
		random.shuffle(self._cards)
			
	def pop(self) -> Card:
		return self._cards.pop()
		
d = Deck()
hand = [d.pop(), d.pop()]

""" Extending a collection class"""
class Deck2(list):
	def __init__(self) -> None:
		super().__init__(card(r+1, s) 
			for r in range(13) for s in iter(Suit))		
		
		random.shuffle(self)

""" Include burned Card"""
class Deck3(list):
    def __init__(self, decks: int = 1) -> None:
        super().__init__()
        for i in range(decks):
            self.extend(
                card(r+1, s)
                for r in range(13) for s in iter(Suit)
                )
        random.shuffle(self)
        burn = random.randint(1, 52)
        for _ in range(burn):
            self.pop()