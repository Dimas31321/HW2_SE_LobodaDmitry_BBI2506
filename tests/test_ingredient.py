import pytest
from src.ingredient import Ingredient

def test_init_of_ingredient():
    r = Ingredient("Бананы", 100, "кг")
    assert r.name == "Бананы"
    assert r.quantity == 100
    assert r.unit == "кг"

def test_str_method():
    r = Ingredient("Бананы", 100, "кг")
    assert str(r) == "Бананы: 100.0 кг"

def test_equality():
    r = Ingredient("Бананы", 100, "кг")
    s = Ingredient("Бананы", 500, "кг")
    a = Ingredient("Яблоки", 100, "кг")
    b = Ingredient("Бананы", 100, "г")

    assert r == s
    assert r != a
    assert r != b