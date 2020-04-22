#!/usr/bin/env python

import sys

done = False

if len(sys.argv) == 3:
    try:
        a, b = int(sys.argv[1]), int(sys.argv[2])
        sum, diff, prod = a + b, a - b, a * b
        try:
            quo = a / b
        except ZeroDivisionError:
            quo = 'ERROR (div by zero)'
        try:
            rem = a % b
        except ZeroDivisionError:
            rem = 'ERROR (modulo by zero)'
        print("""Sum:         {}
Difference:  {}
Product:     {}
Quotient:    {}
Remainder:   {}""".format(sum, diff, prod, quo, rem))
        done = True
    except Exception as e:
        print("InputError: only numbers\n")

if not done:
    if len(sys.argv) > 3:
        print("InputError: too many arguments\n")
    usage = """Usage: python operations.py <number1> <number2>
Example:
    python operations.py 10 3"""
    print(usage)
