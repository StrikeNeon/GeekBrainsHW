# -*- coding: utf-8 -*-
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