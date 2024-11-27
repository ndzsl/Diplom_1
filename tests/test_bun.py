# tests/test_bun.py
import pytest
import data
from praktikum.bun import Bun


class TestBun:

    # Параметризация для теста метода get_name
    @pytest.mark.parametrize("name, price", data.BUNS)
    def test_bun_get_name(self, name, price):
        # Создаем объект булочки с параметрами name и price
        bun = Bun(name, price)

        # Проверяем, что метод get_name() возвращает правильное имя
        bun_name = bun.get_name()
        assert bun_name == name

    # Параметризация для теста метода get_price
    @pytest.mark.parametrize("name, price", data.BUNS)
    def test_bun_get_price(self, name, price):
        # Создаем объект булочки с параметрами name и price
        bun = Bun(name, price)

        # Проверяем, что метод get_price() возвращает правильную цену
        actual_price = bun.get_price()
        assert actual_price == price
