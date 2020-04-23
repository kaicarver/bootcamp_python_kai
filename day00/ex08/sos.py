#!/usr/bin/env python

import sys
import re

morse_code = {
    'A':	'.-',
    'B':	'-...',
    'C':	'-.-.',
    'D':	'-..',
    'E':	'.',
    'F':	'..-.',
    'G':	'--.',
    'H':	'....',
    'I':	'..',
    'J':	'.---',
    'K':	'-.-',
    'L':	'.-..',
    'M':	'--',
    'N':	'-.',
    'O':	'---',
    'P':	'.--.',
    'Q':	'--.-',
    'R':	'.-.',
    'S':	'...',
    'T':	'-',
    'U':	'..-',
    'V':	'...-',
    'W':	'.--',
    'X':	'-..-',
    'Y':	'-.--',
    'Z':	'--..',
    '0':	'-----',
    '1':	'.----',
    '2':	'..---',
    '3':	'...--',
    '4':	'....-',
    '5':	'.....',
    '6':	'-....',
    '7':	'--...',
    '8':	'---..',
    '9':	'----.',
}


def encode(word):
    return ' '.join([f'{morse_code[c]}' for c in word.upper()])


if len(sys.argv) > 1:
    # list = [item for sublist in l for item in sublist]
    print(' / '.join(
        [encode(word) for arg in sys.argv[1:] for word in arg.split(' ')]))
