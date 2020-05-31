# -*- coding: utf-8 -*-
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