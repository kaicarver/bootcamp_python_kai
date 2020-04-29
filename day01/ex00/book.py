#!/usr/bin/env python
import datetime
from recipe import Recipe


class Book:
    """A simple example class"""

    def __init__(self, name):
        self.name = name
        self.creation_date = datetime.datetime.now()
        self.last_update = datetime.datetime.now()
        self.recipes_list = {"starter": [], "lunch": [], "dessert": []}

    def get_recipe_by_name(self, name):
        """Print a recipe with the name `name` and return the instance"""
        for rtype in self.recipes_list:
            print(rtype)
            for rname in self.recipes_list[rtype]:
                print(rname)
                if rname == name:
                    return self.recipes_list[rtype][rname]

    def get_recipes_by_types(self, recipe_type):
        """Get all recipe names for a given recipe_type """
        pass

    def add_recipe(self, recipe):
        """Add a recipe to the book and update last_update"""
        if type(recipe) != Recipe:
            raise TypeError("add_recipe requires a Recipe argument")
        self.last_update = datetime.datetime.now()
        print("adding recipe of type:", recipe.recipe_type, recipe)
        self.recipes_list[recipe.recipe_type].append(recipe)
        self.recipes_list[recipe.recipe_type] = \
            list(set(self.recipes_list[recipe.recipe_type]))

    def __str__(self):
        """Return the string to print with the recipe info"""
        # recipes = '\n'.join([' * ' + x + ':' for x in self.recipes_list])
        recipe_text = ""
        for rtype in self.recipes_list:
            recipe_text += f"* {rtype} :" + "\n"
            for y in self.recipes_list[rtype]:
                recipe_text += ' + ' + y.name + "\n"
            recipe_text += ""
        return f"""
Book: {self.name}
Created: {self.creation_date.strftime('%d %b %Y %H:%M:%S %f')}
Last updated: {self.last_update.strftime('%d %b %Y %H:%M:%S %f')}
All the recipes, by type:
{recipe_text}
{[rtype + ':' for rtype in self.recipes_list]}
"""


def unit_tests():
    print('Book unit tests')
    b = Book('A Recipe Book')
    try:
        b.add_recipe(1)
    except TypeError as e:
        print(e)
    name = 'Sandwich'
    r = Recipe(name, 1, 15,
               ['bread', 'butter', 'ham'], 'starter', 'You got this.')
    b.add_recipe(r)
    print(b)
    name = 'Toast'
    r = Recipe(name, 1, 15,
               ['bread', 'butter', 'jam'], 'starter', 'Real easy w toaster.')
    b.add_recipe(r)
    b.add_recipe(r)
    print(b)


if __name__ == "__main__":
    unit_tests()
