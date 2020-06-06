# -*- coding: utf-8 -*-
#7
class ComplexNum():
    def __init__(self, real,imaginary):
        self.real = real
        self.imaginary = imaginary
        
    def __str__(self):
        return f"{self.real} + {self.imaginary}i"
    
    def __add__(self, other):
        return ComplexNum(self.real+other.real,self.imaginary+other.real)
    def __mul__(self, other):
        return ComplexNum((self.real*other.real) - (self.imaginary*other.imaginary), (self.real*self.imaginary)+(other.real*other.imaginary))
    
num1 = ComplexNum(3, 2)
num2 = ComplexNum(3, 1)
print(num1+num2)
print(num1*num2)