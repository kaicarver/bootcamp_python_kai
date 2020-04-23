#!/bin/sh
# usage: diff <(./test.sh) test.ok.txt

pycodestyle *.py

python sos.py "SOS"
python sos.py
python sos.py "HELLO / WORLD"
python sos.py "96 BOULEVARD" "Bessiere"
