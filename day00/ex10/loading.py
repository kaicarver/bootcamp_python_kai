#!/usr/bin/env python

from time import sleep

def ft_progress(listy):
    for elem in listy:
        print('.', end='', flush=True)
        yield elem

listy = range(100)
ret = 0
for elem in ft_progress(listy):
    ret += (elem + 3) % 5
    sleep(0.01)
print()
print(ret)

listy = range(3333)
ret = 0
for elem in ft_progress(listy):
    ret += elem
    sleep(0.005)
print()
print(ret)
