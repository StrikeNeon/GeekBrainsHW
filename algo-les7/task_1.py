"""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы. Сортировка должна быть реализована в
виде функции. Обязательно доработайте алгоритм (сделайте его умнее).

Идея доработки: если за проход по списку не совершается ни одной сортировки,
то завершение
Обязательно сделайте замеры времени обеих реализаций
и обосновать дала ли оптимизация эффективность

Подсказка: обратите внимание, сортируем не по возрастанию, как в примере,
а по убыванию


"""

def makearr(N):
    arr = [0]*N
    arr[0] = (N//2) * -1
    for i in range(1, N):
        arr[i] = arr[0]+i
    return arr

#1
def bubblesort(array): 
    for i in range(len(array)-1): # количество переборов 9
        for j in range(len(array)-i-1): # при первом переборе i=0
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array

def opt_bubbleSort(array):
    for i in range(len(array)):
        swapped = True
        for j in range(0, len(array) - i - 1):
            if array[j] > array[j + 1]:
                (array[j], array[j + 1]) = (array[j + 1], array[j])
                swapped = False
        if swapped: #заканчивает еслимассив отсортирован
            break
        
from time import time
from random import shuffle


print("_"*10)
print("bubblesort")
print("_"*10)
N = 201
a = makearr(N)
print("\n array created: ", a)
shuffle(a)
print("\n array shuffled: ", a)
bubblestart = time()
print("\n array sorted: ", bubblesort(a))
bubbleend = time()
print(f"bubblesort time: {bubblestart-bubbleend}")


print("_"*10)
print("better bubblesort")
print("_"*10)
N = 201
a = makearr(N)
print("\n array created: ", a)
shuffle(a)
print("\n array shuffled: ", a)
bubbestart = time()
print("\n array sorted: ", opt_bubbleSort(a))
bubbleend = time()
print(f"better bubblesort time: {bubblestart-bubbleend}")