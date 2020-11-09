"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните различные операции с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

главная причина использовать OrderedDict - встроенное перемещение элементов 
и ускоренное получение последнего элемента методом popitem 
(разница - 4 тысячные сотые секунды на объекте в 10 тысяч элементов)
"""

from collections import OrderedDict
from time import time

def_dict = {str(key):int(key) for key in range(10000)}

ord_dict = OrderedDict(def_dict)

print("comparing get last item function")
dictpop_start = time()
print(def_dict.pop(sorted(def_dict)[-1]))
dictpop_end = time()

orddictpop_start = time()
print(ord_dict.popitem())
orddictpop_end = time()

print(dictpop_end-dictpop_start)
print(orddictpop_end-orddictpop_start)


#print(timeit('def_dict.pop(sorted(def_dict)[-1])'...
#File "<timeit-src>", line 6, in inner
#IndexError: list index out of range

#print("comparing get last item function")
#rint(timeit('def_dict.pop(sorted(def_dict)[-1])', setup = "def_dict = {str(key):int(key) for key in range(10000)}"))
#print(timeit('ord_dict.popitem()', setup = "def_dict = {str(key):int(key) for key in range(10000)} ; ord_dict = OrderedDict(def_dict)"))