# -*- coding: utf-8 -*-
#6
#file = input("Enter filename")
file = "class"
debug = {}
with open(f"{file}.txt", 'r') as read_file:
    for line in read_file.readlines():
        data = line.split()
        key = data[0].split(":")[0] #находим название предмета
        debug[key] = 0 #начальные ключевые значения
        for s in data:
            if "(лаб)" in s or "(л)" in s or "(пр)" in s: #находим часы
                debug[key] += int(s.split("(")[0]) #добавляем значения к ключу
print(debug)