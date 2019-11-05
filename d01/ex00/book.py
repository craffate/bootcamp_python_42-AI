import sys
from recipe import Recipe
from datetime import datetime


class Book:
    def __init__(self, name):
        if not name:
            raise ValueError("A name is required")
        self.name = name
        self.recipe_list = {'starter': [], 'lunch': [], 'dessert': []}
        self.creation_date = datetime.now()
        self.last_update = "Never"

    def add_recipe(self, recipe):
        """Add a recipe to the book and update last_update"""
        if not isinstance(recipe, Recipe):
            raise TypeError("You can only add recipes")
        self.recipe_list[recipe.recipe_type].append(recipe)
        self.last_update = datetime.now()

    def get_recipe_by_name(self, name):
        """Print a recipe with the name `name` and return the instance"""
        for k in self.recipe_list:
            for i in self.recipe_list[k]:
                if name in i.name:
                    print(i)

    def get_recipes_by_types(self, recipe_type):
         """Get all recipe names for a given recipe_type"""
         for k in self.recipe_list:
             if k in recipe_type:
                 print(self.recipe_list[k])
