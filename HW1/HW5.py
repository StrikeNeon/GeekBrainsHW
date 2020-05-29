# -*- coding: utf-8 -*-


#1

with open("text.txt", 'w+') as f_obj:
    while True:
        data = input("Input data: ")+'\n'
        if data==""+'\n':
            break
        else:f_obj.write(data)
      
#2
with open("text.txt", 'r') as f_obj:
    data = f_obj.readlines()
    print(f"The file has {len(data)+1} lines")
    for line in data:
        print(f"line {data.index(line)+1} has {len(line.split())} word(s)")
 
#3
#file = input("Enter filename")
file = "sal"
med_wages = 0
with open(f"{file}.txt", 'r') as f_obj:
    data = f_obj.readlines()
    for line in data:
        name, salary = line.split()     
        med_wages+=float(salary)
        if float(salary) <20000:
            print(name)
    med_wages = med_wages/len(data)
    print(med_wages)

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
            
#5
s = 0
with open("text1.txt", 'w+') as f_obj:
    f_obj.write(input("Enter number sequence: "))
    f_obj.seek(0)
    data = f_obj.read().split() 
    for i in data:
        s += int(i)
    print(f"Sequence sum is {s}")


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


#7
from json import dump
#file = input("Enter filename")
file = "firms"
debug = []
with open(f"files/{file}.txt", 'r') as read_file:
    firms, avg = {}, {}
    avg["average_profit"] = 0
    c =0 
    for line in read_file.readlines():
        data = line.split()
        if int(data[2]) - int(data[3].split(".")[0]) >0:
            firms[data[0]] = int(data[2]) - int(data[3].split(".")[0])
            print(int(data[2]) - int(data[3].split(".")[0]))
            avg["average_profit"] += int(data[2]) - int(data[3].split(".")[0])
            c +=1
        else:pass
    print(c)
    print(avg["average_profit"])
    avg["average_profit"] = avg["average_profit"]/c
    print(avg["average_profit"])
    debug.append(avg)
    debug.insert(0,firms)
print(debug)
with open(f"out.json", 'w') as write_file:
    dump(debug, write_file)
