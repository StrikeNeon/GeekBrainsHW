# -*- coding: utf-8 -*-
#2
with open("files/text.txt", 'r') as f_obj:
    data = f_obj.readlines()
    print(f"The file has {len(data)+1} lines")
    for line in data:
        print(f"line {data.index(line)+1} has {len(line.split())} word(s)")