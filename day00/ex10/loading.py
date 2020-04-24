#!/usr/bin/env python

from time import sleep


def ft_progress(rangy):
    leng = len(rangy)
    # for elem in rangy:
    for i, elem in zip(range(leng), rangy):
        print(f'{i}/{leng}\r', end='', flush=True)
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
