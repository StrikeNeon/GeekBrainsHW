# -*- coding: utf-8 -*-

#2
lis1 = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
lis2 = [lis1[i] for i in range(1, len(lis1)) if lis1[i]>lis1[i-1]]
print(lis2)

lis3 = [i for i in range(20, 240) if i%20==0 or i%21==0]
print(lis3)