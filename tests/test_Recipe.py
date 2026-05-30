import pytest
from src.ingredient import Ingredient
from src.recipe import Recipe

def test_constructor_recipe():
    rec = Recipe("Пирог")
    assert rec.ingredients == []

def test_add_method():
    rec = Recipe("Пирог")
    assert rec.ingredients == []
    rec.add_ingredient(Ingredient("Яблоко", 2.5, "кг"))
    assert len(rec.ingredients) == 1
    assert rec.ingredients[0].quantity == 2.5
    rec.add_ingredient(Ingredient("Яблоко", 1.5, "кг"))
    ingr = rec.ingredients[0]
    assert ingr.quantity == 4.0


def test_scale_method():
    rec = Recipe("Пирог")
    rec.add_ingredient(Ingredient("Яблоко", 2.5, "кг"))
    rec.add_ingredient(Ingredient("Банан", 1000.0, "г"))
    new_rec = rec.scale(2.0)
    assert new_rec != rec
    assert isinstance(new_rec, Recipe)
    assert new_rec.ingredients[0].quantity == 5.0
    assert new_rec.ingredients[1].quantity == 2000.0


def test_scale_negative_factor():
    rec = Recipe("Пирог")
    with pytest.raises(ValueError):
        rec.scale(-1.0)

def test_length_method():
    rec = Recipe("Пирог")
    rec.add_ingredient(Ingredient("Яблоко", 2.5, "кг"))
    rec.add_ingredient(Ingredient("Банан", 1000.0, "г"))
    rec.add_ingredient(Ingredient("Яблоко", 1.5, "кг"))
    assert len(rec) == 2