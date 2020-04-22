#!/bin/sh
# usage: diff <(./test.sh) test.ok.txt

pycodestyle *.py

python kata00.py
python kata01.py
