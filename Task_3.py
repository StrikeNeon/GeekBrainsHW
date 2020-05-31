# -*- coding: utf-8 -*-
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