# -*- coding: utf-8 -*-
#1
class Matrix():
    
    def __init__(self, data):
        if type(data) != list or type(data[0]) != list:
            raise TypeError("A matrix has to be a list of lists")
        self.data = data
        
    def __str__(self):
        mat = ""
        for i in self.data:
            mat += str(i) + '\n'
        return mat
    
    def __add__(self, other):
        newmat = []
        if len(self.data) != len(other.data):
            raise ValueError("matrices have to have equal length")
        for i in range(len(self.data)):
            layer = []
            for j in range(len(self.data[i])):
                if len(self.data[i]) != len(other.data[i]):
                    raise ValueError(f"array {i+1} is unequal in length")
                layer.append((self.data[i][j]+other.data[i][j]))
            newmat.append(layer)
        return Matrix(newmat)
                
        
mat1 = Matrix([[1,1], [2,2],[3,3]])
print(mat1)

mat2 = Matrix([[1,2], [2,3],[3,4]])
print(mat2)

print(mat1+mat2)