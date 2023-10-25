import numpy as np
class Matrix:

    def __init__(self, arr1, arr2):
        self.arr1 = np.array(arr1)
        self.arr2 = np.array(arr2)
        self.__a1 = self.arr1.ndim
        self.__a2 = self.arr2.ndim

    def add(self):
        res = np.zeros((self.__a1, self.__a2), dtype='int16')
        for i in range(len(self.arr1)):
            for j in range(len(self.arr2)):
                res[i][j] = (self.arr1[i][j] + self.arr2[i][j])
        return res

    def sub(self):
        res = np.zeros((self.__a1, self.__a2), dtype='int16')
        for i in range(len(self.arr1)):
            for j in range(len(self.arr2)):
                res[i][j] = (self.arr1[i][j] - self.arr2[i][j])
        return res

    def mul(self):
        res = np.zeros((self.__a1, self.__a2), dtype='int16')
        self.arr2 = self.arr2.transpose()
        a = 0
        b = 0
        for i in range(len(self.arr1)):
            b = 0
            for j in range(len(self.arr2)):
                for k in range(len(self.arr2)):
                    res[a][b] += (self.arr1[a][k] * self.arr2[b][k])
                b += 1
            a += 1
        return res


abc = Matrix([[3, 5], [7, 3]], [[3, 6], [2, 4]])
print(abc.mul())