from recipe import Recipe
from book import Book


b = Book("cookbook")

r1 = Recipe("gateau", 3, 60, ['levure', 'chocolat'], "dessert")
r2 = Recipe("grec", 1, 10, ['salade', 'tomate', 'oignon'], "lunch")
r3 = Recipe("croissant", 2, 20, ['in', 'gre', 'dients'], "starter")

b.add_recipe(r1)
b.add_recipe(r2)
b.add_recipe(r3)

b.get_recipe_by_name("grec")

b.get_recipes_by_types("lunch")
