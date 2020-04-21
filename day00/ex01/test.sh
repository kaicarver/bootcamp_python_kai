#!/bin/sh
# usage: diff <(./test.sh) test.ok.txt
python exec.py "Hello World!" | cat -e
python exec.py "Hello" "my Friend" | cat -e
python exec.py
