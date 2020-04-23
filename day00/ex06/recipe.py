#!/usr/bin/env python

recipes = {
    'sandwich': {
        'ingredients': ['ham', 'bread', 'cheese', 'tomatoes'],
        'meal': 'lunch',
        'prep_time': 10,
    },
    'cake': {
        'ingredients': ['flour', 'sugar', 'eggs'],
        'meal': 'dessert',
        'prep_time': 60,
    },
    'salad': {
        'ingredients': ['avocado', 'arugula', 'tomatoes', 'spinach'],
        'meal': 'lunch',
        'prep_time': 15,
    },
}


def print_recipe(name):
    print(f"""Recipe for {name}:
Ingredients list: {recipes[name]['ingredients']}
To be eaten for {recipes[name]['meal']}.
Takes {recipes[name]['prep_time']} minutes of cooking.
""", end='')


def print_cookbook():
    print('Cookbook:')
    for recipe in recipes.keys():
        print_recipe(recipe)
        print()


def delete_cookbook(name):
    del recipes[name]


def prompt():
    print("""Please select an option by typing the corresponding number:
1: Add a recipe
2: Delete a recipe
3: Print a recipe
4: Print the cookbook
5: Quit
""")


prompt()
print_cookbook()
delete_cookbook('sandwich')
print_cookbook()

