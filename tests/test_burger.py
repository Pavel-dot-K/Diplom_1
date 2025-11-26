import pytest
from unittest.mock import Mock
from praktikum.burger import Burger
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from data import BunData, IngredientData, BurgerData, get_expected_receipt, get_expected_receipt_no_ingredients, get_expected_receipt_single_ingredient

class TestBurger:

    # Проверяем, правильно ли формируется чек у бургера во всех деталях
    def test_full_burger_flow(self, mock_bun, burger_with_mocks):
        burger = burger_with_mocks
        bun = burger.bun
        assert bun is not None
        total_price = bun.get_price() * 2
        for ingredient in burger.ingredients:
            total_price += ingredient.get_price()
        expected_receipt_lines = [
            f'(==== {bun.get_name()} ====)'
        ]
        for ingredient in burger.ingredients:
            expected_receipt_lines.append(
                f'= {str(ingredient.get_type()).lower()} {ingredient.get_name()} ='
            )
        expected_receipt_lines.append(f'(==== {bun.get_name()} ====)')
        expected_receipt_lines.append(f'Price: {total_price}')
        expected_receipt = '\n'.join(expected_receipt_lines)
        actual_receipt = burger.get_receipt()
        assert list(filter(None, actual_receipt.splitlines())) == list(filter(None, expected_receipt.splitlines()))

    # Проверям получение чека, если ингридиенты добавлены
    def test_get_check_ingredients_added(self, mock_bun, mock_sauce_ingredient, mock_filling_ingredient): 
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_sauce_ingredient)
        burger.add_ingredient(mock_filling_ingredient)
        receipt = burger.get_receipt()
        expected_receipt = get_expected_receipt(
            bun_name=BunData.MOCK_BUN_NAME,
            ingredients=[
                {"type": "sauce", "name": IngredientData.MOCK_SAUCE_NAME},
                {"type": "filling", "name": IngredientData.MOCK_FILLING_NAME}
            ],
            total_price=400.0
        )
        assert receipt == expected_receipt

    # Проверяем получение чека, без добавления ингридиентов
    def test_get_check_no_ingredients(self, mock_bun):  
        burger = Burger()
        burger.set_buns(mock_bun)
        receipt = burger.get_receipt() 
        expected_receipt = get_expected_receipt_no_ingredients(
            bun_name=BunData.MOCK_BUN_NAME,
            total_price=200.0
        )
        assert receipt == expected_receipt

    # Проверяем, что при создании нового, "пустого" бургера
    def test_burger_initially_empty(self):
        burger = Burger()
        assert burger.bun is None
        assert burger.ingredients == []

    # Проверка установки булочки
    def test_bun_installation(self, mock_bun):  
        burger = Burger()
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

    # Проверка добавления ингридиентов
    def test_adding_ingredients(self, mock_bun, mock_sauce_ingredient):  
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_sauce_ingredient)
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == mock_sauce_ingredient

    # Проверяем, что ингридиенты можно удалить по их индексу
    def test_del_ingredient_by_index(self, burger_with_ingredients):  
        initial_count = len(burger_with_ingredients.ingredients)
        burger_with_ingredients.remove_ingredient(0) 
        assert len(burger_with_ingredients.ingredients) == initial_count - 1

    # Проверяем, удаление ингридиента с некорректным индексом
    def test_del_ingredient_incorrect_index(self, burger_with_ingredients):  
        with pytest.raises(IndexError):
            burger_with_ingredients.remove_ingredient(10)

    # Проверка перемещения ингридиентов 
    def test_move_the_ingredients(self, burger_with_ingredients, mock_sauce_ingredient, mock_filling_ingredient):  
        assert burger_with_ingredients.ingredients[0] == mock_sauce_ingredient
        assert burger_with_ingredients.ingredients[1] == mock_filling_ingredient
        burger_with_ingredients.move_ingredient(0, 1)
        assert burger_with_ingredients.ingredients[0] == mock_filling_ingredient
        assert burger_with_ingredients.ingredients[1] == mock_sauce_ingredient

    # Проверка возможности перемещения ингридиентов с некорректным индексом
    def test_incorrect_invalid_index_move(self, burger_with_ingredients): 
        with pytest.raises(IndexError):
            burger_with_ingredients.move_ingredient(10, 0)

    # Подключаем параметризацию
    @pytest.mark.parametrize("bun_price,ingredient_prices,expected_total", BurgerData.PRICE_PARAMETRIZE_DATA)
    def test_check_price_with_parameterization(self, mock_bun, bun_price, ingredient_prices, expected_total):
        mock_bun.get_price.return_value = bun_price  
        burger = Burger()
        burger.set_buns(mock_bun)
        for price in ingredient_prices:
            mock_ingredient = Mock(spec=Ingredient)
            mock_ingredient.get_price.return_value = price
            burger.add_ingredient(mock_ingredient)
        assert burger.get_price() == expected_total

    # Проверка появления ошибки, при вызове чека, если булочка не добавлена
    def test_error_calling_check_without_bun(self):
        burger = Burger()
        with pytest.raises(AttributeError):
            burger.get_price()

    # Подключаем параметризацию
    @pytest.mark.parametrize("ingredient_type,type_string", BurgerData.RECEIPT_INGREDIENT_TYPES_DATA)
    def test_get_check_parameterized_ingredients(self, mock_bun, ingredient_type, type_string):
        mock_ingredient = Mock(spec=Ingredient)
        mock_ingredient.get_name.return_value = "Test Ingredient"
        mock_ingredient.get_type.return_value = ingredient_type
        mock_ingredient.get_price.return_value = 0
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)
        receipt = burger.get_receipt() 
        expected_receipt = get_expected_receipt_single_ingredient(
            bun_name=BunData.MOCK_BUN_NAME,
            ingredient_type=type_string,
            ingredient_name="Test Ingredient",
            total_price=200.0
        ) 
        assert receipt == expected_receipt