# -*- coding: utf-8 -*-
#3
#file = input("Enter filename")
file = "sal"
med_wages = 0
with open(f"{file}.txt", 'r') as f_obj:
    data = f_obj.readlines()
    for line in data:
        name, salary = line.split()     
        med_wages+=int(salary)
        if int(salary) <20000:
            print(name)
    med_wages = med_wages/len(data)
    print(med_wages)