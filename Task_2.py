# -*- coding: utf-8 -*-

#2
class Road():
    def __init__(self, length, width):
        self._length = length
        self._width = width
        
    def calc(self, thickness):
        return self._width * self._length * 25 * thickness
    
r1 = Road(5000, 20)
print(f"{r1.calc(5)/1000} tons of asphalt needed to cover the road")