from basket.ListItem import ListItem
from basket.Product import Product


class List:
    def __init__(self):
        self._items = []

    def __str__(self):
        return f"W koszyku znajdują się: {self._items}"

    def add_item(self, product: Product, quantity: float):
        for item in self._items:
            if item.get_product() == product:
                item.add_quantity(quantity)
                return
        self._items.append(
            ListItem(product, quantity)
        )

    def remove_item(self, product: Product, quantity: float):
        for item in self._items:
            if item.get_product() == product:
                item.sub_quantity(quantity)
                return

    def list_items(self):
        return self._items

    def calculate_total_cost(self) -> float:
        total = 0
        for item in self._items:
            total += item.get_subtotal()
        return total


new_list = List()

apple = Product('apple', 5)
new_list.add_item(apple, 1)
# print(new_list.list_items())
# print(new_list.list_items())

apple2 = Product('apple', 5)
new_list.add_item(apple2, 2)
# print(new_list)
# print(new_list.list_items())

pineapple = Product('pineapple', 4)
new_list.add_item(pineapple, 2)
# print(new_list)
# print(new_list.list_items())

apple3 = Product('apple', 5)
new_list.add_item(apple3, 1)
# print(new_list)
print(new_list.list_items())
# print(new_list.calculate_total_cost())

apple = Product('apple', 5)
new_list.add_item(apple, 1)
print(new_list.list_items())
print(new_list.calculate_total_cost())
