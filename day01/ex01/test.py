#!/usr/bin/env python

from game import GotCharacter, Stark

ned = Stark("Ned")
print(ned.__dict__)
ned.print_house_words()
ned.die()
print(ned.is_alive)
print(ned.__doc__)
