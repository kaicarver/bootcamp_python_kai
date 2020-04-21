#!/usr/bin/env python

import sys

if len(sys.argv) == 2:
    try:
        if int(sys.argv[1]) == 0:
            print("I'm Zero.")
        elif int(sys.argv[1]) % 2 == 0:
            print("I'm Even.")
        else:
            print("I'm Odd.")
    except Exception:
        print("ERROR")

elif len(sys.argv) > 2:
    print("ERROR")
