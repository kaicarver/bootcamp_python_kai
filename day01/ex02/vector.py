#!/usr/bin/env python

import functools


class Vector:
    """An implementation of mathematical vectors"""

    def __init__(self, param):
        if type(param) == list:
            self.size = len(param)
            self.values = param
        elif type(param) == int:
            if param < 0:
                print("ERROR to be handled? negative size")
                param = 0
            self.size = param
            self.values = [float(x) for x in list(range(param))]
        elif type(param) == tuple:
            (beg, end) = param
            if not (type(beg) == int and type(end) == int):
                print("ERROR to be handled? invalid range param")
                beg = 0
                end = 0
            if beg > end:
                print("ERROR to be handled? invalid range")
                beg = end
            self.size = end - beg
            self.values = [float(x) for x in list(range(beg, end))]
        else:
            print("ERROR to be handled? bad init param")
            self.size = 0
            self.values = []

    def __str__(self):
        return f"Vector({self.values}) ({self.size})"

    def __repr__(self):
        return f"Vector({self.values})"

    def __add__(self, param):
        if type(param) == int or type(param) == float:
            return Vector([x + param for x in self.values])
        elif type(param) == Vector:
            if self.size == param.size:
                return Vector([self.values[i] + param.values[i]
                               for i in range(self.size)])
            else:
                print("ERROR can only add vectors of same size")
        else:
            print("ERROR unknown type")

    def __radd__(self, param):
        return self.__add__(param)

    def __sub__(self, param):
        if type(param) == int or type(param) == float:
            return Vector([x - param for x in self.values])
        elif type(param) == Vector:
            if self.size == param.size:
                return Vector([self.values[i] - param.values[i]
                               for i in range(self.size)])
            else:
                print("ERROR can only subtract vectors of same size")
        else:
            print("ERROR unknown type")

    def __rsub__(self, param):
        if type(param) == int or type(param) == float:
            return Vector([param - x for x in self.values])
        elif type(param) == Vector:
            if self.size == param.size:
                return Vector([self.values[i] - param.values[i]
                               for i in range(self.size)])
            else:
                print("ERROR can only subtract vectors of same size (!)")
        else:
            print("ERROR unknown type")

    def __mul__(self, param):
        if type(param) == int or type(param) == float:
            return Vector([x * param for x in self.values])
        elif type(param) == Vector:
            if self.size == param.size:
                return functools.reduce(
                    lambda x, y: x+y,
                    [self.values[i] * param.values[i]
                        for i in range(self.size)])
            else:
                print("ERROR can only multiply vectors of same size")
        else:
            print("ERROR unknown type")

    def __rmul__(self, param):
        return self.__mul__(param)

    def __truediv__(self, param):
        if type(param) == int or type(param) == float:
            try:
                return Vector([x / param for x in self.values])
            except ZeroDivisionError:
                print("ERROR division by zero")
        elif type(param) == Vector:
            print("ERROR cannot divide by Vector")
        else:
            print("ERROR unknown type")

    def __rtruediv__(self, param):
        if type(param) == int or type(param) == float:
            try:
                return Vector([param / x for x in self.values])
            except ZeroDivisionError:
                print("ERROR division by zero")
        elif type(param) == Vector:
            print("ERROR cannot divide by Vector (should not be called!)")
        else:
            print("ERROR unknown type")
