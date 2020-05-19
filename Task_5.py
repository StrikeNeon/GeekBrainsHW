# -*- coding: utf-8 -*-

#5
def seq_sum():
    s = 0
    while True:
        inp = input("input number sequence, input 00 to stop the program")
        data = inp.split()
        for num in data:
            if num == "00":
                return s
            else:
                s += int(num)
    
print(seq_sum())