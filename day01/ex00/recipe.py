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
        return f"""
Recipe: {self.name}
  {self.recipe_type} / level {self.cooking_lvl} / {self.cooking_time} min
  Ingredients: {', '.join([x for x in self.ingredients])}

{self.description}"""


if __name__ == "__main__":
    # You have to initialize the object Recipe and check all its values,
    # only the description can be empty.
    # In case of input errors, you should print them and exit properly.
    print("\nCheck for a series of errors:\n")
try:
    r = Recipe()
    print(r)
except Exception as e:
    print(type(e), e.args)
try:
    r = Recipe(1, 1, 1)
    print(r)
except Exception as e:
    print(type(e), e.args)
try:
    r = Recipe(1, 0, 0, 0, 0)
    print(r)
except Exception as e:
    print(type(e), e.args)
try:
    r = Recipe(1, 1, 1, 1, 1)
    print(r)
except Exception as e:
    print(type(e), e.args)
try:
    r = Recipe(1, 1, -1, [], 1)
    print(r)
except Exception as e:
    print(type(e), e.args)
try:
    r = Recipe(1, 1, 1, [], 1)
    print(r)
except Exception as e:
    print(type(e), e.args)

    print(
        Recipe(
            'Sandwich', 2, 5, ['bread', 'butter', 'ham'], 'starter',
            """This is easy to do even for you.
Just do it.
"""))
    print(
        Recipe(
            'Cookies', 3, 35, ['sugar', 'eggs', 'flour'], 'dessert',
            """Mix together.
Make patties.
Bake.
"""))
    try:
        print(
            Recipe(
                'Cookies', 3, 35, ['sugar', 'eggs', 'flour'], 'delicious!',
                """Mix together.
Make patties.
Bake.
"""))
    except Exception as e:
        print("error, as expected:", e)
