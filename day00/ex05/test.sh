#!/bin/sh
# usage: diff <(./test.sh) test.ok.txt

pycodestyle *.py

python kata00.py
python kata01.py
python kata02.py
python kata03.py
python kata04.py
