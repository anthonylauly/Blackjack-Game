# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 21:46:34 2020

@author: antho
"""
class BettingStrategy:
    def bet(self) -> int:
        raise NotImplementedError("No bet method")
    
    def record_win(self) -> None:
        pass
    
    def record_loss(self) -> None:
        pass
    
class Flat(BettingStrategy):
    def bet(self) -> int:
        return 1

import abc
from abc import abstractmethod

class BettingStrategy2(metaclass=abc.ABCMeta):
    
    @abstractmethod
    def bet(self) -> int:
        return 1
    
    def record_win(self):
        pass
    
    def record_loss(self):
        pass
