"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на
две равные части: в одной находятся элементы, которые не меньше медианы,
в другой – не больше медианы.

Задачу можно решить без сортировки исходного
массива.

Но если это слишком сложно, то используйте метод сортировки,
который не рассматривался на уроках: Шелла, Гномья, ...

arr[m]
from statistics import median
"""
def makearr(N):
    arr = [0]*N
    
    for i in range(N):
        arr[i] = random.randint(0,N)
    return arr

#3
def cyclesort(array): 
  writes = 0
  for cycleStart in range(0, len(array) - 1): 
    item = array[cycleStart] 

    pos = cycleStart 
    for i in range(cycleStart + 1, len(array)): 
      if array[i] < item: 
        pos += 1

    if pos == cycleStart: 
      continue

    while item == array[pos]: 
      pos += 1
    array[pos], item = item, array[pos] 
    writes += 1

    while pos != cycleStart: 
      pos = cycleStart 
      for i in range(cycleStart + 1, len(array)): 
        if array[i] < item: 
          pos += 1
        
      while item == array[pos]: 
        pos += 1
      array[pos], item = item, array[pos] 
      writes += 1
    
  return array 


import random

print("_"*10)
print("cyclesort")
print("_"*10)
N = 2*int(input())+1
a = makearr(N)
print("\n array created: ", a)
print("\n array sorted: ", cyclesort(a))
print("median found:", a[N//2])