#!/bin/sh
# usage: diff <(./test.sh) test.ok.txt

python whois.py 12
python whois.py 3
python whois.py
python whois.py 0
python whois.py Hello
python whois.py 12 3
