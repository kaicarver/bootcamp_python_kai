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
secret_number = random.randint(1, 99)
num_attempts = 0


def prompt_user():
    global prompt
    global num_attempts
    loop = False
    text = input(prompt)
    num_attempts += 1
    if text == 'exit':
        print('Goodbye!')
    elif text == str(secret_number):
        print(f"""Congratulations, you've got it!
You won in {num_attempts} attempts!""")
    elif text == '42':
        print("""The answer to the ultimate question of life, \
the universe and everything is 42.
Congratulations! You got it on your first try!""")
    else:
        try:
            if int(text) < secret_number:
                print("Too low!")
            else:
                print("Too high!")
        except ValueError:
            print("That's not a number.")
        prompt = number_prompt
        loop = True
    return loop


while prompt_user():
    pass
