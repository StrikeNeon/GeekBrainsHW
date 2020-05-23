# -*- coding: utf-8 -*-

#3
l5 = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
l5_1 = [el for el in l5 if l5.count(el) < 2]
print(l5_1)