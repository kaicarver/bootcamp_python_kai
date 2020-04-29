#!/usr/bin/env python
import datetime


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
        self.last_update = datetime.datetime.now()
        pass

    def __str__(self):
        """Return the string to print with the recipe info"""
        recipes = '\n'.join([' * ' + x + ':' for x in self.recipes_list])
        return f"""
Book: {self.name}
Created: {self.creation_date.strftime('%d %b %Y %H:%M:%S %f')}
Last updated: {self.last_update.strftime('%d %b %Y %H:%M:%S %f')}
All the recipes, by type:
{recipes}
"""


if __name__ == "__main__":
    print('hi this is for testing')
