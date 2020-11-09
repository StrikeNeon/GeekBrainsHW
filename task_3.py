"""
Задача 3.
В соответствии с документацией Python,
deque – это обобщение стеков и очередей.
Вот основное правило: если вам нужно что-то быстро дописать или вытащить, используйте deque.
Если вам нужен быстрый случайный доступ, используйте list.

Задача: создайте простой список (list) и очередь (deque).
Выполните различные операции с каждым из объектов.
Сделайте замеры и оцените, насколько информация в документации
соответствует дейстивтельности.

соответствует, средняя разница: 2-4 сотых секунды в пользу очереди
append left и pop left списка занимают 2к секунд?
"""

from collections import deque
from timeit import timeit

list_obj = [i for i in range(100000)]
deque_obj = deque([i for i in range(100000)])

print("comparing append function")
print(timeit('list_obj.append(1)', globals = globals()))
print(timeit('deque_obj.append(1)', globals = globals()))

print("comparing pop function")
print(timeit('list_obj.pop(-1)', globals = globals()))
print(timeit('deque_obj.pop()', globals = globals()))

print("comparing append left function")
print(timeit('list_obj.insert(0,1)', globals = globals()))
print(timeit('deque_obj.appendleft(1)', globals = globals()))

print("comparing pop left function")
print(timeit('list_obj.pop(0)', globals = globals()))
print(timeit('deque_obj.popleft()', globals = globals()))

print("comparing reverse function")
print(timeit('list_obj[::-1]', globals = globals()))
print(timeit('deque_obj.reverse()', globals = globals()))
