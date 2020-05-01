#!/usr/bin/env python


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

    def __add__(self, param):
        return Vector([x + param for x in self.values])

    def __radd__(self, param):
        return self.__add__(param)

    def __sub__(self, param):
        return Vector([x - param for x in self.values])

    def __rsub__(self, param):
        return Vector([param - x for x in self.values])

    def __mul__(self, param):
        return Vector([x * param for x in self.values])

    def __rmul__(self, param):
        return self.__mul__(param)

    def __truediv__(self, param):
        try:
            return Vector([x / param for x in self.values])
        except ZeroDivisionError:
            print("ERROR dvision by zero")
            return None

    def __rtruediv__(self, param):
        try:
            return Vector([param / x for x in self.values])
        except ZeroDivisionError:
            print("ERROR dvision by zero")
            return None


def test_eval(exp_str):
    label = " -> " + exp_str + ":"
    expr = "print(" + exp_str + ")"
    print(label)
    eval(expr)


def test_op(op):
    print(f'testing operator {op}:')
    test_eval(f'Vector([0.0, 1.0, 2.0, 3.0]) {op} 5')
    test_eval(f'5 {op} Vector([0.0, 1.0, 2.0, 3.0])')
    test_eval(f'Vector([0.0, 1.0, 2.0, 3.0]) {op} 5.1')
    test_eval(f'5.1 {op} Vector([0.0, 1.0, 2.0, 3.0])')
    # test_eval(f'"hi" {op} Vector([0.0, 1.0, 2.0, 3.0])')
#     test_eval(f'Vector([0.0, 1.0, 2.0, 3.0]) \
# {op} Vector([0.0, 1.0, 2.0, 3.0])')


if __name__ == "__main__":
    v1 = Vector([0.0, 1.0, 2.0, 3.0])
    print(v1)
    v2 = v1 * 5
    print(v2)
    test_eval('Vector([0.0, 1.0, 2.0, 3.0])')
    test_eval('Vector([0.0, 1.0, 2.0, 3.0]).size')
    test_eval('Vector(3)')
    test_eval('Vector(1)')
    test_eval('Vector(0)')
    test_eval('Vector(-1)')
    test_eval('Vector(4.2)')
    test_eval('Vector((10, 15))')
    test_eval('Vector((15, 10))')
    test_eval('Vector((15, 15))')
    test_eval('Vector((-15, 10))')
    test_eval('Vector((10, 15.0))')

    test_op('+')
    test_op('-')
    test_op('*')
    test_op('/')
