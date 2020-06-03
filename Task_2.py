# -*- coding: utf-8 -*-
#2
from abc import ABC,abstractmethod

class Clothes(ABC):
    
    @abstractmethod
    def expenditure(self):
        return 0
    
    def __add__(self, other):
        return self.expenditure + other.expenditure
    
class Coat(Clothes):
    def __init__(self, V):
        self.V = V
        
    @property
    def expenditure(self):
        return self.V/6.5+0.5
    
class Suit(Clothes):
    def __init__(self, H):
        self.H = H
        
    @property
    def expenditure(self):
        return 2 * self.H + 0.3
    
coat = Coat(5)
suit = Suit(5)

print(coat.expenditure, suit.expenditure)
print(coat+suit)