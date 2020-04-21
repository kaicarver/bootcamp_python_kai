#!/usr/bin/env python

import sys

sys.argv.pop(0)
if len(sys.argv) > 0:
    print(' '.join(sys.argv)[::-1].swapcase())
