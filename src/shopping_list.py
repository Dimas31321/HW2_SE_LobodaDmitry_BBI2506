from recipe import Recipe
from ingredient import Ingredient

class ShoppingList:
  def __init__(self):
    self._items =[]
  def __len__(self):
    return len(self._items)
  def add_recipe(self, recipe: Recipe, portions: float):
    if portions <0:
      raise ValueError("Количество порций должно быть положительным")
    new_recipe = recipe.scale(portions)
    for ingr in new_recipe.ingredients:
      self._items.append((ingr,recipe.title))
  def remove_recipe(self, title: str):
    new_rec = []
    for para in self._items:
      if para[1] == title:
        continue
      new_rec.append(para)
    self._items = new_rec
  def get_list(self):
    result = {}
    for para in self._items:
      ingredient = para[0]
      key = (ingredient.name, ingredient.unit)
      if key in result:
        result[key] += ingredient.quantity
      else:
        result[key] = ingredient.quantity
    ingredients = []
    for (name, unit), quantity in result.items():
        ingredients.append(Ingredient(name, quantity, unit))
    ingredients.sort(lambda ingredient : ingredient.name)
    return result