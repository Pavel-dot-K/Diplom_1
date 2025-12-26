class BunStub:
    def __init__(self, name: str, price: float):
        self._name = name
        self._price = price

    def get_name(self) -> str:
        return self._name

    def get_price(self) -> float:
        return self._price


class IngredientStub:
    def __init__(self, name: str, price: float, type_: str):
        self._name = name
        self._price = price
        self._type = type_

    def get_name(self) -> str:
        return self._name

    def get_price(self) -> float:
        return self._price

    def get_type(self) -> str:
        return self._type