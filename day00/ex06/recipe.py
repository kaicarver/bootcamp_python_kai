#!/usr/bin/env python

recipes = {
    'sandwich': {
        'ingredients': ['ham', 'bread', 'cheese', 'tomatoes'],
        'meal': 'lunch',
        'prep_time': 10,
    },
    'cake': {
        'ingredients': ['flour', 'sugar', 'eggs'],
        'meal': 'dessert',
        'prep_time': 60,
    },
    'salad': {
        'ingredients': ['avocado', 'arugula', 'tomatoes', 'spinach'],
        'meal': 'lunch',
        'prep_time': 15,
    },
}


def print_recipe(name):
    print(f"""
Recipe for {name}:
Ingredients list: {recipes[name]['ingredients']}
To be eaten for {recipes[name]['meal']}.
Takes {recipes[name]['prep_time']} minutes of cooking.
""")


for recipe in recipes.keys():
    print_recipe(recipe)
