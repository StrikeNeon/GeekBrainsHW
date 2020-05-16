# -*- coding: utf-8 -*-

#1
lis = [1,2,3.0,True, [1,2],{1:2}]
for item in lis:
    print(type(item))
    
#2
lis = [0,1,2,3,4,5]
if len(lis)%2==0:
    for item in range(len(lis)-1):
        lis[item], lis[item+1] = lis[item+1], lis[item]
else:
    for item in range(len(lis)-2):
        lis[item], lis[item+1] = lis[item+1], lis[item]

print(lis)

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
    
    
#4
string = "see you later alligator in a while crocodile aaaaaaaaab"
string2 = string.split(" ")
print(string2)
for item in string2:
    if len(item)<10:
        print(string2.index(item), item)
    else:print(string2.index(item), item[:10])
    
    
    
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
    
#6
count = 1
input_data = []
output_data = {}
print("Use exit as a name to stop input operation")
while True:
    item_data = {}
    print (f"Record {count}:")
    name = input("Enter item name ")
    if name == "exit": break
    else:
        price = int(input("Enter item price "))
        amount = int(input("Enter item amount "))
        cal = input("Enter item calculation measure ")
        item_data["name"] = name
        item_data["price"] = price
        item_data["amount"] = amount
        item_data["calculation measure"] = cal
        input_data.append((count, item_data))
print(input_data)
output_data["name"] = []
output_data["price"] = []
output_data["amount"] = []
output_data["calculation measure"] = []
for item in input_data:
    for key,value in item[1].items():
        output_data[key].append(value)
print(output_data)