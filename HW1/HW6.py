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
            
#light = TraficLight2()
#light.running()

#2
class Road():
    def __init__(self, length, width):
        self._length = length
        self._width = width
        
    def calc(self, thickness):
        return self._width * self._length * 25 * thickness
    
r1 = Road(5000, 20)
print(f"{r1.calc(5)/1000} tons of asphalt needed to cover the road")


#3
class Worker():
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}
        
        
class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__( name, surname, position, wage, bonus)
        
    def get_full_name(self):
        print(self.name, self.surname)
    def get_total_income(self):
        print(f"income is: {self._income['wage']+self._income['bonus']}")

pos = Position("name", "surname", "position", 10, 5)
pos.get_full_name()
pos.get_total_income()

#4
class Car():
    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = False
    def go(self):
        return f"Car {self.name} is going"
    def stop(self):
        return f"Car {self.name} has stopped"
    def turn(self, direction):
        return f"Car {self.name} has turned {direction}"
    def show_speed(self):
        return f"Car {self.name} is going at {self.speed} km\h"
    
class TownCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)
    def show_speed(self):
        if self.speed>60:
            return f"Car {self.name} is going over the speed limit at {self.speed} km\h" 
        else:
            return f"Car {self.name} is going at {self.speed} km\h"    

class SportCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)

class WorkCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)
    def show_speed(self):
        if self.speed>40:
            return f"Car {self.name} is going over the speed limit at {self.speed} km\h" 
        else:
            return f"Car {self.name} is going at {self.speed} km\h" 

class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)
        self.is_police = True

car1 = Car(200, "red", "1")
print(car1.go())
print(car1.stop())
print(car1.turn("left"))
print(car1.show_speed())

car2 = TownCar(200, "red", "TownCar")
print(car2.go())
print(car2.stop())
print(car2.turn("left"))
print(car2.show_speed())

car3 = SportCar(200, "red", "SportCar")
print(car3.go())
print(car3.stop())
print(car3.turn("left"))
print(car3.show_speed())

car4 = PoliceCar(200, "red", "PoliceCar")
print(car4.is_police)
print(car4.go())
print(car4.stop())
print(car4.turn("left"))
print(car4.show_speed())

car5 = WorkCar(200, "red", "WorkCar")
print(car5.go())
print(car5.stop())
print(car5.turn("left"))
print(car5.show_speed())


#5
class Stationary():
    def __init__(self):
        self.title = "stationary"
    def draw(self):
        return f"Drawing with a {self.title}"
    
class Pen(Stationary):
    def __init__(self):
        super().__init__()
        self.title = "pen"
    def draw(self):
        return f"Drawing with a {self.title}"
    
class Pencil(Stationary):
    def __init__(self):
        self.title = "pencil"
    def draw(self):
        return f"Drawing with a {self.title}"
    
class Handle(Stationary):
    def __init__(self):
        self.title = "handle"
    def draw(self):
        return f"Drawing with a {self.title}"
    
s = Stationary()
print(s.title)
print(s.draw())

pen = Pen()
print(pen.title)
print(pen.draw())

pencil = Pencil()
print(pencil.title)
print(pencil.draw())

handle = Handle()
print(handle.title)
print(handle.draw())