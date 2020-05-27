# -*- coding: utf-8 -*-
#4
file = "1234"
conv = {1:"Один", 2: "Два", 3:"Три",
        4:"Четыре", 5:"Пять",6:"Шесть",
        7:"Семь",8:"Восемь",9:"Девять"}
with open(f"{file}.txt", 'r') as read_file:
    with open("output.txt", 'w+') as write_file:
        data = read_file.readlines()
        for line in data:
            data = line.split()    
            write_file.write(f'{conv[int(data[2])]} {data[1]} {data[2]}\n')