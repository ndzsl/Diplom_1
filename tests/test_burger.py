# tests/conftest.py
import pytest
from unittest.mock import MagicMock

@pytest.fixture
def mock_bun():
    mock_bun = MagicMock()
    mock_bun.get_price.return_value = 50  # Примерная цена булочки
    return mock_bun

@pytest.fixture
def mock_ingredient():
    mock_ingredient = MagicMock()
    mock_ingredient.get_price.return_value = 20  # Примерная цена ингредиента
    return mock_ingredient

@pytest.fixture
def mock_second_ingredient():
    mock_ingredient = MagicMock()
    mock_ingredient.get_price.return_value = 30  # Примерная цена второго ингредиента
    return mock_ingredient
