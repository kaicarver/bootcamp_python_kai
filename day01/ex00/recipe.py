#!/usr/bin/env python


class Recipe:
    """A simple example class"""

    def __init__(self, name=None, cooking_lvl=None, cooking_time=None,
                 ingredients=None, recipe_type=None, description=''):
        if name is None or cooking_lvl is None:
            raise TypeError('You must enter right number of arguments')
        self.name = name
        try:
            self.cooking_lvl = int(cooking_lvl)
        except ValueError:
            print("cooking time must be an integer")
        try:
            self.cooking_time = int(cooking_time)
        except ValueError:
            print("cooking time must be an integer")
        self.ingredients = ingredients
        self.recipe_type = recipe_type
        self.description = description

    def __str__(self):
        """Return the string to print with the recipe info"""
        txt = f"Recipe: {self.name}"
        """Your code goes here"""
        return txt
