# -*- coding: utf-8 -*-
from sys import argv

try:
    name, hours, pay_per_hour, bonus = argv
    computed = (int(hours) * int(pay_per_hour))+int(bonus)
    print("salary is ", computed)
except ValueError:
    print("no arguments or insufficent arguments")