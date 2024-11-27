# tests/test_database.py
from praktikum.database import Database


class TestDatabase:

    # Тестирование метода available_buns
    def test_available_buns(self):
        database = Database()  # Создаем объект базы данных
        available_buns = database.available_buns()  # Получаем доступные булочки
        expected_result = ["black bun", "white bun", "red bun"]  # Ожидаемый список имен булочек

        # Составляем список имен булочек из возвращаемых объектов
        bun_names_list = [bun.get_name() for bun in available_buns]

        # Сравниваем полученные имена булочек с ожидаемыми
        assert bun_names_list == expected_result

    # Тестирование метода available_ingredients
    def test_available_ingredients(self):
        database = Database()  # Создаем объект базы данных
        available_ingredients = database.available_ingredients()  # Получаем доступные ингредиенты
        expected_result = ["hot sauce", "sour cream", "chili sauce", "cutlet", "dinosaur",
                           "sausage"]  # Ожидаемый список имен ингредиентов

        # Составляем список имен ингредиентов из возвращаемых объектов
        ingredient_names_list = [ingredient.get_name() for ingredient in available_ingredients]

        # Сравниваем полученные имена ингредиентов с ожидаемыми
        assert ingredient_names_list == expected_result
