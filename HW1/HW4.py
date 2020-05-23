# -*- coding: utf-8 -*-
from functools import reduce
from itertools import count, cycle

#2
lis1 = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
lis2 = [lis1[i] for i in range(1, len(lis1)) if lis1[i]>lis1[i-1]]
print(lis2)

lis3 = [i for i in range(20, 240) if i%20==0 or i%21==0]
print(lis3)

#3
l5 = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
l5_1 = [el for el in l5 if l5.count(el) < 2]
print(l5_1)

#4
def multiply(prev_el, el):
    return prev_el* el
l6 = [i for i in range(100, 1001)]
print(reduce(multiply, l6))

#5
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
        
print("----------------")
#6
def generator(n):
    s = 1
    for el in range(1, n+1):
        s *= el 
        yield s


for el in generator(4):
    print(el)