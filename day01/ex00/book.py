#!/usr/bin/env python


class Book:
    """A simple example class"""

    def __init__(self, name, last_update, creation_date, recipes_list):
        self.name = name
        self.last_update = last_update
        self.creation_date = creation_date
        self.recipes_list = recipes_list

    def get_recipe_by_name(self, name):
        """Print a recipe with the name `name` and return the instance"""
        pass

    def get_recipes_by_types(self, recipe_type):
        """Get all recipe names for a given recipe_type """
        pass

    def add_recipe(self, recipe):
        """Add a recipe to the book and update last_update"""
        pass

    def __str__(self):
        """Return the string to print with the recipe info"""
        recipes = '\n'.join([x + ':' for x in self.recipes_list])
        txt = f"""
Book: {self.name}
Created: {self.creation_date}
Last updated: {self.last_update}
Recipes:
{recipes}
"""
        return txt
