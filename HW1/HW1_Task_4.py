# -*- coding: utf-8 -*-

#4
num = int(input("Number to analyse "))
maxd = 0
if num<0:
    num = -1
while num >0:
    if num%10>maxd:
        maxd = num%10
    num=num//10
print(maxd)