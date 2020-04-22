#!/bin/sh
# usage: diff <(./test.sh) test.ok.txt

pycodestyle *.py

python exec.py "Hello World!" | cat -e
python exec.py "Hello" "my Friend" | cat -e
python exec.py
