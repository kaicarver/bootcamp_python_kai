#!/bin/sh
# usage: diff <(./test.sh < test.in.txt) test.ok.txt

pycodestyle operations.py

python operations.py 10 3
python operations.py 42 10
python operations.py 1 0
python operations.py
python operations.py 12 10 5
python operations.py "one" "two"
python operations.py "512" "63.1"
