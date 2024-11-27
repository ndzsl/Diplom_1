# data.py

# Данные для булочек
BUNS = [("Cosmic", 1000), ("Galactic", 1500)]

# Данные для ингредиентов
INGREDIENTS = [
    ('SAUCE', "chili", 100),  # Тип, имя и цена для соуса
    ('SAUCE', "tomato", 200),  # Тип, имя и цена для соуса
    ('FILLING', "cheese", 500),  # Тип, имя и цена для начинки
    ('FILLING', "onion", 300)  # Тип, имя и цена для начинки
]

# Ожидаемый результат для чека
TEST_BURGER_RECEIPT = (
    '(==== Cosmic ====)\n'
    '= sauce chili =\n'
    '= filling cheese =\n'
    '(==== Cosmic ====)\n'
    '\n'
    'Price: 2600'
)
