# -*- coding: utf-8 -*-
from itertools import count, cycle
#5
l5 = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
n=20
for el in count(1):
    if el > n:
        break
    else:
        print(el)

c=0        
for el in cycle(l5):
    if c > len(l5)-1:
        break
    print(el)
    c+=1