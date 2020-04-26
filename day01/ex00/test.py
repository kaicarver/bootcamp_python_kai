#!/usr/bin/env python
import datetime
from book import Book
from recipe import Recipe

recipes = {
    'sandwich': {
        'ingredients': ['ham', 'bread', 'cheese', 'tomatoes'],
        'recipe_type': 'starter',
        'cooking_time': 10,
        'cooking_lvl': 1,
        'description': "",
    },
    'cake': {
        'ingredients': ['flour', 'sugar', 'eggs'],
        'recipe_type': 'dessert',
        'cooking_time': 60,
        'cooking_lvl': 3,
        'description': "yummy",
    },
    'salad': {
        'ingredients': ['avocado', 'arugula', 'tomatoes', 'spinach'],
        'recipe_type': 'lunch',
        'cooking_time': 15,
        'cooking_lvl': 2,
        'description': "good for u",
    },
}

name = 'sandwich'
r = Recipe(name, recipes[name]['cooking_lvl'], 1, 1, 1, 1)
print(r)
print(Book('The Big Book', datetime.datetime.now(), datetime.datetime.now(),
           {"starter": [], "lunch": [], "dessert": []}))
