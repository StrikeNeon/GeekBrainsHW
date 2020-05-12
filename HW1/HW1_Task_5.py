# -*- coding: utf-8 -*-

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