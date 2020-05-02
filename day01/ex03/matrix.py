#!/usr/bin/env python

import functools


class Matrix:
    """An implementation of mathematical matrices"""

    def __init__(self, param):
        if type(param) == tuple:
            self.shape = param
            self.data = [[0.0] * param[0]] * param[1]
        else:
            self.shape = (2, 2)
            self.data = [[0.0, 1.0], [2.0, 3.0], [4.0, 5.0]]

    def __str__(self):
        return f"(Matrix {self.data}) ({self.shape})"

    def __repr__(self):
        return f"(Matrix {self.data})"

    def __add__(self, param):
        if type(param) == int or type(param) == float:
            return Matrix([x + param for x in self.values])
        elif type(param) == Matrix:
            if self.size == param.size:
                return Matrix([self.values[i] + param.values[i]
                               for i in range(self.size)])
            else:
                print("ERROR can only add Matrixs of same size")
        else:
            print("ERROR unknown type")

    def __radd__(self, param):
        return self.__add__(param)

    def __sub__(self, param):
        if type(param) == int or type(param) == float:
            return Matrix([x - param for x in self.values])
        elif type(param) == Matrix:
            if self.size == param.size:
                return Matrix([self.values[i] - param.values[i]
                               for i in range(self.size)])
            else:
                print("ERROR can only subtract Matrixs of same size")
        else:
            print("ERROR unknown type")

    def __rsub__(self, param):
        if type(param) == int or type(param) == float:
            return Matrix([param - x for x in self.values])
        elif type(param) == Matrix:
            if self.size == param.size:
                return Matrix([self.values[i] - param.values[i]
                               for i in range(self.size)])
            else:
                print("ERROR can only subtract Matrixs of same size (!)")
        else:
            print("ERROR unknown type")

    def __mul__(self, param):
        if type(param) == int or type(param) == float:
            return Matrix([x * param for x in self.values])
        elif type(param) == Matrix:
            if self.size == param.size:
                return functools.reduce(
                    lambda x, y: x+y,
                    [self.values[i] * param.values[i]
                        for i in range(self.size)])
            else:
                print("ERROR can only multiply Matrixs of same size")
        else:
            print("ERROR unknown type")

    def __rmul__(self, param):
        return self.__mul__(param)

    def __truediv__(self, param):
        if type(param) == int or type(param) == float:
            try:
                return Matrix([x / param for x in self.values])
            except ZeroDivisionError:
                print("ERROR division by zero")
        elif type(param) == Matrix:
            print("ERROR cannot divide by Matrix")
        else:
            print("ERROR unknown type")

    def __rtruediv__(self, param):
        if type(param) == int or type(param) == float:
            try:
                return Matrix([param / x for x in self.values])
            except ZeroDivisionError:
                print("ERROR division by zero")
        elif type(param) == Matrix:
            print("ERROR cannot divide by Matrix (should not be called!)")
        else:
            print("ERROR unknown type")


if __name__ == "__main__":
    print("Welcome to Matrix")
    m1 = Matrix([[0.0, 1.0, 2.0, 3.0],
                 [0.0, 2.0, 4.0, 6.0]])
    m2 = Matrix([[0.0, 1.0],
                 [2.0, 3.0],
                 [4.0, 5.0],
                 [6.0, 7.0]])
    print(m1)
    print(m2)
    print(Matrix((4, 2)))
    print(Matrix((2, 4)))
