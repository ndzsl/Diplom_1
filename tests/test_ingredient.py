# tests/test_ingredient.py
import pytest
from praktikum.ingredient import Ingredient
import data


class TestIngredient:
    # Параметризация для теста метода get_type
    @pytest.mark.parametrize("ingredient_type, name, price", data.INGREDIENTS)
    def test_ingredients_type(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_type() == ingredient_type

    # Параметризация для теста метода get_name
    @pytest.mark.parametrize("ingredient_type, name, price", data.INGREDIENTS)
    def test_ingredients_name(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_name() == name

    # Параметризация для теста метода get_price
    @pytest.mark.parametrize("ingredient_type, name, price", data.INGREDIENTS)
    def test_ingredients_price(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_price() == price
