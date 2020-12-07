# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 20:47:48 2020

@author: antho
"""
from typing import Tuple
from enum import Enum
import random

class Card:
    def __init__(self, rank: str, suit: str) -> None:
        self.suit = suit
        self.rank = rank
        self.hard, self.soft = self._points()
    def _points(self) -> Tuple[int, int]:
        return int(self.rank), int(self.rank)

class AceCard(Card):
    def _points(self) -> Tuple[int, int]:
        return 1, 11

class FaceCard(Card):
    def _points(self) -> Tuple[int, int]:
        return 10, 10
    
class Suit(str, Enum):
    Club = "♣"
    Diamond = "♦"
    Heart = "♥"
    Spade = "♠"
    
def card(rank: int, suit: Suit) -> Card:
    if rank == 1:
        return AceCard("A", suit)
    elif 2 <= rank < 11:
        return Card(str(rank), suit)
    elif 11 <= rank < 14:
        name = {11: "J", 12: "Q", 13: "K"}[rank]
        return FaceCard(name, suit)
    raise Exception("Design Failure")
 
""" Mapping and Class Objects """
def card2(rank: int, suit: Suit) ->  Card:
    class_ = {1: AceCard, 11: FaceCard, 12: FaceCard,
              13: FaceCard}.get(rank, Card)
    return class_(str(rank), suit)

""" Two Parallel Mappings """
def card5(rank: int, suit: Suit) -> Card:
    class_ = {1: AceCard, 11: FaceCard, 12: FaceCard,
              13: FaceCard}.get(rank, Card)
    rank_str = {1: 'A', 11: 'J', 12: 'Q',
                13: 'K'}.get(rank, str(rank))
    return class_(rank_str, suit)

""" Mapping to a Tuple of Values """
def car6(rank: int, suit: Suit) -> Card:
    class_, rank_str = {
        1: (AceCard, 'A'),
        11: (FaceCard, 'J'),
        12: (FaceCard, 'Q'),
        13: (FaceCard, 'K')
        }.get(rank, (Card, str(rank)))
    
    return class_(rank_str, suit)

""" Partial Function Solution """
def card7(rank: int, suit: Suit) -> Card:
    class_rank = {
        1: lambda suit: AceCard('A', suit),
        11: lambda suit: FaceCard('J', suit),
        12: lambda suit: FaceCard('Q', suit),
        13: lambda suit: FaceCard('K', suit),
        }.get(rank, lambda suit: Card(str(rank), suit))
    
    return class_rank(suit)

class CardFactory:
    def rank(self, rank: int) -> "CardFactory":
        self.class_, self.rank_str = {
            1: (AceCard, 'A'),
            11: (FaceCard, 'J'),
            12: (FaceCard , 'Q'),
            13: (FaceCard, 'K'),
            }.get(rank, (Card, str(rank)))
        
        return self
    
    def suit(self, suit: Suit) -> Card:
        return self.class_(self.rank_str, suit)
    
card8 = CardFactory()
card8 = [card8.rank(r+1).suit(s) for r in range(13) for s in Suit]

class Card3:
    def __init__(self, rank: str, suit: Suit,
                 hard: int, soft: int) -> None:
        self.rank = rank
        self.suit = suit
        self.hard = hard
        self.soft = soft
        
class NumberCard3(Card3):
    def __init__(self, rank: int, suit: Suit) -> None:
        super().__init__(rank, suit, rank, rank)
        
class AceCard3(Card3):
    def __init__(self, rank: int, suit: Suit) -> None:
        super().__init__('A', suit, 1, 11)

class FaceCard3(Card3):
    def __init__(self, rank: int, suit: Suit) -> None:
        rank_str = {11: 'J', 12: 'Q', 13: 'K'}[rank]
        super().__init__(rank_str, suit, 10, 10)










