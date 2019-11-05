import sys


class Recipe:
    def __init__(self, name, cooking_lvl, cooking_time, ingredients,
                 recipe_type, description="No description"):
        if not isinstance(name, str):
            raise TypeError("Name has to be a string")
        if not isinstance(cooking_lvl, int):
            raise TypeError("Cooking level has to be an unsigned integer")
        elif not 1 <= int(cooking_lvl) <= 5:
            raise ValueError("Cooking level has to be contained between 1 and 5 (included)")
        if not isinstance(cooking_time, int):
            raise TypeError("Cooking time has to be an unsigned integer")
        elif not 0 < int(cooking_time):
            raise ValueError("Cooking time can not be zero or less")
        if not ingredients:
            raise ValueError("Ingredients can not be empty")
        elif not isinstance(ingredients, list):
            raise TypeError("Ingredients have to be a list")
        if not isinstance(recipe_type, str):
            raise TypeError("Recipe type has to be a string")
        elif recipe_type not in ["starter", "lunch", "dessert"]:
            raise ValueError("Recipe type can either be 'starter', 'lunch' or 'dessert'")

        self.name = name
        self.cooking_lvl = int(cooking_lvl)
        self.cooking_time = int(cooking_time)
        self.ingredients = ingredients
        self.recipe_type = recipe_type
        self.description = description

    def __str__(self):
        """Return the string to print with the recipe info"""
        txt = "Name: {}\nCooking level: {}\nCooking time: {}\nIngredients: {}\nRecipe type: {}\nDescription: {}".format(
                self.name, self.cooking_lvl, self.cooking_time, self.ingredients,
                self.recipe_type, self.description)
        return txt
