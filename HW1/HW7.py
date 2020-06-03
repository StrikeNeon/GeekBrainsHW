# -*- coding: utf-8 -*-

#1
class Matrix():
    
    def __init__(self, data):
        if type(data) != list or type(data[0]) != list:
            raise TypeError("A matrix has to be a list of lists")
        self.data = data
        
    def __str__(self):
        mat = ""
        for i in self.data:
            mat += str(i) + '\n'
        return mat
    
    def __add__(self, other):
        newmat = []
        if len(self.data) != len(other.data):
            raise ValueError("matrices have to have equal length")
        for i in range(len(self.data)):
            layer = []
            for j in range(len(self.data[i])):
                if len(self.data[i]) != len(other.data[i]):
                    raise ValueError(f"array {i+1} is unequal in length")
                layer.append((self.data[i][j]+other.data[i][j]))
            newmat.append(layer)
        return Matrix(newmat)
                
        
mat1 = Matrix([[1,1], [2,2],[3,3]])
print(mat1)

mat2 = Matrix([[1,2], [2,3],[3,4]])
print(mat2)

print(mat1+mat2)

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

#3
class Cell():
    def __init__(self, amt):
        self.amt = amt
    def __add__(self, other):
        return self.amt + other.amt
    def __sub__(self,other):
        if self.amt >0 or other.amt>0:
            if self.amt>other.amt:
                return self.amt - other.amt
            else:
                return other.amt - self.amt
        else: raise ValueError("one or more cells is below 0")
    def __mul___(self, other):
        return self.amt * other.amt
    def __truediv__(self, other):
        return self.amt//other.amt
    def make_order(self, one_row):
        s = ''
        i = self.amt
        while i >one_row:
            s += '*'*one_row+'\n'
            i-=one_row
        s += '*'*i+'\n'
            
        return s
            
cell = Cell(6)
print(cell.make_order(4))
cell = Cell(6)
print(cell.make_order(3))
cell = Cell(6)
print(cell.make_order(1))