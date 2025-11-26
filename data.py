from typing import List, Tuple, Dict, Any
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class BunData:
    """Тестовые данные для булочек"""
    
    # Параметризованные данные для тестов булочек
    BUN_PARAMETRIZE_DATA: List[Tuple[str, float]] = [
        ("Black Bun", 100.0),
        ("White Bun", 200.0),
        ("Red Bun", 300.0),
    ]
    
    # Данные для моков булочек
    MOCK_BUN_NAME = "Test Bun"
    MOCK_BUN_PRICE = 100.0
    
    # Данные из базы данных
    DB_BUNS_DATA = [
        {"name": "black bun", "price": 100.0},
        {"name": "white bun", "price": 200.0},
        {"name": "red bun", "price": 300.0},
    ]


class IngredientData:
    """Тестовые данные для ингредиентов"""
    
    # Параметризованные данные для тестов ингредиентов
    INGREDIENT_PARAMETRIZE_DATA: List[Tuple[str, str, float]] = [
        (INGREDIENT_TYPE_SAUCE, "Hot Sauce", 100.0),
        (INGREDIENT_TYPE_SAUCE, "Sour Cream", 200.0),
        (INGREDIENT_TYPE_SAUCE, "Chili sauce", 300.0),
        (INGREDIENT_TYPE_FILLING, "Cutlet", 100.0),
        (INGREDIENT_TYPE_FILLING, "Dinosaur", 200.0),
        (INGREDIENT_TYPE_FILLING, "Sausage", 300.0)
    ]
    
    # Данные для моков соуса
    MOCK_SAUCE_NAME = "Hot Sauce"
    MOCK_SAUCE_PRICE = 100.0
    MOCK_SAUCE_TYPE = INGREDIENT_TYPE_SAUCE
    
    # Данные для моков начинки
    MOCK_FILLING_NAME = "Cutlet"
    MOCK_FILLING_PRICE = 100.0
    MOCK_FILLING_TYPE = INGREDIENT_TYPE_FILLING
    
    # Данные из базы данных
    DB_INGREDIENTS_DATA = [
        {"type": INGREDIENT_TYPE_SAUCE, "name": "hot sauce", "price": 100.0},
        {"type": INGREDIENT_TYPE_SAUCE, "name": "sour cream", "price": 200.0},
        {"type": INGREDIENT_TYPE_SAUCE, "name": "chili sauce", "price": 300.0},
        {"type": INGREDIENT_TYPE_FILLING, "name": "cutlet", "price": 100.0},
        {"type": INGREDIENT_TYPE_FILLING, "name": "dinosaur", "price": 200.0},
        {"type": INGREDIENT_TYPE_FILLING, "name": "sausage", "price": 300.0},
    ]


class BurgerData:
    """Тестовые данные для бургеров"""
    # Параметризованные данные для тестов цены
    PRICE_PARAMETRIZE_DATA: List[Tuple[float, List[float], float]] = [
        (100.0, [100.0, 100.0], 400.0),      # 2*100 + 100 + 100 = 400
        (200.0, [100.0, 200.0, 300.0], 1000.0),  # 2*200 + 100 + 200 + 300 = 1000
        (50.0, [], 100.0),             # 2*50 + 0 = 100
        (75.0, [100.0], 250.0),           # 2*75 + 100 = 250
    ]
    
    # Данные для тестов типов ингредиентов в чеке
    RECEIPT_INGREDIENT_TYPES_DATA = [
        ("SAUCE", "sauce"),
        ("FILLING", "filling"),
    ]
    
    # Тестовые данные для полного чека
    FULL_RECEIPT_TEST_DATA = {
        "bun_name": "Test Bun",
        "sauce_ingredient": "Hot Sauce", 
        "filling_ingredient": "Cutlet",
        "total_price": 400.0  # 2*100 + 100 + 100
    }


def get_expected_receipt(bun_name: str, ingredients: List[Dict[str, str]], total_price: float) -> str:
    """Генерирует ожидаемый чек на основе переданных данных"""
    receipt_lines = [f'(==== {bun_name} ====)']
    for ingredient in ingredients:
        receipt_lines.append(f'= {str(ingredient["type"]).lower()} {ingredient["name"]} =')
    
    receipt_lines.append(f'(==== {bun_name} ====)')
    receipt_lines.append('')
    receipt_lines.append(f'Price: {total_price}')
    
    return '\n'.join(receipt_lines)


def get_expected_receipt_no_ingredients(bun_name: str, total_price: float) -> str:
    """Генерирует ожидаемый чек для бургера без ингредиентов"""
    receipt_lines = [
        f'(==== {bun_name} ====)',
        f'(==== {bun_name} ====)',
        '',
        f'Price: {total_price}'
    ]
    return '\n'.join(receipt_lines)


def get_expected_receipt_single_ingredient(bun_name: str, ingredient_type: str, ingredient_name: str, total_price: float) -> str:
    """Генерирует ожидаемый чек для бургера с одним ингредиентом"""
    receipt_lines = [
        f'(==== {bun_name} ====)',
        f'= {str(ingredient_type).lower()} {ingredient_name} =',
        f'(==== {bun_name} ====)',
        '',
        f'Price: {total_price}'
    ]
    return '\n'.join(receipt_lines)