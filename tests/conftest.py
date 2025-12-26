import pytest
from unittest.mock import Mock
from praktikum.burger import Burger
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from data import BunData, IngredientData, BurgerData, get_expected_receipt, get_expected_receipt_no_ingredients, get_expected_receipt_single_ingredient

@pytest.fixture
def mock_bun() -> Mock:
    bun_mock = Mock(spec=Bun)
    bun_mock.get_name.return_value = BunData.MOCK_BUN_NAME
    bun_mock.get_price.return_value = BunData.MOCK_BUN_PRICE
    return bun_mock


@pytest.fixture
def mock_sauce_ingredient() -> Mock:
    ingredient_mock = Mock(spec=Ingredient)
    ingredient_mock.get_name.return_value = IngredientData.MOCK_SAUCE_NAME
    ingredient_mock.get_price.return_value = IngredientData.MOCK_SAUCE_PRICE
    ingredient_mock.get_type.return_value = IngredientData.MOCK_SAUCE_TYPE
    return ingredient_mock


@pytest.fixture
def mock_filling_ingredient() -> Mock:
    ingredient_mock = Mock(spec=Ingredient)
    ingredient_mock.get_name.return_value = IngredientData.MOCK_FILLING_NAME
    ingredient_mock.get_price.return_value = IngredientData.MOCK_FILLING_PRICE
    ingredient_mock.get_type.return_value = IngredientData.MOCK_FILLING_TYPE
    return ingredient_mock


@pytest.fixture
def burger_with_mocks(mock_bun, mock_sauce_ingredient, mock_filling_ingredient) -> Burger:
    burger = Burger()
    burger.set_buns(mock_bun)
    burger.add_ingredient(mock_sauce_ingredient)
    burger.add_ingredient(mock_filling_ingredient)
    return burger


@pytest.fixture
def burger_with_ingredients(mock_bun, mock_sauce_ingredient, mock_filling_ingredient) -> Burger:
    burger = Burger()
    burger.set_buns(mock_bun)
    burger.add_ingredient(mock_sauce_ingredient)
    burger.add_ingredient(mock_filling_ingredient)
    return burger