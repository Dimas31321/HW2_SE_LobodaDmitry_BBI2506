import pytest
from src.ingredient import Ingredient
from src.recipe import Recipe
from src.shopping_list import ShoppingList


def test_add_recipe():
    sh_list = ShoppingList()
    recipe = Recipe("Пицца")
    recipe.add_ingredient(Ingredient("Сыр", 100, "г"))
    sh_list.add_recipe(recipe, 1)
    assert len(sh_list._items) == 1
    with pytest.raises(ValueError):
        sh_list.add_recipe(recipe, -1)


def test_remove_recipe():
    sh_list = ShoppingList()
    pizza = Recipe("Пицца")
    pizza.add_ingredient(Ingredient("Сыр", 100, "г"))
    pasta = Recipe("Паста")
    pasta.add_ingredient(Ingredient("Макароны", 200, "г"))
    sh_list.add_recipe(pizza, 1)
    sh_list.add_recipe(pasta, 1)
    sh_list.remove_recipe("Пирог")
    assert len(sh_list._items) == 2
    sh_list.remove_recipe("Пицца")
    assert len(sh_list._items) == 1
    assert sh_list._items[0][1] == "Паста"


def test_get_list():
    pizza = Recipe("Пицца")
    pizza.add_ingredient(Ingredient("Сыр", 100, "г"))
    pizza.add_ingredient(Ingredient("Томат", 50, "г"))
    pasta = Recipe("Паста")
    pasta.add_ingredient(Ingredient("Сыр", 150, "г"))
    sh_list = ShoppingList()
    sh_list.add_recipe(pizza, 1)
    sh_list.add_recipe(pasta, 1)
    result = sh_list.get_list()
    assert len(result) == 2
    cheese = next(i for i in result if i.name == "Сыр")
    assert cheese.quantity == 250
    names = [i.name for i in result]
    assert names == sorted(names)

