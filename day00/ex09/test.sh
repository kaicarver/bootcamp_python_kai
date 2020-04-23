#!/bin/sh
# usage: diff <(./test.sh) test.ok.txt

pycodestyle *.py

python guess.py
