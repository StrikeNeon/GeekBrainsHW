# -*- coding: utf-8 -*-

#1
run = True
while run == True:
    numb1 = int(input("First number "))
    op = str(input("op "))
    
    if op == "+":
        numb2 = int(input("Number to summ "))
        res = numb1 + numb2
        print(res)
    if op == "-":
        numb2 = int(input("Number to substract "))
        res = numb1 - numb2
        print(res)
    if op == "*":
        numb2 = int(input("Multiplier "))
        res = numb1 * numb2
        print(res)
    if op == "/":
        numb2 = int(input("Divisor "))
        while numb2==0:
            print("Division by 0")
            numb2 = int(input("Divisor "))
        res = numb1 / numb2
        print(res)
    if op == "//":
        numb2 = int(input("Divisor "))
        while numb2==0:
            print("Division by 0")
            numb2 = int(input("Divisor "))
        res = numb1 // numb2
        print(res)
    if op == "0":
        run = False
    else:print("operation is invalid")