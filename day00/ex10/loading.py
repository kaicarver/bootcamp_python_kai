#!/usr/bin/env python

from time import sleep

def ft_progress(listy):
    n = 1
    print('This is printed first')
    # Generator function contains yield statements
    yield n

    n += 1
    print('This is printed second')
    yield n

    n += 1
    print('This is printed at last')
    yield n

listy = range(1000)
ret = 0
for elem in ft_progress(listy):
    print('elem:', elem)
    ret += (elem + 3) % 5
    sleep(0.01)
print()
print(ret)
