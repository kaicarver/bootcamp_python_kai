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

# You have to initialize the object Recipe and check all its values,
# only the description can be empty.
# In case of input errors, you should print what they are and exit properly.
try:
    r = Recipe()
    print(r)
except Exception as e:
    print(type(e), e, e.args)
try:
    r = Recipe(1, 0, 0, 0, 0)
    print(r)
except Exception as e:
    print(type(e), e, e.args)
try:
    r = Recipe(1, 1, 1, 1, 1)
    print(r)
except Exception as e:
    print(type(e), e, e.args)

name = 'sandwich'
r = Recipe(name, recipes[name]['cooking_lvl'], 1, 1, 1, 1)

# You will have to implement the built-in method __str__
# (there's no difference between these)
print(r)
to_print = str(r)
print(to_print)

b = Book('The Big Book', datetime.datetime.now(), datetime.datetime.now(),
         {"starter": [], "lunch": [], "dessert": []})
print(b)
# You will have to implement some methods in Book
b.get_recipe_by_name(name)
lr = b.get_recipes_by_types('lunch')
b.add_recipe(r)
