# -*- coding: utf-8 -*-
#1

with open("files/text.txt", 'w+') as f_obj:
    while True:
        data = input("Input data: ")+'\n'
        if data==""+'\n':
            break
        else:f_obj.write(data)