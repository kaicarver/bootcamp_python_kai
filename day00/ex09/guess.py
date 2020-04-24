#!/usr/bin/env python

import random

intro = """This is an interactive guessing game!
You have to enter a number between 1 and 99 to find out the secret number.
Type 'exit' to end the game.
Good luck!

"""
number_prompt = """What's your guess between 1 and 99?
>> """
prompt = intro + number_prompt
secret_number = str(random.randint(1, 99))

def prompt_user():
    global prompt
    loop = False
    text = input(prompt)
    if text == 'exit':
        print('Goodbye!')
    elif text == secret_number:
        print("""Congratulations, you've got it!
You won in ? attempts!""")
    elif text == '42':
        print("""The answer to the ultimate question of life, the universe and everything is 42.
Congratulations! You got it on your first try!""")
    else:
        print("Keep trying...", secret_number)
        prompt = number_prompt
        loop = True
    return loop

while prompt_user():
    pass
