# -*- coding: utf-8 -*-

#3
num = 11
seas = [[12,1,2],[3,4,5],[6,7,8],[9,10,11]]
if num <0 or num >12:
    print("invalid")
for item in seas:
    for i in item:
        if i == num:
            if seas.index(item)==0:
                print("winter")
            elif seas.index(item)==1:
                print("spring")
            elif seas.index(item)==2:
                print("summer")
            else:
                print("fall")

seasons = {"winter":[12,1,2], "spring":[3,4,5], "summer":[6,7,8], "fall":[9,10,11]}
for key,value in seasons.items():
    if num in value:
        print(key)