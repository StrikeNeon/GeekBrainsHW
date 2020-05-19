# -*- coding: utf-8 -*-

#4
def power1(x,y):
    return 1/x**y

def power2(x,y):
    i = x
    while y !=1:
        x *= i
        y -=1
    return 1/x

print(power1(2,2), power2(2,2))