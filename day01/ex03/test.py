#!/usr/bin/env python

from matrix import Matrix
import sys
sys.path.insert(0, "../ex02")
from vector import Vector


def test_eval(exp_str):
    label = "-> " + exp_str + ":"
    expr = "print(" + exp_str + ")"
    print(label)
    eval(expr)
    print()


def test_op(op):
    print(f'testing operator {op}:')
    test_eval(f'Matrix([0.0, 1.0, 2.0, 3.0]) {op} 5')
    test_eval(f'5 {op} Matrix([0.0, 1.0, 2.0, 3.0])')
    test_eval(f'Matrix([0.0, 1.0, 2.0, 3.0]) {op} 5.1')
    test_eval(f'5.1 {op} Matrix([0.0, 1.0, 2.0, 3.0])')
    test_eval(f'"hi" {op} Matrix([0.0, 1.0, 2.0, 3.0])')
    test_eval(f'Matrix([0.0, 1.0, 2.0, 3.0]) \
{op} Matrix([0.0, 1.0, 2.0, 3.0])')
    test_eval(f'Matrix([0.0, 1.0, 2.0, 3.0]) \
{op} Matrix([0.0, 1.0, 2.0])')


if __name__ == "__main__":
    m1 = Matrix([[0.0, 1.0, 2.0, 3.0],
                 [0.0, 2.0, 4.0, 6.0]])
    m2 = Matrix([[0.0, 1.0],
                 [2.0, 3.0],
                 [4.0, 5.0],
                 [6.0, 7.0]])
    print(m1 * m2)
    print('m1', m1)
    print('repr(m1)', repr(m1))
    print('m1.__repr__()', m1.__repr__())
    # WHY is this False??
    print(eval(repr(m1)) == m1)  # test __repr__
    m3 = m1 * 5
    print(m3)
    quit()

    test_eval('Matrix([0.0, 1.0, 2.0, 3.0])')
    test_eval('Matrix([0.0, 1.0, 2.0, 3.0]).shape')
    test_eval('Matrix(3)')
    test_eval('Matrix(1)')
    test_eval('Matrix(0)')
    test_eval('Matrix(-1)')
    test_eval('Matrix(4.2)')
    test_eval('Matrix((10, 15))')
    test_eval('Matrix((15, 10))')
    test_eval('Matrix((15, 15))')
    test_eval('Matrix((-15, 10))')
    test_eval('Matrix((10, 15.0))')

    test_op('+')
    test_op('-')
    test_op('*')
    test_op('/')
