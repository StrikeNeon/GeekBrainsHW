# -*- coding: utf-8 -*-
#3
class NaN(Exception):
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
        
lis = []
while True:
    el = input("enter number ")
    if el != "stop":
        try:
            el = int(el)
            lis.append(el)
        except ValueError:
            raise NaN()
    else:
        break