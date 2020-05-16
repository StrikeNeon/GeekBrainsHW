# -*- coding: utf-8 -*-
#4
string = "see you later alligator in a while crocodile aaaaaaaaab"
string2 = string.split(" ")
print(string2)
for item in string2:
    if len(item)<10:
        print(string2.index(item), item)
    else:print(string2.index(item), item[:10])