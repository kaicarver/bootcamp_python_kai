#!/usr/bin/env python
from book import Book
from recipe import Recipe
import time
import subprocess

recipe_data = {
    'Sandwich': {
        'ingredients': ['ham', 'bread', 'cheese', 'tomatoes'],
        'recipe_type': 'starter',
        'cooking_time': 10,
        'cooking_lvl': 1,
        'description': "",
    },
    'Basic Cake': {
        'ingredients': ['flour', 'sugar', 'eggs'],
        'recipe_type': 'dessert',
        'cooking_time': 60,
        'cooking_lvl': 3,
        'description': "yummy",
    },
    'Salad': {
        'ingredients': ['avocado', 'arugula', 'tomatoes', 'spinach'],
        'recipe_type': 'lunch',
        'cooking_time': 15,
        'cooking_lvl': 2,
        'description': "good for u",
    },
}

# also see unit testing for each class
subprocess.call("./recipe.py")
subprocess.call("./book.py")

print("\nNon-error testing:\n")
name = 'Sandwich'
r = Recipe(name, recipe_data[name]['cooking_lvl'], 5,
           ['bread', 'butter', 'ham'], 'starter', 'Good.')
assert type(r) is Recipe, "Should be a Recipe"

# You will have to implement the built-in method __str__
print(r)
# there's no difference with the above simpler form
#   to_print = str(r)
#   print(to_print)
# but this fails, can only concatenate str (not "Recipe") to str
#   to_print = "recipe: " + r
# so have to use str()
#   to_print = "recipe: " + str(r)

b = Book('The Big Recipe Book')
print(b)
# You will have to implement some methods in Book
time.sleep(1)
b.add_recipe(r)
print(b)

r = b.get_recipe_by_name(name)
# assert r is not None, "Should not be None"
assert type(r) is Recipe, "get_recipe should return a Recipe"
print(r)

lr = b.get_recipes_by_types('starter')
print(lr)

for name in recipe_data:
    r = recipe_data[name]
    b.add_recipe(
        Recipe(name, r['cooking_lvl'], r['cooking_time'],
               r['ingredients'], r['recipe_type'], r['description']))
print(b)
