# -*- coding: utf-8 -*-
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
    def __mul__(self, other):
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

#тест функции make_order            
cell = Cell(6)
print(cell.make_order(4))
cell = Cell(6)
print(cell.make_order(3))
cell = Cell(6)
print(cell.make_order(1))

#тест перегрузки арифметики
cell1 =Cell(10)
cell2 =Cell(5)
print(f"addition: {cell1+cell2}, substraction: {cell1-cell2}, multiplication: {cell1*cell2}, division: {cell1/cell2}")