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

#2
a = int(input("Input seconds "))
h=str(a//3600)
m=(a//60)%60
s=a%60
if m<10:
    m='0'+str(m)
else:
    m=str(m)
if s<10:
    s='0'+str(s)
else:
    s=str(s)
print(h+':'+m+':'+s)


#3
n = int(input("Input seconds "))
nsum = int(f"{n}")+int(f"{n}"+f"{n}")+int(f"{n}"+f"{n}"+f"{n}")
print(nsum)

#4
num = int(input("Number to analyse "))
maxd = 0
if num<0:
    num = -1
while num >0:
    if num%10>maxd:
        maxd = num%10
    num=num//10
print(maxd)

#5
profit = int(input("Profit: "))
costs = int(input("Costs: "))
if profit > costs:
    print(f"Profitable, {profit - costs}")
else:
    print("Loss, {profit - costs}")
profitability = profit/costs
print(f"Profitability: {profitability}")
numE = int(input("Number of employees: "))
print(f"Profit per employee: {(profit - costs)/numE}")

#6
a = int(input("First result: "))
b = int(input("Target result: "))
c = 2
while a < b:
    a += a/10
    print (f"Day {c}:", round(a, 2))
    c+=1
    
