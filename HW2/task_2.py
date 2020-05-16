# -*- coding: utf-8 -*-

#2
lis = [0,1,2,3,4,5]
if len(lis)%2==0:
    for item in range(len(lis)-1):
        lis[item], lis[item+1] = lis[item+1], lis[item]
else:
    for item in range(len(lis)-2):
        lis[item], lis[item+1] = lis[item+1], lis[item]

print(lis)