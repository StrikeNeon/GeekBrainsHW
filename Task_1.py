# -*- coding: utf-8 -*-

#1
from time import sleep
from itertools import cycle

class TraficLight1():
    def __init__(self):
        self.__color = ("\033[31mred","\033[33myellow","\033[32mgreen")#это слишком просто
        self.__state = (7, 2, 7) 
        
    def running(self):
        for i in cycle([0,1,2]):
            print(self.__color[i])
            sleep(self.__state[i])
            
#light = TraficLight1()
#light.running()


class TraficLight2():
    def __init__(self):
        self.__color = ""#это сложнее но хуже
        
    def running(self):
        for i in cycle(["\033[31mred","\033[33myellow","\033[32mgreen"]):
            self.__color = i
            print(self.__color)
            if i == "red":
                sleep(7)
            elif i == "yellow":
                sleep(2)
            else:
                sleep(7)
            
light = TraficLight2()
light.running()