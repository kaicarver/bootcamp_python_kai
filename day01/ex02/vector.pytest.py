#!/usr/bin/env python


class Vector:
    """An implementation of mathematical vectors"""

    def __init__(self, param):
        if type(param) == list:
            self.size = len(param)
            self.values = param
        else:
            self.size = 2
            self.values = [4.0, 2.0]

    def __str__(self):
        return str(self.values)

    def __mul__(self, param):
        return 42


def test_eval(exp_str):
    label = "-> " + exp_str + ":"
    expr = "print(" + exp_str + ")"
    print(label)
    eval(expr)


if __name__ == "__main__":
    v1 = Vector([0.0, 1.0, 2.0, 3.0])
    print(v1)
    v2 = v1 * 5
    print(v2)
    test_eval('Vector([0.0, 1.0, 2.0, 3.0])')
    test_eval('Vector(3)')
    test_eval('Vector((10, 15))')
    test_eval('Vector([0.0, 1.0, 2.0, 3.0]) * 5')
