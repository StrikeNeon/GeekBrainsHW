# -*- coding: utf-8 -*-

#5
seq = [7, 5, 3, 3, 2]
s_min, s_max = min(seq), max(seq)
print("Input -1 to exit")
while True:
    num = (int(input("Enter a number ")))
    if num == -1: # Inputing -1 will end the loop
        break
    else:
        if num >= s_max: #Number equal or over maximum will put in the beginning of the list 
            seq.insert(0,num)
            s_max = max(seq)
        elif num <= s_min: #Ditto, but with minimal number added to the end
            seq.append(num)
            s_min = min(seq)
        else:#For numbers between min and max (works with reverse indexes)
            i = -1
            while i != range(len(seq)*(-1)):
                if seq[i*(-1)] < num:
                    seq.insert(i*(-1), num)
                    break
                i -=1
print(seq)