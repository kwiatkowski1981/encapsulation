class Product:
    def __init__(self, name: str, price: float):
        self._name = name
        self._price = price

    def get_price(self) -> float:
        return self._price
