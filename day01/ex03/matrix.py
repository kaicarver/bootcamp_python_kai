#!/usr/bin/env python

import functools


class Matrix:
    """An implementation of mathematical matrices"""

    def __init__(self, param, param2=None):
        if type(param) == tuple:
            (rows, cols) = param
            self.shape = param
            self.data = [[0.0] * cols] * rows
        elif type(param) == list:
            self.shape = (2, 2)
            self.data = param
        else:
            self.shape = (0,0)
            self.data = []
            print("ERROR bad parameter")

    def __str__(self):
        return f"(Matrix {self.data}) \
({self.shape[0]} rows x {self.shape[1]} cols)"

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

    from pprint import pprint

    print("which are rows, which are columns?")
    (nrows, ncols) = (3, 4)
    print(f'm={nrows} rows, n={ncols} columns')
    m = []
    for x in range(0, nrows):
        m.append([])
        for y in range(0, ncols):
            m[x].append(f'm{x}n{y}')
    pprint(m)
    # one-liner
    # this inverts rows and cols...
    pprint([[f'm{x}n{y}' for x in range(nrows)] for y in range(ncols)])
    # this comes out right
    pprint([[f'm{x}n{y}' for y in range(ncols)] for x in range(nrows)])
