#!/usr/bin/env python
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

# also see unit testing for each class

print("\nNon-error testing:\n")
name = 'sandwich'
r = Recipe(name, recipes[name]['cooking_lvl'], 5,
           ['bread', 'butter', 'ham'], 'starter', 1)

# You will have to implement the built-in method __str__
print(r)
# there's no difference with the above simpler form
# to_print = str(r)
# print(to_print)

b = Book('The Big Recipe Book')
print(b)
# You will have to implement some methods in Book
b.get_recipe_by_name(name)
lr = b.get_recipes_by_types('lunch')
b.add_recipe(r)
print(b)
