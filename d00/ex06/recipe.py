import sys


__infos = {
        'ingredients': [],
        'meal': 'lunch',
        'prep_time': 60,
        }


cookbook = {
        'sandwich': dict(__infos),
        'cake': dict(__infos),
        'salad': dict(__infos),
        }


def __presets():
    cookbook['sandwich']['ingredients'] =
    ['ham', 'bread', 'cheese', 'tomatoes']
    cookbook['sandwich']['meal'] = 'lunch'
    cookbook['sandwich']['prep_time'] = 10
    cookbook['cake']['ingredients'] = ['flour', 'sugar', 'eggs']
    cookbook['cake']['meal'] = 'dessert'
    cookbook['cake']['prep_time'] = 60
    cookbook['salad']['ingredients'] =
    ['avocado', 'arugula', 'tomatoes', 'spinach']
    cookbook['salad']['meal'] = 'lunch'
    cookbook['salad']['prep_time'] = 15


def __print_recipe(name=None):
    if name is None:
        print("Pick a recipe, please.")
    elif name not in cookbook:
        print("Recipe not found.")
    else:
        print("Recipe for {}:".format(name))
        print("Ingredients list: {}".format(cookbook[name]['ingredients']))
        print("To be eaten for {}.".format(cookbook[name]['meal']))
        print("Preparation time is {} minutes.".format(
            cookbook[name]['prep_time']))


def __del_recipe(name=None):
    if name is None:
        print("Pick a recipe, please.")
        return
    elif name not in cookbook:
        print("Recipe not found.")
        return
    else:
        del cookbook[name]
        print("Recipe {} deleted.".format(name))


def __add_recipe(name=None, ingredients=[], meal=None, prep_time=None):
    if name is None:
        print("Your recipe needs a name.")
        return
    elif not len(ingredients):
        print("Your recipe needs ingredients.")
        return
    elif meal is None:
        print("Your recipe needs a meal type.")
        return
    elif prep_time is None:
        print("Your recipe needs a preparation time.")
        return
    cookbook[name] = dict(__infos)
    cookbook[name]['ingredients'] = ingredients
    cookbook[name]['meal'] = meal
    cookbook[name]['prep_time'] = prep_time


def __print_recipe_all():
    for k, v in cookbook.items():
        __print_recipe(k)


def __print_menu():
    print("1. Add a recipe")
    print("2. Delete a recipe")
    print("3. Print a recipe")
    print("4. Print the cookbook")
    print("5. Quit")


def __sel_handler(sel):
    if sel > 5 or sel < 1:
        print("This option does not exist.")
    if sel == 1:
        sel2 = input("Enter a name: ")
        sel3 = input("Enter a list of ingredients (separated by spaces): ")
        sel4 = input("Enter a meal type: ")
        sel5 = input("Enter a preparation time: ")
        __add_recipe(sel2, sel3.split(" "), sel4, sel5)
    elif sel == 2:
        sel2 = input("Please enter the recipe name to delete: ")
        __del_recipe(sel2)
    elif sel == 3:
        sel2 = input("Please enter a recipe name to get its details: ")
        __print_recipe(sel2)
    elif sel == 4:
        __print_recipe_all()
    elif sel == 5:
        print("Cookbook closed.")
        sys.exit(0)


def menu():
    while 42:
        __print_menu()
        sel = input("Please select an option using the corresponding number: ")
        if not sel.isdigit():
            print("Please input a number.")
        else:
            __sel_handler(int(sel))


__presets()
menu()
