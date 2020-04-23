#!/bin/sh
# usage: diff <(./test.sh) test.ok.txt

pycodestyle *.py

python filterwords.py "Hello, my friend" 3
python filterwords.py "A robot must protect its own existence as \
long as such protection does not conflict with the First or Second Law" 6
python filterwords.py Hello World
python filterwords.py 300 3
