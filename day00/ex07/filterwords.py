#!/usr/bin/env python

import sys
import re

done = False

if len(sys.argv) == 3:
    text = sys.argv[1]
    try:
        num = int(sys.argv[2])
        print(
            [word for word in re.findall(r"[\w']+", text) if len(word) > num])
    except ValueError:
        print("ERROR")
else:
    print(f"usage: {sys.argv[0]} string number")
