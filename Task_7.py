# -*- coding: utf-8 -*-
#7
from json import dump
#file = input("Enter filename")
file = "firms"
debug = []
with open(f"{file}.txt", 'r') as read_file:
    firms, avg = {}, {}
    avg["average_profit"] = 0
    c =1 
    for line in read_file.readlines():
        data = line.split()
        if int(data[2]) - int(data[3].split(".")[0]) >0:
            firms[data[0]] = int(data[2]) - int(data[3].split(".")[0])
            avg["average_profit"] += int(data[2]) - int(data[3].split(".")[0])
            c +=1
        else:pass
    if avg["average_profit"] >0:
        avg["average_profit"] = avg["average_profit"]/c
        debug.append(avg)
    else:
        saved = avg["average_profit"]
        avg["average_profit"] = f"Conglomerate loss: {saved}"
        debug.append(avg)
    debug.insert(0,firms)
print(debug)
with open(f"out.json", 'w') as write_file:
    dump(debug, write_file)