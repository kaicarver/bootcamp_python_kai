#!/usr/bin/env python

import inspect


class Recipe:
    """A simple example class"""

    type_list = ['starter', 'lunch', 'dessert']

    def __init__(self, name=None, cooking_lvl=None, cooking_time=None,
                 ingredients=None, recipe_type=None, description=''):
        args = locals()
        label = type(self).__name__ + '.' \
            + inspect.stack()[0][3] + '()'
        for arg in args:
            if arg != 'self' and args[arg] is None:
                raise TypeError(f'{label}: must specify argument "{arg}"')
        self.name = name
        try:
            self.cooking_lvl = int(cooking_lvl)
            if self.cooking_lvl < 1 or self.cooking_lvl > 5:
                raise ValueError
        except ValueError:
            raise ValueError("cooking level must be integer between 1 and 5")
        try:
            self.cooking_time = int(cooking_time)
            if self.cooking_time < 0:
                raise ValueError
        except ValueError:
            raise ValueError("cooking time must be a non-negative number")
        self.ingredients = ingredients
        if type(ingredients) != list:
            raise ValueError("ingredients must be a list")
        self.recipe_type = recipe_type
        if recipe_type not in self.type_list:
            raise ValueError(
                f"recipe type must be one of: {', '.join(self.type_list)}")
        self.description = description

    def __str__(self):
        """Return the string to print with the recipe info"""
        txt = f"Recipe: {self.name}"
        """Your code goes here"""
        return txt
