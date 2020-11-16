"""
Задание 2.**

Доработайте пример структуры "дерево",
рассмотренный на уроке.

Предложите варианты доработки и оптимизации
(например, валидация значений узлов в соответствии с требованиями для бинарного дерева)

Поработайте с доработанной структурой, позапускайте на реальных данных.
"""

class BinaryTree:
    def __init__(self, root_obj):
        # корень
        self.root = root_obj
        # левый потомок
        self.left_child = None
        # правый потомок
        self.right_child = None
        data = {self.root:{"left":self.left_child,"right":self.right_child}}

    # добавить левого потомка
    def insert_left(self, new_node):
        # если у узла нет левого потомка
        if self.left_child == None:
            # тогда узел просто вставляется в дерево
            # формируется новое поддерево
            self.left_child = BinaryTree(new_node)
        # если у узла есть левый потомок
        else:
            # тогда вставляем новый узел
            tree_obj = BinaryTree(new_node)
            # и спускаем имеющегося потомка на один уровень ниже
            tree_obj.left_child = self.left_child
            self.left_child = tree_obj

    # добавить правого потомка
    def insert_right(self, new_node):
        # если у узла нет правого потомка
        if self.right_child == None:
            # тогда узел просто вставляется в дерево
            # формируется новое поддерево
            self.right_child = BinaryTree(new_node)
        # если у узла есть правый потомок
        else:
            # тогда вставляем новый узел
            tree_obj = BinaryTree(new_node)
            # и спускаем имеющегося потомка на один уровень ниже
            tree_obj.right_child = self.right_child
            self.right_child = tree_obj

    # метод доступа к правому потомку
    def get_right_child(self):
        return self.right_child

    # метод доступа к левому потомку
    def get_left_child(self):
        return self.left_child

    # метод установки корня
    def set_root_val(self, obj):
        self.root = obj

    # метод доступа к корню
    def get_root_val(self):
        return self.root
    
    #swap children of this root
    def swap(self):
        self.right_child, self.left_child  = self.left_child, self.right_child
    
    #swap 2 roots        
    def swap_children(self, other):
        tmp = self.right_child, self.left_child
        self.right_child, self.left_child  = other.right_child, other.left_child
        other.right_child, other.left_child  = tmp
        
    def get(self,key):
      if self.root:
          res = self._get(key,self.root)
          if res:
              return res.payload
          else:
              return None
      else:
          return None
    
    def _get(self,key,currentNode):
      if not currentNode:
          return None
      elif currentNode.key == key:
          return currentNode
      elif key < currentNode.key:
          return self._get(key,currentNode.leftChild)
      else:
          return self._get(key,currentNode.rightChild)

def __getitem__(self,key):
    return self.get(key)
    #get representation dict
    def __str__(self):
        return self.data
    
    def __iter__(self):
      return self.root.__iter__()
    
r = BinaryTree(8)
print(r.get_root_val())
print(r.get_left_child())
r.insert_left(4)
print(r.get_left_child())
print(r.get_left_child().get_root_val())
r.insert_right(12)
print(r.get_right_child())
print(r.get_right_child().get_root_val())
r.get_right_child().set_root_val(16)
print(r.right_child.right_child.get_root_val())
print(r.get_right_child().get_root_val())