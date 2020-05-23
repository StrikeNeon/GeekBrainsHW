# -*- coding: utf-8 -*-

#6
def generator(n):
    s = 1
    for el in range(1, n+1):
        s *= el 
        yield s


for el in generator(4):
    print(el)