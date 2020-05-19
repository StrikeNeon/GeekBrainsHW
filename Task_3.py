# -*- coding: utf-8 -*-

#3
def my_func(a,b,c):
    if a>=b>=c or b>=a>=c:
        return a+b
    elif c>=b>=a or b>=c>=a:
        return c+b
    elif c>=a>=b or a>=c>=b:
        return c+a
print(my_func(2,5,3))