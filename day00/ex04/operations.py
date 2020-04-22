#!/usr/bin/env python

import sys

if len(sys.argv) == 3:
    try:
        a = int(sys.argv[1])
        b = int(sys.argv[2])
        (sum, diff, prod, quo, rem) = (a + b, a - b, a * 3, a / b, a % b)
        print("""Sum:         {} 
Difference:  {} 
Product:     {} 
Quotient:    {} 
Remainder:   {}""".format(sum, diff, prod, quo, rem))
    except Exception:
        print("ERROR")

elif len(sys.argv) > 2:
    print("ERROR")
