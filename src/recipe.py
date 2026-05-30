from src.ingredient import Ingredient
class Recipe:
  def __init__(self,title: str, ingredients = None):
    self.title = title
    self.ingredients = ingredients if ingredients is not None else []
  def add_ingredient(self, ingredient: Ingredient):
    for existing in self.ingredients:
      if existing == ingredient:
        existing.quantity += ingredient.quantity
        return
    self.ingredients.append(ingredient)

  @staticmethod
  def is_valid_ratio(ratio):
    if isinstance(ratio, (int, float)) and ratio>0:
      return True
    return False
  def scale(self, ratio: float):
    if not Recipe.is_valid_ratio(ratio):
        raise ValueError("Коэффициент должен быть положительным")
    new_recipe = Recipe(self.title)
    for ingr in self.ingredients:
        new_recipe.add_ingredient(
            Ingredient(ingr.name, ingr.quantity * ratio, ingr.unit)
        )
    return new_recipe
  def __len__(self):
    return len(self.ingredients)
  def __str__(self):
    return f"{self.title}\nИнгредиенты:\n{self.ingredients}"