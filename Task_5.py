# -*- coding: utf-8 -*-
#5
s = 0
with open("text1.txt", 'w+') as f_obj:
    f_obj.write(input("Enter number sequence: "))
    f_obj.seek(0)
    data = f_obj.read().split() 
    for i in data:
        s += int(i)
    print(f"Sequence sum is {s}")