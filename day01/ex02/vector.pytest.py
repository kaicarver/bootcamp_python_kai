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


if __name__ == "__main__":
    v1 = Vector([0.0, 1.0, 2.0, 3.0])
    v2 = v1 * 5
    print(v1)
    print(v2)
