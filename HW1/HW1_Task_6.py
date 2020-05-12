# -*- coding: utf-8 -*-

#6
a = int(input("First result: "))
b = int(input("Target result: "))
c = 2
while a < b:
    a += a/10
    print (f"Day {c}:", round(a, 2))
    c+=1
    