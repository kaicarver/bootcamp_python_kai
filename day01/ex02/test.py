#!/usr/bin/env python

from vector import Vector


def test_eval(exp_str):
    label = "-> " + exp_str + ":"
    expr = "print(" + exp_str + ")"
    print(label)
    eval(expr)
    print()


def test_op(op):
    print(f'testing operator {op}:')
    test_eval(f'Vector([0.0, 1.0, 2.0, 3.0]) {op} 5')
    test_eval(f'5 {op} Vector([0.0, 1.0, 2.0, 3.0])')
    test_eval(f'Vector([0.0, 1.0, 2.0, 3.0]) {op} 5.1')
    test_eval(f'5.1 {op} Vector([0.0, 1.0, 2.0, 3.0])')
    test_eval(f'"hi" {op} Vector([0.0, 1.0, 2.0, 3.0])')
    test_eval(f'Vector([0.0, 1.0, 2.0, 3.0]) \
{op} Vector([0.0, 1.0, 2.0, 3.0])')
    test_eval(f'Vector([0.0, 1.0, 2.0, 3.0]) \
{op} Vector([0.0, 1.0, 2.0])')


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
