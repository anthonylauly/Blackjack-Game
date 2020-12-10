# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 21:43:55 2020

@author: antho
"""
from card import Card, Suit
from deck import Deck

class Hand:
    def __init__(self, dealer_card: Card) -> None:
        self.dealer_card: Card = dealer_card
        self.cards: List[Card] = []
    
    def hard_total(self) -> int:
        return sum(c.hard for c in self.cards)
    
    def soft_totsl(self) -> int:
        return sum(c.soft for c in self.cards)
    
    def __str__(self) -> str:
        return ", ".join(map(str, self.cards))
    
    def __repr__(self) -> str:
        cards_text = ", ".join(map(repr, self.cards))
        return f"{self.__class__.__name__}({self.dealer_card!r}, {cards_text})"
    
    def __format__(self, spec: str) -> str:
        if spec == "":
            return str(self)
        return ", ".join(f"{c:{spec}}" for c in self.cards)
    
d = Deck()
h = Hand(d.pop())
h.cards.append(d.pop())
h.cards.append(d.pop())

class Hand2:
    def __init__(self, dealer_card: Card, *cards: Card)-> None:
        self.dealer_card = dealer_card
        self.cards = list(cards)
    
    def card_append(self, card: Card) -> None:
        self.cards.append(card)
    
    def hard_total(self) -> int:
        return sum(c.hard for c in self.cards)
    
    def soft_total(self) -> int:
        return sum(c.soft for c in self.cards)
    
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.dealer_card!r}, *{self.cards})"

d = Deck()
h = Hand2(d.pop(), d.pop(), d.pop())

from typing import overload, Union, Optional, List, cast
""" Overloading Built-in Method"""
class Hand3:
    @overload
    def __init__(self, arg1: "Hand3") -> None:
        ...
    
    @overload
    def __init__(self, arg1: Card, arg2: Card, arg3: Card) -> None:
        ...
        
    def __init__(self, arg1: Union[Card, "Hand3"], arg2: Optional[Card] = None,
                 arg3: Optional[Card] = None) -> None:
        
        self.dealer_card: Card
        self.cards: List[Card]
        
        if isinstance(arg1, Hand3) and not arg2 and not arg3:
            #Clone an existing hand
            self.dealer_card = arg1.dealer_card
            self.cards = arg1.cards
        
        elif(isinstance(arg1, Card) and isinstance(arg2, Card)
             and isinstance(arg3, Card)):
            
            #Build a fresh, new hand
            self.dealer_card = cast(Card, arg1)
            self.cards = [arg2, arg3]
            
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.dealer_card!r}, *{self.cards})"
        
""" Multi-Strategy Initialization """		
class Hand4:
    @overload
    def __init__(self, arg1: "Hand4") -> None:
        ...
    
    @overload
    def __init__(self, arg1: "Hand4", arg2: Card, *,
                 split: int) -> None:
        ...
        
    @overload
    def __init__(self, arg1: Card, arg2: Card, 
                 arg3: Card) -> None:
        ...
    
    def __init__(self, arg1: Union["Hand4", Card],
                 arg2: Optional[Card] = None,
                 arg3: Optional[Card] = None,
                 split: Optional[int] = None,) -> None:
       
        self.dealer_card: Card
        self.cards: List[Card]
        
        if isinstance(arg1, Hand4):
            self.dealer_card = arg1.dealer_card
            self.cards = arg1.cards
            
        elif isinstance(arg1, Hand4) and isinstance(arg2, Card) and "split" is not None:
            
            self.dealer_card = arg1.dealer_card
            self.cards = [arg1.cards[split], arg2]
            
        elif (isinstance(arg1, Card) and isinstance(arg2, Card) and isinstance(arg3, Card)):
            self.dealer_card = arg1
            self.cards = [arg2, arg3]
        
        else:
            raise TypeError("Invalid constructor {arg1!r} {arg2!r} {arg3!r}")
        
    def __str__(self) -> str:
        return ", ".join(map(str, self.cards))
    
d = Deck()
h = Hand4(d.pop(), d.pop(), d.pop())
s1 = Hand4(h, d.pop(), split=0)
s2 = Hand4(h, d.pop(), split=1)

""" Implementing staticmethods as surrogate cunstructor """		
class Hand5:
    def __init__(self, dealer_card: Card, *cards: Card) -> None:
        self.dealer_card = dealer_card
        self.cards = list(cards)
        
    @staticmethod
    def freeze(other) -> "Hand5":
        hand = Hand5(other.dealer_card, *other.cards)
        return hand
    
    @staticmethod
    def split(other, card0, card1) -> Tuple["Hand5", "Hand5"]:
        hand0 = Hand5(other.dealer_card, other.cards[0], card0)
        hand1 = Hand5(other.dealer_card, other.cards[1], card1)
        return hand0, hand1
    
    def __str__(self) -> str:
        return ", ".join(map(str, self.cards))

d = Deck()
h = Hand5(d.pop(), d.pop(), d.pop())
s1, s2 = Hand5.split(h, d.pop(), d.pop())