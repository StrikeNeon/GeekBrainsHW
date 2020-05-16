# -*- coding: utf-8 -*-

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