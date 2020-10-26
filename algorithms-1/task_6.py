"""
Задание 7.
Задание на закрепление навыков работы с очередью

Примечание: в этом задании вспомните ваши знания по работе с ООП
и опирайтесь на пример урока

Реализуйте структуру "доска задач".


Структура должна предусматривать наличие несольких очередей задач, например
1) базовой, откуда задачи берутся, решаются и отправляются в список решенных
2) очередь на доработку, когда нерешенные задачи из первой очереди отправляются
на корректировку решения

После реализации структуры, проверьте ее работу на различных сценариях
"""

class Queue:
    def __init__(self):
        self.el = []

    def is_empty(self):
        return self.el == []

    def to_queue(self, item):
        self.el.insert(0, item)

    def from_queue(self):
        return self.el.pop()

    def size(self):
        return len(self.el)


class TaskBoard:
    def __init__(self):
        self.cur_queue = Queue()
        self.revision_queue = Queue()  
        self.log = []  

    def resolve_task(self):
        task = self.cur_queue.from_queue()
        self.log.append(task)

    def to_revision_task(self):
        task = self.cur_queue.from_queue()
        self.revision_queue.to_queue(task)

    def to_current_queue(self, item):
        self.cur_queue.to_queue(item)

    def from_revision(self):
        task = self.revision_queue.from_queue()
        self.cur_queue.to_queue(task)

    def current_task(self):
        return self.cur_queue.elems[len(self.cur_queue.elems) - 1]

    def current_revision(self):
        return self.revision_queue.elems[len(self.revision_queue.elems) - 1]