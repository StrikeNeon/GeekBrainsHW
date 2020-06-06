# -*- coding: utf-8 -*-
#2
class ZeroDiv(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None
    def __str__(self):
        if self.message:
            return self.message
        else:
            return "element is not a number"
        
a,b = 10, 2
if b ==0:
    raise ZeroDiv("divided by zero")
else: print(a/b)