import pytest
from unittest.mock import Mock
from data import BUNS, INGREDIENTS  # Здесь предполагается, что у вас есть такие данные

# Мок для булочки
@pytest.fixture
def mock_bun():
    mock_bun = Mock()
    mock_bun.get_name.return_value = BUNS[0][0]  # Имя первой булочки из BUNS
    mock_bun.get_price.return_value = BUNS[0][1]  # Цена первой булочки из BUNS
    return mock_bun

# Мок для ингредиента
@pytest.fixture
def mock_ingredient():
    mock_ingredient = Mock()
    mock_ingredient.get_type.return_value = INGREDIENTS[0][0]  # Тип первого ингредиента
    mock_ingredient.get_name.return_value = INGREDIENTS[0][1]  # Имя первого ингредиента
    mock_ingredient.get_price.return_value = INGREDIENTS[0][2]  # Цена первого ингредиента
    return mock_ingredient

# Мок для второго ингредиента
@pytest.fixture
def mock_second_ingredient():
    mock_ingredient = Mock()
    mock_ingredient.get_type.return_value = INGREDIENTS[2][0]  # Тип второго ингредиента
    mock_ingredient.get_name.return_value = INGREDIENTS[2][1]  # Имя второго ингредиента
    mock_ingredient.get_price.return_value = INGREDIENTS[2][2]  # Цена второго ингредиента
    return mock_ingredient
