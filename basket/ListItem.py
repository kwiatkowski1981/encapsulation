from basket.Product import Product


class ListItem:
    def __init__(self, product: Product, quantity: float):
        self._product = product
        self._quantity = quantity

    def get_product(self) -> Product:
        return self._product

    def get_quantity(self) -> float:
        return self._quantity

    def add_quantity(self, quantity):
        self._quantity += quantity

    def sub_quantity(self, quantity):
        self._quantity -= quantity

    def get_subtotal(self):
        return self._quantity * self._product.get_price()


