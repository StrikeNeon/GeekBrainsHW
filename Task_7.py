# -*- coding: utf-8 -*-
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