#!/usr/bin/env python

import sys

done = False

if len(sys.argv) == 3:
    try:
        a = int(sys.argv[1])
        b = int(sys.argv[2])
        (sum, diff, prod, quo, rem) = (a + b, a - b, a * b, a / b, a % b)
        print("""Sum:         {}
Difference:  {}
Product:     {}
Quotient:    {}
Remainder:   {}""".format(sum, diff, prod, quo, rem))
        done = true
    except Exception:
        print("InputError: only numbers\n")

if not done:
    if len(sys.argv) > 3:
        print("InputError: too many arguments\n")
    usage = """Usage: python operations.py <number1> <number2>
Example:
    python operations.py 10 3"""
    print(usage)
