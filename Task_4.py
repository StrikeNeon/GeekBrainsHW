# -*- coding: utf-8 -*-
from functools import reduce
#4
def multiply(prev_el, el):
    return prev_el* el
l6 = [i for i in range(100, 1001)]
print(reduce(multiply, l6))