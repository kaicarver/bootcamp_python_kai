#!/bin/sh
# usage: diff <(./test.sh < test.in.txt) test.ok.txt

pycodestyle *.py
python test.py
